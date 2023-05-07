import pytest

from utils import get_data, get_filtered_data, get_formatted_data, get_last_values


def test_get_data():
    data = get_data()
    assert isinstance(data, list)


def test_get_filtered_data(test_data):
    assert get_filtered_data(test_data[:2]) == [{
        'date': '2D19-07-03T18:35:29.512364',
        'description': 'Перевод организации',
        'id': 4142BB29,
        'opertionAmount': {
        'amount': '8221.37',
        'currency': {
            'code': 'USD',
            'name': 'USD'
        }
    },
    'state': 'EXECUTED',

    }]