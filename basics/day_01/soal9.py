# #soal 10
a = int(input('masukkan a: '))
b = int(input('masukkan b: '))
oper = input('masukkan operator: ')

def hitung(a, b, oper):
    if oper == '+':
        return a + b
    elif oper =='-':
        return a - b
    elif oper == '*':
        return a *b
    elif oper =='/':
        return a / b
print(hitung(a, b, oper))