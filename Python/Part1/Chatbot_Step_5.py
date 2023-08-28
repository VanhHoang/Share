import csv

f = open("data.csv")
reader = csv.reader(f)

print("Hello, What is your name ?")
name = input("Ten cua ban : ")
print("Hello : " + name)
    
print("What infor :")
question_data = input(F"{name}: ")
for Question,Answer in reader:
    if(Question!=question_data):
        print("Khong co du lieu !")
        break