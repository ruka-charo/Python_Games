#現在持っているゲームの情報をclassを用いて管理

class GameItem() :
    def __init__(self,name,time,clear,eval) :
        #名前
        self.name = name
        #プレイ時間
        self.time = time
        #クリア済みか
        self.clear = clear
        #評価
        self.eval = eval

    def info(self) :
        print('タイトル名：' + self.name)
        print('プレイ時間：' + self.time)
        print('クリア　　：' + self.clear)
        print('評価　　　：' + self.eval)

#基本情報
game_item1 = GameItem('Monster Hunter World','約500時間','クリア済み','★★★★★')
game_item2 = GameItem('Devil May Cry 5','100時間未満','クリア済み','★★★★☆(バージル加入以降：★★★★★)')
game_item3 = GameItem('Sword Art Online Hollow Realization','約150時間','クリア済み','★★★★★')
game_item4 = GameItem('Persona5 The Royal','50時間未満','未クリア','★★★☆☆')

game_items = [game_item1,game_item2,game_item3,game_item4]
index = 1

#初期表示
for game_item in game_items :
    print(str(index) + '.' + game_item.name)
    index = index + 1

#ゲームを選択
game_number = int(input('詳細を表示したいゲームを選んでください。:')) - 1
select_game = game_items[game_number]
select_game.info()
