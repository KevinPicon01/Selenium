from unittest import TestLoader, TestSuite
from pyunitreport import HTMLTestRunner
from Assertions import Assertion
from SearchTest import SearchTest

assertion_test = TestLoader().loadTestsFromTestCase(Assertion)
search_test = TestLoader().loadTestsFromTestCase(SearchTest)
smoke_test = TestSuite([assertion_test, search_test])

kwargs = {
    'output': 'reportes'
}

runner = HTMLTestRunner(**kwargs)
runner.run(smoke_test)