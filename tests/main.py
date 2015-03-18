import unittest
import unishark
from test_reporter import ReporterTestCase
from test_runner import RunnerTestCase
from test_loader import LoaderTestCase
from test_decorator import DecoratorTestCase
from test_testprogram import TestProgramTestCase
from test_util import UtilTestCase
import sys


if __name__ == '__main__':
    # prepare test suite
    suite = unittest.TestSuite()
    loader = unittest.TestLoader()
    test_classes = [RunnerTestCase, ReporterTestCase, LoaderTestCase,
                    DecoratorTestCase, TestProgramTestCase, UtilTestCase]
    suite.addTests(list(map(loader.loadTestsFromTestCase, test_classes)))
    # run test suite
    result = unishark.BufferedTestRunner([], verbosity=2).run(suite)
    exit_code = 0 if result.wasSuccessful() else 1
    print('Exit Code: %d' % exit_code)
    sys.exit(exit_code)