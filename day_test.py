#%%任意の日付の曜日を表示

import datetime
day = datetime.date(1996,1,20)
#0(月)1(火)2(水)3(木)4(金)5(土)6(日)
day.weekday()
print('1996年1月20日の曜日は' + str(day.weekday()) + 'です。')
print('※ 0(月)1(火)2(水)3(木)4(金)5(土)6(日)')

#%%今日の日付を表示 & 曜日の表示

today = datetime.date.today()
print('今日は' + str(today) + 'です。')
today.weekday()
print('今日の曜日は' + str(today.weekday()) + 'です。')

#%%今の時間を表示

time = datetime.datetime.now()
print('現在の日時は' + str(time) + 'です。')

#%%ある日付からある日付まで何日あるか

date_a = datetime.date(1996,1,20)
date_b = datetime.date.today()

mylife_days = date_b - date_a
print('僕が生きてきた日数は' + str(mylife_days) + 'です。')
