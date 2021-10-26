# Составить алгоритм решения ребуса КОТ + КОТ = ТОК (различные буквы означают различные цифры,
# старшая буква ‒ не 0).
for k in range(1, 10):
    for o in range(0, 10):
        for t in range(1, 10):
            if (k * 200 + o * 20 + t * 2) == t * 100 + o * 10 + k * 1:
                print(k, o, t, '+', k, o, t, '=', t, o, k)
else:
    print(' Для ребуса КОТ + КОТ = ТОК: решений нет')


for k in range(1, 10):
    for o in range(0, 10):
        for t in range(1, 10):
            if k * 100 + o * 10 + t * 1 + k * 100 + t * 10 + o * 1 == t * 100 + o * 10 + k * 1:
                print(' Для ребуса КОТ + КTO = ТОК:', k, t, o, '+', k, o, t, '=', t, o, k)
