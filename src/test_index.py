import pytest
import index

def test_uncovered_if():
    assert index.uncovered_if() == False
    assert index.uncovered_if() == True

def test_fully_covered():
    assert index.fully_covered() == True




