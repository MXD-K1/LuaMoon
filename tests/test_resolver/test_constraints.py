from random import randint, choice
from string import ascii_lowercase, digits
import operator

import pytest

from luamoon.resolver.constraints import *

def make_parse_constraint_test_cases():
    letters = ascii_lowercase + digits + '_-'

    test_cases = []
    for _ in range(100):
        pkg_name = ''.join([choice(letters) for _ in range(randint(3, 10))])
        op = choice(['<', '>', '==', '<=', '>='])
        x, y, z = randint(0, 10), randint(0, 10), randint(0, 10)
        if pkg_name.startswith(tuple(digits + '-')):
            test_cases.append((f'{pkg_name}{op}{x}.{y}.{z}', {}))
        else:
            dict_ = {
                'package_name': pkg_name,
                'operator': op,
                'version': f'{x}.{y}.{z}'
            }
            test_cases.append((f'{pkg_name}{op}{x}.{y}.{z}', dict_))

    for _ in range(20):
        pkg_name = ''.join([choice(letters) for _ in range(randint(3, 10))])
        op = choice(['=>', '=>', '!=', '', '~='])
        x, y, z = randint(0, 10), randint(0, 10), randint(0, 10)
        test_cases.append((f'{pkg_name}{op}{x}.{y}.{z}', {}))

    return test_cases

def make_normalize_version_test_cases():
    test_cases = []
    for _ in range(60):
        x, y, z = randint(0, 10), randint(0, 50), randint(0, 50)
        version = f"{'0' * randint(0, 3)}{x}.{'0' * randint(0, 3)}{y}.{'0' * randint(0, 3)}{z}"
        test_cases.append((version, f'{x}.{y}.{z}'))

    for _ in range(20):
        x, y = randint(0, 10), randint(0, 50)
        version = f"{'0' * randint(0, 3)}{x}.{'0' * randint(0, 3)}{y}"
        test_cases.append((version, f'{x}.{y}.0'))

    for _ in range(20):
        x = randint(0, 10)
        version = f"{'0' * randint(0, 3)}{x}"
        test_cases.append((version, f'{x}.0.0'))

    return test_cases

# todo: implement test_cases for matches

@pytest.mark.resolver_constraints
@pytest.mark.parametrize("raw, expected", make_parse_constraint_test_cases())
def test_parse_constraints(raw, expected):
    assert parse_constraint(raw) == expected

@pytest.mark.resolver_constraints
@pytest.mark.parametrize("raw, expected", make_normalize_version_test_cases())
def test_normalize_version(raw, expected):
    assert normalize_version(raw) == expected

