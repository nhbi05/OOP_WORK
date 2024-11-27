subjects =["Maths","Eng","sci","sst","pe"]
marks=[]
for subject in subjects:
    mark=int(input(f"Enter the mark for {subject}:"))
    marks.append(mark)
total = sum(marks)
avg = sum(marks)/len(marks)
print(marks)
print(total)
print(avg)