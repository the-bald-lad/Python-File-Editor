import os
os.system("cls")

folder = input("Enter path to directory: ")

for i in os.listdir(folder):
    print(i)