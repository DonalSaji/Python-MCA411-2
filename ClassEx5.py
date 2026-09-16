student={"name": "John", "age": 20, "grade": "A"}
print(student["name"])  # Output: John
print(student["age"])   # Output: 20
print(student["grade"]) # Output: A
print(student)
#print(student[marks])
print(student.get("marks"))
print(student.get("name"))
print(student)

student.update({"marks":90})
print(student)

print(student.items())
for key,value in student.items():
	print(key, ':', value)

print("remove:", student.pop("age"))
print("remove items:", student.popitem())
print("clear:", student.clear())


#writer the coed for find the even numbers

numbers=[1,2,3,4,5,6]
even_sqr={n:n*n for n in numbers if n% 2==0}
print(even_sqr) 


students={"2647256":{"name":"Donal","marks":{"Python":85,"DBMS":90,"AI":88}},
         "2647257":{"name":"jose","marks":{"Python":92,"dbms":82,"AI":95}}}

print(students["2647257"]["marks"]["AI"])
print()

marks=students["2647256"]["marks"]
print(marks)

avg=sum(marks.values())/len(marks)
print(avg)