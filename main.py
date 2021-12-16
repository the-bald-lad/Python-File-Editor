import os
os.system("cls")
folder = input("Enter path to directory: ")
print("WARNING, this will rename every file in the given directory!")
for count, filename in enumerate(os.listdir(folder)): os.rename(f"{folder}/{filename}", f"{folder}/{input(f"Enter new name for files: ")} {str(count+1)}.{filename.split(".")[1]}")