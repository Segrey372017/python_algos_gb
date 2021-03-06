"""
Задание 6.
Задание на закрепление навыков работы со стеком

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях
"""
import random

# определение класса StackPlate
class StackPlate(): # структура класса из примера к уроку
    def __init__(self, limit):
        """ Конструктор класса. Поле limit определяет количество тарелов одной стопке при превышении будет создаваться следующая """
        self.elems = [[]] # список списков
        self.limit = limit

        return 
    
    def is_empty(self):
        """ Проверка на пустоту"""
        return self.elems == [[]]
        

    def push_in(self, el):
        """ Добавление тарелки в стек
        Верхний элемент в конце списка"""
        if len(self.elems[-1]) < self.limit: # проверим заполненность стопки
            self.elems[-1].append(el)
        else:
            self.elems.append([]) # добавим новую пустую стопку
            self.elems[-1].append(el)
        return

    def pop_out(self):
        """ извлекает элемент из стопки"""
        if not self.is_empty() :
            if not self.elems[-1] == []: # проверяем стопку на пустоту
                return self.elems[-1].pop()
            else:
                self.elems.pop() # выбрасывыем пустую стопку
                return self.elems[-1].pop()
        else:
            return 

    def get_plate_val(self): 
        """возращает значение последнего записанного элемента"""
        return self.elems[-1][-1]

    
    def stack_shape(self):
        """ Возвращает общее количество тарелок, количество тарелок в каждой 
        стопке"""

        shape = []
        for itm in self.elems :
            shape.append(len(itm))
        return [sum(shape), shape] 

       
# клиентская часть

if __name__ == '__main__':

    N = 15 # количество тарелок

    plates = [random.randint(10,99) for i in range(N)] # массив тарелок

    p_stack = StackPlate(7) # экземпляр класса

    # упаковываем тарелки по стопкам

    for plate in plates:
        p_stack.push_in(plate)

    print('Стек пустой', p_stack.is_empty())

    print("форма стека", p_stack.stack_shape())

    #извлекаем элементы из стека

    while p_stack.is_empty() == False:
        print(p_stack.pop_out())

