import numpy as np

def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))
#Из колоды в 52 карты извлекаются случайным образом 4 карты.
# a) Найти вероятность того, что все карты – крести
a = combinations(13, 4)
t = combinations(52, 4) #overall combinations
p = round(a*100/t,2)
print('1.a The probability that all cards are cross ',p, '%')

#б) Найти вероятность, что среди 4-х карт окажется хотя бы один туз.
#first solution
#find all combinations for aces
a1=combinations(4, 1)
a2=combinations(4, 2)
a3=combinations(4, 3)
a4=combinations(4, 4)

#find all combinations for the remainig cards
b1=combinations(48,3)
b2=combinations(48,2)
b3=combinations(48,1)

p=round((a1*b1+a2*b2+a3*b3+a4)*100/t,2)
print('1.b.1 The probability that among 4 cards there will be at least one ace ',p, '%')

#second solution
#find all combinations without aces
a=combinations(48,4)
p=round((1-a/t)*100,2)
print('1.b.2 The probability that among 4 cards there will be at least one ace ',p, '%')

#-------------------------------------------------------------------------------------------------
#На входной двери подъезда установлен кодовый замок, содержащий десять кнопок с цифрами от 0 до 9.
# Код содержит три цифры, которые нужно нажать одновременно.
# Какова вероятность того, что человек, не знающий код, откроет дверь с первой попытки?

t = combinations(10, 3) #overall combinations
#let's say only one code is correct
p = round(100/t,2)
print('2 The probability that a person who does not know the code will open the door on the first try ',p, '%')

#-------------------------------------------------------------------------------------------------
#В ящике имеется 15 деталей, из которых 9 окрашены. Рабочий случайным образом извлекает 3 детали.
# Какова вероятность того, что все извлеченные детали окрашены?

t = combinations(15, 3) #overall combinations
a = combinations(9, 3) #all painted combinations
p = round(100*a/t,2)
print('3 The probability that all extracted parts are painted ',p, '%')

#-------------------------------------------------------------------------------------------------
#В лотерее 100 билетов. Из них 2 выигрышных. Какова вероятность того, что 2 приобретенных билета окажутся выигрышными?

t = combinations(100, 2) #overall combinations
p = round(100*2/t,4)
print('4 The probability that all extracted parts are painted ', p, '%')

print(t)
print(a1,a2,a3,a4)
print(b1,b2,b3)