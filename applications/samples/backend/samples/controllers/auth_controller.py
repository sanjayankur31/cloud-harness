import connexion
import six

from samples.models.valid import Valid  # noqa: E501
from samples import util


def valid_token():  # noqa: E501
    """Check if the token is valid. Get a token by logging into the dashboard

    Check if the token is valid  # noqa: E501


    :rtype: List[Valid]
    """
    return 'OK!'
