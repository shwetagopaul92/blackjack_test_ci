# TDD
'''
1. if no cards are chosen
2.
'''
import pytest
from blackjack.blackjack import card_score

@pytest.mark.skip
def test_empty_input():
    assert card_score('') == 0

def test_simple_case():
    assert card_score('KK') == 20

def test_negative_case():
    assert card_score('JKQ') == 0

def test_simple_case2():
    assert card_score('AK') == 21

def test_simple_case3():
    assert card_score('AA') == 12

# to prevent repetition of the code above

#@pytest.mark.parametrize("input, output", [("input", "output"), ("input", "output")])
@pytest.mark.parametrize("cards, score", [("KK",20), ("JKQ",0),("AK",21),("AA", 12)])
def test_simple_with_params(cards, score):
    assert card_score(cards) == score

# check errors are caught
def test_value_errors_raised():
    with pytest.raises(ValueError):
        # if error was raised, it will be green
        # give an invalid input to check if the code does raise a valueError or not.
        card_score("")

def test_value_errors_raised_nonstrinput():
    with pytest.raises(ValueError):
        card_score(1)
        card_score(2)