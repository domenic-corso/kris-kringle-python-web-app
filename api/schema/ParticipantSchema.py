class ParticipantSchema:
    def __init__(self, participant, hint_collection_dao):
        self.participant = participant
        self.hint_collection_dao = hint_collection_dao

    def to_dict(self):
        return {
            'name': self.participant.name,
            'hints': self.hint_collection_dao.get(self.participant).hints
        }