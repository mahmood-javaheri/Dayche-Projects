# hope_weez = 0
#
# for number in range(101):
#     # hope_weez = "hope" if (number%3=0) else "weez"
#     # print(hope_weez)
#     if number % 3 == 0:
#         print("hope")
#
#     elif number % 5 == 0:
#         print('weez')
#
#     elif number % 15 == 0:
#         print('hope-weez')
#
#     else:
#       print(number)
#
# print ('*' * 40)



# hope_weez = 0
# for number in range (101) :
#      hope_weez = 'hope' if number % 3 == 0  else ""
#      hope_weez = 'weez' if number % 5 == 0 else ''
#      hope_weez = 'hope-weez' if number % 15 == 0 else number
#      print(hope_weez)

print ('*' * 40)

for number in range (101) :
     print('hope' if number % 3 == 0 else '' , 'weez' if number % 5 == 0 else '' , 'hope-weez' if number % 15 == 0 else number)

