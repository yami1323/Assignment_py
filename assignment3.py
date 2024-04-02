 ##1##
# a = [[6,9],
#      [2,3],
#      [23,7]]
# result = [[0,0,0],
#           [0,0,0]]
# for i in range(len(a)):
#     for j in range(len(a[0])):
#         result[j][i]=a[i][j]
# for b in result:
#     print(b)  


##2## 
# inputstr =input("enter text :")
# capitalized=inputstr.upper()
# print("first input : ",inputstr)
# print("after capitalizing : ",capitalized)     


###3###
# oddnumber=[1,3,5,7,9]
# evennumber=[2,6,8,10]
# oddnumber.append(11)
# print(oddnumber)
# evennumber.insert(2,4)
# print(evennumber)
# oddandeven=oddnumber+evennumber
# print(oddandeven)
# oddnumber.append(2.4)
# print(oddnumber)
# oddnumber.remove(2.4)
# print(oddnumber)
# evennumber.insert(3,4)
# print(evennumber)
# poppedeve=evennumber.pop(3)
# print(poppedeve)
# sls=oddnumber[1:4]
# print(sls)
# print(evennumber[4])        


##4##
# d1={1:'a',2:'b',3:'c',4:'d'}
# d2={'a':1,'b':2,'c':3,'d':4}
# d1d2=(d1|d2)
# print(d1d2)

##5##
# myd={'name': 'Yami','age': 22,'city':'Alappuzha'}
# #accessing
# print(myd['name'])
# #modifying/adding
# myd['occupation']='Student'
# myd['city']='kochi'
# # print(myd)
# #removing
# # remmyd=myd.pop('age')
# # print(myd)
# #key/value/item
# key=myd.keys()
# values=myd.values()
# items=myd.items()
# print(myd)
# print(key)
# print(values)
# print(items)
# #to check if a key exists
# if 'city' in myd:
#     print("city is given")


##6##
# def sumlist(list):
#     sum=0
#     for i in range(len(list)):
#         sum = sum+list[i]
#     return sum
# list = [10, 9, 7, 5]
# print(list)
# print("sum of list: ",sumlist(list))


##7##
# def generate_dictionary(n):
#     dictionary = {i: i * 1 for i in range(1, n + 1)}
#     return dictionary

# def main():
#     n = int(input("Enter the value of n: "))
#     result_dict = generate_dictionary(n)
#     print("Generated Dictionary:")
#     print(result_dict)
# if __name__ == "__main__":
#     main()


##8##
# str = input("enter text : ")
# digit=letter=0
# for ch in str:
#    if ch.isdigit():
#       digit=digit+1
#    elif ch.isalpha():
#       letter=letter+1
#    else:
#       pass
# print("Letters:", letter)
# print("Digits:", digit)


##9##
# numbers = [1, 2, 3, 4, 5]
# doubled_numbers = list(map(lambda x: x * 2, numbers))
# print(doubled_numbers)

# strings = ["1", "2", "3", "4", "5"]
# numbers = list(map(int, strings))
# print(numbers)

# numbers = [1, 2, 3, 4, 5]
# odds = list(filter(lambda x: x % 2 != 0, numbers))
# print(odds)


##10##
# ls=[x**2 for x in range(10)]
# print(ls)


##11##
# dc={x**2 for x in range(12)}
# print(dc)  


##12##
# lst=[]
# n=int(input("how many numbers:"))
# for num in range(n):
#     nm=int(input("enter number:"))
#     lst.append(nm)
# print("largest: ",max(lst))
# print("smallest: ",min(lst))


##13##
# number=[12,13,67,89,88,123,234,678,345,88]
# number=[x for x in number if x % 2 != 0]
# print(number)


##14##
# def print_values():
#     l=list()
#     for x in range(1,31):
#         l.append(x**2)
#     print(l[:5])
#     print(l[-5:])
# print_values()


