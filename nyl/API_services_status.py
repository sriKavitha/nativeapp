import unittest, time, re  # unittest is the testing framework, provides module for organizing test cases
import requests, json           # Requests provides ability to hit API Json provides ability to encode & decode Json files
import HtmlTestRunner

import var, funct, confTest     # Custom class for NYL

class NYLServices(confTest.NYLservicesBASE):

    def test_apiStatusCode(self):
        """Checks that response status code 200 is returned for Nylservices APIs with proper payloads in requests

        All proper headers and payloads with valid information (pulled from the credentials file) is
        submitted in the requests to the API

        :return:
        """


        # time.sleep() added between calls so tests do not hit AWS Batch API limits

        testenv = self.env

        ts = funct.timeStamp()
        # email for ssn registration
        testemailSSO = f'qa+sso{ts}@rosedigital.co'
        # email for mobile app registration
        testemailMOB = f'qa+mobile{ts}@rosedigital.co'

        # Check for existing test SSO user and wipe it from userpool prior to register api call
        # Purge with email search on dev and phone search on qa/ stage env
        if self.env != 'dev':
            try:
                funct.purgeSSOphone(self, var.CREDSapi.ssoPhone)
            except:
                pass
        else:
            try:
                funct.purgeSSOemail(self, testemailSSO)
            except:
                pass
        # # Check for existing test Mobile user and wipe it from userpool prior to register api call
        try:
            funct.purgeMobile(self, testemailMOB)
            print(f'test user {testemailMOB} purged \n')
        except:
            print(f'no test user {testemailMOB} found \n')

        print(f'Current environment = {testenv}')

        # grabbing entry info through localized var/ funct files
        if testenv == 'dev':
            client_id = var.CREDSapi.devSSOcid
            x_api_key = var.CREDSapi.devSSOxkey
            handle_govid_code = var.CREDSapi.devSSOhgcode
            m_client_id = var.CREDSapi.devMOBILEcid
            m_x_api_key = var.CREDSapi.devMOBILExkey
            m_fcm_token = var.CREDSapi.devFCMtoken
        elif testenv == 'qa':
            client_id = var.CREDSapi.qaSSOcid
            x_api_key = var.CREDSapi.qaSSOxkey
            handle_govid_code = var.CREDSapi.qaSSOhgcode
            m_client_id = var.CREDSapi.qaMOBILEcid
            m_x_api_key = var.CREDSapi.qaMOBILExkey
            m_fcm_token = var.CREDSapi.qaFCMtoken
        elif testenv == 'stage':
            client_id = var.CREDSapi.stageSSOcid
            x_api_key = var.CREDSapi.stageSSOxkey
            m_client_id = var.CREDSapi.stageMOBILEcid
            m_x_api_key = var.CREDSapi.stageMOBILExkey
            m_fcm_token = var.CREDSapi.stageFCMtoken

        # [Documentation - detail] setting up an api call using the requests method
        # [Documentation - detail] setting headers to let api know that we have proper permissions to run api call
        # [Documentation - detail] setting payload in json body in the api call

        # POST /sso/register-verify (SSO User)
        sso_register_payload = {'clientId': client_id, 'email': testemailSSO, 'password': var.CREDSapi.ssoPW,
                                'firstName': var.CREDSapi.ssoFName, 'lastName': var.CREDSapi.ssoLName,
                                'phone': var.CREDSapi.ssoPhone,
                                'birthdate': var.CREDSapi.ssoDOBmonth + '/' + var.CREDSapi.ssoDOBDate + '/' + var.CREDSapi.ssoDOBYear,
                                'streetNumber': var.CREDSapi.ssoHNum, 'street': var.CREDSapi.ssoStreet,
                                'city': var.CREDSapi.ssoCity, 'state': var.CREDSapi.ssoState,
                                'zip': var.CREDSapi.ssoZip, 'ssn4': var.CREDSapi.ssoSSN, 'noSsn4': 'false'}
        sso_registerCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/register-verify',
                                         json=sso_register_payload)
        if sso_registerCall.status_code == 200:
            print(f'PASS - POST /sso/register-verify (SSN Registration) Status Code: {sso_registerCall.status_code}')
            # print(sso_registerCall.text)
        else:
            print(f'\nERROR - POST /sso/register-verify (SSN Registration) Status Code: {sso_registerCall.status_code}')
            print(f'RESPONSE HEADERS - {sso_registerCall.headers}')
            print(f'RESPONSE - {sso_registerCall.text}\n')

        # [Documentation - detail] Conditional check due to IDDW verification dependency with user verification
        if '"phoneDuplicate":true' in str(sso_registerCall.text):
            print(f'ERROR - Duplicate phone for user and user not created.\nRegistration response =\n{sso_registerCall.text}')
            raise Exception('Failed user creation. Unable to proceed further. Purge phone number or change user data.')
        elif '"hardFail":true' in str(sso_registerCall.text):
            print(f'ERROR - IDDW Verification failed for user and user not created.\nRegistration response = \n{sso_registerCall.text}')
            raise Exception('Failed user creation. Unable to proceed further. Change test user data in creds file.')

        # [Documentation - detail] grabbing the accessToken and refreshToken from the registration response body for use in later api calls
        registerResponse = []
        quoted = re.compile('"(.*?)"')
        for value in quoted.findall(sso_registerCall.text):
            # print(value)
            registerResponse.append(value)
        sso_register_access_token = registerResponse[2]
        sso_register_refresh_token = registerResponse[7]
        # For debugging token issues
        # print(sso_registerCall.text)
        # print(sso_register_access_token)
        # print(sso_register_refresh_token)

        # POST /sso/refresh-token
        time.sleep(1)
        refresh_token_headers = {'x-api-key': x_api_key}
        refresh_token_payload = {'clientId': client_id, 'refreshToken': sso_register_refresh_token}
        refreshTokenCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/refresh-token',
                                         headers=refresh_token_headers, json=refresh_token_payload)
        if refreshTokenCall.status_code == 200:
            print(f'PASS - POST /sso/refresh-token Status Code: {refreshTokenCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/refresh-token Status Code: {refreshTokenCall.status_code}')
            print(f'RESPONSE HEADERS - {refreshTokenCall.headers}')
            print(f'RESPONSE - {refreshTokenCall.text}\n')

        # PUT /sso/register-verify (SSN Confirmation)
        time.sleep(1)
        ssn_confirm_payload = {"ssnConfirmation": {"ssn": "1111"}}
        ssn_confirm_headers = {'Authorization': sso_register_access_token}
        ssnConfirmCall = requests.put(f'https://api-{self.env}.nylservices.net/sso/register-verify',
                                      headers=ssn_confirm_headers, json=ssn_confirm_payload)
        if ssnConfirmCall.status_code == 200:
            print(f'PASS - PUT /sso/register-verify (SSN Confirmation) Status Code: {ssnConfirmCall.status_code}')
        else:
            print(f'\nERROR - PUT /sso/register-verify (SSN Confirmation) Status Code: {ssnConfirmCall.status_code}')
            print(f'RESPONSE HEADERS - {ssnConfirmCall.headers}')
            print(f'RESPONSE - {ssnConfirmCall.text}\n')

        # POST /sso/phone-code-gen
        time.sleep(1)
        phone_gen_payload = {"type": "sms"}
        phone_gen_headers = {'Authorization': sso_register_access_token}
        phoneGenCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/phone-code-gen',
                                     headers=phone_gen_headers, json=phone_gen_payload)
        if phoneGenCall.status_code == 200:
            print(f'PASS - POST /sso/phone-code-gen Status Code: {phoneGenCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/phone-code-gen Status Code: {phoneGenCall.status_code}')
            print(f'RESPONSE HEADERS - {phoneGenCall.headers}')
            print(f'RESPONSE - {phoneGenCall.text}\n')

        # PUT /sso/register-verify (Phone Confirmation)
        time.sleep(1)
        phone_confirm_payload = {"phoneConfirmation": {"asi": "true", "pincode": "111111", "pinType": "sms"}}
        phone_confirm_headers = {'Authorization': sso_register_access_token}
        phoneConfirmCall = requests.put(f'https://api-{self.env}.nylservices.net/sso/register-verify',
                                        headers=phone_confirm_headers, json=phone_confirm_payload)
        if phoneConfirmCall.status_code == 200:
            print(f'PASS - PUT /sso/register-verify (Phone Confirmation) Status Code: {phoneConfirmCall.status_code}')
        else:
            print(f'\nERROR - PUT /sso/register-verify (Phone Confirmation) Status Code: {phoneConfirmCall.status_code}')
            print(f'RESPONSE HEADERS - {phoneConfirmCall.headers}')
            print(f'RESPONSE - {phoneConfirmCall.text}\n')

        # PUT /sso/register-verify (Profile Update)
        time.sleep(1)
        profile_update_headers = {'Authorization': sso_register_access_token}
        profile_update_payload = {'profileUpdate': {'verify': 'true', 'firstName': var.CREDSapi.ssoFName, 'lastName': var.CREDSapi.ssoLName,
                                'phone': var.CREDSapi.ssoPhone,
                                'birthdate': var.CREDSapi.ssoDOBmonth + '/' + var.CREDSapi.ssoDOBDate + '/' + var.CREDSapi.ssoDOBYear,
                                'streetNumber': var.CREDSapi.ssoHNum, 'street': var.CREDSapi.ssoStreet,
                                'city': var.CREDSapi.ssoCity, 'state': var.CREDSapi.ssoState,
                                'zip': var.CREDSapi.ssoZip}}
        sso_profileUpdateCall = requests.put(f'https://api-{self.env}.nylservices.net/sso/register-verify',
                                              headers=profile_update_headers, json=profile_update_payload)
        if sso_profileUpdateCall.status_code == 200:
            print(f'PASS - PUT /sso/register-verify (Profile Update) Status Code: {sso_profileUpdateCall.status_code}')
        else:
            print(f'\nERROR - PUT /sso/register-verify (Profile Update) Status Code: {sso_profileUpdateCall.status_code}')
            print(f'RESPONSE HEADERS - {sso_profileUpdateCall.headers}')
            print(f'RESPONSE - {sso_profileUpdateCall.text}\n')

        # TODO this request needs to be refactored for STAGE as the handle_govid_code must be dynamically generated
        # PUT /sso/handle-govid-response
        time.sleep(1)
        if testenv == 'stage':
            pass
        elif testenv == 'dev' or 'qa':
            handle_govid_payload = {"code": handle_govid_code, "govIdType": "usdl-desktop"}
            handle_govid_headers = {'Authorization': sso_register_access_token}
            handleGovidCall = requests.put(f'https://api-{self.env}.nylservices.net/sso/handle-govid-response', headers=handle_govid_headers,
                                     json=handle_govid_payload)
            if handleGovidCall.status_code == 200:
                print(f'PASS - PUT /sso/handle-govid-response Status Code: {handleGovidCall.status_code}')
            else:
                print(f'\nERROR - PUT /sso/handle-govid-response Status Code: {handleGovidCall.status_code}')
                print(f'RESPONSE HEADERS - {handleGovidCall.headers}')
                print(f'RESPONSE - {handleGovidCall.text}\n')

        # GET /users (SSO User)
        time.sleep(1)
        sso_users_headers = {'Authorization': sso_register_access_token}
        ssoUsersGetCall = requests.get(f'https://api-{self.env}.nylservices.net/users', headers=sso_users_headers)
        if ssoUsersGetCall.status_code == 200:
            print(f'PASS - GET /users (SSO User) Status Code: {ssoUsersGetCall.status_code}')
        else:
            print(f'\nERROR - GET /users (SSO User) Status Code: {ssoUsersGetCall.status_code}')
            print(f'RESPONSE HEADERS - {ssoUsersGetCall.headers}')
            print(f'RESPONSE - {ssoUsersGetCall.text}\n')

        # POST /sso/login (SSO user)
        time.sleep(1)
        sso_login_payload = {"email": testemailSSO, "clientId": client_id, "password": var.CREDSapi.ssoPW}
        sso_loginCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/login', json=sso_login_payload)
        if sso_loginCall.status_code == 200:
            print(f'PASS - POST /sso/login (SSO User) Status Code: {sso_loginCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/login (SSO User) Status Code: {sso_loginCall.status_code}')
            print(f'RESPONSE HEADERS - {sso_loginCall.headers}')
            print(f'RESPONSE - {sso_loginCall.text}\n')

        # POST /sso/logout
        time.sleep(1)
        sso_logout_headers = {'Authorization': sso_register_access_token}
        sso_logout_payload = {"clientId": client_id, "accessToken": sso_register_access_token}
        sso_logoutCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/logout', headers=sso_logout_headers, json=sso_logout_payload)
        if sso_logoutCall.status_code == 200:
            print(f'PASS - POST /sso/logout (SSO User) Status Code: {sso_logoutCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/logout (SSO User) Status Code: {sso_logoutCall.status_code}')
            print(f'RESPONSE HEADERS - {sso_logoutCall.headers}')
            print(f'RESPONSE - {sso_logoutCall.text}\n')

        # POST /sso/email-exists-check (SSO user)
        time.sleep(1)
        email_exists_payload = {"email": testemailSSO, "clientId": client_id}
        emailExistsCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/email-exists-check',
                                        json=email_exists_payload)
        if emailExistsCall.status_code == 200:
            print(f'PASS - POST /sso/email-exists-check (SSO user) Status Code: {emailExistsCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/email-exists-check (SSO user) Status Code: {emailExistsCall.status_code}')
            print(f'RESPONSE HEADERS - {emailExistsCall.headers}')
            print(f'RESPONSE - {emailExistsCall.text}\n')

        # POST /sso/reset-password (SSO user)
        time.sleep(1)
        reset_password_headers = {'Authorization': sso_register_access_token}
        reset_password_payload = {"email": testemailSSO, "clientId": client_id}
        resetPasswordCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/reset-password', headers=reset_password_headers,
                                          json=reset_password_payload)
        if resetPasswordCall.status_code == 200:
            print(f'PASS - POST /sso/reset-password (SSO user) Status Code: {resetPasswordCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/reset-password (SSO user) Status Code: {resetPasswordCall.status_code}')
            print(f'RESPONSE HEADERS - {resetPasswordCall.headers}')
            print(f'RESPONSE - {resetPasswordCall.text}\n')

        # POST /sso/register (Mobile user)
        time.sleep(1)
        mobile_register_payload = {'clientId': m_client_id, 'email': testemailMOB, 'password': var.CREDSapi.mobilePW, 'firstName': var.CREDSapi.mobileFName, 'lastName': var.CREDSapi.mobileLName, 'phone': var.CREDSapi.mobilePhone}
        mobile_registerCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/register',
                                         json=mobile_register_payload)
        if mobile_registerCall.status_code == 200:
            print(f'PASS - POST /sso/register (Mobile Registration) Status Code: {mobile_registerCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/register (Mobile Registration) Status Code: {mobile_registerCall.status_code}')
            print(f'RESPONSE HEADERS - {mobile_registerCall.headers}')
            print(f'RESPONSE - {mobile_registerCall.text}\n')

        # [Documentation - detail] grabbing the accessToken and refreshToken from the registration response body for use in later api calls
        mobile_registerResponse = []
        quoted = re.compile('"(.*?)"')
        for value in quoted.findall(sso_registerCall.text):
            # print(value)
            mobile_registerResponse.append(value)
        mobile_register_access_token = mobile_registerResponse[2]
        # For debugging token issues
        # print(mobile_registerCall.text)
        # print(mobile_register_access_token)

        # GET /promotions (Mobile user)
        time.sleep(1)
        promotions_headers = {'x-api-key': m_x_api_key}
        promotionsCall = requests.get(f'https://api-{self.env}.nylservices.net/promotions',
                                      headers=promotions_headers)
        if promotionsCall.status_code == 200:
            print(f'PASS - GET /promotions (Mobile user) Status Code: {promotionsCall.status_code}')
        else:
            print(f'\nERROR - GET /promotions (Mobile user) Status Code: {promotionsCall.status_code}')
            print(f'RESPONSE HEADERS - {promotionsCall.headers}')
            print(f'RESPONSE - {promotionsCall.text}\n')

        # GET /retailers/all (Mobile user)
        time.sleep(1)
        retailers_headers = {'x-api-key': m_x_api_key}
        retailersAllCall = requests.get(f'https://api-{self.env}.nylservices.net/retailers/all',
                                        headers=retailers_headers)
        if retailersAllCall.status_code == 200:
            print(f'PASS - GET /retailers/all (Mobile user) Status Code: {retailersAllCall.status_code}')
        else:
            print(f'\nERROR - GET /retailers/all (Mobile user) Status Code: {retailersAllCall.status_code}')
            print(f'RESPONSE HEADERS - {retailersAllCall.headers}')
            print(f'RESPONSE - {retailersAllCall.text}\n')

        # POST /sso/login (Mobile user)
        time.sleep(1)
        mobile_login_payload = {'email': testemailMOB, 'clientId': m_client_id, 'password': var.CREDSapi.mobilePW}
        mobile_loginCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/login', json=mobile_login_payload)
        if mobile_loginCall.status_code == 200:
            print(f'PASS - POST /sso/login (Mobile user) Status Code: {mobile_loginCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/login (Mobile user) Status Code: {mobile_loginCall.status_code}')
            print(f'RESPONSE HEADERS - {mobile_loginCall.headers}')
            print(f'RESPONSE - {mobile_loginCall.text}\n')

        # GET /preferences (Mobile user)
        time.sleep(1)
        preferences_headers = {'x-api-key': m_x_api_key, 'Authorization': mobile_register_access_token}
        params = {'type': 'app'}
        preferencesGetCall = requests.get(f'https://api-{self.env}.nylservices.net/preferences', headers=preferences_headers, params=params)
        if preferencesGetCall.status_code == 200:
            print(f'PASS - GET /preferences (Mobile user) Status Code: {preferencesGetCall.status_code}')
        else:
            print(f'\nERROR - GET /preferences (Mobile user) Status Code: {preferencesGetCall.status_code}')
            print(f'RESPONSE HEADERS - {preferencesGetCall.headers}')
            print(f'RESPONSE - {preferencesGetCall.text}\n')

        # POST /preferences (Mobile user)
        time.sleep(1)
        preferences_headers = {'Authorization': mobile_register_access_token, 'x-api-key': m_x_api_key, 'Fcm-token': m_fcm_token}
        params = {'type': 'app'}
        preferences_payload = {"myGames": ["lotto", "megamillions"], "notifications": {"lotto": {"dayOfDrawing": "true", "minimumJackpot": "2500000"}}, "draws": {"lotto": [[1, 8, 72, 2, 1], [2, 8, 72, 2, 1], [3, 8, 72, 2, 1], [4, 8, 72, 2, 1]], "cash4life": [[1, 8, 72, 2, 1], [2, 8, 72, 2, 1], [3, 8, 72, 2, 1], [4, 8, 72, 2, 1]]}, "quickdraw": {"theme": 1}}
        preferencesPostCall = requests.post(f'https://api-{self.env}.nylservices.net/preferences', headers=preferences_headers, params=params, json=preferences_payload)
        if preferencesPostCall.status_code == 200:
            print(f'PASS - POST /preferences (Mobile user) Status Code: {preferencesPostCall.status_code}')
        else:
            print(f'\nERROR - POST /preferences (Mobile user) Status Code: {preferencesPostCall.status_code}')
            print(f'RESPONSE HEADERS - {preferencesPostCall.headers}')
            print(f'RESPONSE - {preferencesPostCall.text}\n')

        # GET /mobile-static-views/:pageid
        time.sleep(1)
        pages = ['settings-page', 'visit-customer-service-center', 'conditions', 'privacy-policy', 'contact-us','faq-page', 'ticket-purchase-policy', 'faq-how-often-winning-numbers-updated', 'faq-other-sources-winning-numbers', 'faq-accurate-information', 'faq-where-claim-prize', 'faq-how-long-tickets-valid', 'faq-connection-use-app', 'faq-how-get-quick-draw-results', 'faq-how-often-quick-draw-drawings', 'faq-trouble-seeing-results', 'faq-draw-times-games', 'list-view-no-retailers-found', 'mega-millions-how-to-play', 'powerball-how-to-play', 'lotto-how-to-play', 'cash4life-how-to-play', 'take-5-how-to-play', 'numbers-how-to-play', 'win-4-how-to-play', 'quick-draw-how-to-play', 'pick-10-how-to-play']
        pages_headers = {'x-api-key': m_x_api_key}
        pagePassedFlags = []
        pageFailedFlags = []
        pageFailedStatusCode = []
        pageFailedList = []
        for page in pages:
            time.sleep(2)
            indiPageCall = requests.get(f'https://api-{self.env}.nylservices.net//mobile-static-views/{page}', headers=pages_headers)
            if indiPageCall.status_code == 200:
                pagePassedFlags.append(page)
            else:
                pagePassedFlags.append('xfail')
                pageFailedFlags.append(page)
                pageFailedStatusCode.append(indiPageCall.status_code)
        for f, s in zip(pageFailedFlags, pageFailedStatusCode):
            pageFailedList.append([(f, s)])

        if pageFailedList != []:
            print(f'\nERROR - These individual GET /mobile-static-views/:pageid endpoints and their status codes:')
            print(pageFailedList)
        else:
            # print(pagePassedFlags)
            print('PASS - ALL individual GET /mobile-static-views/:pageid endpoints received Status Code: 200 ')

        print('\n***WARNING***\nBelow requests may fail due to IGT test environment availability')
        print('POST /ticket-scan/inquiry')
        print('GET /games/all/draws')
        print('GET /games/{game-name}/draws')
        print('Review IGT status for CAT and SQA here if failures are observed')
        info_headers = {'x-api-key': m_x_api_key}
        infoCall = requests.get(f'https://api-{self.env}.nylservices.net/info', headers=info_headers)
        print(infoCall.text)
        print('***WARNING*** \n')

        # GET /ticket-scan/count (Mobile user)
        time.sleep(1)
        ticketscan_count_headers = {'Authorization': mobile_register_access_token, 'x-api-key': m_x_api_key}
        ticketscanCountCall = requests.get(f'https://api-{self.env}.nylservices.net/ticket-scan/count', headers=ticketscan_count_headers)
        if ticketscanCountCall.status_code == 200:
            print(f'PASS - GET /ticket-scan/count Status Code: {ticketscanCountCall.status_code}')
        else:
            print(f'\nERROR - GET /ticket-scan/count Status Code: {ticketscanCountCall.status_code}')
            print(f'RESPONSE HEADERS - {ticketscanCountCall.headers}')
            print(f'RESPONSE - {ticketscanCountCall.text}\n')

        # POST /ticket-scan/inquiry (Mobile user)
        time.sleep(1)
        ticketscan_inquiry_payload = {"barcodeData": "87600275207207466326295006"}
        ticketscan_inquiry_headers = {'Authorization': mobile_register_access_token, 'x-api-key': m_x_api_key}
        ticketscanInquiryCall = requests.post(f'https://api-{self.env}.nylservices.net/ticket-scan/inquiry', headers=ticketscan_inquiry_headers, json=ticketscan_inquiry_payload)
        if ticketscanInquiryCall.status_code == 200:
            print(f'PASS - POST /ticket-scan/inquiry Status Code: {ticketscanInquiryCall.status_code}')
        else:
            print(f'\nERROR - POST /ticket-scan/inquiry Status Code: {ticketscanInquiryCall.status_code}')
            print(f'RESPONSE HEADERS - {ticketscanInquiryCall.headers}')
            print(f'RESPONSE - {ticketscanInquiryCall.text}\n')

        # GET /ticket-scan/count-cms (Mobile user)
        time.sleep(1)
        ticketscan_count_cms_headers = {'Authorization': mobile_register_access_token, 'x-api-key': m_x_api_key}
        ticketscanCountCmsCall = requests.get(f'https://api-{self.env}.nylservices.net/ticket-scan/count-cms', headers=ticketscan_count_cms_headers)
        if ticketscanCountCmsCall.status_code == 200:
            print(f'PASS - GET /ticket-scan/count-cms Status Code: {ticketscanCountCmsCall.status_code}')
        else:
            print(f'\nERROR - GET /ticket-scan/count-cms Status Code: {ticketscanCountCmsCall.status_code}')
            print(f'RESPONSE HEADERS - {ticketscanCountCmsCall.headers}')
            print(f'RESPONSE - {ticketscanCountCmsCall.text}\n')

        # POST /ticket-scan/inquiry-cms (Mobile user)
        time.sleep(1)
        ticketscan_inquiry_cms_payload = {"barcodeData": "87600275207207466326295006"}
        ticketscan_inquiry_cms_headers = {'Authorization': mobile_register_access_token, 'x-api-key': m_x_api_key}
        ticketscanInquiryCmsCall = requests.post(f'https://api-{self.env}.nylservices.net/ticket-scan/inquiry', headers=ticketscan_inquiry_cms_headers, json=ticketscan_inquiry_cms_payload)
        if ticketscanInquiryCmsCall.status_code == 200:
            print(f'PASS - POST /ticket-scan/inquiry-cms Status Code: {ticketscanInquiryCmsCall.status_code}')
        else:
            print(f'\nERROR - POST /ticket-scan/inquiry-cms Status Code: {ticketscanInquiryCmsCall.status_code}')
            print(f'RESPONSE HEADERS - {ticketscanInquiryCmsCall.headers}')
            print(f'RESPONSE - {ticketscanInquiryCmsCall.text}\n')

        # GET /games/all/draws
        time.sleep(1)
        games_alldraws_headers = {'x-api-key': m_x_api_key}
        gamesAllDrawsCall = requests.get(f'https://api-{self.env}.nylservices.net/games/all/draws', headers=games_alldraws_headers)
        if gamesAllDrawsCall.status_code == 200:
            print(f'PASS - GET /games/all/draws Status Code: {gamesAllDrawsCall.status_code}')
        else:
            print(f'\nERROR - GET /games/all/draws Status Code: {gamesAllDrawsCall.status_code}')
            print(f'RESPONSE HEADERS - {gamesAllDrawsCall.headers}')
            print(f'RESPONSE - {gamesAllDrawsCall.text}\n')

        # GET /games/{game-name}/draws
        time.sleep(1)
        games = ['megamillions', 'powerball', 'lotto', 'cash4life', 'take5', 'numbers', 'win4', 'quickdraw', 'pick10']
        headers = {'x-api-key': m_x_api_key}
        gamePassedFlags = []
        gameFailedFlags = []
        gameFailedStatusCode = []
        gameFailedList = []
        for game in games:
            time.sleep(2)
            indiGameCall = requests.get(f'https://api-{self.env}.nylservices.net/games/{game}/draws', headers=headers)
            if indiGameCall.status_code == 200:
                gamePassedFlags.append(game)
            else:
                gamePassedFlags.append('xfail')
                gameFailedFlags.append(game)
                gameFailedStatusCode.append(indiGameCall.status_code)
        for f, s in zip(gameFailedFlags, gameFailedStatusCode):
            gameFailedList.append([(f, s)])

        if gameFailedList != []:
            print('ERROR - These individual GET /games/{game-name}/draws endpoints and their status codes:')
            print(gameFailedList)
        else:
            # print(gamePassedFlags)
            print('PASS - ALL individual GET /games/{game-name}/draws endpoints received Status Code: 200 ')

        # POST /sso/logout (Mobile user)
        time.sleep(1)
        mobile_logout_headers = {'Authorization': mobile_register_access_token}
        mobile_logout_payload = {'clientId': m_client_id, 'accessToken': mobile_register_access_token}
        mobile_logoutCall = requests.post(f'https://api-{self.env}.nylservices.net/sso/logout', headers=mobile_logout_headers, json=mobile_logout_payload)
        if mobile_logoutCall.status_code == 200:
            print(f'PASS - POST /sso/logout (Mobile user) Status Code: {mobile_logoutCall.status_code}')
        else:
            print(f'\nERROR - POST /sso/logout (Mobile user) Status Code: {mobile_logoutCall.status_code}')
            print(f'RESPONSE HEADERS - {mobile_logoutCall.headers}')
            print(f'RESPONSE - {mobile_logoutCall.text}\n')

        # TODO Need to get correct headers and payload for the following endpoints
        # TODO POST /sso/confirm-reset-password
        # TODO GET /sso/email-confirmation-resend
        # TODO POST /sso/verify-jwt
        # TODO PATCH /users
        # TODO GET /users (Mobile user)

        # Clean up - clear test user from userpool
        # Check for existing test SSO user and wipe it from userpool prior to register api call
        print('\n\nAPI test complete\n\nTest clean up commencing')
        try:
            funct.purgeSSOemail(self, testemailSSO)
        except:
            print('no test user ' + testemailSSO + ' found \n')
        # Check for existing test Mobile user and wipe it from userpool prior to register api call
        try:
            funct.purgeMobile(self, testemailMOB)
            print('test user ' + testemailMOB + ' purged \n')
        except:
            print('no test user ' + testemailMOB + ' found \n')


# use "report" variable in conftest.py to change report style on runner
if __name__ == "__main__":
    if confTest.NYlottoBASE.report == "terminal":
        unittest.main(warnings='ignore')
    elif confTest.NYlottoBASE.report == "html":
        unittest.main(warnings='ignore', testRunner=HtmlTestRunner.HTMLTestRunner(output='<html_report_dir>'))