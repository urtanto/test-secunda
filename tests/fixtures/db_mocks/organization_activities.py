from tests.fixtures.db_mocks.activities import ACTIVITIES
from tests.fixtures.db_mocks.organizations import ORGANIZATIONS

ORGANIZATION_ACTIVITIES = (
    {'organization_id': ORGANIZATIONS[0]['id'], 'activity_id': ACTIVITIES[4]['id']},
    {'organization_id': ORGANIZATIONS[1]['id'], 'activity_id': ACTIVITIES[1]['id']},
    {'organization_id': ORGANIZATIONS[2]['id'], 'activity_id': ACTIVITIES[3]['id']},
    {'organization_id': ORGANIZATIONS[3]['id'], 'activity_id': ACTIVITIES[2]['id']},
    {'organization_id': ORGANIZATIONS[4]['id'], 'activity_id': ACTIVITIES[0]['id']},
    {'organization_id': ORGANIZATIONS[5]['id'], 'activity_id': ACTIVITIES[5]['id']},
    {'organization_id': ORGANIZATIONS[6]['id'], 'activity_id': ACTIVITIES[4]['id']},
    {'organization_id': ORGANIZATIONS[6]['id'], 'activity_id': ACTIVITIES[3]['id']},
    {'organization_id': ORGANIZATIONS[7]['id'], 'activity_id': ACTIVITIES[4]['id']},
)
