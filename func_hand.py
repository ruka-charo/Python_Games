#ジャンケンに対応する手（数字）を選ぶ関数
def choice(player_hand,player_name) :
    hands = {1:'グー',2:'チョキ',3:'パー'}

    print(player_name + 'は' + hands[player_hand] + 'を出しました。')

#勝ち負けの判定
def judge(a,b,player_name) :
    if a == b :
        print('引き分けです。')
    elif a == 1 and b == 2 :
        print(player_name + 'の勝ちです。')
    elif a == 2 and b == 3 :
        print(player_name + 'の勝ちです。')
    elif a == 3 and b == 1 :
        print(player_name + 'の勝ちです。')
    else :
        print('Computerの勝ちです。')
