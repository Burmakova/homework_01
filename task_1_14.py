# Для целого числа К от 1 до 9 напечатать фразу «мне К лет», учитывая при этом,
# что при некоторых значениях К слово «лет» надо заменить на слово «год» или «года».
from random import *

txt = 'лет'
k = str(randrange(1, 10))
print('Случайное число:', k)
if k in '1':
    txt = 'год'
elif k in '234':
    txt = 'года'
print(f'Мне {k} {txt}')