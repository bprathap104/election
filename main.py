from election.election import StateElection, CentralElection
from election.citizen import Citizen
from election.party import Party
import json

def handle_input():
    choice = input("Choice: ")
    if choice == "3":
        return False
    if(choice == "1"):
        state_election_date = input("Enter Election Date in YYYY-MM-DD:")
        se = StateElection(state_election_date)
        se.display_election_details()
    elif(choice == "2"):
        central_election_date = input("Enter Election Date in YYYY-MM-DD:")
        ce = CentralElection(central_election_date)
    else:
        print("Invalid menu option")
    return True

def print_main_menu():
    print()
    print('|--------------|')
    print('|  ElectionApp |')
    print('|      for     |')
    print('|  EC of India |')
    print('|--------------|')
    print('* * * * * * * * *')
    print('Please select an option:')
    print()
    print('1) State Election')
    print('2) Central Election')
    print('3) Exit')

def main():
    print_main_menu()
    handle_input()

if __name__ == '__main__':
    main()