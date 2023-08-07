import unittest

if __name__ == "__main__":
###Please uncomment the proper test suite below:
# #All tests
    suite1 = unittest.TestLoader().discover('.', pattern = "API_*.py")
    suite2 = unittest.TestLoader().discover('.', pattern = "AD_*.py")
    suite3 = unittest.TestLoader().discover('.', pattern = "SSO_*.py")
    alltests = unittest.TestSuite((suite1, suite2, suite3))
    unittest.TextTestRunner(verbosity=2).run(alltests)

# #API tests
#     suite = unittest.TestLoader().discover('.', pattern = "API_*.py")
#     unittest.TextTestRunner(verbosity=2).run(suite)

# #Admin Dash Tests
    # suite = unittest.TestLoader().discover('.', pattern = "AD_*.py")
    # unittest.TextTestRunner(verbosity=2).run(suite)

# #SSO Testrunner
    # suite = unittest.TestLoader().discover('.', pattern = "SSO_*.py")
    # unittest.TextTestRunner(verbosity=2).run(suite)

