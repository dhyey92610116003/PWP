student={
    "name":["dhyey","Rahul","Jaimin"],
    "age":[20,30,40],
    "course":["python","DBMS","DS"],
}

print(student,"\n")

print(student["name"])

print(student.get("name"))
print(student.get("city"))

student["city"]="rajkot"
print(student)

student["name"][0]="abc"
print(student)

student.pop("name")
print(student)