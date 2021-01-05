class Town() :
    def __init__(self,name,dist,way,money,time):
        self.name = name
        self.dist = dist
        self.way = way
        self.money = money
        self.time = time

    def info_name(self):
        return self.name

    def info(self):
        print(self.name + 'までの距離は' + str(self.dist) + 'kmです。')
        print('交通手段は' + self.way + 'です。')
        print('かかる費用は' + self.money + 'です。')
        print('所要時間は' + self.time + 'です。')
