import pandas as pd

class Table :
    def __init__(self, file_name, begin_sheet_name, end_sheet_name) :
        # Excelファイルを読み込む
        self.file_name = file_name  # ファイル名を適切なものに変更
        self.data = list()
        self.centering = []
        self.begin_sheet_name = begin_sheet_name -1
        self.end_sheet_name = end_sheet_name
        counter = 0
        for i in range(self.begin_sheet_name, self.end_sheet_name):
            self.centering.append('')
            self.sheet_name = i
            self.data.append(pd.read_excel(self.file_name, sheet_name=self.sheet_name))
            num_colums = len(self.data[counter].columns)  # 列数を取得
            for j in range(num_colums):
                self.centering[counter] += 'c'
            counter += 1
        
    def print_data(self):
         for i in range(len(self.data)):
            print("Sheet{} : ".format(self.begin_sheet_name + i))
            print('\n')
            print(self.data[i].head())
            print('\n')
            print(self.tex_table[i])

    def to_latex(self, index=False):
        # データをTeX形式の表に変換
        self.tex_table = list()
        for i in range(len(self.data)):
            self.tex_table.append(self.data[i].to_latex(index=False, column_format=self.centering[i]))
            self.tex_table[i] = '\\begin{table}[H]\n' + '\\centering\n' + '\\caption{}\n' + '\\label{tab:}\n' + self.tex_table[i] + '\\end{table}\n' + '\n-------------------------------------------------\n\n'

    def save_tex(self, file_name):
        # テキストファイルにTeX表を保存
        with open(file_name, 'a') as file:
            for i in range(len(self.tex_table)):
                file.write(self.tex_table[i])
    
    def delete_tex(self, file_name):
        # テキストファイルにTeX表を保存
        with open(file_name, 'w') as file:
            file.write('')

