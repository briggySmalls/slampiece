"""
String comaprison logic
"""
import pandas as pd
from Levenshtein import ratio  # pylint: disable=no-name-in-module


def find_suggestions(to_fix: set, to_search: set) -> pd.DataFrame:
    """Suggests corrections for a set of strings, from provided options

    Args:
        to_fix (set): List of strings to find a suggestion for
        to_search (set): LIst of strings suggestions are selected from

    Returns:
        pd.DataFrame: Matrix that supplies suggestions and probabilities for
                      each string in to_fix
    """
    # Convert the sets to pandas series (so we can build a matrix)
    to_fix_series = pd.Series(list(to_fix))
    to_search_series = pd.Series(list(to_search))

    # Create a matrix, where:
    # - each row corresponds to a string to fix
    # - each column corresponds to a suggestion
    # - each cell is the probability of the suggestion being correct
    mat = to_fix_series.apply(lambda name_to_fix: to_search_series.apply(
        lambda name_to_search: ratio(name_to_fix, name_to_search)))
    mat.rename(columns=to_search_series, index=to_fix_series, inplace=True)
    mat.index.name = "original"

    # Create a dataframe which holds:
    # - the most-probable suggestion
    # - the probability of the suggestion
    return pd.DataFrame({
        'suggestion': mat.idxmax(axis=1),
        'probability': mat.max(axis=1),
    })
