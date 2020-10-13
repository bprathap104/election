from abc import ABC, abstractmethod
from datetime import datetime
from datetime import timedelta  
import csv

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
    def __repr__(self):
        campaign_end_date = self.date - timedelta(days=3) 
        return(f'{campaign_end_date}')
    def __str__(self):
        campaign_end_date = self.date - timedelta(days=3) 
        return(f'The Campaign End Date is : {campaign_end_date}')

class Voting:
    """
    In this calss, we define the methods & attributes required for an Election voting
    """
    def __init__(self, election_date):
        self.date = convert_string_to_date(election_date)
    def __repr__(self):
        return(f'{self.date}')
    def __str__(self):
        vote_counting_date = self.date
        return(f'The Election Date is : {vote_counting_date}')

class Counting:
    """
    In this calss, we define the methods & attributes required for an Election counting
    """
    def __init__(self, election_date):
        self.date = convert_string_to_date(election_date)
    def __repr__(self):
        vote_counting_date = self.date + timedelta(days=3) 
        return(f'{vote_counting_date}')
    def __str__(self):
        vote_counting_date = self.date + timedelta(days=3) 
        return(f'The Counting Date is : {vote_counting_date}')


class StateElection(IElection):
    """
    In this calss, we define the methods & attributes required for a StateElection
    """
    def __init__(self, state_code, state_name, election_date):
        self.date = election_date
        self.state_code = state_code
        self.state_name = state_name
        self.campaign = Campaign(self.date)
        self.voting = Voting(self.date)
        self.counting = Counting(self.date)

    def display_election_details(self):
        print(self.voting)
        print(self.campaign)
        print(self.counting)
    
    def write_to_csv(self):
        vote_counting_date=repr(self.counting).split(' ')[0]
        campaign_end_date=repr(self.campaign).split(' ')[0]
        year = self.date.split('-')[0]
        state_election_exist = self._check_state_availability_in_election_list(year)
        if state_election_exist:
            print(f'Election date for {self.state_name} already scheduled, so exiting....')
            exit(0)
        with open('state_election.csv', 'a',newline='\n') as se_file:
            writer = csv.writer(se_file)
            writer.writerow([self.state_code, self.state_name, year, self.date, campaign_end_date, vote_counting_date])
        se_file.close()
    
    def _check_state_availability_in_election_list(self,year):
        with open('state_election.csv', 'r') as se_file:
            reader = csv.reader(se_file)
            for row in reader:
                if self.state_code == row[0] and year == row[2]:
                    print(f'Election for {self.state_code} in {year} already scheduled')
                    return(True)
            return(False)
        se_file.close()




class CentralElection(IElection):
    """
    In this calss, we define the methods & attributes required for a CentralElection
    """
    def __init__(self, election_date):
        pass

def convert_string_to_date(election_date):
    date_time_obj = datetime.strptime(election_date, '%Y-%m-%d')
    return(date_time_obj)
