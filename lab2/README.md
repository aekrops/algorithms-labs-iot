## Finding algorithm
### Task
Горила Джекі  із зоопарку Мюнхена любить їсти банани. На складі зоопарку є N кошиків (piles) з бананами, у і-тому кошику
є певна кількість бананів Х. Кошики знаходяться під охороною, але охорона здійснює обхід зоопарку на Н годин, протягом 
якого Джекі може поласувати своєю улюбленою стравою.
Джекі може з'їсти за годину К бананів. Кожну годину вона вибирає кошик з бананами і їсть К бананів звідти. Якщо кошик
має менше, ніж К бананів, вона з'їдає всі банани з нього і більше не буде їсти бананів протягом цієї години.
Джекі любить їсти повільно, але все ж хочеться закінчити споживання всіх бананів, перш ніж охоронці повернуться.
Визначіть мінімальне ціле число К таким чином, щоб Джекі могла з'їсти всі банани на складі протягом Н годин, поки 
повернеться охорона.
## 
### Description of the algorithm
The algorithm is finding the minimum amount of hours at which the gorilla can eat all piles of bananas while there
is not protection
##
### Instruction:
1. Clone repository `git clone https://github.com/aekrops/algorithms-labs-iot.git`
1. Open project folder in console `cd algorithms-labs-iot/lab2`
1. Run code with command `python bananas.py` or `python -m unittest bananas.py`
## 
### Algorithm analysis:
#### Complexity:

`O(N(log(MAX - AVERAGE) + 1))`

* N - is length of piles list
* MAX - is biggest element in piles
* AVERAGE -  is the sum of all elements in piles divided by hours
###
Space complexity: `O(1)`

