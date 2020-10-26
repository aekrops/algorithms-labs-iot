class WaterPump:
    def __init__(self, power_in_watts, brand, liter_per_hour):
        self.power_in_watts = power_in_watts
        self.brand = brand
        self.liter_per_hour = liter_per_hour

    def __str__(self):
        return '\nBrand: ' + self.brand + \
                '\nPower in watts: ' + str(self.power_in_watts) + \
                '\nLiter per hour: ' + str(self.liter_per_hour) + '\n'

    def __del__(self):
        pass
