import sys
print('', sys.argv)
if len(sys.argv) > 1:
    print(f'Переданые аргументы:{sys.argv[1:]}')
else:
    print('All')