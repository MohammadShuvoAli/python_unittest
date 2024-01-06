import unittest

from Test_Suite.Package1.TC_Login_Test import LoginTest
from Test_Suite.Package1.TC_SignupTest import SignupTest

from Test_Suite.Package2.TC_PaymentTest import PaymentTest
from Test_Suite.Package2.TC_PaymentReturnsTest import PaymentReturnsTest

# Get all tests from LoginTest, SignUpTest, Payment Test and PaymentReturnsTest
TC1 = unittest.TestLoader().loadTestsFromTestCase(LoginTest)
TC2 = unittest.TestLoader().loadTestsFromTestCase(SignupTest)
TC3 = unittest.TestLoader().loadTestsFromTestCase(PaymentTest)
TC4 = unittest.TestLoader().loadTestsFromTestCase(PaymentReturnsTest)

# Creating test suites
sanityTestSuite = unittest.TestSuite([TC1, TC2])
functionalTestSuite = unittest.TestSuite([TC3, TC4])
masterTestSuite = unittest.TestSuite([TC1, TC2, TC3, TC4])

# Running Test Suite
unittest.TextTestRunner().run(masterTestSuite)

