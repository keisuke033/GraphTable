from graph import Graph

x = [[1, 0], [2, 0], [3, 0]]
y = [[1, 3], [2, 3], [3, 3]]
xlabel = "周波数 f [Hz]"
ylabel = "ゲイン G"
label = ["Rf = 100kΩ", "Rf = 30kΩ", "Rf = 10kΩ"]
data1 = Graph('~/report/experiment/D3/D3_report15/D3_report15.xlsx', 2, 4)
data1.set_graph(x, y, True)
data1.print_data()
data1.draw_graph(xlabel, ylabel, label)
data1.save_graph("graph1.png")
data1.show_graph()