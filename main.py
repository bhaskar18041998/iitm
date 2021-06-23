# Module 1 content
# Transition from files to DBMS

import csv
import os.path
from os import path

# Schema of Student table
col_name = ['Enrollment_id', 'Name', 'Address', 'Phone_no', 'Dob', 'Department', 'Semester']
if not path.exists('B:\\IIT Madras\\mod1\\Student.csv'):
    f_ob = open('Student.csv', 'a+')
    f_wr = csv.DictWriter(f_ob, fieldnames=col_name)
    f_wr.writeheader()
    f_ob.close()


# utility methods
def addRecord():
    f_obj = open('Student.csv', 'a+')
    f_writer = csv.DictWriter(f_obj, fieldnames=col_name)
    enrollment_id = input("Enter Enrollment_id of the student : ")
    name = input("Enter Name of the student : ")
    address = input("Enter Address of the student : ")
    phone_no = input("Enter Phone_no of the student : ")
    dob = input("Enter Dob of the student : ")
    department = input("Enter Department of the student : ")
    semester = input("Enter Semester of the student : ")
    f_writer.writerow({'Enrollment_id':enrollment_id ,'Name':name ,'Address': address ,'Phone_no': phone_no ,
                       'Dob': dob ,'Department': department,'Semester':semester})
    f_obj.close()


def displayStudent():
    f_obj = open('Student.csv', 'r')
    f_reader = csv.DictReader(f_obj)
    print("\n")
    for record in f_reader:
        print(record)
    f_obj.close()


def searchRecord():
    search_field = input("\nEnter the column name on which you want to search record : ")
    if search_field not in col_name:
        print("\nWrong column name !!!")
        return
    key = input("\nEnter the value for the search field : ")
    f_obj = open('Student.csv', 'r')
    f_reader = csv.DictReader(f_obj)
    try:
        for record in f_reader:
            if record[search_field] == key :
                print(record)
    except KeyError as e:
        print('\nWrong search field ', e, ' entered !!!')
    f_obj.close()
    print("\nData updated")


def deleteRecord():
    temp = []
    search_field = input("\nEnter the column name(search field) on the basis of which you want to delete record : ")
    if search_field not in col_name:
        print("\nWrong column name !!!")
        return
    key = input("\nEnter the value for the search field : ")
    f_obj = open('Student.csv', 'r')
    f_reader = csv.DictReader(f_obj)
    try:
        for record in f_reader:
            if record[search_field] != key:
                temp.append(record)
    except KeyError as e:
        print('\nWrong search field ', e, ' entered !!!')
    f_obj.close()

    f_obj = open('Student.csv', 'w+', newline='')
    f_writer = csv.DictWriter(f_obj, fieldnames= col_name)
    f_writer.writeheader()
    for data in temp:
        f_writer.writerow(data)
    f_obj.close()
    print("\nData deleted")


def updateRecord():
    temp = []
    search_field = input('\nEnter the column name(search field) on the basis of which you want to update record : ')
    if search_field not in col_name:
        print("\nWrong column name !!!")
        return
    key = input('\nEnter the value for the search field : ')
    update_field = input('\nEnter the column name which is to be updated : ')
    if update_field not in col_name:
        print("\nWrong column name !!!")
        return
    update_value = input('\nEnter the updated value of that column : ')
    f_obj = open('Student.csv', 'r')
    f_reader = csv.DictReader(f_obj)
    try:
        for record in f_reader:
            if record[search_field] == key:
                record[update_field] = update_value
            temp.append(record)
    except KeyError as e:
        print('\nWrong search field ', e, ' entered !!!')
    f_obj.close()

    f_obj = open('Student.csv', 'w+', newline='')
    f_writer = csv.DictWriter(f_obj, fieldnames=col_name)
    f_writer.writeheader()
    for data in temp:
        f_writer.writerow(data)
    f_obj.close()


end = 1
print("===================================================================================")
print("\nSchema of Student table :\n", col_name)
while end == 1:
    choice = int(input("\nFor adding a record to Student table Press 1\n" +
                       "For displaying all records in Student table Press 2\n" +
                       "For searching a record in Student table Press 3\n" +
                       "For deleting a record from student table Press 4\n" +
                       "For updating record of a student Press 5\n==> "))
    if choice == 1:
        addRecord()
        print("\nData added")
    elif choice == 2:
        displayStudent()
    elif choice == 3:
        searchRecord()
    elif choice == 4:
        deleteRecord()

    elif choice == 5:
        updateRecord()

    else:
        print("\nIllegal input !!!")
    end = int(input("\nDo you want to continue ?, If Yes press 1 else press 0\n==>"))
    if end != 0 and end != 1:
        print("\nIllegal input !!!")
        exit()




