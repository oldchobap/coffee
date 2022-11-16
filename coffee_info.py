MENU = {
    "americano": {
        "ingredients": {
            "water": 250,
            "coffee": 18,
        },
        "cost": 1500,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2500,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3000,
    }
}

resources = {
    "water": 700,
    "milk": 300,
    "coffee": 200,
}

profit = 0


class Error(Exception):
  '''에러발생'''
  pass

class Coffee_error(Error):
  '''정확하게 입력해주세요'''
  pass

def pay_money() :
  while True :
    try:
      money_list = list()
      money = int(input("10000원권 수를 입력하세요"))
      money_list.append(money)
      money = int(input("5000 수를 입력하세요"))
      money_list.append(money)
      money = int(input("1000원권 수를 입력하세요"))
      money_list.append(money)
      money = int(input("500원권 수를 입력하세요"))
      money_list.append(money)
      money = int(input("100원권 수를 입력하세요"))
      money_list.append(money)
      money = int(input("50원권 수를 입력하세요"))
      money_list.append(money)
      money = int(input("10원권 수를 입력하세요"))
      money_list.append(money)
      pay_money_1 = int(money_list[0]) * 10000 + int(money_list[1]) * 5000 + int(money_list[2]) * 1000 + int(money_list[3]) * 500 + int(money_list[4]) * 100 + int(money_list[5]) * 50 + int(money_list[6]) * 10
      break
    except :
      print('정확하게 입력하세요')
  return pay_money_1

def sadf(coffee_name):
  global profit
  menu_list = []
  menu_key = []
  for i in MENU[coffee_name]:
    menu_list.append(MENU[coffee_name][i])
  for y in (menu_list[0].keys()):
    menu_key.append(y)
  cost = menu_list[1]
  answer = False
  for i in menu_key:
    if menu_list[0][i] < resources[i]:
      answer = True
    else:
      print('재료가 부족합니다')
      answer = False
  if answer == True:
    money = pay_money()
    if money >= MENU[coffee_name]['cost']:
      resources['water'] = resources['water'] - MENU[coffee_name]['ingredients']['water']
      resources['coffee'] = resources['coffee'] - MENU[coffee_name]['ingredients']['coffee']
      profit += MENU[coffee_name]['cost']
      cost = MENU[coffee_name]['cost']
      print('커피제작')
      print(f'거스름돈 {money - cost}입니다')
    else:
      print('돈없는데요')
  else:
    pass
