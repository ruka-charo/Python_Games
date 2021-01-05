#ジャンケンで先行後攻を決める
import func_hand
import random

#%%プレイヤーが出す手
player_name = input('名前を入力してください。:')
player_hand = input('出す手を選んでください。(1:グー,2:チョキ,3:パー):')
player_hand = int(player_hand)
func_hand.choice(player_hand,player_name)

#%%コンピュータの出す手
computer_hand = random.randint(1,3)
func_hand.choice(computer_hand,'Computer')

#%%ジャンケンの勝ち負け
func_hand.judge(player_hand,computer_hand,player_name)
