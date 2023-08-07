import unittest

# import your test modules
import SSO_login_incorrect_input
import SSO_login_success
import SSO_pw_change
import SSO_reg_hardfail_fakedata
import SSO_reg_otp_bad_fail
import SSO_reg_real_duplicate_email_fail
import SSO_reg_real_duplicate_phone_fail
import SSO_reg_real_ss_success
import SSO_reg_reattempt_success
import SSO_update_dob
import SSO_update_name_address
import SSO_update_phone


# #SSO Critical Testrunner

# initialize the test suite
loader = unittest.TestLoader()
suite  = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.loadTestsFromModule(SSO_login_incorrect_input))
suite.addTests(loader.loadTestsFromModule(SSO_login_success))
suite.addTests(loader.loadTestsFromModule(SSO_pw_change))
suite.addTests(loader.loadTestsFromModule(SSO_reg_hardfail_fakedata))
suite.addTests(loader.loadTestsFromModule(SSO_reg_otp_bad_fail))
suite.addTests(loader.loadTestsFromModule(SSO_reg_real_duplicate_email_fail))
suite.addTests(loader.loadTestsFromModule(SSO_reg_real_duplicate_phone_fail))
suite.addTests(loader.loadTestsFromModule(SSO_reg_real_ss_success))
suite.addTests(loader.loadTestsFromModule(SSO_reg_reattempt_success))
suite.addTests(loader.loadTestsFromModule(SSO_update_dob))
suite.addTests(loader.loadTestsFromModule(SSO_update_name_address))
suite.addTests(loader.loadTestsFromModule(SSO_update_phone))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
