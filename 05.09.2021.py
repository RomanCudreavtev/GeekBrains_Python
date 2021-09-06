print('Hello Romeo!')
#print(5 + 4 /1*5)

# x = 50
# y = 9
# x=x/y
# print (x)

# name = 'Romeo'
# sum_papers = 10
#
# is_admin= True
#
#
# print(3 < 3)
# print( 5 >= 1)
#
# age = int(input('Who are you'))
# print (age > 19)
#

# age = int(input('Who Old are you '))
#
# if age >= 18 :
#     print('Enter')
# else:
#     print('No Entrance')


# color = ''
#
# if color =='red':
#     print('Red')
# elif color == 'blue':
#     print('Blue')
# elif color == 'Green':
#     print('Green')
# else:
#     print('Did not recognize')

# num_1 = int(input())
#
# num_2 = int(input())
# #
# if  num_1 != num_2:
#     print('не равны')
#     if num_1 > num_2:
#         print('Первое больше')
#     else:
#         print('Второе Больше')
# else:
#     print('Равны')

num = int(input('Enter value from 0 - 9 : '))

while num <= 10:
    num = num + 1
    if num == 5:
        continue
        if num == 8:
            break
        print(num)
    print('end', num, 'programm')
