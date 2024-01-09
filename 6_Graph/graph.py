import networkx as nx
import matplotlib.pyplot as plt
import csv


a = ""
b = ""
w = int
rows = [[a, b, w]]

with open('F:/data_science_course/git/Lesson_19/cities.csv', 'r', newline="") as file:
    rows = list(csv.reader(file))
    list1 = []
    for i in rows:
        for l in i:
            print(l.split(';'))

            list1.append(l.split(';'))

# print(list1)
edgelist = list1
# edgelist=[['Voznesensk', 'Odesa', '3'], ['Odesa', 'Voznesensk', '3'],
#           ['Odesa', 'Kyiv', '4'], ['Kyiv', 'Odesa', '4'], ['Kyiv', 'Voznesensk', '5'],['Voznesensk', 'Kyiv',  '5'], ['Snizhne', 'Voznesensk', '3'], ['Snizhne', 'Voznesensk', '3']]


g = nx.Graph()
for edge in edgelist:
    g.add_edge(edge[0], edge[1], weight=int(edge[2]))

pos = nx.spring_layout(g)
nx.draw_networkx(g, pos)
plt.title('Граф МІСТА')
plt.show()

#пошук найкоротшого

print(nx.shortest_path(g, 'Kyiv', 'Snizhne', weight='weight'))
print(nx.shortest_path_length(g, 'Kyiv', 'Snizhne', weight='weight'))