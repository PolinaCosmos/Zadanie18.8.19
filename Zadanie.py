all_price = 0
ticket_quantity = int(input('Сколько билетов вам нужно?\n'))
for i in range(ticket_quantity):
    i += 1
    age_for_ticket = int(input(f'Введите цифрами возраст для {i} билета: '))
    if age_for_ticket < 18:
            print('Билет бесплатный')
    elif 18 <= age_for_ticket < 25:
            all_price += 990
            print('Стоимость билета - 990 руб.')
    else:
            all_price += 1390
            print('Стоимость билета - 1390 руб.')

if ticket_quantity > 3:
    all_price = all_price - ((all_price / 100) * 10)
    print(f'Сумма к оплате - {all_price} руб. (с учетом скидки 10%)')
else:
    print(f'Сумма к оплате - {all_price} руб.')