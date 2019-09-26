"""
String comaprison logic
"""
from Levenshtein import ratio  # pylint: disable=no-name-in-module
import pandas as pd


def find_suggestions(to_fix: set, to_search: set) -> pd.DataFrame:
    """Suggests corrections for a set of strings, from provided options

    Args:
        to_fix (pd.Series): List of strings to find a suggestion for
        to_search (pd.Series): LIst of strings suggestions are selected from
    """
    common_names = to_fix.intersection(to_search)
    to_fix_s = pd.Series(list(to_fix - common_names))
    to_search_s = pd.Series(list(to_search - common_names))
    # Create a matrix, where:
    # - each row corresponds to a string to fix
    # - each column corresponds to a suggestion
    # - each cell is the probability of the suggestion being correct
    mat = to_fix_s.apply(
        lambda name_to_fix: to_search_s.apply(lambda name_to_search: ratio(
            name_to_fix, name_to_search)))
    mat.rename(columns=to_search_s, index=to_fix_s, inplace=True)
    mat.index.name = "original"

    # Create a dataframe which holds:
    # - the most-probable suggestion
    # - the probability of the suggestion
    return pd.DataFrame({
        'suggestion': mat.idxmax(axis=1),
        'probability': mat.max(axis=1),
    })
