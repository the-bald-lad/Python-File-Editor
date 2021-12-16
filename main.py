import os
os.system("cls")

def main():
    file_formats = ["txt", "jpeg", "png", "html", "docx", "pptx", "csv", "mp3", "mp4", "m4a", "mid", "wav", "py"]

    folder = input("Enter path to directory: ")
    while True:
        enter = input("Enter file type to rename: ")
        if enter not in file_formats:
            print("Sorry, that file format is not accepted.")
        else:
            break
    
    name = input(f"Enter new name for file type .{enter}: ")

    for count, filename in enumerate(os.listdir(folder)):
        temp = filename.split(".")
        file_ext = temp[1]
        if file_ext == enter:
            dst = f"{name} {str(count+1)}.{file_ext}"
            src = f"{folder}/{filename}"
            dst = f"{folder}/{dst}"  
            os.rename(src, dst)

if __name__ == "__main__":
    main()