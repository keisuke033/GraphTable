from table import Table
from graph import Graph

data = []
counter = -1
label = list()
while True:
    print("1:グラフを作成する")
    print("2:表を作成する")
    print("3:終了する")
    print("番号を入力してください : ")
    number = int(input())
    print("-------------------------------------------------")

    if number == 1:
        counter += 1
        print("ファイル名を入力してください : ")
        file_name = input()
        print("開始シート番号を入力してください : ")
        begin_sheet_name = int(input())
        print("終了シート番号を入力してください : ")
        end_sheet_name = int(input())
        print("横軸の数を入力してください : ")
        x_number = int(input())
        print("縦軸の数を入力してください : ")
        y_number = int(input())
        x = list()
        y = list()
        for i in range(x_number):
            print("横軸{}のシート番号を入力してください : ".format(i))
            x_sheet_number = int(input())
            print("横軸{}の列番号を入力してください : ".format(i))
            x_column_number = int(input())
            x.append([x_sheet_number, x_column_number])
        for i in range(y_number):
            print("縦軸{}のシート番号を入力してください : ".format(i))
            y_sheet_number = int(input())
            print("縦軸{}の列番号を入力してください : ".format(i))
            y_column_number = int(input())
            y.append([y_sheet_number, y_column_number])
        print("横軸を対数軸にしますか？(y/n) : ")
        isXLog = input()
        if isXLog == 'y':
            isXLog = True
        else:
            isXLog = False
        # print("縦軸を対数軸にしますか？(y/n) : ")
        # isYLog = input()
        # if isYLog == 'y':
        #     isYLog = True
        # else:
        #     isYLog = False
        # print("グラフに補助線を追加しますか？(y/n) : ")
        # isGrid = input()
        # if isGrid == 'y':
        #     isGrid = True
        # else:
        #     isGrid = False
        print("横軸のラベルを入力してください : ")
        xlabel = input()
        print("縦軸のラベルを入力してください : ")
        ylabel = input()
        for i in range(x_number):
            print("横軸{}の凡例を入力してください : ".format(i))
            label.append(input())
        data.append(Graph(file_name, begin_sheet_name, end_sheet_name))
        data[counter].set_graph(x, y, isXLog)
        data[counter].draw_graph(xlabel, ylabel, label)
        print("-------------------------------------------------")
        while True :
            print("1:グラフを表示する")
            print("2:グラフを保存する")
            print("3:データを表示する")
            print("4:戻る")
            print("番号を入力してください : ")
            number = int(input())
            if number == 1:
                data[counter].show_graph()
            elif number == 2:
                print("ファイル名を入力してください : ")
                file_name = input()
                data[counter].save_graph(file_name)
            elif number == 3:
                data[counter].print_data()
            elif number == 4:
                print("-------------------------------------------------")
                break
            else:
                print("番号が間違っています")
        
    elif number == 2:
        counter += 1
        print("ファイル名を入力してください : ")
        file_name = input()
        print("開始シート番号を入力してください : ")
        begin_sheet_name = int(input())
        print("終了シート番号を入力してください : ")
        end_sheet_name = int(input())
        data.append(Table(file_name, begin_sheet_name, end_sheet_name))
        data[counter].to_latex()
        # data[counter].print_data()
        while True :
            print("1:表を表示する")
            print("2:表を保存する")
            print("3:表を削除する")
            print("4:戻る")
            print("番号を入力してください : ")
            number = int(input())
            if number == 1:
                data[counter].print_data()
            elif number == 2:
                print("ファイル名を入力してください : ")
                file_name = input()
                data[counter].save_tex(file_name)
            elif number == 3:
                print("ファイル名を入力してください : ")
                file_name = input()
                data[counter].delete_tex(file_name)
            elif number == 4:
                break
            else:
                print("番号が間違っています")

    elif number == 3:
        exit()

