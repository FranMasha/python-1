x = float(input("Введите 1-ое число: "))
action = input("Введите действие (+,-,*,/): ")
if action in ("+","-","*","/"):
  y = float(input("Введите 2-ое число: "))
  if action == "+":
    print("Результат: ", x+y)
  elif action == "-":
    print("Результат: ", x-y)
  elif action == "*":
    print("Результат: ", x*y)
  elif action == "/":
    if y != 0:
      print("Результат: ", x/y)
    else:
      print("Ошибка, деление на ноль")
else:
  print("Такого действия нет")