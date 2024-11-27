pe = int(input("Enter the Sales for pe :"))
sci = int(input("Enter the Sales for Science :"))
eng = int(input("Enter the Sales for English :"))
maths = int(input("Enter the Sales for Maths :"))
sst = int(input("Enter the Sales for SSt :"))

score={
    "pe":pe,
    "sci":sci,
    "eng":eng,
    "maths":maths,
    "sst":sst,
    
}

total = sum(score.values())
avg=sum(score.values())/len(score)
print(score)
print(total)
print(avg)
#grade
if avg >= 80 and avg <= 100:
    print("A")
elif avg >= 70 and avg <= 79:
    print("B")
elif avg >= 60 and avg <= 69:
    print("C")
else:
    print("F")



