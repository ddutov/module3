def test():
    a = [2, 4, 6]
    b = ('sun', 'mon', 'tue')
    print(a, b)


test()


def test2(p1='111', *, p2=222, p3='str3'):
    print(p1, p2, p3)


test2('day1', p2='2.0', p3='string')
