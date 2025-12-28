import csv
file_path='data_emp.csv'
def read_csv_file(file_path):
    li=[]
    with open(file_path,mode='r') as file:
        csv_reader=csv.reader(file)
        i=0
        for row in csv_reader:
            if(i>0):
                li.append({"Name":row[0],"City":row[1],"Designation":row[2], "Experience":row[3]})
            i+=1
    return li

