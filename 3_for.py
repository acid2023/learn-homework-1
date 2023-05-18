"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""
def total_and_average(items_sold):
    items_total = 0
    for item in items_sold:
        items_total += item
    items_average = items_total / len(items_sold) 
    return [items_total, items_average]

def main():
    phones =   [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
    total_phones = 0
    total_records = 0
    for product in phones:
      product_data = total_and_average(product['items_sold'])
      total = product_data[0]
      average = product_data[1]
      total_phones += total
      total_records += len(product['items_sold'])
      phone=product['product']
      print (f'суммарное количество продаж {phone} равно {total}')
      print (f'среднее количество продаж {phone} равно {average}')
      print ("--------------------------------------------------")
    total_average = total_phones / total_records
    print(f'суммарное количество продаж всех товаров равно {total_phones}')
    print(f'среднее количество продаж всех товаров равно {total_average}')
    
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    pass
    
if __name__ == "__main__":
    main()
