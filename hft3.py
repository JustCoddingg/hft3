# hft3
print('Galatasaray gol sayisi:')
g = int(input())  # Kullanıcıdan gelen değeri tam sayıya çeviriyoruz
print('Fenerbahçe gol sayisi:')
f = int(input())

if g > f:
    print('Galatasaray kazandı')
elif g == f:
    print('Berabere')
else:
    print('Fenerbahçe kazandı.')
