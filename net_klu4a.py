di = {"34": 4,
      "2": 4}

user_in = input("угадай ключ")  #
# print(di[user_in])  # сломалось если userin нету

if user_in in di:
      print(di[user_in])  # сломалось если userin нету
else:
      print("хаха такого ключа нет")

