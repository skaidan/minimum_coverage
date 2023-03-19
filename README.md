# minimum_coverage
A calculator for python test set so keep the coverage reducing number of tests to minimum.


Many times, developers teams produce many tests during code and many of them are testing same lines of code. This utility expect to analyze coverage reports and extract lists of tests we can study to remove because the lines they test are fully covered for others.


Example

test_1 covers lines 1 to 5 from example_file.py
test_2 covers lines 1 to 7 from example_file.py

Output:

test_1 is covered by test_2, please study semantic of the test because probably it could be removed.

