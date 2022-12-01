import pandas
import numpy
import matplotlib.pyplot as plt

n = 5000
# df = pandas.DataFrame({
#     'x': numpy.random.uniform(-5,5, size=n),
#     'y': numpy.random.uniform(-5,5, size=n),
#     'C': numpy.random.randint(1,9, size=n)
# })
df = pandas.DataFrame({
    'x': 2*numpy.random.randn(n),
    'y': 1 + 2*numpy.random.randn(n)
})

#df.plot.hexbin(x='x',y='y',C='C',gridsize=25,cmap='Blues')
df.plot.hexbin(x='x',y='y',gridsize=35,cmap='Blues')
plt.show()