 # Tuple Based Practice Problem :
'''Q1 Create a tuple with integers from 1 to 5.'''

lst = []
for i in range(1,6) :
    lst.append(i)
tup = tuple(lst)
print("Tuple containing integers from 1 to 5 :", tup)
Tuple containing integers from 1 to 5 : (1, 2, 3, 4, 5)
'''Q2 Access the third element of a tuple.'''

tup = eval(input("Enter a tuple :"))
index = int(input("Enter element number which you want to access :"))
element = tup[index-1]
print(f"Element : {element}")
Element : 3
'''Q3 Find the length of a tuple without using the `len()` function.'''

tup = eval(input("Enter a tuple :"))
count = 0
for i in list(tup) :
    count += 1
print("Length of tuple :", count)
Length of tuple : 10
'''Q4 Count the occurrences of an element in a tuple.'''

tup = eval(input("Enter a tuple :"))
element = eval(input("Enter element which you want to count occurrences :"))
count = tup.count(element)
print(f"Occurrences of {element} : {count}")
Occurrences of Berlin : 3
'''Q5 Find the index of the first occurrence of an element in a tuple.'''

tup = eval(input("Enter a tuple :"))
element = eval(input("Enter element which you want to find first occurrence :"))
index = tup.index(element)
print(f"Index of first occurrence of {element} : {index}")
Index of first occurrence of Paris : 2
'''Q6 Check if an element exists in a tuple.'''

tup = eval(input("Enter a tuple :"))
element = eval(input("Enter element to check :"))
if element in tup :
    print(f"{element} exists in tuple")
else :
    print(f"{element} does not exist in tuple")
Rio exists in tuple
'''Q7 Convert a tuple to a list.'''

tup = eval(input("Enter a tuple :"))
lst_tup = list(tup)
print("Conversion of tuple to list ", lst_tup) 
Conversion of tuple to list  ['Berlin', 'Tokyo', 'Paris', 'Berlin', 'Rio', 'Berlin']
'''Q8 Convert a list to a tuple.'''

lst = eval(input("Enter a list :"))
tup_lst = tuple(lst)
print("Conversion of list to tuple :", tup_lst) 
Conversion of list to tuple : ('Berlin', 'Tokyo', 'Paris', 'Berlin', 'Rio', 'Berlin')
'''Q9 Unpack the elements of a tuple into variables.'''

tup = eval(input("Enter a tuple :"))
a,b,c,d = tup
print("Elements of tuple into variables :")
print("Variable_1 :", a)
print("Variable_1 :", b)
print("Variable_1 :", c)
print("Variable_1 :", d)
Elements of tuple into variables :
Variable_1 : Berlin
Variable_1 : Tokyo
Variable_1 : Paris
Variable_1 : Rio
'''Q10 Create a tuple of even numbers from 1 to 10.'''

lst = []
for i in range(1,11) :
    if i%2 == 0 :
        lst.append(i)
print("Tuple of even numbers :", tuple(lst))
Tuple of even numbers : (2, 4, 6, 8, 10)
'''Q11 Create a tuple of odd numbers from 1 to 10.'''

lst = []
for i in range(1,11) :
    if i%2 != 0 :
        lst.append(i)
print("Tuple of odd numbers :", tuple(lst))
Tuple of odd numbers : (1, 3, 5, 7, 9)
'''Q12 Concatenate two tuples.'''

tup_1 = eval(input("Enter 1st tuple :"))
tup_2 = eval(input("Enter 2nd tuple :"))
tup_3 = tup_1 + tup_2
print("Concatenation of two tuples :", tup_3)
Concatenation of two tuples : (1, 2, 3, 4, 5)
'''Q13 Repeat a tuple three times.'''

tup = eval(input("Enter a tuple :"))
repeat_tup = tup * 3
print("Tuple repeated 3 times :", repeat_tup)
Tuple repeated 3 times : (1, 2, 3, 1, 2, 3, 1, 2, 3)
'''Q14 Check if a tuple is empty.'''

tup = eval(input("Enter a tuple :"))
if tup == () :
    print("Tuple is empty")
else  :
    print("Tuple is not empty ")
Tuple is not empty 
'''Q15 Create a nested tuple.'''

tup = eval(input("Create a nested tuple :"))
print("Nested tuple :", tup)
Nested tuple : ((1, 3, 5), ('Berlin', 'Rio'), 6, (True,))
'''Q16 Access the first element of a nested tuple.'''

