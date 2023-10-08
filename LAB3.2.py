# < Іваньо Іван >
# Лабораторна робота № 3.2
# Розгалуження, задане формулою: функція з параметрами.
# Варіант 0.6

a = int(input())
b = int(input())
c = int(input())
x = int(input())
F = ''

# Спосіб 1: розгалуження в скороченій формі

if c < 0 and b != 0:
    F = a * x ** 2 + x * b ** 2
if c > 0 and b == 0:
    F = (x + a) / (x + c)
if not(c < 0 and b != 0) and not(c > 0 and b == 0):
    F = x / c

print(F)

# Спосіб 2: розгалуження в повній формі

if c < 0 and b != 0:
    F = a * x ** 2 + x * b ** 2
elif c > 0 and b == 0:
    F = (x + a) / (x + c)
else:
    F = x / c

print(F)
