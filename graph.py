import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams['font.family'] = 'Hiragino Sans'  # 使いたい日本語フォントを選択

# グラフを出力するための Graph クラスを定義
class Graph:

    # コンストラクタ
    def __init__(self, file_name, begin_sheet_name, end_sheet_name) :
        self.file_name = file_name
        self.data = list()
        self.begin_sheet_name = begin_sheet_name -2
        self.end_sheet_name = end_sheet_name
        for i in range(self.begin_sheet_name, self.end_sheet_name):
            self.sheet_name = i
            self.data.append(pd.read_excel(self.file_name, sheet_name=self.sheet_name))
        
        
    # データの確認
    def print_data(self):
        # excel ファイルの読み込み
        for i in range(self.begin_sheet_name, self.end_sheet_name):
            print("Sheet{} : ".format(i))
            print(self.data[i].head())
            print("-------------------------------------------------")
        # グラフの設定の読み込み
        for i in range(len(self.x)):
            print("横軸{} : {}".format(i, self.x[i]))
        print("-------------------------------------------------")
        for i in range(len(self.y)):
            print("縦軸{} : {}".format(i, self.y[i]))
        print("-------------------------------------------------")

    # グラフの設定
    def set_graph(self, x, y , isXLog = False, isYLog = False, isGrid = True):
        # x = [[Int : シート番号, Int : 列番号], [Int : シート番号, Int : 列番号], [Int : シート番号, Int : 列番号], ...]
        # y = [[Int : シート番号, Int : 列番号], [Int : シート番号, Int : 列番号], [Int : シート番号, Int : 列番号], ...]

        plt.figure(figsize=(8, 6)) # グラフのサイズを設定
        self.sheet_number = list()
        self.length = len(x)
        for i in range(len(x)) :
            self.sheet_number.append(x[i][0]) # シート番号
        self.x = list()
        for i in range(len(x)) :
            self.x.append(self.data[x[i][0]].columns[x[i][1]]) #x軸の列名
        self.y = list()
        for i in range(len(y)) :
            self.y.append(self.data[y[i][0]].columns[y[i][1]]) #Y軸の列名
        if isXLog: 
            plt.xscale('log') # X軸を対数軸に設定
        if isYLog:
            plt.yscale('log') # Y軸を対数軸に設定
        if isGrid:
            plt.grid(True) # 補助線を追加
    
    # グラフの描画
    def draw_graph(self, xlabel, ylabel, label):
        # データからグラフをプロット
        for i in range(self.length):
            plt.plot(self.data[self.sheet_number[i]][self.x[i]], self.data[self.sheet_number[i]][self.y[i]], label=label[i])
            plt.legend() # 凡例を表示
        # グラフにラベルを追加
        plt.xlabel(xlabel)  # X軸のラベルを適切なものに変更
        plt.ylabel(ylabel)  # Y軸のラベルを適切なものに変更
        
    # グラフの表示
    def show_graph(self):
        plt.show()
    
    # グラフの保存
    def save_graph(self, file_name):
        plt.savefig(file_name)

