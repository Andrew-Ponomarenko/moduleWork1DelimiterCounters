from wordFunction import *
from sentenceFunction import *

from unittest import TestCase

class TryTesting(TestCase):
    def wordTest(self):
        if word_count(r"C:\Users\lul\PycharmProjects\module1\textTest.txt") == 305:
            self.assertTrue(True)
        else:self.assertTrue(False)
    def sentenceTest(self):
        if sentence_count(r"C:\Users\lul\PycharmProjects\module1\textTest.txt") == 39:
            self.assertTrue(True)
        else:self.assertTrue(False)
