#Import modules
import os
import csv

# Get directory path
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open("Results.txt","w")

# Set variable for input file
data_file = os.path.join(dir_path, "budget_data.csv")

TotalAmount = 0
#Open file
with open(data_file) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=",")

    header = next(csvreader)

    b = []
    a = []

    for row in csvreader:
        profits = int(row[1])
        TotalAmount = TotalAmount + profits    
        a.append(row[1])

    a = list(map(int, a))

    length = len(a)
    for index,value in enumerate(a,0):
        if (index > length):
            break
        else:
            c=(value-(index+1))
            b.append(c)
            avg=sum(b)/length
            max_b = max(b)
            min_b = min(b)

line1 = print("Total Months: " + str(length))       
line2 = print("Total Amount: $" + str(TotalAmount))   
line3 = print("Average Change: " + str(avg))
line4 = print("Greatest Increase in Profits:", max(b)) 
line5 = print("Least Increase in Profits:", min(b)) 

f.write("Total Months: " + str(length))   
f.write("Total Amount: $" + str(TotalAmount))   
f.write("Average Change: " + str(avg))
f.write("Greatest Increase in Profits:" + str(max_b))
f.write("Least Increase in Profits:" + str(min_b))
f.close()
