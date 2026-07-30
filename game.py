import random

Win = True

win_count = 0


while Win:

   cpu_card = random.randint(1,13)

   print("CPUのカードは:",cpu_card,"です。")

   player_card = random.randint(1,13)

   print("1:High or 2:Low or 3:Break")

   high_low = int(input())

   if high_low == 1:
      if player_card > cpu_card:
         print("Win!!")
         win_count += 1
      elif player_card < cpu_card:
         print("Lose")
         Win = False
      else:
         print("Drow")

   if high_low == 2:
      if player_card < cpu_card:
         print("Win!!")
         win_count += 1
      elif player_card > cpu_card:
         print("Lose")
         Win = False
      else:
         print("Drow")

   if high_low == 3:
      break

   print("あなたのカードは:",player_card,"でした。")

   print("勝利回数:",win_count)