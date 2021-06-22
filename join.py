# Module 1 content
# Transition from files to DBMS

import csv
import os.path
from os import path

# Schema of Student table
col_name1 = ['Enrollment_id', 'Name', 'Address', 'Phone_no', 'Dob']
col_name2 = ['Enrollment_id', 'Department', 'Semester', 'Stipend']

if not path.exists('B:\\IIT Madras\\mod1\\Student_personal.csv'):
    f_ob1 = open('Student_personal.csv', 'a+')
    f_wr1 = csv.DictWriter(f_ob1, fieldnames=col_name1)
    f_wr1.writeheader()
    f_ob1.close()

if not path.exists('B:\\IIT Madras\\mod1\\Student_academic.csv'):
    f_ob2 = open('Student_academic.csv', 'a+')
    f_wr2 = csv.DictWriter(f_ob2, fieldnames=col_name2)
    f_wr2.writeheader()
    f_ob2.close()


# utility methods
'''
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
    '''


def searchRecord():
    search_field = input("\nEnter the column name on which you want to search record : ")
    key = input("\nEnter the value for the search field : ")
    f_obj2 = open('Student_academic.csv', 'r')
    f_obj1 = open('Student_personal.csv', 'r')
    f_reader1 = csv.DictReader(f_obj1)
    f_reader2 = csv.DictReader(f_obj2)
    if search_field in col_name1:
        outer_reader = f_reader1
        inner_reader = f_reader2
    elif search_field in col_name2:
        outer_reader = f_reader2
        inner_reader = f_reader1
    else:
        print('\n Incorrect field inserted !!!')
        return
    try:
        for record_outer in outer_reader:
            if record_outer[search_field] == key :
                for record_inner in inner_reader:
                    if record_outer['Enrollment_id'] == record_inner['Enrollment_id']:
                        temp = record_outer.copy()
                        temp.update(record_inner)
                        print(temp)
                        break

    except KeyError as e:
        print('\nWrong search field ', e, ' entered !!!')

    f_obj1.close()
    f_obj2.close()

'''
def deleteRecord():
    temp = []
    search_field = input("\nEnter the column name(search field) on the basis of which you want to delete record : ")
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


def updateRecord():
    temp = []
    search_field = input('\nEnter the column name(search field) on the basis of which you want to update record : ')
    key = input('\nEnter the value for the search field : ')
    update_field = input('\nEnter the column name which is to be updated : ')
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

'''
end = 1
print("===================================================================================")
print("\nSchema of Student_personal table :\n", col_name1)
print("\nSchema of Student_academic table :\n", col_name2)
'''
while end != 0:
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
        print("\nData deleted")
    elif choice == 5:
        updateRecord()
        print("\nData updated")
    else:
        print("\nIllegal input !!!")
    end = int(input("\nDo you want to continue ?, If Yes press 1 else press 0\n==>"))'''

searchRecord()





