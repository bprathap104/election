from election.election import Election
from election.citizen import Citizen
from election.party import Party
import json

citizen_list = []
party_list = []

with open('citizen.json') as citizen_file:
    citizen_json = json.load(citizen_file)

with open('party.json') as party_file:
    party_json = json.load(party_file)

for citizen in citizen_json['citizens']:
    citizen_list.append(Citizen(citizen['name'], citizen['age'], citizen['gender'], citizen['aadhar']))

for party in party_json['parties']:
    party_list.append(Party(party['party_id'], party['party_name']))

print(citizen_list)
