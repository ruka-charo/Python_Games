from town import Town

class Shop(Town) :
    def __init__(self,name,way,freq):
        self.name = name
        self.way = way
        self.freq = freq

    def info_name(self) :
        return self.name

    def info(self):
        print(self.name + 'までの距離は近いです。')
        print('交通手段は' + self.way + 'です。')
        print('行く頻度は' + self.freq + 'です。')
