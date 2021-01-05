#西暦から年号に変換

year = int(input('現在の「年」を入力してください（西暦）。:'))

if 2019 < year :
    reiwa = year - 2019 + 1
    print('令和' + str(reiwa) + '年です。')

elif year == 2019 :
    print('令和元年（平成31年）です。')

elif 1989 < year < 2019 :
    heisei = year - 1989 + 1
    print('平成' + str(heisei) + '年です。')

elif year == 1989 :
    print('平成元年（昭和64年）です。')

elif 1926 < year < 1989 :
    syowa = year - 1926 + 1
    print('昭和' + str(syowa) + '年です。')

elif year == 1926 :
    print('昭和元年（大正15年）です。')

elif 1912 < year < 1926 :
    taisyo = year - 1912 + 1
    print('大正' + str(taisyo) + '年です。')

elif year == 1912 :
    print('大正元年（明治45年）です。')

else :
    print('昔すぎるので割愛します。')
