from model import GiverReceiverLink
from .AbstractDAO import AbstractDAO

class GiverReceiverLinkDAO(AbstractDAO):
    def __init__(self, file_path, participant_dao):
        super().__init__(file_path)

        self.participant_dao = participant_dao

    def get(self, giver):
        raw_links = super().read_raw()

        for raw in raw_links:
            if raw['giverParticipantId'] == giver.id:
                return GiverReceiverLink(giver, self.participant_dao.get(raw['receiverParticipantId']))

        return None