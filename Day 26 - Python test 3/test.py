students={"Tushita" : 90, "Ron" : 85, "Aarya" : 75, "Rita" : 88, "Gowri" : 78}
total=0
for score in students.values():
    total+=score
avg=total/len(students)
top_scorer=max(students, key=students.get)
bottom_scorer=min(students, key=students.get)
print("STUDENT GRADE BOOK")
for name, score in students.items():
    print(name, ":" , score)
print("Class avg: ", avg)
print("Highest Scorer:", top_scorer)
print("Lowest Score:", bottom_scorer)
name=input("Enter a students name to check: ")
if name in students:
    print(name, "grade=", students.get(name))
else:
    print("student not there")