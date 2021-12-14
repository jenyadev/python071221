#popMap = { 'TEL-AVIV': 44339, 'LONDON': 882500, 'PARIS' : 0 ,'TOKYO' : 139123}

#cityName = input("Please enter a city name: ")
#print(f'{cityName} population is:{popMap[cityName.upper()]} hello you beutiful city')

'''
def doesKeyExist(d , k):
    if k in d.keys():
        return True
    else:
        return False

def tryAddValue(d, k, v):
    if doesKeyExist(d , k)== False:
        d [ k ] = v
        return True
    else:
        return False

def printDictionary(d):
    for k, v, in d.items():
        print(f'dictionary key : {k} = {v}')
myDict = {1 : 'moshe', 2 : 'erez', 3 :'dana'}


if doesKeyExist(myDict, 4 ) == False:
    myDict[4] = 'anat'
if doesKeyExist(myDict, 4) == False:
    myDict[4] = 'rona'

if tryAddValue(myDict, 7 , 'Rozner'):
    print('Rozner added successfully')
else:
    print('rozner was not added')
print(myDict)
printDictionary(myDict)
'''
'''
class MobilePhone():
    def __init__(self, brand, model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def __repr__(self):
        return f'MobilePhone: ({self.brand}, {self.model}, {self.price})'
    def __str__(self):
        return f'MobilePhone: brand = {self.brand}  model = {self.model} price = {self.price}'
    def __eq__(self, other):
        if self.brand == other.brand\
            and self.mobel == other.model\
            and self.price == other.price:
            return True
        else:
            return False
    def __add__(self, other):
        return self.price + other.price
    def __gt__(self, other):
        if self.price > other.price:
            return True
        else:
            return False




iphoneX = MobilePhone('Apple', 'IphoneX', 3500)
iphoneX11 = MobilePhone('Apple', 'IphoneX', 3500)
print('phone equels?', iphoneX == iphoneX11)
samsung = MobilePhone('samsung', 'S9' , 4000)
print(samsung > iphoneX)


        #print('new phone was created')
    #def turnOn(self):
        #print('turn on phone')
'''


#iphone = MobilePhone()
#samsung = MobilePhone()

#iphone.turnOn()
#samsung.turnOn()
class MobilePhone():
    def __init__(self, brand,
             model, price):
        self.brand = brand
        self.model = model
        self.price = price
    def __repr__(self):
        return f'MobilePhone({self.brand}, {self.model}, {self.price})'
    def __str__(self):
        return f'MobilePhone: brand = {self.brand} model = {self.model} price = {self.price}'
    def __eq__(self, other):
        if self.brand == other.brand\
            and self.model == other.model\
            and self.price == other.price:
            return True
        else:
            return False
    def __add__(self, other):
        return self.price + other.price
    def __gt__(self, other):
        #return self.price > other.price
        if self.price > other.price:
            return True
        else:
            return False

iphoneX = MobilePhone("Apple",
    "IPhoneX", 3500)
iphoneX11 = MobilePhone("Apple",
    "IPhoneX", 3500)
print('phone equals? ',iphoneX == iphoneX11)
print(iphoneX11 + iphoneX)
samsung = MobilePhone("Samsung",
    "S9+", 4000)
print(samsung > iphoneX)
