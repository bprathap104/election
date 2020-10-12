from abc import ABC, abstractmethod
from datetime import datetime
from datetime import timedelta  

class IElection(ABC):
    """
    In this class, we define the methods & attributes required for an election    
    """

class Campaign:
    """
    In this calss, we define the methods & attributes required for an Election camapign
    """
    def __init__(self, election_date):
        self.date = convert_string_to_date(election_date)
    def __str__(self):
        campaign_end_date = self.date - timedelta(days=3) 
        return(f'The Campaign End Date is : {campaign_end_date}')

class Voting:
    """
    In this calss, we define the methods & attributes required for an Election voting
    """
    def __init__(self, election_date):
        self.date = convert_string_to_date(election_date)
    def __str__(self):
        return(f'The Election Date is : {self.date}')

class Counting:
    """
    In this calss, we define the methods & attributes required for an Election counting
    """
    def __init__(self, election_date):
        self.date = convert_string_to_date(election_date)
    def __str__(self):
        vote_counting_date = self.date + timedelta(days=3) 
        return(f'The Counting Date is : {vote_counting_date}')


class StateElection(IElection):
    """
    In this calss, we define the methods & attributes required for a StateElection
    """
    def __init__(self, election_date):
        self.date = election_date
        self.campaign = Campaign(self.date)
        self.voting = Voting(self.date)
        self.counting = Counting(self.date)
    def display_election_details(self):
        print(self.voting)
        print(self.campaign)
        print(self.counting)

class CentralElection(IElection):
    """
    In this calss, we define the methods & attributes required for a CentralElection
    """
    def __init__(self, election_date):
        pass

def convert_string_to_date(election_date):
    date_time_obj = datetime.strptime(election_date, '%Y-%m-%d')
    return(date_time_obj)
