###モジュール（正規表現、ファイルダイアログ）をインポート

import re
from tkinter import filedialog

###置換したい正規表現を変数に格納（例：More）
match_target_replace = '置換する正規表現'
###拡張子を表す正規表現
match_target_file = '(.+)\.(\w)+'

###ファイルダイアログを表示し、選択されたファイルのパスを格納

typ = [('すべて', '*'),('テキストファイル','*.txt'),('CSVファイル', '*.csv')] 
dir = '開くパス'
fles = filedialog.askopenfilenames(filetypes = typ, initialdir = dir) 

###生成するファイルの名前を取得する（拡張子の有無で分岐）
for fle in fles:
    match_obj = re.match(match_target_file,fle)
    if match_obj:
        path_w = fle[:-4] + '_' + match_target_replace[X:Y] + '_置換後' + fle[-4:]

    else:
        path_w = fle + '_置換後'

    ###fleを開いて、データを変数に格納###

    f1 = open(fle, 'r', encoding='UTF-8')
    data = f1.read()
    f1.close()

    ###ファイルを新規に作成し、中身をリスト型でオリジナルからコピーする###

    f2 = open(path_w,mode='w')
    data_list = data.split('\n')

    ###リストの要素を一行ずつ取り出す###
    for data_line in data_list:
        ###要素の中から正規表現で探す###
        match_obj2 = re.match(match_target_replace,data_line)
        ###マッチした文字列を置き換えて書き込む###
        if match_obj2:
            data_copy_replace = re.sub(match_target_replace,'置換後の文字列・数字',data_line)
            f2.write('%s\n' % data_copy_replace)
            
        else:
            f2.write('%s\n' % data_line)

    f2.close()

    print(path_w + 'を作成しました')
