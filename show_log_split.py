###モジュール（正規表現、ファイルダイアログ）をインポート
import re
import datetime
from tkinter import filedialog
import os
import pathlib

###変数宣言
match_target_file = '(.+)\.(\w)+'
match_target_config = '^(hostname\s\w+)'
match_target_hostname = ''
now = datetime.datetime.now()

###ファイル選択ダイアログ
typ = [('すべて', '*'),('テキストファイル','*.txt'),('CSVファイル', '*.csv')] 
dir = 'C:/Users/jumpei/Desktop/作業用/自動化勉強/python'
fles = filedialog.askopenfilenames(filetypes = typ, initialdir = dir) 

###新規ファイル作成（作成ファイル名は拡張子の有無で条件分岐）
for fle in fles:
    print(type(fle))
    match_obj = re.match(match_target_file,fle)
    
    ###fleを開いて、データを変数に格納###
    f1 = open(fle, 'r', encoding='UTF-8')
    data = f1.read()
    f1.close()

    ###hostname取得
    data_list = data.split('\n')

    for data_line in data_list:
        #条件分岐（行頭がプロンプトshowで始まる場合）
        match_target_hostname = re.match(match_target_config,data_line)
        if match_target_hostname:
            break
    match_target_hostname_list = match_target_hostname.group().split(' ')
        
    ###検索するプロンプトを作成
    match_target_prompt_user = '^' + match_target_hostname_list[1] + '>'
    match_target_prompt_en = '^' + match_target_hostname_list[1] + '#'
    match_target_prompt_gconf = '^' + match_target_hostname_list[1] + '\(config\)#'
    match_target_prompt_rconf = '^' + match_target_hostname_list[1] + '\(\w+-config\)#'
    match_target_prompt_fconf = '^' + match_target_hostname_list[1] + '\(config-\w+\)#'
    match_target_prompt_integration = match_target_prompt_user + '|' + match_target_prompt_en + '|' + match_target_prompt_gconf + '|' + match_target_prompt_rconf + '|' + match_target_prompt_fconf
    print(match_target_prompt_integration)
    
    #繰り返し処理で、コマンドをキーに、出力結果を値に代入する
    command_file_dict = {}
    
    ###fle[0]からプロンプトを取り出していく
    ###data_listにはfle[0]がリスト形式で格納されている
    for data_line in data_list:
        match_obj_prompt = re.match(match_target_prompt_integration,data_line)
        #print(data_line)
        if match_obj_prompt:
            if data_line in command_file_dict.keys():
                pass
            else:
                command_file_dict[data_line] = ['data_line']
        else:
            pass
    #print(command_file_dict.keys())
    
    
    #command_file = pathlib.Path(fle)
    #command_file = pathlib.Path(fle).as_posix()
    #command_file = str(pathlib.PurePosixPath(fle))
    print('67行目において' + 'fleのパスは' + fle)
    print(command_file_dict.keys())
    for command_key in command_file_dict.keys():
        for data_line in data_list:
             
            #print('command_key:' + command_key)
            #print('data_line:' + data_line)
            
            if data_line == command_key:
                if 'sh' in data_line:
                    command_file = open(command_key,'w')
                    command_file.write("%s\n" % data_line)
                elif 'sh' not in data_line:
                    try:
                        #command_fileを閉じれるか？
                        command_file.close()
                    except:
                        #print('command_fileを閉じれませんでした')
                        #print('読込ファイル該当箇所:' + data_line + '書込対象:' + command_key)
                        pass
                                    
                else:
                    pass

            elif data_line != command_key:
                #出力が終わりプロンプトが返ったら閉じる
                if data_line in command_file_dict.keys():
                    try:
                        command_file.close()
                    except NameError:
                        print('変数command_fileの値が定義されていません')
                else:
                    try:
                        command_file.write("%s\n" % data_line)
                    except NameError:
                        print('変数command_fileの値が定義されていません')
                    except ValueError:
                        print('変数command_file:I/O operation on closed file.')
            else:
                pass
    print('End of file')




    #for data_line in data_list:
    #    if data_line in command_file_dict:
    #        open(data_line,'w')
    #        
    #
    #    else:
    #        pass
    

    
    #f3 = open(fle,mode='w')
    #for data_line in data_list:
        

#    ###ファイルを新規に作成し、中身をリスト型でオリジナルからコピーする###
#    f2 = open(path_w,mode='w')
#    data_list = data.split('\n')
#
#    ###リストの要素を一行ずつ取り出す###
#    for data_line in data_list:
#        f2.write('%s\n' % data_line)
#
#    f2.close()
#
#    print(path_w + 'を作成しました')
