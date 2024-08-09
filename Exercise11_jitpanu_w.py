number = int(input())
for x in range(number):
        print(' ' * (number - x - 1),end='')
        print('*' * (2 * x + 1))