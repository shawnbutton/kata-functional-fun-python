import pytest

from kata_base_python.kata import Kata


class TestKata:

    def test_should_do_something(self):
        kata = Kata()
        assert kata.something() == 'not implemented YET'