import os, reassign, renamer, both, rename_picker
if os.name == 'nt':
    os.system("cls")
else:
    os.system("clear")

def main():
    ask = input("Bulk rename, Reassign, Rename and Reasign(both) or picker[RN/R/B/P]: ").lower()
    if ask == "rn": renamer.rename()
    elif ask == "rs": reassign.reassign()
    elif ask == "b": both.both()
    elif ask == "p": rename_picker.picker()
    else: print("Not a valid option. Please try again")
        
if __name__ == "__main__":
    main()