import os 
import reassign
import renamer
os.system("cls")

def main():
    ask = input("Bulk rename or reassign[RN/RS]: ").lower()
    if ask == "rn":
        renamer.rename()
    elif ask == "rs":
        reassign.reassign()
    else:
        print("Not a valid option. Please try again")
        
if __name__ == "__main__":
    main()