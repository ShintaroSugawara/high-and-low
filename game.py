import random

win = True

win_count = 0


while win:

   cpu_card = random.randint(1,13)
   print("CPUのカードは:",cpu_card,"です。")

   player_card = random.randint(1,13)

   print("1:High or 2:Low or 3:Break")
   high_low = int(input())
   
   while high_low != 1 and high_low != 2 and high_low != 3:
      print("1~3の数字を入力してください。")
      high_low = int(input())

   if high_low == 3:
      break

   print("あなたのカードは:",player_card,"でした。")

   if high_low == 1:
      if player_card > cpu_card:
         print("Win!!")
         win_count += 1
      elif player_card < cpu_card:
         print("Lose")
         win = False
      else:
         print("Draw")

   elif high_low == 2:
      if player_card < cpu_card:
         print("Win!!")
         win_count += 1
      elif player_card > cpu_card:
         print("Lose")
         win = False
      else:
         print("Draw")

   print("勝利回数:",win_count)

print("ゲーム終了")
print("最終勝利回数:", win_count)