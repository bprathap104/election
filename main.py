from election.election import StateElection, CentralElection
from election.citizen import Citizen
from election.party import Party, Voter, Candidate
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

def fetch_voter_list(state_code):
    voter_list = []
    with open('citizen.json') as citizen_file:
        citizen_json = json.load(citizen_file)
    for citizen in citizen_json['citizens']:
        if int(citizen['age']) >= 18 and citizen['state_code'] == state_code:
            voter_list.append(Voter(citizen['name'], citizen['age'], citizen['gender'], citizen['aadhar']))
    return(voter_list)

def fetch_state_election_list():
    try:
        with open('state_election.csv', 'r') as se_file:
            reader = csv.reader(se_file)
            for row in reader:
                print(f'{row[1]}-{row[2]}')
    except:
        print('No elections created yet')

def eligible_candidate(voter_list, candidate_aadhar):
    eligible_candidate = list(filter(lambda voter:(voter.aadhar == candidate_aadhar), voter_list))
    return(eligible_candidate)

def state_election_selection_menu():
    print('Please select an option: ')
    print('Before candidate addition first generate voter list')
    print()
    print('1) Generate Voter List')
    print('2) Candidate Addition')
    print('3) Exit')
    sub_sub_choice = input('Choice: ')
    return(sub_sub_choice)

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
            while True:
                if sub_choice == "4":
                    exit(0)
                if sub_choice == "1":
                    display_states_and_update_csv()
                if sub_choice == "2":
                    fetch_state_election_list()
                    state_code = input('Enter state code')
                    year_of_election =  input('Enter year of election:')
                    sub_sub_choice = state_election_selection_menu()
                    if sub_sub_choice == "1":
                        voter_list = fetch_voter_list(state_code)
                    if sub_sub_choice == "2":
                        candidate_aadhar = input('Enter Candidate aadhar')
                        eligiblecandidate = eligible_candidate(voter_list, candidate_aadhar)
                        if len(eligiblecandidate) == 1:
                            party_id = input('Enter Candidate representing party id')
                            candidate = Candidate(eligiblecandidate[0].name, eligiblecandidate[0].age, eligiblecandidate[0].gender, eligiblecandidate[0].aadhar, party_id, state_code, year_of_election)
                            candidate.add_candidate()
                        state_election_selection_menu()
                if sub_choice == "3":
                    fetch_state_election_list()
                    print_main_menu()
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