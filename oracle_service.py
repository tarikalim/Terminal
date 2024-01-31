import os
import sys

def manage_oracle_service(action):
    if action == 'start':
        os.system('sudo systemctl start oracle-xe')
    elif action == 'stop':
        os.system('sudo systemctl stop oracle-xe')
    else:
        print("invalid.")

def main():
    choice = input("Start or stop oracle xe service start/stop: ").lower()
    manage_oracle_service(choice)

if __name__ == "__main__":
    main()
