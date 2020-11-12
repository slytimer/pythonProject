import numpy as np
from scipy.stats import  binom
from scipy.stats import  poisson

def combinations(n, k):
    return (np.math.factorial(n)/(np.math.factorial(k)*np.math.factorial(n-k)))
#===========================HW2===============================================================================
#1
#Вероятность того, что стрелок попадет в мишень, выстрелив один раз, равна 0.8. Стрелок выстрелил 100 раз.
#Найдите вероятность того, что стрелок попадет в цель ровно 85 раз.
p = binom.pmf(85,100,.8)
print("1.The probability that the shooter will hit the target exactly 85 times is",p)

#2
#Вероятность того, что лампочка перегорит в течение первого дня эксплуатации, равна 0.0004.
# В жилом комплексе после ремонта в один день включили 5000 новых лампочек. Какова вероятность,
# что ни одна из них не перегорит в первый день? Какова вероятность, что перегорят ровно две?
#2 way
#via binom
p1 = binom.pmf(0,5000,0.0004)
p2 = binom.pmf(2,5000,0.0004)

#via poisson
lam = 5000*0.0004
p3 = poisson.pmf(0,lam)
p4 = poisson.pmf(2,lam)
print('2.1.a The probability that none of them will burn out on the first day (binom)',p1)
print('2.1.a The probability that none of them will burn out on the first day (poisson)',p3)
print('2.1.b The probability that that exactly 2 will burn out (binom)',p2)
print('2.1.b The probability that that exactly 2 will burn out (poisson)',p4)


#3
#Монету подбросили 144 раза. Какова вероятность, что орел выпадет ровно 70 раз?
p = binom.pmf(70,144,.5)
print('3 The probability that heads will come up exactly 70 times ',p)

#4
#В первом ящике находится 10 мячей, из которых 7 - белые. Во втором ящике - 11 мячей, из которых 9 белых.
# Из каждого ящика вытаскивают случайным образом по два мяча. Какова вероятность того, что все мячи белые?
# Какова вероятность того, что ровно два мяча белые? Какова вероятность того, что хотя бы один мяч белый?

#overall combinations
t1 = combinations(10, 2)
t2 = combinations(11, 2)

#4.1 Какова вероятность того, что все мячи белые?
# кол-во вариантов белых среди белых
a1 = combinations(7, 2)
a2 = combinations(9, 2)

p1=a1/t1
p2=a2/t2
# оба события должны произойти
p=p1*p2
print('4.1 Вероятность того, что все мячи белые p=',p)

#4.2 Какова вероятность того, что ровно два мяча белые?
# 3 варианта: 2 белых + 0 белых, 1 белый + 1 белый, 0 белых + 2 белых
a1 = combinations(7, 2)
a2 = combinations(2, 2)
p1=a1/t1
p2=a2/t2
pa=p1*p2
print('2 белых + 0 белых pa=',pa)


a1 = combinations(2, 2)
a2 = combinations(9, 2)
p1=a1/t1
p2=a2/t2
pb=p1*p2
print('0 белых + 2 белых pb=',pb)

a1 = combinations(7, 1)
a2 = combinations(9, 1)
b1 = combinations(3, 1)
b2 = combinations(2, 1)
p1=(a1*b1)/t1
p2=(a2*b2)/t2
pc=p1*p2
print('1 белый + 1 белый pc=',pc)

p=pa+pb+pc
print('4.2 Вероятность того, что ровно два мяча белые p=',p)

#4.3 Какова вероятность того, что хотя бы один мяч белый?
a1 = combinations(3, 2)
a2 = combinations(2, 2)
p1=a1/t1
p2=a2/t2
p=1-p1*p2
print('4.3 Вероятность того, что хотя бы один мяч белый p=',p)

#===========================HW1===============================================================================


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
p = round(1*100/t,4)
print('4 The probability that 2 purchased tickets will be winning ', p, '%')

a = combinations(2, 1)
b = combinations(2, 2)
print(a)
