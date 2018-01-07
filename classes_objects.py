lottery_player_dict = {
    'name': 'Rolf',
    'numbers': (13, 45, 66, 23, 22)
}


class LotteryPlayer:
    def __init__(self, name):
        self.name = name
        self.numbers = (5, 9, 12, 3, 1, 21)

    def total(self):
        return sum(self.numbers)


player_one = LotteryPlayer('Rolf')
player_two = LotteryPlayer('Jerf')
print(player_one == player_two) 

##

class Student:
    def __init__(self, name, school):
        self.name = name
        self.school = school
        self.marks = []

    def average(self):
        return sum(self.marks) / len(self.marks)

    def go_to_school_at(self):
        print('I am going to {}.'.format(self.school))

    @classmethod
    def go_to_school(cls):
        print('I am going to school')
        print(cls) #cls prints:   <class '__main__.Student'>

    @staticmethod
    def go_to_college():
        print('I am in college, I do not need parameters because I am a static method, I have no self.')

anna = Student('Anna', 'MIT')
anna.marks.append(56)
anna.marks.append(71)
print(anna.average())
anna.go_to_school()


##

class Store:
    def __init__(self, name):
        self.name = name
        self.items = []

    def add_item(self, name, price):
        item = {'name': name, 'price': price}
        self.items.append(item)

    def stock_price(self):
        return sum([item['price'] for item in self.items])

    