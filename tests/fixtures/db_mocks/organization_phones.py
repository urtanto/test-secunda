from uuid import uuid4

from tests.fixtures.db_mocks.organizations import ORGANIZATIONS

ORGANIZATION_PHONES = (
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[0]['id'], 'number': '8-495-111-11-11'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[0]['id'], 'number': '8-800-555-00-01'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[1]['id'], 'number': '8-495-222-22-22'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[1]['id'], 'number': '8-800-555-00-02'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[2]['id'], 'number': '8-495-333-33-33'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[3]['id'], 'number': '8-495-444-44-44'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[4]['id'], 'number': '8-495-555-55-55'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[5]['id'], 'number': '8-495-666-66-66'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[6]['id'], 'number': '8-495-777-77-77'},
    {'id': uuid4(), 'organization_id': ORGANIZATIONS[7]['id'], 'number': '8-495-888-88-88'},
)
