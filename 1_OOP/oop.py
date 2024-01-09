#Напишіть функцію яка повертатиме назву місяця за його номером
import sys

d =  {"Січень":1, "Лютий":2, "Березень":3, "Квітень":4, "Травень":5, "Червень":6, "Липень":7, "Серпень":8, "Вересень":9, "Жовтень":10, "Листопад":11, "Грудень":12}
def get_key(d, value):
        for k, v in d.items():
            if v == value:
                return k
try:
    s = int(input("Введіть номер місяцю: "))
    if s>12:
        print("В році усього 12 місяців!")

except ValueError as ex:
    print(ex, file=sys.stderr)
    print("Ви ввели некоректне значення!", file=sys.stderr)
try:
    print(get_key(d, s))
except NameError as ex:
    print("Помилка написання не цифрового значення!", file=sys.stderr)
except Exception as ex:
    print(ex, file=sys.stderr)
    print("Упс, щось не працює - зверніться до розробників!", file=sys.stderr)

####Напишіть програму з списком чисел і перевіркою їх на унікальність
spysok= [1,3,5,87,35,3,5]
spysok=5

# print(type(spysok))
try:
    spysok= input("введіть список чисел через кому: ").split(",")
    spysok=int(spysok)
except TypeError as ex:
    print(ex, file=sys.stderr)
    print("Значення не є списком чисел", file=sys.stderr)

try:
    setspysok = set(spysok)
    if len(spysok) == len(setspysok):
        print("Усі елементи унікальні")
    else:
        print("Є однакові елементи")
except Exception as ex:
    print(ex, file=sys.stderr)
    print("Упс, щось не працює - зверніться до розробників!", file=sys.stderr)

#Напишіть користувацький клас
class MyCustomError(Exception):
    def __init__(self, *args):
        if args:
            self.message= args[0]
        else:
            self.message=None

    def __str__(self):
        print(" HAHAHAHA you are looser", file=sys.stderr)
        if self.message:
            return "MyCustomError, {0}".format(self.message)
        else:
            return "MyCustomError has been raised"

raise MyCustomError('We have a problem')

