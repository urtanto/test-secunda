from src.utils.constans import Tags

TAG_METADATA = [
    {
        'name': Tags.ORGANIZATION_V0_1,
        'description': 'Operation with organizations',
    },
    {
        'name': Tags.HEALTHZ,
        'description': 'Standard health check.',
    },
]

TITLE = 'FastAPI Test'
DESCRIPTION = 'FastAPI Test'
VERSION = '0.1'

ERRORS_MAP = {
    'mongo': 'Mongo connection failed',
    'postgres': 'PostgreSQL connection failed',
    'redis': 'Redis connection failed',
    'rabbit': 'RabbitMQ connection failed',
}
