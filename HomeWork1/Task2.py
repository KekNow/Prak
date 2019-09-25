from Task1 import *

def sum(t1, t2):  #Функция суммирования двух чисел, представленных в виде списка в обратном порядке. Возвращает список суммы, так же в обратном порядке
    c = List()
    x = t1.value + t2.value
    c.add(x % 10)
    x //= 10
    while t1.next != None:
        t1 = t1.next
        if t2.next != None:
            t2 = t2.next
            tmp = x + t1.value + t2.value
            c.add(tmp % 10)
            x = tmp // 10
        else:
            tmp = x + t1.value
            c.add(tmp % 10)
            x = tmp // 10
    else:
        while t2.next != None:
            t2 = t2.next
            tmp = x + t2.value
            c.add(tmp % 10)
            x = tmp // 10
        if x > 0:
            c.add(1)
    return c
#Примеры для проверки
if __name__ == "__main__":
    p1 = List()
    p1.separate(10101001)
    p2 = List()
    p2.separate(99999999999)
    print(p1)
    print(p2)

    print(sum(p1.head, p2.head))