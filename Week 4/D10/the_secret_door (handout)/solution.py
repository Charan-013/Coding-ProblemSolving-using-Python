def secretDoor(action1, action2, action3):
   a = ((action1 and action2 and action3) == True)
   b = ((action1 and action3) == True)
   c = (action2 and (action1 or action3) == True)

   return a or b or c

action1 = input() == "True"
action2 = input() == "True"
action3 = input() == "True"


print(secretDoor(action1,action2,action3))