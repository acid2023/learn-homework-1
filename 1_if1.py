"""

Домашнее задание №1

Условный оператор: Возраст

* Попросить пользователя ввести возраст при помощи input и положить 
  результат в переменную
* Написать функцию, которая по возрасту определит, чем должен заниматься пользователь: 
  учиться в детском саду, школе, ВУЗе или работать
* Вызвать функцию, передав ей возраст пользователя и положить результат 
  работы функции в переменную
* Вывести содержимое переменной на экран

"""

def occupancy(age):
    if isinstance(age, str): age = int(age)
    if age <= 6:
        occupation = 'детский сад'
    elif age <= 17:
        occupation = 'школа'
    elif age <= 21:
        occupation = 'ВУЗ'
    elif age <= 65:
        occupation = 'работа'
    else:
        occupation = 'пенсия'
    return occupation
      

def main():
    age = input('Введите свой возраст ')
    print (age)
    occupation = occupancy (age)
    print(occupation)
if __name__ == "__main__":
    main()
