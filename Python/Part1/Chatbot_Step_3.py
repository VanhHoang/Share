import csv

f = open("data.csv")
reader = csv.reader(f)

for question, answer in reader:
    print(question)
    print(answer)