tup = eval(input("Enter a nested tuple :"))
index = int(input("Enter element number which you want to access :"))
element = tup[index-1]
print(f"Element : {element}")
Element : (1, 3, 5)
'''Q17 Create a tuple with a single element.'''

tup = eval(input("Create a tuple with single element :"))
print("Tuple with single element :", tup)
Tuple with single element : (2,)
'''Q18 Compare two tuples.'''

tup_1 = eval(input("Enter 1st tuple :"))
tup_2 = eval(input("Enter 2nd tuple :"))
print("Tuple 1 == Tuple 2 :", tup_1 == tup_2)  
print("Tuple 1 != Tuple 2 :", tup_1 != tup_2)  
print("Tuple 1 > tTple 2 :", tup_1 > tup_2)
print("Tuple 1 < tTple 2 :", tup_1 < tup_2)  
print("Tuple 1 >= Tuple 2 :", tup_1 >= tup_2)    
print("Tuple 1 <= Tuple 2 :", tup_1 <= tup_2)  
Tuple 1 == Tuple 2 : False
Tuple 1 != Tuple 2 : True
Tuple 1 > tTple 2 : False
Tuple 1 < tTple 2 : True
Tuple 1 >= Tuple 2 : False
Tuple 1 <= Tuple 2 : True
'''Q19 Delete a tuple.'''

tup = eval(input("Enter a tuple :"))
del(tup)
print("Tuple deleted :", tup)
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
Cell In[40], line 5
      3 tup = eval(input("Enter a tuple :"))
      4 del(tup)
----> 5 print("Tuple deleted :", tup)

NameError: name 'tup' is not defined
'''Q20 Slice a tuple.'''

tup = eval(input("Enter a tuple :"))
slice_tup = tup[2:4]
print("Sliced tuple :", slice_tup)
Sliced tuple : ('Paris', 'Berlin')
'''Q21 Find the maximum value in a tuple.'''

tup = eval(input("Enter a tuple :"))
max_num = max(tup)
print("Maximum value in tuple :", max_num)
Maximum value in tuple : 6785
'''Q22 Find the minimum value in a tuple.'''

tup = eval(input("Enter a tuple :"))
min_num = min(tup)
print("Minimum value in tuple :", min_num)
Minimum value in tuple : 2
'''Q23 Convert a string to a tuple of characters.'''

string = input("Enter a string :")
tup_str = tuple(string)
print("Conversion of string to tuple of characters :", tup_str)
Conversion of string to tuple of characters : ('M', 'y', ' ', 'n', 'a', 'm', 'e', ' ', 'i', 's', ' ', 'A', 'k', 's', 'h', 'a', 't', ' ', 'S', 'a', 'x', 'e', 'n', 'a', ' ', '.')
'''Q24 Convert a tuple of characters to a string.'''

tup = eval(input("Enter a tuple :"))
str_tup = "".join(tup)
print("Conversion of tuple to a string of characters :", str_tup)
Conversion of tuple to a string of characters : My name is Akshat Saxena .
'''Q25 Create a tuple from multiple data types.'''

tup = eval(input("Create a tuple of multiple data types :"))
print("Tuple of multiple data types :", tup)
Tuple of multiple data types : (1, 'Berlin', True, False, 'Hi', 45)
'''Q26 Check if two tuples are identical.'''

tup_1 = eval(input("Enter 1st tuple :"))
tup_2 = eval(input("Enter 2nd tuple :"))
if tup_1 == tup_2 :
    print("Tuples are identical")
else :
    print("Tuples are not identical")
Tuples are identical
'''Q27 Sort the elements of a tuple.'''

tup = eval(input("Enter a tuple :"))
sorted_tup = tuple(sorted(tup))
print("Sorted tuple :", sorted_tup)
Sorted tuple : (2, 6, 45, 78, 735, 900, 6785)
'''Q28 Convert a tuple of integers to a tuple of strings.'''

int_tup = eval(input("Enter a tuple of integers :"))
str_lst = []
for i in list(int_tup) :
    str_lst += str(i)
str_tup = tuple(str_lst)
print("Tuple of strings :", str_tup)
Tuple of strings : ('1', '2', '3', '4', '5', '6')
'''Q29 Convert a tuple of strings to a tuple of integers.'''

