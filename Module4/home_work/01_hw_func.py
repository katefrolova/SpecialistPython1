# Дан шестизначный номер билета. Определить, является ли билет счастливым.
# Решение реализовать в виде функции.
# Билет считается счастливым, если сумма его первых и последних цифр равны.

def lucky_ticket(ticket_number):
    ticket_number = str(ticket_number)

    left = ticket_number[:3]
    sum_left = 0
    for el in left:
        sum_left += int(el)

    right = ticket_number[3:]
    sum_right = 0
    for el in right:
        sum_right += int(el)

    return sum_left == sum_right


# Тестируем функцию
print(lucky_ticket(123006))
print(lucky_ticket(12321))
print(lucky_ticket(436751))
