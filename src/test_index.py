import pytest
import index

def test_uncovered_if():
    assert index.uncovered_if() == False
    assert index.uncovered_if(False) == True

def test_fully_covered():
    assert index.fully_covered() == True

def test_uncovered():
    assert index.uncovered() == True


