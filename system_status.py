import os

def system_shutdown():
    print("For close  press 'c'")
    print("For sleep press 's'.")
    
    choice = input("(c/s): ").lower()
    
    if choice == 'c':
        os.system("sudo shutdown now")  # Sistemi kapat
    elif choice == 's':
        os.system("sudo systemctl suspend")  # Uyku moduna geçir
    else:
        print("Invalid!")
        return

if __name__ == "__main__":
    system_shutdown()
