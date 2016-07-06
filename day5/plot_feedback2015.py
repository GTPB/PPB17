'''
out = open('finger_data/feedback_data.txt', 'w')

data = [
    ['unix', 0, 2, 3, 10, 3],
    ['python_shell', 0, 1, 4, 12, 1],
    ['python_programs', 0, 0, 9, 7, 1],
    ['parsing', 0, 5, 11, 2, 1],
    ['functions', 1, 6, 4, 6, 2],
    ['debugging', 0, 0, 0, 13, 5],
    ['data_columns', 3, 1, 8, 5, 1],
    ['tabular_data', 1, 1, 9, 7, 1],
    ['searching', 0, 5, 8, 2, 3],
    ['pipelines', 0, 1, 8, 5, 2],
    ['python_libraries', 0, 0, 4, 12, 2]
    ]


for row in data:
    line = row[0]
    for column in row[1:]:
        line = line + '\t' + str(column)
    line = line + '\n'
    out.write(line)

out.close()

'''

from pylab import figure, title, xlabel, ylabel, xticks, bar, \
                  legend, axis, savefig

import matplotlib.pyplot as plt


modules = ['unix', 'pythonshell', 'programs',
           'parsing', 'functions', 'debugging',
           'datacolumns', 'tabulardata','searching',
           'pipelines', 'libraries' 
          ] 
counts = [[0, 0, 0, 0, 1, 0, 3, 1, 0, 0, 0],
         [2, 1, 0, 5, 6, 0, 2, 1, 5, 1, 0],
         [3, 4, 9, 11, 4, 0, 8, 9, 8, 8, 4],
         [10, 12, 7, 2, 6, 13, 5, 7, 2, 5, 12],
         [3, 1, 1, 1, 2, 5, 1, 1, 3, 2, 2]  
         ]

figure()
title('Feedback distribution in TGAC2015 Python course')
xlabel('module')
ylabel('finger count')

x1 = [2.0, 5.0, 8.0, 11.0, 14.0, 17.0, 
     20.0, 23.0, 26.0, 29.0, 32.0]
x2 = [x - 0.5 for x in x1]
x3 = [x - 1.0 for x in x1]
x4 = [x - 1.5 for x in x1]
x5 = [x - 2.0 for x in x1]

xticks(x2, modules)

bar(x1, counts[4], width=0.5, color="#0000FF", label="5")
bar(x2, counts[3], width=0.5, color="#808080", label="4")
bar(x3, counts[2], width=0.5, color="#FF0000", label="3")
bar(x4, counts[1], width=0.5, color="#CCEEFF", label="2")
bar(x5, counts[0], width=0.5, color="#00FF00", label="1")

legend()
axis([0.0, 35.0, 0, 16])
savefig('barplot.png')
plt.show()

