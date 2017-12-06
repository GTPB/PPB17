from pylab import *
counts = [
[16.38, 29.03, 40.93, 142.3],
[139.9, 441.46, 202.07, 346.0, 300.0],
]
figure()
title('length of primary and secondary neuron axons')
xlabel('axon length')
ylabel('')
y1 = [1.0, 1.5, 2.0, 2.5]
y2 = [4.0, 4.5, 5.0, 5.5, 6.0]
yticks((1.75, 5.0), ("primary", "secondary"))

barh(y1, counts[0], height=0.5, color="#cccccc", label="primary")
barh(y2, counts[1], height=0.5, color="#808080", label="secondary")
legend()
axis([0, 450.0, 0, 8.0])
savefig('horizontalbar.png')
