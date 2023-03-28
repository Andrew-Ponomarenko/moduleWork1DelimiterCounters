from wordFunction import *
from sentenceFunction import *

import pytest
import unittest

class TryTesting(unittest.TestCase):
    @pytest.fixture(autouse=True)
    def test_method(self):
        with open("samplefile.ini") as f:
            s = f.read()
        assert "testdata" in s

    def wordTest(self):
        if word_count(r"C:\Users\lul\PycharmProjects\module1\textTest.txt") == 305:
            self.assertTrue(True)
        else:self.assertTrue(False)
    def sentenceTest(self):
        if sentence_count(r"C:\Users\lul\PycharmProjects\module1\textTest.txt") == 39:
            self.assertTrue(True)
        else:self.assertTrue(False)
