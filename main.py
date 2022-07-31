import csv

dataset_1=[]
dataset_2=[]

with open("dwarf_stars.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_1.append(row)

with open("star.csv",'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        dataset_2.append(row)

data1 = dataset_1[0]
data2 = dataset_2[0]

sd1 = dataset_1[1:]
sd2 = dataset_2[1:]

h = [data1+data2]

sd = []

for index, data_row in enumerate(sd1):
    sd.append(sd1[index] + sd2[index])

with open("merged_dataset.csv", "a+") as f:
    csvwriter = csv.writer(f)
    csvwriter.writerow(h)
    csvwriter.writerows(sd)