import os, reassign, renamer, both, rename_picker
os.system("cls")

def main():
    ask = input("Bulk rename, reassign, both or picker[RN/RS/B/P]: ").lower()
    if ask == "rn":
        renamer.rename()
    elif ask == "rs":
        reassign.reassign()
    elif ask == "b":
        both.both()
    elif ask == "p":
        rename_picker.picker()
    else:
        print("Not a valid option. Please try again")
        
if __name__ == "__main__":
    main()