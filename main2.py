# weight,height=map(eval,input().split())
# bmi=weight/(height*height)
# if bmi>0:
#     print(bmi)
# else :
#     print("invalid input")

# p=float(input())
# r=float(input())
# t=float(input())
# SI = (p*r*t)/100
# if SI < 0:
#     print("invalid input")
# else:
#     print(SI)

# import math 
# radius=float(input())
# area=math.pi*radius**2
# if radius<0:
#     print("input cant be a negative number")
# else:
#     print(area)


# distance,time=map(eval,input().split())
# acc=(2*distance)/(time**2)
# if distance <0 or time <0 :
#     print ("invalid input")
# else:
#     print(acc)


# rows = int(input())
# for i in range(0,rows):
#     if rows<0:
#         print('invalid input')
#     else:
#         print(' ' * (rows - i - 1) + '* ' * (i + 1))

# km = float(input())
# miles = 0.62*km
# if km<0:
#     print("wrong input")
# else:
#     print(miles)


# force,distance=map(eval,input().split())
# joule=force*distance
# if force <0 or distance <0 :
#     print("wrong input")
# else:
#     print(joule , "joules")


# import math 
# math.sqrt 
# x1 = int(input())
# x2 = int(input())
# y1 = int(input())
# y2 = int(input())
# point_a = ((x2-x1)**2)
# point_b = ((y2-y1)**2)
# d=(math.sqrt(point_a+point_b))
# print(d)


cents = float(input())
dollars = cents // 100
cents %= 100
quarters = cents // 25
cents %= 25
pennies = cents % 5
print(f"Dollars: {dollars}, Quarters: {quarters},  Pennies: {pennies}")






