class Node:  #Класс - узел
    def __init__(self, value=None, next=None):  #Конструктор
        self.value = value
        self.next = next

class List:  #Класс - список
    def __init__(self):  #Конструктор
        self.head = None
        self.last = None

    def __str__(self):  #Процедура для корректного вывода списка
        if self.head == None:
            return "Empty List"
        else:
            tmp = self.head
            str_out = str(tmp.value) + " "
            while tmp.next != None:
                tmp = tmp.next
                str_out = str_out + str(tmp.value) + " "
            return str_out

    def add(self, num):  #Процедура добавляет элемент в конец списка
        if self.head == None:
            self.head = self.last = Node(num)
        else:
            self.last.next = Node(num)
            self.last = self.last.next

    def find(self, num):  #Процедура поиска - ничего не выводит, только ищет, возвращает указатель на нужный элемент или None
        if self.head == None:
            print("List is Empty;", end = ' ')
            return
        elif self.head.value == num:
            return self.head
        else:
            tmp = self.head
            while tmp.next != None:
                if tmp.next.value == num:
                    return tmp
                tmp = tmp.next
        return None

    def delete(self, num):  #Процедура удаления, работает с помощью find, удаляет элемент из списка (если он есть в нём)
        tmp = self.find(num)
        if tmp == None:
            print("Number is not defined")
        elif tmp == self.head and self.head.value == num:
            self.head = tmp.next
        elif tmp.next.next == None:
            tmp.next = None
            self.last = tmp
        else:
            tmp.next = tmp.next.next

    def separate(self, num):  #Процедура разделения числа на цифры и его представления в виде списка
        if num == 0:
            self.add(0)
        else:
            while num != 0:
                self.add(num % 10)
                num //= 10
#Примеры для проверки
if __name__ == "__main__":
    p = List()
    p.add(1)
    p.add(2)
    p.add(3)
    print(p)
    p.delete(1)
    p.add(4)
    print(p)
    p.delete(3)
    p.delete(4)
    print(p)
    p.delete(50)
    p.delete(2)
    p.delete(2)
    print(p)

    vector = List()
    vector.separate(874849615165)
    print(vector)