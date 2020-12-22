from lab5.constant import prime_number, size


def rabin_karp(text: str, pattern: str):
    found_patterns_idx = []
    text_len = len(text)
    pattern_len = len(pattern)
    if text_len < pattern_len:
        return -1
    pattern_hash = hash(pattern, pattern_len)
    text_hash = hash(text, pattern_len)
    if pattern_hash == text_hash:
        if check_match(text, pattern, 0):
            found_patterns_idx.append({'start': 0, 'end': 0 + pattern_len - 1})
    for i in range(1, text_len - pattern_len + 1):
        text_hash = substring_new_hash(pattern, text_hash, text[i - 1], text[i + pattern_len - 1])
        if pattern_hash == text_hash:
            if check_match(text, pattern, i):
                found_patterns_idx.append({'start': i, 'end': i + pattern_len - 1})
    return found_patterns_idx


def hash(pattern, pattern_len):
    pattern_hash = 0
    for i in range(pattern_len):
        pattern_hash = (pattern_hash * size + ord(pattern[i])) % prime_number
    return pattern_hash


# hash for  substring with next letter
def substring_new_hash(pattern_length, prev_hash, old_letter, new_letter):
    new_hash = size ** (len(pattern_length) - 1) % prime_number
    return ((prev_hash - ord(old_letter) * new_hash) * size + ord(new_letter)) % prime_number


def check_result(expected_res, text: str, pattern: str):
    found_patterns = rabin_karp(text, pattern)
    confirmation = False
    for index in range(len(found_patterns)):
        confirmation = expected_res[index][0] == found_patterns[index]['start'] and \
                       expected_res[index][1] == found_patterns[index]['end']
    return confirmation


def check_match(text, pattern, start_index):
    for i in range(len(pattern)):
        if pattern[i] != text[start_index + i]:
            return False
    return True
