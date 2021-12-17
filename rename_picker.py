import os
os.system("cls")

folder = input("Enter path to directory: ")
files = []

while True:
    count_ = 0
    os.system("cls")
    print(f"Directory: {folder}")
    for i in os.listdir(folder):
        if count_ in files:
            print(f"{count_+1}. {i} [X]")
        else:
            print(f"{count_+1}. {i} [ ]")
        count_ += 1
    ask = input("Enter files to be renamed or type done: ").lower()
    if ask == "done":
        break
    files.append(int(ask)-1)

print(files)
name = input(f"Enter new name for files: ")

for count, filename in enumerate(os.listdir(folder)):
    temp = filename.split(".")
    file_ext = temp[1]
    if count in files:
        dst = f"{name} {str(count+1)}.{file_ext}"
        src = f"{folder}/{filename}"
        dst = f"{folder}/{dst}"  
        os.rename(src, dst)