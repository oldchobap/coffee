import os
from coffee_info import *

while True:
  try:
    coffee_name = input('어떤 커피를 원하세요? (아메리카노/라떼/카푸치노')
    if coffee_name == '아메리카노':
      coffee_name = 'americano'
      sadf(coffee_name)
      break
    elif coffee_name == '라떼':
      coffee_name = 'latte'
      sadf(coffee_name)
      break
    elif coffee_name == '카푸치노':
      coffee_name = 'cappuccino'
      sadf(coffee_name)
      break
    elif coffee_name == 'off':
      print('사용을 중단합니다')
      break
    elif coffee_name == 'report':
      print(resources)
      break
    elif coffee_name == '재료추가':
      print(resources)
      while True:
        try:
          add_water = int(input('물을 얼마나 추가하시겠습니까?'))
          add_milk = int(input('우유를 얼마나 추가하시겠습니까?'))
          add_coffee = int(input('커피를 얼마나 추가하시겠습니까?'))
          break
        except:
          print('숫자로 입력하세요')
      resources['water'] += add_water
      resources['milk'] += add_milk
      resources['coffee'] += add_coffee
    else:
      raise Coffee_error
  except Coffee_error:
    print('정확하게 입력해주세요')
  break    
print(f'수익 : {profit} \n 남은 재료 : {resources}')