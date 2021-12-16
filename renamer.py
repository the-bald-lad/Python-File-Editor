import os
os.system("cls")

def rename():
    folder = input("Enter path to directory: ")
    os.system("cls")
    print(f"WARNING, this will rename every file in the directory: {folder}!")
    name = input(f"Enter new name for files: ")

    for count, filename in enumerate(os.listdir(folder)):
        temp = filename.split(".")
        file_ext = temp[1]
        dst = f"{name} {str(count+1)}.{file_ext}"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"  
        os.rename(src, dst)
