import pandas as pd

print('Hello, world~')
print("Let's do something about pydata~")

chunker = pd.read_csv('examples/ex6.csv', chunksize=1000)
print(type(chunker))
#print(chunker.shape)
tot = pd.Series([])
for piece in chunker:
    print(type(piece))
    tot = tot.add(piece['key'].value_counts(), fill_value=0)

tot = tot.sort_values(ascending=False)
print(tot[:10])




