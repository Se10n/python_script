###モジュール（正規表現、ファイルダイアログ）をインポート
import re
import datetime
from tkinter import filedialog

###マッチさせたい正規表現を変数に格納
match_target_file = '(.+)\.(\w)+'
###ファイル名に付け加えるもの（時刻）
now = datetime.datetime.now()
kakuchousi = '.txt'

###ファイルダイアログを表示し、選択されたファイルのパスを格納
typ = [('すべて', '*'),('テキストファイル','*.txt'),('CSVファイル', '*.csv')] 
dir = 'C:/Users/jumpei/Desktop/作業用/自動化勉強/python'
fles = filedialog.askopenfilenames(filetypes = typ, initialdir = dir) 

###生成するファイルの名前を取得する（拡張子の有無で条件分岐）
for fle in fles:
    match_obj = re.match(match_target_file,fle)
    
    ###選択したファイルに拡張子がある場合
    if match_obj:
        path_w = fle[:-4] + '_' + now.strftime('%Y%m%d_%H%M%S')  + fle[-4:]
    ###選択したファイルに拡張子が無い場合
    else:
        path_w = fle + '_' + now.strftime('%Y%m%d_%H%M%S') + kakuchousi 

    ###fleを開いて、データを変数に格納###
    f1 = open(fle, 'r', encoding='UTF-8')
    data = f1.read()
    f1.close()

    ###ファイルを新規に作成し、中身をリスト型でオリジナルからコピーする###
    f2 = open(path_w,mode='w')
    data_list = data.split('\n')

    ###リストの要素を一行ずつ取り出す###
    for data_line in data_list:
        f2.write('%s\n' % data_line)
        

    f2.close()

    print(path_w + 'を作成しました')
