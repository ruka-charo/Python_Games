#家から指定の場所までの経路情報

from town import Town
from shop import Shop

town_1 = Town('東京','100','電車＋新幹線','片道5000円超','1時間30分')
town_2 = Town('栃木','100','車','片道2500円','2時間')
town_3 = Town('北海道','1000','自転車','？？？','1週間')

shop_1 = Shop('ベイシア','自転車','頻繁')
shop_2 = Shop('ダルマ大使','自転車','1ヶ月に1回')
shop_3 = Shop('アニメイト','自転車+電車','1ヶ月に1回未満')

towns = [town_1,town_2,town_3]
shops = [shop_1,shop_2,shop_3]

index = 1
for town in towns :
    print(str(index) + '：' + town.info_name())
    index += 1

for shop in shops :
    print(str(index) + '：' + shop.info_name())
    index += 1

number = int(input('詳細を知りたい行き先を選んでください。:')) - 1

if 0 <= number <= 2:
    select = towns[number]
    select.info()

elif 3 <= number <= 5:
    select = shops[number - 3]
    select.info()

else:
    print('適切な数字を入力してください。')
