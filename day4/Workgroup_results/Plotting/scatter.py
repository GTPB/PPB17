from pylab import *

figure()
counts = [
[606, 1024, 759, 398],
[762, 912, 639, 591],
]
xdata = [2.0, 4.0, 6.0, 8.0]
ydata = counts[0]
plot (xdata, ydata, 'kd', linewidth=2)
axis([0, 10.0, 300.0, 1050.0])
savefig('scatter.png')
