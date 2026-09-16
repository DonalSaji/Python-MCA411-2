print(ord('A'))  # Output: 65
print(chr(65))  # Output: 'A'
x="christ"
y="university"
print(x + " " + y)  # Output: 'christ university'
print(x * 3)  # Output: 'christchristchrist'
print(x[0:2])
print(x[3:6])  # Output: 'ch'
print(y[-6:-2])  # Output: 'ris'
print(y)

tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print(tuple1[1]) 
print(tuple1[2:5]) 

numbers=(10,20,10,30,40,50,20)

print(numbers[1:4])

print(len(numbers))

print(numbers.count(10))
print(numbers.index(20))
first_index = numbers.index(20)
print(numbers.index(20, first_index + 1))

list1 = [1, 2, 3, 4, 5]
list2 =["ArithmeticError", "AssertionError", "AttributeError", "EOFError", "FloatingPointError"]
list3 = [1, 2, 3, "ArithmeticError", "AssertionError", "AttributeError", "EOFError", "FloatingPointError"]

print(list1)
print(list2)
print(list3)
print(list1[0])
print(list2[1:4])
print(list3[-2:-5])

if (list1[1] is 10):
    print("True")
else:
    print("False")


#display the even numbers from the list using slicing
newlist=[1,2,3,4,5,6,7,8,9,10]
print(newlist[1:10:+2])


newlist[3]=40
print(newlist)

newlist[3:5]=[40,50]
print(newlist)


#insert the element and shift the elements to the right
newlist.insert(5, 60)
print(newlist)

#insert the element at the end of the list
newlist.append(70)
print(newlist)

#merge two lists using extend() method
newlist.extend([80, 90, 100])
print(newlist)

#remove the element from the list using remove() method
newlist.remove(60)
print(newlist)

#remove the element from the list using pop() method - using index
newlist.pop(3)
print(newlist)