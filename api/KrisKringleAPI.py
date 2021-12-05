import json
from os.path import abspath, join, isfile

from bottle import debug, get, put, run, request, HTTPResponse, static_file

from dataaccess import ParticipantDAO, GiverReceiverLinkDAO, HintCollectionDAO
from schema import ParticipantSchema
from common import InputValidationError

# Configure data access objects
participant_dao = ParticipantDAO(abspath('../data/participants.json'))
giver_receiver_link_dao = GiverReceiverLinkDAO(abspath('../data/mappings.json'), participant_dao)
hint_collection_dao = HintCollectionDAO(abspath('../data/hints.json'))

def respond_with_error(status, message):
    return HTTPResponse(status=status, content_type='application/json', body=json.dumps({
        'message': message
    }))

def response(status, data):
    return HTTPResponse(status=status, content_type='application/json', body=json.dumps(data))

@get('/api/participants/<participant_id>/receiver')
def get_receiver(participant_id):
    participant = participant_dao.get(participant_id)

    if participant is None:
        return respond_with_error(404, 'Unable to find Participant with ID {}'.format(participant_id))

    link = giver_receiver_link_dao.get(participant)

    if link is None:
        return respond_with_error(404, 'Unable to find a Receiver for {}'.format(participant.name))

    return response(200, ParticipantSchema(link.receiver, hint_collection_dao).to_dict())

@get('/api/participants/<participant_id>')
def create_hint(participant_id):
    participant = participant_dao.get(participant_id)

    if participant is None:
        return respond_with_error(404, 'Unable to find Participant with ID {}'.format(participant_id))

    return response(200, ParticipantSchema(participant, hint_collection_dao).to_dict())

@put('/api/participants/<participant_id>/hints')
def create_hint(participant_id):
    participant = participant_dao.get(participant_id)

    if participant is None:
        return respond_with_error(404, 'Unable to find Participant with ID {}'.format(participant_id))

    hints = request.json

    if type(hints) is not list:
        return respond_with_error(400, 'Hints not provided.')

    try:
        hint_collection_dao.set(participant, hints)

        return response(200, ParticipantSchema(participant, hint_collection_dao).to_dict())
    except InputValidationError as err:
        return respond_with_error(400, str(err))

@get('/view/<uuid>')
def view(uuid):
    return static_file('index.html', abspath('../frontend/dist'))

@get('/<path:path>')
def frontend_handler(path):
    return static_file(path, abspath('../frontend/dist'))

run(host='0.0.0.0', port=4900, server='waitress', debug=True)