str_tup = eval(input("Enter a tuple of strings :"))
int_lst = []
for i in list(str_tup) :
    int_lst += [int(i)]
int_tup = tuple(int_lst)
print("Tuple of integers :", int_tup)
Tuple of integers : (1, 2, 3, 4, 5, 6)
'''Q30 Merge two tuples.'''

tup_1 = eval(input("Enter 1st tuple :"))
tup_2 = eval(input("Enter 2nd tuple :"))
merge = tup_1 + tup_2
print("Merge of both tuples :", merge)
Merge of both tuples : (1, 2, 3, 4, 5, 6)
'''Q31 Flatten a nested tuple.'''

nested_tup = eval(input("Enter a nested tuple :"))
flatten_lst = []
for tup in nested_tup :
    if type(tup) != type(()) :
        flatten_lst.append(tup)
        continue
    for element in tup :
        flatten_lst.append(element)
print("Flattened nested list :", tuple(flatten_lst))
Flattened nested list : (1, 2, 3, 6, 'Berlin', 'Paris', True)
'''Q32 Create a tuple of the first 5 prime numbers.'''

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1) :
        if num % i == 0 :
            return False
    return True

n = int(input("Enter number of first prime numbers you want(max 100) :"))
prime_num_lst = [num for num in range(2, 100) if check_prime(num)][:n]

prime_num_tup = tuple(prime_num_lst)

print("Tuple of the first 5 prime numbers:", prime_num_tup)
Tuple of the first 5 prime numbers: (2, 3, 5, 7, 11)
'''Q33 Check if a tuple is a palindrome.'''    

def check_palindrome(lst) :
    if lst == lst[::-1] :
        return True
    else :
        return False

tup = eval(input("Enter a tuple :"))
result = check_palindrome(list(tup))
if result :
    print("Tuple is palindrome")
else :
    print("Tuple is not palindrome")
Tuple is palindrome
'''Q34 Create a tuple of squares of numbers from 1 to 5.'''

lst_square = list(map(lambda i : i**2 , [1,2,3,4,5]))
print("Tuple of squares :", tuple(lst_square))
Tuple of squares : (1, 4, 9, 16, 25)
'''Q35 Filter out all even numbers from a tuple.'''

tup = eval(input("Enter a tuple :"))
even_lst = []
for i in list(tup) :
    if i % 2 == 0 :
        even_lst += [i]
print("All even numbers from tuple :", tuple(even_lst))
        
All even numbers from tuple : (2, 4, 6, 8, 10)
'''Q36 Multiply all elements in a tuple by 2.'''

tup = eval(input("Enter a tuple :"))
mult_tup = tuple(map(lambda i : i*2 , tup))
print("Each element multiplied by 2 :", mult_tup)
Each element multiplied by 2 : (4, 8, 12, 16, 20)
'''Q37 Create a tuple of random numbers.'''

import random 

lst = []
n = int(input("Enter number of elements you want in tuple :"))
for i in range(n) :
    lst.append(random.randint(0,100))
print("Tuple of random numbers :", tuple(lst))
Tuple of random numbers : (95, 92, 16, 63, 2, 54)
'''Q38 Check if a tuple is sorted.'''

tup = eval(input("Enter a tuple :"))
if list(tup) == sorted(tup) :
    print("Tuple is sorted")
else :
    print("Tuple is not sorted")
Tuple is sorted
'''Q39 Rotate a tuple to the left by `n` positions.'''

tup = eval(input("Enter a tuple :"))
n = int(input("Enter number of positions to rotate tuple to the left :"))
lst = list(tup)
rotated_lst = lst[n:] + lst[0:n]
print(f"List rotated to left by {n} positions : {tuple(rotated_lst)}")
List rotated to left by 3 positions : (4, 5, 6, 7, 8, 9, 10, 1, 2, 3)
'''Q40 Rotate a tuple to the right by `n` positions.'''

tup = eval(input("Enter a tup :"))
n = int(input("Enter number of positions to rotate tuple to the right :"))
lst = list(tup)
rotated_lst = lst[:n-1:-1] + lst[0:n]
print(f"List rotated to right by {n} positions : {tuple(rotated_lst)}")
List rotated to right by 3 positions : (10, 9, 8, 7, 6, 5, 4, 1, 2, 3)
'''Q41 Create a tuple of the first 5 Fibonacci numbers.'''

