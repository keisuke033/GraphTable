# PlotGraph

Graph Class Methods and Variables
Methods
**init**(file_name, begin_sheet_name, end_sheet_name)
Constructor method initializing the Graph class.
Parameters:
file_name: Name of the Excel file.
begin_sheet_name: Starting sheet index (subtracting 2 for internal use).
end_sheet_name: Ending sheet index.
print_data()
Method to display loaded data and graph settings.
set_graph(x, y, isXLog=False, isYLog=False, isGrid=True)
Configures the graph settings.
Parameters:
x: List of lists with sheet and column indices for x-axis.
y: List of lists with sheet and column indices for y-axis.
isXLog: Boolean (optional) - Set x-axis to logarithmic scale (default: False).
isYLog: Boolean (optional) - Set y-axis to logarithmic scale (default: False).
isGrid: Boolean (optional) - Show gridlines on the graph (default: True).
draw_graph(xlabel, ylabel, label)
Draws and plots the graph.
Parameters:
xlabel: Label for the x-axis.
ylabel: Label for the y-axis.
label: List of labels for data plotted on the graph.
show_graph()
Displays the graph.
save_graph(file_name)
Saves the graph as an image file.
Parameters:
file_name: Name for the saved image file.
Variables
file_name
Name of the Excel file.
data
List containing loaded data from Excel sheets.
begin_sheet_name
Starting sheet index adjusted for internal use.
end_sheet_name
Ending sheet index.
sheet_name
Variable to hold current sheet index during data loading.
x
List containing x-axis column names.
y
List containing y-axis column names.
sheet_number
List of sheet indices for data plotting.
length
Length of x-axis data for iteration.

グラフクラスのメソッドと変数
メソッド
**init**(file_name, begin_sheet_name, end_sheet_name)
グラフクラスのコンストラクタメソッド。
パラメータ：
file_name：Excel ファイルの名前。
begin_sheet_name：開始シートのインデックス（内部での利用のために 2 を減算）。
end_sheet_name：終了シートのインデックス。
print_data()
読み込まれたデータとグラフの設定を表示するメソッド。
set_graph(x, y, isXLog=False, isYLog=False, isGrid=True)
グラフの設定を行うメソッド。
パラメータ：
x：x 軸のシートと列のインデックスのリストのリスト。
y：y 軸のシートと列のインデックスのリストのリスト。
isXLog：ブール値（オプション） - x 軸を対数スケールに設定するかどうか（デフォルト：False）。
isYLog：ブール値（オプション） - y 軸を対数スケールに設定するかどうか（デフォルト：False）。
isGrid：ブール値（オプション） - グラフにグリッド線を表示するかどうか（デフォルト：True）。
draw_graph(xlabel, ylabel, label)
グラフを描画してプロットするメソッド。
パラメータ：
xlabel：x 軸のラベル。
ylabel：y 軸のラベル。
label：グラフ上にプロットされるデータのラベルのリスト。
show_graph()
グラフを表示するメソッド。
save_graph(file_name)
グラフを画像ファイルとして保存するメソッド。
パラメータ：
file_name：保存する画像ファイルの名前。
変数
file_name
Excel ファイルの名前。
data
Excel シートから読み込まれたデータを含むリスト。
begin_sheet_name
内部での利用のために調整された開始シートのインデックス。
end_sheet_name
終了シートのインデックス。
sheet_name
データ読み込み中の現在のシートインデックスを保持する変数。
x
x 軸の列名を含むリスト。
y
y 軸の列名を含むリスト。
sheet_number
データプロット用のシートインデックスのリスト。
length
イテレーションのための x 軸データの長さ。
