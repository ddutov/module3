def test_params(a=600, b=True, c='Mercedes', *days, **words):
    print(a)
    print(b)
    print(c)
    print(*days)
    print(words)
    print(f'word "dog" is number {words['dog']}')


day = ('sunday', 'monday')
animals = {'cat': 1, 'dog': 2, 'cow': 3}
test_params(500, False, 'BMW', day, **animals)
print()
print()
print()
f_ = int(input('введите число для расчета его факториала: '))


def factorial(i):
    if i == 0:
        return 1
    if i == 1:
        return 1
    if i < 0:
        return print('факториал отрицательного целого числа не определен')
    else:
        return i * factorial(i - 1)


print(f'{f_}! = {factorial(f_)}')
