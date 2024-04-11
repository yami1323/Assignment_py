##1##
# num=int(input("ENTER A NUMBER : "))
# def check_e_O(number):
#     if number % 2 == 0:
#         print("IT'S EVEN NUMBER")
#     else:
#         print("IT'S ODD NUMBER")
# check_e_O(num)  


##2##
# def print_sq_dict():
#     sq_dict={num:num**2 for num in range(1,21)}
#     print(sq_dict)
# print_sq_dict()  


##3##
# def rem_vowel(string): 
# 	vowels = ['a','e','i','o','u'] 
# 	result = [letter for letter in string if letter.lower() not in vowels] 
# 	result = ''.join(result) 
# 	print(result) 
# string=input("enter text : ")
# rem_vowel(string)    


##4##
# terms=int(input("HOW MANY TERMS : "))
# result=list(map(lambda x: 2** x,range(terms)))
# print("NUMBER OF TERMS : ",terms)
# for i in range (terms):
#     print("POWER",i,"is",result[i])


##6##
# key=['a','b','c','d']
# value=[1,2,3,4]
# dictionary = dict(zip(key,value))
# print(dictionary)


##7##
# def recur_fibo(n):
#    if n <= 1:
#        return n
#    else:
#        return(recur_fibo(n-1) + recur_fibo(n-2))
# nterms = 10
# if nterms <= 0:
#    print("Plese enter a positive integer")
# else:
#    print("Fibonacci sequence:")
#    for i in range(nterms):
#        print(recur_fibo(i))


##8##
# num=6
# print("number :",num)
# def factorial(n):
#     if (n == 1 or n ==0):
#         return 1
#     else:
#         return(n * factorial(n-1))
# print("FACTORIAL : ",factorial(num))


##9##
# import time

# def measure_execution_time(func):
#     def wrapper(*args, **kwargs):
#         start_time = time.time()
#         result = func(*args, **kwargs)
#         end_time = time.time()
#         execution_time = end_time - start_time
#         print(f"Function {func.__name__} took {execution_time:.4f} seconds to execute")
#         return result
#     return wrapper
# @measure_execution_time
# def calculate_multiply(numbers):
#     tot = 1
#     for x in numbers:
#         tot *= x
#     return tot
# result = calculate_multiply([1, 2, 3, 4, 5])
# print("Result:", result)


##10##
# def divisible_5_and7(n):
#     for i in range(n+1):
#         if i % 5 ==0 and i % 7 ==0:
#             yield i
# def main():
#     n = int(input("Enter Number: "))
#     result = divisible_5_and7(n)
#     print(','.join(map(str,result)))
# if __name__ == "__main__":
#     main()   


##11##
# def even_numbers(n):
#     for num in range(n+1):
#         if num % 2 == 0:
#             yield num
# n = int(input("Enter Number: "))
# even = even_numbers(n)
# print(','.join(map(str,even)))


##12##
# def second_smallest(numbers):
#     unique_numbers=list(set(numbers))
#     unique_numbers.sort()
#     return unique_numbers[1] if len(unique_numbers) > 1 else "There is none"
# my_list =[5,2,4,3,8,10]
# print("second smallest is: ",second_smallest(my_list))


##17##
# def power_of_number(number,exponent=2):
#     return number ** exponent
# print(power_of_number(3))  

##18#
# def square_values(input_list):
#     squared_values=[ x ** 2 for x in input_list]
#     for value in squared_values:
#         print(value)
# input_list = [1,2,3,4,5]
# square_values(input_list)  


##19##
# num =int(input("Enter a number: "))
# sum=0
# for i in range(1,num +1):
#     sum +=1
#     print("The sum of all numbers from 1 to" , num,"is: ",sum)