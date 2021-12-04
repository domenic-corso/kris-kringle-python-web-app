from model import HintCollection
from common.InputValidationError import InputValidationError
from .AbstractDAO import AbstractDAO

class HintCollectionDAO(AbstractDAO):
    def __init__(self, file_path):
        super().__init__(file_path)

    def get(self, participant):
        raw_hint_collections = super().read_raw()

        for raw in raw_hint_collections:
            if raw['participantId'] == participant.id:
                return HintCollection(participant, raw['hints'])

        return HintCollection(participant, [])

    def add(self, participant, new_hint):
        raw_hint_collections = super().read_raw()
        target = None

        for raw in raw_hint_collections:
            if raw['participantId'] == participant.id:
                target = raw

        # Participant doesn't have existing hints - create an object for them
        if target is None:
            target = {
                'participantId': participant.id,
                'hints': []
            }

            raw_hint_collections.append(target)

        if len(target['hints']) >= 5:
            raise InputValidationError('A maximum of 5 hints is allowed.')

        target['hints'].append(new_hint)
        super().save_raw(raw_hint_collections)

        return self.get(participant)