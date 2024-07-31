# # fileC:\\Users\\GOLLA SRINIVAS\\PycharmProjects\\pythonProject1\\myfile.txt"
# #
# # f=open(file,'r')="
# # c=f.read()
# # print(c)
#
# ######## Write a Python program to take user input and write it to a new text file named output.txt
# # try:
# #   # Prompt the user for input
# #   user_input = input("Enter the text you want to write to the file: ")
# #
# #   # Open the file in write mode ("w")
# #   with open("output.txt", "w") as output_file:
# #     # Write the user input to the file
# #     output_file.write(user_input)
# #
# #   print("Successfully wrote the text to output.txt!")
# #
# # except IOError:
# #   print("An error occurred while writing to the file.")
#  ####### copies one text file to another file
# # try:
# #   # Open source file in read mode ("r")
# #   with open("source.txt", "r") as source_file:
# #     # Read all lines of the source file
# #     contents = source_file.readlines()
# #
# #   # Open destination file in write mode ("w")
# #   with open("destination.txt", "w") as destination_file:
# #     # Write each line from source to destination
# #     for line in contents:
# #       destination_file.write(line)
# #
# #   print("Successfully copied contents of source.txt to destination.txt")
# #
# # except FileNotFoundError:
# #   print("Error: One or both files not found.")
# # except IOError:
# #   print("An error occurred while copying the f
# ##reading a file
# # s=open('source.txt',mode='r')
# # print(s.read())
# # s.close()
# ## writing a file
# # s=open('source.txt',mode='a')
# # s.write("hello srikamth ,how are you")
# # s.close()
# ###### reading and writing a file at a time
# # s=open('source.txt',mode='r+')
# # print(s.read())
# #
# # s.write("hello srikamth ,how are you  kaise hai")
# # s.close()
#
#
# import csv
# f=open('C:\\Users\\GOLLA SRINIVAS\\data.csv','w')
# wo=csv.writer(f,delimiter=',')
# n=int(input("enter no of students:"))
# lr=[]
# for i in range (n):
#     rn=int(input("enter the rn:"))
#     name=input("enter the name:")
#     age=int(input("enter the age"))
#     lr.append([rn,name,age,])
# wo=writerows(lr)
# f.close()
#  import Json
# def read_json(file_path):
#     with open (file_path,"r") as file:
#         data = json.read(file)
#         return data
# file_path('C:\\Users\\GOLLA \\PycharmProjects\\pythonProject1\\test.json')
# json_data=read_json(file_path)
# print(json_data)
import json

# Sample data to be written to JSON file
data = [
    {
        "name": "John Doe",
        "age": 30,
        "city": "New York"
    },
    {
        "name": "Jane Smith",
        "age": 25,
        "city": "Los Angeles"
    },
    {
        "name": "Alice Johnson",
        "age": 28,
        "city": "Chicago"
    }
]

# Define the filename
filename = 'C:\\Users\\GOLLA \\PycharmProjects\\pythonProject1\\test.json'

# Open the file in write mode and write the JSON data
with open('C:\\Users\\GOLLA \\PycharmProjects\\pythonProject1\\test.json', 'w') as file:
    json.dump(data, file, indent=4)

print(f"Data has been written to {filename}")



