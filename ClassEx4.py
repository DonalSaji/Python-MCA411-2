list1 = [1, 2, 3, 4, 5]
list2 = [6,7,8,9,10]
print(list1)
print(list2)

tuple1=(10,20,30,40,50)

list3= list(tuple1)

#join list

print(list1+list2)

newlist=list1
for x in list2:
	newlist.append(x)
print(newlist)

newlist2=list1
newlist2.extend(list2)
print(newlist2)


#write a py priogram to check the string recived from the user is a palandeom or not

#val1=input("Enter the value")
#print(val1)
#print(val1[::-1])



lis1=["crist","jain"]
lis2=["college","unin"]

res= [x +" "+ y for x in lis1 for y in lis2]

print(res)

set1={1, 2, 3, 4, 5}
set2={6,7,8,9,10}
set3={10,20,30,40,50,50,30}
set4={(10,20,30,40,50),(6,7,8,9,10)}

print(type(set1))
print(type(list1))
print(type(tuple1))

print(set2.union(set2))
print(set3.intersection(set3))
print(set3.difference(set2))

print(set2.isdisjoint(set3))





"""
Create two sets of students namely java students python students,write a command for the following:
1) print students learning python
2)print students learning java
3)print students learning both java and python
4)print students learning either python or java
5)print students learning python but not java

"""
java={"a","b","c","d"}
python={"a","e","d","f"}

print(python)
print(java)
print(python.union(java))
b=python.union(java)-python.intersection(java)
print(b)
print(python.difference(java))




