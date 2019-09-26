"""Tests for the suggestion logic"""

from typing import Dict

import pytest

from src.suggest import find_suggestions


@pytest.mark.parametrize("to_fix, to_search, expected", [(set(
    ("Bn", "Sm", "Dn", "Laure")), set(("Ben", "Sam", "Dan", "Laurie")), {
        "Bn": "Ben",
        "Sm": "Sam",
        "Dn": "Dan",
        "Laure": "Laurie"
    })])
def test_find_suggestions(to_fix: set, to_search: set,
                          expected: Dict[str, str]):
    """Test that find suggestions returns the expected results

    Args:
        to_fix (set): A set of names to fix
        to_search (set): A set of suggestions to provide
        expected (Dict[str, str]): The expected mapping from fix/suggestion
    """
    # Run the comparison
    result = find_suggestions(to_fix, to_search)
    # Check the results
    for orig_n, expected_n in expected.items():
        assert result.loc[orig_n, 'suggestion'] == expected_n
