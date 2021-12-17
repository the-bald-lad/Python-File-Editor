import os 
import reassign
import renamer
import both
os.system("cls")

def main():
    ask = input("Bulk rename, reassign or both[RN/RS/B]: ").lower()
    if ask == "rn":
        renamer.rename()
    elif ask == "rs":
        reassign.reassign()
    elif ask == "b":
        both.both()
    else:
        print("Not a valid option. Please try again")
        
if __name__ == "__main__":
    main()