import csv



print("Hello, What is your name ?")
name = input("Ten cua ban : ")
print("Hello : " + name)

f = open("data.csv")
reader = csv.reader(f) 
for i in range(0,100):  
 
    print("What infor :")
    question_data = input(f"{name}: ")
    for Question, Answer in reader:
        if(Question==question_data):
            print(Answer)
            break
        else:
            print("Khong co data")
          