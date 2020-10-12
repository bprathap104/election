from election.election import StateElection, CentralElection
from election.citizen import Citizen
from election.party import Party
import json

def display_states():
    with open('state.json') as state_file:
        state_json = json.load(state_file)
    counter = 1
    for state in state_json['states']:
        print(f'{state["state_id"]}: {state["state_name"]}')
    state_code = input("Enter State Code:")
    state_name_list = list(filter(lambda state:(state["state_id"]==state_code), state_json['states']))
    if len(state_name_list) > 0:
        state_name = state_name_list[0].get('state_name')
    else:
        print(f'Enter proper state code')
        exit(0)
    state_election_date = input("Enter Election Date in YYYY-MM-DD:")
    print(f'{state_code},{state_name}')
    se = StateElection(state_code, state_name, state_election_date)
    se.display_election_details()
    se.write_to_csv()

def handle_input():
    choice = input("Choice: ")
    if choice == "3":
        return False
    if(choice == "1"):
        display_states()
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