##15##
# prefix = 'pet: '
# pets = ['cat', 'dog', 'mouse']
# prefixed_pets = [prefix + pet for pet in pets]
# print(prefixed_pets)


##16##
# list1 = [1, 2, 3, 4]
# list2 = ['a', 'b', 'c', 'd']

# # Assuming both lists are of the same length
# for i in range(len(list1)):
#     print(list1[i], list2[i])


# ##17##
# d = {0: 10, 1: 20}
# print(d)
# d.update({2: 30})
# print(d) 


##18##
# dic1 = {1:10,2:20}
# dic2 = {3:30,4:40}
# dic3 = {5:50,6:60}
# dic4 = {}
# for d in (dic1, dic2, dic3):
#     dic4.update(d)
# print(dic4) 


##19##
# dict1 = {'a': 1, 'b': 2, 'c': 3}
# dict2 = {'x': 10, 'y': 20, 'z': 30}
# for key1, value1 in dict1.items():
#     for key2, value2 in dict2.items():
#         print("Dict1 key:", key1, ", Dict1 value:", value1)
#         print("Dict2 key:", key2, ", Dict2 value:", value2)
#         print()  


##20##
# dic={ 'x':455, 'y':223, 'z':300, 'p':908 }
# print("Dictionary: ", dic)
# print("sum: ",sum(dic.values()))


##21##
# pets={'Fighter_Fish':'iker','Cat':'Mittu','Fish':'Kuroo'}
# for name, animal in pets.items():
#     print(f"{name} is  {animal}.")


##22##
# def create_new_dict(subject_marks):
#     new_dict = {}
#     for subject,mark in subject_marks.items():
#         if mark > 50:
#             new_dict[subject] = mark
#     return new_dict
# marks = {'English': 72,'Maths':38,'Hindi':56,'Chemistry':42,'physics':51}
# new_dict = create_new_dict(marks)
# print(new_dict)


##23##
# sentence=input("Enter the sentence : ")
# def count_letters_digit(sentence):
#     letter =0
#     digit =0
#     for char in sentence:
#         if char.isalpha():
#             letter +=1
#         elif char.isdigit():
#             digit +=1
#     return {'letter':letter,'digit':digit}
# result=count_letters_digit(sentence)
# print(result)


##24##
# n = 5
# def generate_square_dict(n):
#     square_dict ={}
#     for i in range(1,n+1):
#         square_dict[i]=i*i
#     return square_dict
# result=generate_square_dict(n)
# print(result)


##25##
# my_l=[1,10,2,9,3,8,4,7,5,6]
# sum_l=sum(my_l)
# print("sum of list elements : ",sum_l)
# average=sum(my_l)/len(my_l)
# print("Average of list elements :",average)
# maximum = max(my_l)
# print("Maximum of list elements :",maximum)
# minimum = min(my_l)
# print("Minimum of list element :",minimum)  


##26##
# s1={1,2,3,4,5,6,7,8,9}
# s2={9,8,7,6,5,4,3,2,1}
# print("Union :", s1.union(s2))
# print("Intersection :", s1.intersection(s2))
# print("is s1 subset of s2 :",s1.issubset(s2))


##27##
# squares=[x ** 2 for x in range(1,11)]
# print(squares)  


##28##
# tu_ple=()
# int_tup=(1,3,5,7,9)
# new_tup=(12,'hi',22.14,'hello')
# print(tu_ple)
# print(int_tup)
# print(new_tup)


##29##
# t1=(1,2,3,4,5)
# t2=(6,7,8,9,10)
# t1t2=t1+t2
# print(t1t2)
# multiplied_t1t2=t1t2*2
# print(multiplied_t1t2)
# element_3=t1t2[2]
# print(element_3)


##30##
# new_tup=(1,1,1,2,3,5,6,4,5,7,7,5)
# c_tup=new_tup.count(5)
# print("number of times : ",c_tup)
# index_tup=new_tup.index(7)
# print("index : ",index_tup)