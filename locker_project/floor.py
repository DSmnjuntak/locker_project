def check_locker_value(vals,x):
    if x.isdigit():
        for i in vals:
            if int(x) in vals[i]:
                return 'Locker is found. Please go to floor ' + str(i)
        return 'Locker is not found. Try other locker'
    else:
        return 'Please input a digit'

locker = {}
count_floor = 1
flag_nine = True
flag_three = False
flag_seven = False
flag_two = False
flag=False
temp = []
while(not flag):
  for i in range(1,43):
    temp.append(i)
    if flag_nine and len(temp)==9:
      locker[count_floor] = temp
      count_floor+=1
      flag_nine = False
      flag_three = True
      temp = []
    elif flag_three and len(temp)==3:
      locker[count_floor] = temp
      count_floor+=1
      flag_three = False
      flag_seven = True
      temp = []
    elif flag_seven and len(temp)==7:
      locker[count_floor] = temp
      count_floor+=1
      flag_seven = False
      flag_two = True
      temp = []
    elif flag_two and len(temp)==2:
      locker[count_floor] = temp
      count_floor+=1
      flag_two = False
      flag_nine = True
      temp = []
  # print(locker)
  print('Enter your locker:')
  x = input()
  print(check_locker_value(locker,x))