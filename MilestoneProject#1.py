import sys
Numbered_List = [1,2,3,4,5,6,7,8,9]
#This List Monitors all possible moves for the two Players
row1 = [{ }, { }, { }]
row2 = [{ }, { }, { }]
row3 = [{ }, { }, { }]
seperation = '--------------'

def Display():
  print(row1)
  print(seperation.strip())
  print(row2)
  print(seperation.strip())
  print(row3)
def Directions():
  print("\nIf you Enter 1, Your Token Will be Inserted To The Top Left Box.\nFrom there the order goes left to right, and up to down.")
def Players_Choose_Their_Tokens():
  global Player_1
  Player_1=input('Which token Does Player 1 Want?\nO or X?')
  if Player_1 != 'X' and Player_1 != 'O':
      sys.exit("Enter Either O or X. Click Run To Try Again.")
  else:
      pass
  global Player_2
  if Player_1 == 'O':
      Player_2 = 'X'
  else:
      Player_2 = 'O'
  print(f"Player 1 is {Player_1} and Player 2 is {Player_2}" )
def User_Input_Player_1():
  Player_1_Answer = input('Player 1 - Please Enter One Number from 1 through 9 To Determine Where You Want To Place Your Token.')
  try:
    int(Player_1_Answer)
  except ValueError:
    sys.exit("Enter An Integer. Click Run To Try Again.")
  else:
    pass
  while int(Player_1_Answer) in Numbered_List:
    for possible_answer in Numbered_List:
      if int(Player_1_Answer) == possible_answer:
        Numbered_List.remove(possible_answer)
        global Answer
        Answer = possible_answer
        return
      else:
        continue
  else:
    sys.exit("Please Enter A Number Not Used Already or A Number From 1 - 9. Click Run To Try Again.")
def User_Input_Player_2():  
  Player_2_Answer = input('Player 2 - Please Enter One Number from 1 through 9 To Determine Where You Want To Place Your Token.')
  try:
    int(Player_2_Answer)
  except ValueError:
    sys.exit("Enter An Integer. Click Run To Try Again.")
  while int(Player_2_Answer) in Numbered_List:
    for possible_answer2 in Numbered_List:
      if int(Player_2_Answer) == possible_answer2:
        Numbered_List.remove(possible_answer2)
        global Answer_2
        Answer_2 = possible_answer2
        return
    else:
        continue
  else:
    sys.exit("Please Enter A Number Not Used Already. Click Run To Try Again.")
def New_Display_Player_1():
  try:
    Answer
  except NameError:
    sys.exit("Please Enter A Number From 1 through 9. Click Run To Try Again.")
  else:
    pass
  if Answer == 1:
    del row1[0]
    row1.insert(0,Player_1)
  elif Answer == 2:
    del row1[1]
    row1.insert(1,Player_1)
  elif Answer == 3:
    del row1[2]
    row1.insert(2,Player_1)
  elif Answer == 4:
    del row2[0]
    row2.insert(0,Player_1)
  elif Answer == 5:
    del row2[1]
    row2.insert(1,Player_1)
  elif Answer == 6:
    del row2[2]
    row2.insert(2,Player_1)
  elif Answer == 7:
    del row3[0]
    row3.insert(0,Player_1)
  elif Answer == 8:
    del row3[1]
    row3.insert(1,Player_1)
  else:
    del row3[2]
    row3.insert(2,Player_1)
  Display()
def New_Display_Player_2():
  try:
    Answer
  except NameError:
    sys.exit("Please Enter A Number From 1 through 9. Click Run To Try Again.")
  if Answer_2 == 1:
    del row1[0]
    row1.insert(0,Player_2)
  elif Answer_2 == 2:
    del row1[1]
    row1.insert(1,Player_2)
  elif Answer_2 == 3:
    del row1[2]
    row1.insert(2,Player_2)
  elif Answer_2 == 4:
    del row2[0]
    row2.insert(0,Player_2)
  elif Answer_2 == 5:
    del row2[1]
    row2.insert(1,Player_2)
  elif Answer_2 == 6:
    del row2[2]
    row2.insert(2,Player_2)
  elif Answer_2 == 7:
    del row3[0]
    row3.insert(0,Player_2)
  elif Answer_2 == 8:
    del row3[1]
    row3.insert(1,Player_2)
  else:
    del row3[2]
    row3.insert(2,Player_2)
  Display()
def Check_Diagnols():
  if row1[0] == row2[1] and row2[1] == row3[2]:
    if row1[0] == {}:
      return
    elif Player_1 == row1[0]:
      sys.exit("Player 1 Wins!")
    else:
      sys.exit('Player 2 Wins!')
  elif row1[2] == row2[1] and row2[1] == row3[0]:
    if row1[2] == {}:
      return
    elif Player_1 == row1[2]:
      sys.exit('Player 1 Wins!')
    else:
      sys.exit("Player 2 Wins!")
  else:
    return
def Check_Horizontals():
  if row1[0] == row1[1] and row1[1] == row1[2]:
    if row1[0] == {}:
      return
    elif row1[0] == Player_1:
      sys.exit("Player 1 Wins!")
    else:
      sys.exit('Player 2 Wins!')
  elif row2[0] == row2[1] and row2[1] == row2[2]:
    if row2[0] == {}:
      return
    elif row2[0] == Player_1:
      sys.exit("Player 1 Wins!")
    else:
      sys.exit('Player 2 Wins!')
  elif row3[0] == row3[1] and row3[1] == row3[2]:
    if row3[0] == {}:
      return
    elif row3[0] == Player_1:
      sys.exit("Player 1 Wins!")
    else:
      sys.exit('Player 2 Wins!')
  else:
    return
def Check_Verticals():
  if row1[0] == row2[0] and row2[0] == row3[0]:
    if row1[0] == {}:
      return
    elif Player_1 == row1[0]:
      sys.exit("Player 1 Wins!")
    else:
      sys.exit("Player 2 Wins!")
  elif row1[1] == row2[1] and row2[1] == row3[1]:
    if row1[1] == {}:
      return
    elif Player_1 == row1[1]:
      sys.exit("Player 1 Wins!")
    else:
      sys.exit("Player 2 Wins!")
  elif row1[2] == row2[2] and row2[2] == row3[2]:
    if row1[2] == {}:
      return
    elif Player_1 == row1[2]:
      sys.exit("Player 1 Wins!")
    else:
      sys.exit("Player 2 Wins!")
  else:
    return
Players_Choose_Their_Tokens()
Directions()
Display()
for i in range(4):
  User_Input_Player_1()
  New_Display_Player_1()
  Check_Diagnols()
  Check_Horizontals()
  Check_Verticals()
  User_Input_Player_2()
  New_Display_Player_2()
  Check_Diagnols()
  Check_Horizontals()
  Check_Verticals()
sys.exit('Its a Tie!')
