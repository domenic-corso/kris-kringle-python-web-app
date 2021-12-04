from model import Participant
from .AbstractDAO import AbstractDAO

def raw_to_instance(raw):
    return Participant(raw['id'], raw['name'])

class ParticipantDAO(AbstractDAO):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get_all(self):
        raw_participants = super().read_raw()

        return list(map(raw_to_instance, raw_participants))

    def get(self, id):
        for participant in self.get_all():
            if participant.id == id:
                return participant

        return None