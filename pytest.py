class Restaurant():
    def __init__(self, r_name, c_type, number_s):
        self.name = r_name
        self.type = c_type
        self.number_s = 0

    def describe_r(self):
        print('R name is '+self.name)
        print('R type is '+self.type)

    def open_r(self):
        print(self.name + ' is opening')

    def set_number(self, new_n):
        self.number_s = new_n
        return self.number_s

    def increase_number(self, in_n):
        self.number_s += in_n
        return self.number_s

class IceCream(Restaurant):
    def __init__(self, r_name, c_type, number_s, flavors):
        super().__init__(r_name, c_type, number_s)
        self.flavors = 'abc'
        self.r_name = 'ice111'
        self.number_s = number_s

    def aIce(self):
        print('Ice name is ' + self.flavors + self.r_name + str(self.number_s))
ice=IceCream('ice_name','ice_type',222,'fla')
ice.aIce()
