import datetime
import os
import os.path

folder_pass = input('情報を引き出すフォルダのパスを入力してください。')
file_info = os.listdir(folder_pass)

def file_size():
    print('名前\t\tサイズ')
    for file_name in file_info:
        file_size = os.path.getsize(folder_pass + '/' + file_name)
        print(file_name,'\t',file_size,'バイト')
    print()

def file_make_time():
    print('名前\t\t作成時刻')
    for file_name in file_info:
        file_timestamp = os.path.getmtime(folder_pass + '/' + file_name)
        file_time1 = datetime.datetime.fromtimestamp(file_timestamp)
        file_time = file_time1.strftime('%Y-%m-%d(%a) %H:%M:%S')
        print(file_name,'\t',file_time)
    print()

def file_time():
    print('名前\t\t最終アクセス時刻')
    for file_name in file_info:
        file_timestamp = os.path.getatime(folder_pass + '/' + file_name)
        file_time1 = datetime.datetime.fromtimestamp(file_timestamp)
        file_time = file_time1.strftime('%Y-%m-%d(%a) %H:%M:%S')
        print(file_name,'\t',file_time)
    print()

file_size()
file_make_time()
file_time()
