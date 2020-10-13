from election.election import StateElection, CentralElection
from election.citizen import Citizen
from election.party import Party
import json
import csv

def display_states_and_update_csv():
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

def fetch_citizen_object_list():
    citizen_list=[]
    with open('citizen.json') as citizen_file:
        citizen_json = json.load(citizen_file)
    for citizen in citizen_json['citizens']:
        citizen_list.append(Citizen(citizen['name'], citizen['age'], citizen['gender'], citizen['aadhar']))
    return(citizen_list)

def handle_input():
    while True:
        choice = input("Choice: ")
        if choice == "3":
            return False
        if(choice == "1"):
            print('Please select an option:')
            print()
            print('1) State Election Addition')
            print('2) State Election Selection')
            print('3) Show Election')
            print('4) Exit')
            sub_choice = input("Choice: ")
            if sub_choice == "4":
                exit(0)
            if sub_choice == "1":
                display_states_and_update_csv()
            if sub_choice == "2":
                pass
            if sub_choice == "3":
                try:
                    with open('state_election.csv', 'r') as se_file:
                        reader = csv.reader(se_file)
                        for row in reader:
                            print(f'{row[1]}-{row[2]}')
                    print_main_menu()
                except:
                    print('No elections created yet')
        elif(choice == "2"):
            central_election_date = input("Enter Election Date in YYYY-MM-DD:")
            ce = CentralElection(central_election_date)
        else:
            print("Invalid menu option")

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