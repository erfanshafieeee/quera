t = int(input())
l = []
for i in range(t):
    x_saeed, y_saeed, x_sajad, y_sajad = map(int, input().split(' '))
    if x_saeed == x_sajad and y_saeed == y_sajad:
        res = '0.000'
    elif x_saeed == x_sajad == 0:
        if y_saeed*y_sajad < 0:
            res = f'{abs(y_saeed)+abs(y_sajad)}.000'
        else:
            res = f'{abs(abs(y_saeed)-abs(y_sajad))}.000'
    elif y_saeed == y_sajad == 0:
        if x_saeed*x_sajad < 0:
            res = f'{abs(x_saeed)+abs(x_sajad)}.000'
        else:
            res = f'{abs(abs(x_saeed)-abs(x_sajad))}.000'
    else:
        saeed_not_zero = x_saeed if x_saeed != 0 else y_saeed
        sajad_not_zero = x_sajad if x_sajad != 0 else y_sajad
        res = abs(abs(saeed_not_zero)-abs(sajad_not_zero))
        addition = abs(0.25*(2*3.141592653589793 *
                       min(abs(saeed_not_zero), abs(sajad_not_zero))))
        res += addition
    l.append(res)
for i in l:
    print(i)
