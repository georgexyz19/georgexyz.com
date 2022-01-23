title: Unittest Module
slug: unittest-module
date: 2022-01-22 09:28
modified: 2022-01-22 09:28
tags: python
note: unittest module discussion
no: 79

Unit test is one of the Python techniques I want to learn for quite some time. 
This post records some articles I read and some notes I wrote in the past few days.  

### Links

There are lots of excellent materials on this topics.  Here are some 
nice articles. 

The Python documentation website has an official page for unittest, which 
is a good starting point. 

[Unit Testing Framework](https://docs.python.org/3/library/unittest.html)

Ned Batchelder's Pycon talk *Get Started Testing* is excellent. Ned is one of 
the best speakers in Python community.  The two slide pages *Under The Covers* 
are superb. 

[Getting Started Testing - PyCon 2014 Video](https://youtu.be/FxSsnHeWQBY)


Real Python website has an article *Getting Started with Testing in Python*, 
which is a nice intro article with broad views. 

[Getting Started With Testing in Python](https://realpython.com/python-testing/)

The articles I spent most of my time on are two articles by Miguel Grinberg, 
who is one of my favorite authors. He recently posts three articles on 
testing.  Here are the links, 

[How to Write Unit Tests in Python, Part 1: Fizz Buzz](https://blog.miguelgrinberg.com/post/how-to-write-unit-tests-in-python-part-1-fizz-buzz)

[How to Write Unit Tests in Python, Part 2: Game of Life](https://blog.miguelgrinberg.com/post/how-to-write-unit-tests-in-python-part-2-game-of-life)

[How to Write Unit Tests in Python, Part 3: Web Applications](https://blog.miguelgrinberg.com/post/how-to-write-unit-tests-in-python-part-3-web-applications)

I haven't read the third article yet, but the first two are classics 
in my view. 

There are many other Pycon talks and articles in Python testing.  I will gradually 
add links to them when I have more time to study. 

### Source Code

This article will only discuss the *unittest* module code.  I am concentrating 
on the standard Python modules now. 

The source code is in this directory.  

```
~/.pyenv/versions/3.9.7/lib/python3.9/unittest
```

The source code directory includes a `test` subdirectory which has files 
that test the unittest code. If we do not consider code in this directory, 
here is the statistics of the unittest code base. 

```
$ find . -maxdepth 1 -name '*.py' -exec wc -l '{}' + | sort -n
    18 ./__main__.py
    69 ./_log.py
    71 ./signals.py
    95 ./__init__.py
   160 ./async_case.py
   170 ./util.py
   216 ./result.py
   221 ./runner.py
   275 ./main.py
   379 ./suite.py
   517 ./loader.py
  1435 ./case.py
  2891 ./mock.py
  6517 total
```

It has thirteen files and the total line count is 6,517. The `mock.py` 
module alone has 2,891 lines of code, which is more than a third of 
total lines. 

### Test Example

Let's create two simple functions and write some test code.  The `mysum.py` 
has two functions and the `test_mysum.py` file has code testing the functions. 

```
#  mysum.py 

def sum(arg):
    total = 0
    for val in arg:
        total += val
    return total

def add(a, b):
    return a + b
```
I copied the `unittest` directory to the project directory and renamed it 
to be `myunittest`. So I can change the source code and add logging 
statements without modifying the standard library code.  

```
# test_mysum.py

import myunittest as unittest
from mysum import sum, add

class TestSum(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(sum([1, 2, 3]), 6, "Should be 6")

    def test_sum_tuple(self):
        self.assertEqual(sum((1, 2, 2)), 5, "Should be 6")


class TestAdd(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(1, 2), 3, "should be 3")


if __name__ == '__main__':
    unittest.main()
```

#### Main Function Call

The `main` part of the `unittest.main()` function call is actually a class 
`TestProgram` in `main.py`.  The `unittest.main()` function call actually 
invokes the `__init__` method of the class.  The `__init__` method sets 
some instance variables and invokes two methods `parseArgs` and 
`runTests`. 

Let's look at the `runTests` method first.  If we ignore exception handling 
code, the method looks like this,

```
# concept code
self.testRunner = runner.TextTestRunner
testRunner = self.testRunner(verbosity=self.verbosity, ... )
self.result = testRunner.run(self.test)
```

The `runTests` method initialize a `TextTestRunner` object, and calls the 
`run` method of the class.  The return value is assigned to the `result` 
instance variable. 

#### Load Tests

The `self.test` argument in the last line of the code is a `TestSuite` object. 
The instance variable is set in the `createTests` method.  The `parseArgs` 
method sets up arguments and calls the `createTests` method as its last line. 
The `createTests` method mainly calls this method.

```
self.test = self.testLoader.loadTestsFromModule(self.module)  # load tests
```

The `self.testLoader` itself is `loader.defaultTestLoader` object, which is 
an instance of `TestLoader` class.  The above statement calls the 
`loadTestsFromModule` method of `TestLoader` class and saves its 
return value in the `self.test` instance variable. The `loadTestsFromModule` 
method looks like this,

```
# concept code
def loadTestsFromModule(self, module, ...):
    ...
    tests = []
    for name in dir(module):
        obj = getattr(module, name)
        if isinstance(obj, type) and issubclass(obj, case.TestCase):
            tests.append(self.loadTestsFromTestCase(obj))
    tests = self.suiteClass(tests)
    ...
    return tests

```

The `self.suiteClass` is referring to `suite.TestSuite` class. The 
`loadTestsFromModule` creates a list and passes the list to the 
`TestSuite` class. The method returns an `TestSuite` class instance. 
The instance is in this form if we print it out in console. 

```
<myunittest.suite.TestSuite tests= 
    [<myunittest.suite.TestSuite 
         tests=[<__main__.TestAdd testMethod=test_add>]>, 
     <myunittest.suite.TestSuite 
         tests=[<__main__.TestSum testMethod=test_sum>, 
                <__main__.TestSum testMethod=test_sum_tuple>]>
    ]
>
```

The code in the `loadTestsFromTestCase` method is shown below. 

```
def loadTestsFromTestCase(self, testCaseClass):
    ...
    testCaseNames = self.getTestCaseNames(testCaseClass)
    if not testCaseNames and hasattr(testCaseClass, 'runTest'):
        testCaseNames = ['runTest']
    loaded_suite = self.suiteClass(map(testCaseClass, testCaseNames))
    return loaded_suite
```

The `loaded_suite = self.suiteClass(map(...))` line is a little strange. 
The `testCaseClass` is one of the two classes `TestSum` and `TestAdd`, and 
both are derived from `TestCase`.  The `testCaseNames` are the method 
names defined in the classes like `test_sum`, `test_sum_tuple`, and 
`test_add`. The `testCaseNames` is a list.  The `map` function turns 
out to call the `__init__` method of `TestCase`, which is defined in the 
`case.py` module. 

#### Run Tests

Let's go back to the `self.result = testRunner.run(self.test)` line 
of code and what  the `run` is doing.  The method invoked the 
method `run` in the `TextTestRunner` class. The method looks like 
this, 

```
def run(self, test):
    result = self._makeResult()
    ...
    test(result)
    ...
    return result
```

The `test` argument is the `TestSuite` object return by the `loadTestsFromModule` 
method. The run method above calls the `__call__` method of the `TestSuite` object, 
which in turn calls the `run` method of `TestSuite`.  The `run` method of `TestSuite` 
class is very interesting, and it is recursive.  The code looks like this, 

```
# concept code
def run(self, result, ...):
    ...
    for index, test in enumerate(self):
        ...
        test(result)
    ...
    return result
```

The `run` method of `TestSuite` class will invoke the `run` method of `TestCase` 
class during the recursive call.  The `run` method of `TestCase` code looks 
like this, 

```
def run(self, result=None):
    ...
    result.startTest(self)

    try:
        ...
        outcome = _Outcome(result)
        try:
            self._outcome = outcome

            with outcome.testPartExecutor(self):
                self.setUp()
            if outcome.success:
                outcome.expecting_failure = expecting_failure
                with outcome.testPartExecutor(self, isTest=True):
                    testMethod()
                outcome.expecting_failure = False
                with outcome.testPartExecutor(self):
                    self.tearDown()

            self.doCleanups()
            ....

```

The `testPartExecutor` is a context manager defined in the `_Outcome` class. 
It catches most exceptions.  The code is shown below. 

```
# testPartExecutor method in _Outcome

@contextlib.contextmanager
def testPartExecutor(self, test_case, isTest=False):
    old_success = self.success
    self.success = True
    try:
        yield
    except KeyboardInterrupt:
        raise
    except SkipTest as e:
        self.success = False
        self.skipped.append((test_case, str(e)))
    except _ShouldStop:
        pass
    except:
        exc_info = sys.exc_info()
        if self.expecting_failure:
            self.expectedFailure = exc_info
        else:
            self.success = False
            self.errors.append((test_case, exc_info))
        # explicitly break a reference cycle:
        # exc_info -> frame -> exc_info
        exc_info = None
    else:
        if self.result_supports_subtests and self.success:
            self.errors.append((test_case, None))
    finally:
        self.success = self.success and old_success
```

The source code becomes quite complicated at this stage. But this is 
essentially how the unittest module works. 

### Next Steps

I actually have two Python testing books which I haven't started 
reading. Also I need to add some unittest code to my own projects. 

