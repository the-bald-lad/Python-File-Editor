import os
os.system("cls")

def reassign():
    folder = input("Enter path to directory: ")
    os.system("cls")
    print("WARNING, this could cause problems if file extention is invalid!")
    file_ext = input("Enter new file extention: ")

    for count, filename in enumerate(os.listdir(folder)):
        temp = filename.split(".")
        name = temp[0]
        dst = f"{name} {str(count+1)}.{file_ext}"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"  
        os.rename(src, dst)
