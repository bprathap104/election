from election.citizen import Citizen
import csv

class Party:
    """
    In this class, we defines attributes & methods for a party 
    """
    def __init__(self, party_id, party_name):
        self.party_id = party_id
        self.party_name = party_name
    
class Candidate(Citizen):
    """
    In this class, we define attributes & methods for a candidate
    """
    def __init__(self, name, age, gender, aadhar, party, state_code, year_of_election):
        super().__init__(name, age, gender, aadhar)
        self.state_code = state_code
        self.year_of_election = year_of_election
        self.party = party
    def add_candidate(self):
        with open('candidate.csv', 'a',newline='\n') as ca_file:
            writer = csv.writer(ca_file)
            writer.writerow([self.state_code, self.year_of_election, self.name, self.age, self.aadhar, self.party])
        print(f'{self.name} is eligible for being a candidate')
        ca_file.close()

class Voter(Citizen):
    """
    In this class, we define attributes & methods for a voter
    """
    def __init__(self, name, age, gender, aadhar):
        super().__init__(name, age, gender, aadhar)
    def add_to_voter_list(self):
        if self.is_adult():
            print(f'{self.name} is eligible for being a voter')
        else:
            print(f'{self.name} is not elgible for being a voter')

