# num = float(input("ENTER THE VALUE : "))
# if num > 0:
#     print("THE ENTERED VALUE IS POSTIVE NUMBER :" , num)
# elif num == 0:
#     print ("THE ENTERED VALUE IS ZERO :" , num)
# else :
#     print("THE ENTERED VALUE IS NEGATIVE NUMBER :" , num)






# x = int(input("ENTER THE FIRST VALUE : "))
# y = int(input("ENTER THE SEECOND VALUE : "))
# o = x
# x = y
# y = o
# print("THE FIRST VALUE AFTER SWAPPING IS : {}  " .format(x))
# print("THE SECOND VALUE AFTER SWAPPING IS : {}  " .format(y))







# year = int(input("Enter a year: "))

# if (year % 400 == 0) and (year % 100 == 0):
#     print("{0} is a leap year".format(year))

# elif (year % 4 ==0) and (year % 100 != 0):
#     print("{0} is a leap year".format(year))

# else:
#     print("{0} is not a leap year".format(year))








# num = int(input("ENTER A NUMBER : "))
# if (num % 2) == 0:
#     print("IT'S AN EVEN NUMBER : " , num)
# else:
#     print("IT'S AN ODD NUMBER : " , num)







# width = int(input("Enter the width of rectangle : "))
# height = int(input("Enter the height of the rectangle : "))
# area = width * height
# print("The are of the Rectangle is " + str (area))





# n = int(input("Enter a Number : "))
# i = 1
# while i<=n:
#     if n%i==0:
#         print(i)
#     i = i+1





# my_str = 'OnEPIecE'
# my_str = my_str.casefold()
# rev_str = reversed(my_str)
# if list(my_str) == list(rev_str):
#    print("The string is a palindrome.")
# else:
#    print("The string is not a palindrome.")






# number = 22
# for i in range(1 ,11):
#     print(number, 'x', i, '=', number*i)






# length = int(input("Enter the Length of the Rectangle : "))
# width = int(input("Enter the Width of the Rectangle : "))
# area = length * width
# perimeter = 2 * (length * width)
# print("AREA : " , area)
# print("PERIMETER : " , perimeter)





# num = int(input("Enter a number: "))  
  
# if num < 0:
#     print("ENTER A POSITIVE NUMBER ")  
# else:  
#    sum = 0  
# while(num>0):
#     sum += num
#     num -= 1
# print("the sum is " , sum)






# num = int(input("Enter a number : "))
# sum = 0
# temp = num
# while temp > 0:
#     digit = temp%10
#     sum += digit **3
#     temp //= 10
# if num == sum:
#     print(num,"Is an armstrong number")
# else:
#     print(num,"Is not an armstrong number")






# a = int(input("Enter a number : "))
# b = int(input("Enter second number : "))
# c = int(input("Enter third number : "))
# if a>=b and a>=c:
#     print("A is the largest number : " , a)
# elif b>=a and b>=c:
#     print("B is the largest number : " , b)
# else:
#     print("C is the largest number : " , c)





# a = 2
# b = 3+4j
# c = a+b
# print("Addition value is: ", c)
# d = a-b
# print("subtraction value is : ", d)
# e = a*b
# print("multiplication value is : " ,e)
# f = a/b
# print("division value is : " , f)






# a = int(input("enter first number: "))
# b = int(input("enter second number:"))
# c = int(input("enter third number:"))
# if a>=b and a>=c:
#     print("A is the greatest:",a)
# elif b>=a and b>=c:
#     print("B is the greatest:",b)
# else:
#     print("C is the greatest:",c)







# width = int(input("ENTER THE WIDTH OF THE RECTANGLE:"))
# length = int(input("ENTER THE LENGTH OF THE RECTANGLE :"))
# area = width*length
# print("THE AREA OF THE RECTANGLE IS : " , area)




# number = int(input("ENTER THE NUMBER : "))
# for i in range(1 ,11):
#     print(number, 'x', i, '=', number*i)




# num = int(input("Enter A Value:"))
# sum=0
# for i in range(num):
#   if i%2==0:
#     sum=sum+i
# print("sum =",sum)