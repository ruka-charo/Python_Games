#石取り関数
def catch(stone,number,name) :
    stone = stone - number
    if stone >= 1 :
        print(name + 'は' + str(number) + '個取りました。')
        print('現在の石の個数は' + str(stone) + '個です。')
    else :
        print('最後の石を取りました。' + name + 'の負けです。')
