"""The module contains application constants."""

COMPANY_NOT_FOUND_MSG = 'Company Not Found'
USER_NOT_FOUND_MSG = 'User not found'


class Exceptions:
    NOT_CORRECT_COORDS = 'You must provide or not all needed settings of filtering'
    NO_TYPE_FILTERING = 'You must select type of filtering'
    RADIUS_NOT_SELECTED = 'You must select radius of circle filtering'
    RECTANGLE_SIZES_NOT_DEFINED = 'You must select width and height of rectangle filtering'


class Tags:
    """Tags for API documentation."""

    ORGANIZATION_V0_1 = 'Organization | v0.1'
    HEALTHZ = 'healthz'
