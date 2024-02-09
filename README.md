# Functional Fun

## Overview
The goal of this kata is to practice refactoring [imperative code to a more declarative](https://dev.to/ruizb/declarative-vs-imperative-4a7l) style.

Python provides great support for [functional](https://medium.com/akava/functional-programming-in-python-e492f2ad1e37) programming, and by using
these built-in tools you can make your code more readable, changeable, and testable.

## Instructions

If you look at [ReadingProcessor](./kata_function_fun/reading_processor.py) you will find that there is a
large "for" loop that goes through an array of "readings".

The loop ignores some readings, changes some readings (converts celcius to farenheit),
and then finally groups the readings by "type" into arrays in a new object.

Your job is to replace the imperative "for" loop and "if" statements with the functional Array built-ins such as
[filter](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/filter),
[map](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/map), and
[reduce](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array/reduce)

There are tests to allow you to refactor with safety. You can assume that the tests cover the behaviour we want to preserve, so if the tests keep running you're gold.

### Bonus
You'll notice that there is a skipped test `test_should_not_mutate_readings`

The current code changes the readings that are passed to it. Changing your inputs is a bad practice because it can cause unpredictable problems in other parts of the code that might rely on the readings.

Once you have refactored a bit do you see an opportunity to not mutate the reading? If so, stop ignoring the test and write new code to fix the problem.

## How to run the code

To run the tests you need to install dependencies with [poetry](https://python-poetry.org/)

run:
```bash
poetry install
```

Then to run tests:
```bash
poetry run pytest
```


# Facilitators Notes

The intention of this kata is to practice the refactoring that Martin Fowler calls [Replace Loop With Pipeline](https://refactoring.com/catalog/replaceLoopWithPipeline.html) [(example)](https://martinfowler.com/articles/refactoring-pipelines.html)



And that's it!

Happy Mobbing / Pairing!

Kata created by [Shawn Button](mailto:shawn@leanintuit.com) of [LeanIntuit](http://www.leanintuit.com)

