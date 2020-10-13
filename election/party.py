from election.citizen import Citizen
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
    def __init__(self, name, age, gender, aadhar, party):
        super().__init__(name, age, gender, aadhar)
        self.party = party
    def add_candidate(self):
        if self.is_adult():
            if self.is_citizen():
                print(f'{self.name} is eligible for being a candidate')
            else:
                print(f'{self.name} is not elgible for being a candiate')
        else:
            print(f'{self.name} is not elgible for being a candiate')

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

