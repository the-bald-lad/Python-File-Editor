import os
os.system("cls")

def both():
    folder = input("Enter path to directory: ")
    os.system("cls")
    print(f"WARNING, this will rename every file in the directory: {folder}!")
    name = input(f"Enter new name for files: ")
    os.system("cls")
    print("WARNING, this could cause problems if file extention is invalid!")
    file_ext = input("Enter new file extention: ")

    for count, filename in enumerate(os.listdir(folder)):
        dst = f"{name} {str(count+1)}.{file_ext}"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"  
        os.rename(src, dst)