def fib_num(n) :
    lst = [0,1]
    for i in range(2,n) :
        next_fib_num = lst[i-1] + lst[i-2]
        lst.append(next_fib_num)
    return lst

n = int(input("Enter number of fibnacci numbers you want :"))
lst = fib_num(n)
print("Tuple of the first ",n ,"Fibnacci numbers :", tuple(lst))
Tuple of the first  5 Fibnacci numbers : (0, 1, 1, 2, 3)
'''Q42 Create a tuple from user input.'''

tup = eval(input("Enter a tuple :"))
print("Tuple :", tup)
Tuple : (1, 2, 3, 4, 5)
'''Q43 Swap two elements in a tuple.'''

tup = eval(input("Enter a tuple :"))
ele_1 = int(input("Enter element 1 which you want to swap :"))
ele_2 = int(input("Enter element 2 which you want to swap :"))
index_1 = tup.index(ele_1)
index_2 = tup.index(ele_2)
lst = list(tup)
lst[index_1] = ele_2
lst[index_2] = ele_1
print("Tuple after updation :", tuple(lst))
Tuple after updation : (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
'''Q44 Reverse the elements of a tuple.'''

tup = eval(input("Enter a tuple :"))
lst = list(tup)
reverse_tup = tuple(lst[::-1])
print("Reversed tuple :", reverse_tup)
Reversed tuple : (10, 9, 8, 7, 6, 5, 4, 3, 2, 1)
'''Q45 Create a tuple of the first `n` powers of 2.'''

n = int(input("Enter number of n powers of 2 you want :"))
lst = []
for i in range(n) :
    lst.append(2 ** i)
print(f"Tuple of first {n} powers of 2 : {tuple(lst)}")
Tuple of first 10 powers of 2 : (1, 2, 4, 8, 16, 32, 64, 128, 256, 512)
'''Q46 Find the longest string in a tuple of strings.'''

tup = eval(input("Enter a tuple of strings :"))
longest_string = max(list(map(lambda i : len(i) , list(tup))))
for i in list(tup) :
    if len(i) == longest_string :
        print("Longest string in tuple of strings :", i)
Longest string in tuple of strings : Berlin
'''Q47 Find the shortest string in a tuple of strings.'''

tup = eval(input("Enter a tuple of strings :"))
shortest_string = min(list(map(lambda i : len(i) , list(tup))))
for i in list(tup) :
    if len(i) == shortest_string :
        print("Shortest string in tuple of strings :", i)
Shortest string in tuple of strings : Rio
'''Q48 Create a tuple of the first `n` triangular numbers.'''

def triangular_numbers(n) :
    return [i * (i+1) // 2 for i in range(1,n+1)]

n = int(input("Enter number of first n triangular numbers you want :"))
lst = triangular_numbers(n)
print(f"List of the first {n} triangular numbers : {tuple(lst)}")
List of the first 6 triangular numbers : (1, 3, 6, 10, 15, 21)
'''Q49 Check if a tuple contains another tuple as a subsequence.'''

def check_subsequence(tup , subsequence) :
    index = 0
    for i in tup :
        if i == subsequence[index] :
            index += 1
            if index == len(subsequence) :
                return True
    return False
            

tup = eval(input("Enter a tuple :"))              
subsequence = eval(input("Enter another tuple :")) 

result = check_subsequence(tup,subsequence)
if result :
    print("Tuple ccontains another tuple as subsequence")
else :
    print("Tuple does not contain another tuple as subsequence")
Tuple ccontains another tuple as subsequence
'''Q50 Create a tuple of alternating 1s and 0s of length `n`.'''

n = int(input("Enter length of tuple you want :"))
start = int(input("Do you want to start tuple with 0 or 1 :"))
lst = []
if start == 1 :
    for i in range(n) :
        lst.append(start)
        if len(lst) == n :
            break
        else :
            lst.append(0)
if start == 0 :
    for i in range(n) :
        lst.append(start)
        if len(lst) == n :
            break
        else :
            lst.append(1)
else :
    print("You entered an invalid number")

print(f"Tuple of alternating 1s and 0s of length {n} : {tuple(lst)}")
Tuple of alternating 1s and 0s of length 7 : (0, 1, 0, 1, 0, 1, 0)
 
