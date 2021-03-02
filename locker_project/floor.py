def check_locker_value(x):
    locker = {}
    count_floor = 1
    flag_nine = True
    flag_three = False
    flag_seven = False
    flag_two = False
    temp = []
    if x.isdigit():
      for i in range(1,int(x)+1):
        temp.append(i)
        locker[count_floor] = temp
        if flag_nine and len(temp)==9:
          count_floor+=1
          flag_nine = False
          flag_three = True
          temp = []
        elif flag_three and len(temp)==3:
          count_floor+=1
          flag_three = False
          flag_seven = True
          temp = []
        elif flag_seven and len(temp)==7:
          count_floor+=1
          flag_seven = False
          flag_two = True
          temp = []
        elif flag_two and len(temp)==2:
          count_floor+=1
          flag_two = False
          flag_nine = True
          temp = []
      for i in locker:
          if int(x) in locker[i]:
              return 'Locker is found. Please go to floor ' + str(i)
      return 'Locker is not found. Try other locker'
    else:
        return 'Please input a digit'


flag=False
while(not flag):
  print('Enter your locker:')
  x = input()
  print(check_locker_value(x))
  # print(locker)