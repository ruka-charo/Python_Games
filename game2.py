#石取りゲーム
import random
import func_stone

stone = 20
print('現在の石の個数は' + str(stone) + '個です。')

#ゲーム
while stone > 0 :
    print('Playerの番です。')
    player = int(input('いくつ取りますか？（1,2,3個のうちから数字で入力）:'))

    if player > 3 or player > stone :
        print('石を取れません。適切な個数を入力してください。')
        player = int(input('いくつ取りますか？（1,2,3個のうちから数字で入力）:'))

    func_stone.catch(stone,player,'Player')
    stone = stone - player

    print('Computerの番です。')
    if stone >= 4 :
        computer = random.randint(1,3)
        func_stone.catch(stone,computer,'Computer')
        stone = stone - computer

    elif stone == 3 :
        computer = 2
        func_stone.catch(stone,computer,'Computer')
        stone = stone - computer

    elif stone == 2 :
        computer = 1
        func_stone.catch(stone,computer,'Computer')
        stone = stone - computer

    elif stone == 1 :
        computer = 1
        func_stone.catch(stone,computer,'Computer')
        stone = stone - computer

    else :
        print('Computerは石を取ることができません。')
