import json
from os.path import abspath
from random import choice
import sys
from uuid import uuid4

class Result:
    def __init__(self):
        self.id = str(uuid4())
        self.giver = None
        self.receiver = None

class ResultCollection:
    def __init__(self):
        self.results = []
        pass

    def add(self, result):
        self.results.append(result)

    def get_result(self, id):
        for result in self.results:
            if result.id == id:
                return result

    def is_valid(self):
        for result in self.results:
            if result.giver == result.receiver:
                return False

        return True

def create_collection(names):
    while True:
        collection = ResultCollection()
        used_receivers = []

        for name in names:
            result = Result()
            available_receivers = list(filter(lambda x: x not in used_receivers + [name], names))

            result.giver = name

            # Easy workaround for when the last person in the list has got themselves
            try:
                result.receiver = choice(available_receivers)
            except:
                continue

            used_receivers.append(result.receiver)
            collection.add(result)

        break

    if len(collection.results) != len(names):
        raise Exception('Error occurred. Please try again')

    return collection

names = sys.argv[1:]

collection = create_collection(names)
participants_file = open(abspath('data/participants.json'), 'w+')
mappings_file = open(abspath('data/mappings.json'), 'w+')
hints_file = open(abspath('data/hints.json'), 'w+')

participants = []
participant_uuid_map = {}
mappings = []
hints = []

for name in names:
    name_uuid = str(uuid4())
    participant_uuid_map[name] = name_uuid
    participants.append({
        'id': name_uuid,
        'name': name
    })

for result in collection.results:
    mappings.append({
        'giverParticipantId': participant_uuid_map[result.giver],
        'receiverParticipantId': participant_uuid_map[result.receiver],
    })

json.dump(participants, participants_file, indent=4, sort_keys=True)
json.dump(mappings, mappings_file, indent=4, sort_keys=True)
json.dump(hints, hints_file, indent=4, sort_keys=True)