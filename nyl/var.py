# [Documentation - Setup] This section lists all dependencies
# that are imported for variable file to work
from selenium.webdriver.common.by import By

import funct, confTest

###==============================================================###
# NYL Admin Dash
###==============================================================###
# [Documentation - Summary] This section creates the variables for
# NYL Admin Dashboard objects for testing user flows

# Credentials for NYL Admin Dashboard
class CREDSadmin:
    # obtain creds file from the 1Password QA vault (contact QA lead on project for access)
    # opens specific local creds file with user data according to confTest variable
    if confTest.NYLadminBASE.testdata == 'iddw':
        notepadfile = open('/Users/Shared/testing/andrewpii1212022.txt', 'r')
    elif confTest.NYLadminBASE.testdata == 'real':
        notepadfile = open('/Users/Shared/testing/nyl1212022.txt', 'r')
    # turns variable into a list of every line in above notepadfile
    entry_info = notepadfile.read().splitlines()
    superadmin_username = funct.getCredential(entry_info, 'admin-super-un')
    superadmin_psw = funct.getCredential(entry_info, 'admin-super-psw')

class CREDSaws:
    # obtain creds file from the 1Password QA vault (contact QA lead on project for access)
    # opens specific local creds file with user data according to confTest variable
    notepadfile = open('/Users/Shared/testing/andrewpii1212022.txt', 'r')
    entry_info = notepadfile.read().splitlines()
    aws_acctId = funct.getCredential(entry_info, 'aws-test-accountID')
    aws_email = funct.getCredential(entry_info, 'aws-test-username')
    aws_password = funct.getCredential(entry_info, 'aws-test-password')

# [Documentation - Variables] Elements on Login page
class adminLoginVar:
    email = [By.XPATH, '(//input[@id="signInFormUsername"])[2]', 'email_field']
    password = [By.XPATH, '(//input[@id="signInFormPassword"])[2]', 'password_field']
    forgotPassword_link = [By.XPATH, '/html/body/div[1]/div/div[1]/div[2]/div[2]/div[3]/div/div/form/a', 'forgotPassword_link']
    signin_button = [By.XPATH, '(//input[@name="signInSubmitButton"])[2]', 'signin_button']

# [Documentation - Variables] Elements on Dashboard pages
class adminDashVar:
    home_breadcrumb_link = [By.XPATH, '//*[@id="kt_subheader"]/div/div/div/a[1]', 'home_breadcrumb_link']
    users_link = [By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[1]/a/span', 'users_link']
    pendingDeletion_link = [By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[2]/a/span', 'pendingDeletion_link']
    permanentlyDeleted_link = [By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[3]/a/span', 'permanentlyDeleted_link']
    admins_link = [By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[4]/a/span', 'admins_link']
    features_link = [By.XPATH, '//*[@id="kt_aside_menu"]/ul/li[5]/a/span', 'features_link']
    search_input = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/input', 'search_input']
    category_fname = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/span/ul/li[2]/a', 'category_fname']
    category_lname = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/span/ul/li[3]/a', 'category_lname']
    category_address = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/span/ul/li[4]/a', 'category_address']
    category_phone = [By.XPATH,
                      '//*[@id="kt_content"]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/span/ul/li[5]/a',
                      'category_phone']
    category_email = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/span/ul/li[6]/a', 'category_email']
    operator_contains = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div[1]/div/div[1]/div/div[3]/span/ul/li[2]/a', 'operator_contains']
    search_button = [By.XPATH, '//button[@class="ml-2 btn btn-wide btn-primary btn-upper"]', 'search_button']
    # TODO verify bulk action button references are all removed
    # bulkAction_button = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[2]/div[2]/div/div/div/div/button', 'bulkAction_button']
    # li_verification = [By.XPATH, '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[1]', 'li_verification']
    # li_unverification = [By.XPATH, '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]', 'li_unverification']
    # li_lock = [By.XPATH, '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[3]', 'li_lock']
    # li_unlock = [By.XPATH, '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[4]', 'li_unlock']
    # li_delete = [By.XPATH, '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[5]', 'li_delete']
    # li_cancelDelete = [By.XPATH, '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[1]', 'li_cancelDelete']
    # li_permDelete = [By.XPATH, '//ul[@class="ant-dropdown-menu ant-dropdown-menu-light ant-dropdown-menu-root ant-dropdown-menu-vertical"]/li[2]', 'li_permDelete']
    view_edit_button = [By.XPATH, '//*[@id="local_data"]/div/div/div/div/div/div/table/tbody/tr[1]/td[10]/a/button', 'view_edit_button'] # first row view/edit button
    comment_textarea = [By.XPATH, '//textarea[@id="comment"]', 'comment_textarea']
    comment_phrase_textarea = [By.XPATH, '//input[@id="phrase"]', 'comment_phrase_textarea']
    modal_ok_button = [By.XPATH, '//button[@class="ant-btn ant-btn-primary"]', 'modal_ok_button']
    ext1_modal_ok_button = [By.XPATH, '(//button[@class="ant-btn ant-btn-primary"])[1]', 'ext1_modal_ok_button']
    ext2_modal_ok_button = [By.XPATH, '(//button[@class="ant-btn ant-btn-primary"])[2]', 'ext2_modal_ok_button']

    # TODO due to ongoing Admin Dash work in dev env, different locators are used for same element, will need to update once AD work is complete
    if confTest.globalVar.env == 'dev':
        searchedUser_checkbox = [By.XPATH, '(//input[@type="checkbox"])[2]', 'searchedUser_checkbox']
    else:
        searchedUser_checkbox = [By.XPATH, '//*[@id="local_data"]/div/div/div/div/div/div/table/tbody/tr/td[1]/label/span/input', 'searchedUser_checkbox']
        # searchedUser_checkbox = [By.XPATH, '//*[@id="local_data"]/div/div/div/div/div/div/table/tbody/tr/td[1]/label/span/input']
    pendingDeleteUser_checkbox = [By.XPATH, '(//input[@type="checkbox"])[1]', 'pendingDeleteUser_checkbox']
    no_data_msg = [By.XPATH, '//*[@id="local_data"]/div/div/div/div/div/div/table/tbody/tr/td/div/p', 'no_data_msg']
    extend_button = [By.XPATH, '//button[@class="ant-btn ant-btn-primary"]', 'extend_button']

# Users - Users Details view
class adminUsersVar:
    user_details_tab = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[1]/div[1]/ul/li[1]/a',
                        'user_details_tab']
    user_status_tab = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[1]/div[1]/ul/li[2]/a', 'user_status_tab']
    audit_trail_tab = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[1]/div[1]/ul/li[3]/a', 'audit_trail_tab']
    # Users Details view
    edit_button = [By.XPATH, '//*[@id="local_data"]/div/button/u', 'edit_button']
    phone_input = [By.XPATH, '//*[@id="phone"]', 'phone_input']
    back_button = [By.XPATH, '//button[@class="btn btn-primary"]', 'back_button']
    cancel_button = [By.XPATH, '//*[@id="local_data"]/form/div[12]/div/button[1]', 'cancel_button']
    save_button = [By.XPATH, '//button[@type="submit"]', 'save_button']
    # User Status view
    verification_button = [By.XPATH, '(//button[@type="button"])[1]', 'verification_button']
    reset_password_button = [By.XPATH, '(//button[@type="button"])[2]', 'reset_password_button']
    lock_user_button = [By.XPATH, '(//button[@type="button"])[3]', 'lock_user_button']
    delete_button = [By.XPATH, '(//button[@type="button"])[4]', 'delete_button']

# Pending Deletion - User Details view
class adminPendingDeletionVar:
    user_details_tab = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[1]/div[1]/ul/li[1]/a',
                        'user_details_tab']
    user_status_tab = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[1]/div[1]/ul/li[2]/a', 'user_status_tab']
    audit_trail_tab = [By.XPATH, '//*[@id="kt_content"]/div[2]/div/div/div/div[1]/div[1]/ul/li[3]/a', 'audit_trail_tab']
    # User Details view
    back_button = [By.XPATH, '//button[@class="btn btn-primary"]', 'back_button']
    # User Status view
    verification_button = [By.XPATH, '(//button[@type="button"])[1]', 'verification_button']
    reset_password_button = [By.XPATH, '(//button[@type="button"])[2]', 'reset_password_button']
    lock_user_button = [By.XPATH, '(//button[@type="button"])[3]', 'lock_user_button']
    cancel_deletion_button = [By.XPATH, '(//button[@type="button"])[4]', 'cancel_deletion_button']
    permanently_delete_button = [By.XPATH, '(//button[@type="button"])[5]', 'permanently_delete_button']
###==============================================================###
# NYL Services API
###==============================================================###
# [Documentation - Summary] This file creates the variables for
# NYL Services Api testing

# Credentials for NYL Services API
class CREDSapi:
    # obtain creds file from the 1Password QA vault (contact QA lead on project for access)
    # opens specific local creds file with user data according to confTest variable
    if confTest.NYLservicesBASE.testdata == 'iddw':
        notepadfile = open('/Users/Shared/testing/andrewpii1212022.txt', 'r')
    elif confTest.NYLservicesBASE.testdata == 'real':
        notepadfile = open('/Users/Shared/testing/nyl1212022.txt', 'r')
    # turns variable into a list of every line in above notepadfile
    entry_info = notepadfile.read().splitlines()

    ssoFName = funct.getCredential(entry_info, 'sso-first-name')
    ssoLName = funct.getCredential(entry_info, 'sso-last-name')
    ssoHNum = funct.getCredential(entry_info, 'sso-house-number')
    ssoStreet = funct.getCredential(entry_info, 'sso-street-address')
    ssoCity = funct.getCredential(entry_info, 'sso-city')
    ssoState = funct.getCredential(entry_info, 'sso-state')
    ssoZip = funct.getCredential(entry_info, 'sso-zip')
    ssoPhone = funct.getCredential(entry_info, 'sso-phone')
    ssoSSN = funct.getCredential(entry_info, 'sso-ssn')
    ssoDOBmonth = funct.getCredential(entry_info, 'sso-dob-month')
    ssoDOBDate = funct.getCredential(entry_info, 'sso-dob-date')
    ssoDOBYear = funct.getCredential(entry_info, 'sso-dob-year')
    ssoPW = funct.getCredential(entry_info, 'sso-test-password')
    mobileFName = funct.getCredential(entry_info, 'mobile-first-name')
    mobileLName = funct.getCredential(entry_info, 'mobile-last-name')
    mobilePhone = funct.getCredential(entry_info, 'mobile-phone')
    mobilePW = funct.getCredential(entry_info, 'mobile-test-password')
    devSSOcid = funct.getCredential(entry_info, 'nyl-services-client-id-dev')
    qaSSOcid = funct.getCredential(entry_info, 'nyl-services-client-id-qa')
    stageSSOcid = funct.getCredential(entry_info, 'nyl-services-client-id-stage')
    devSSOxkey = funct.getCredential(entry_info, 'nyl-services-x-api-key-dev')
    qaSSOxkey = funct.getCredential(entry_info, 'nyl-services-x-api-key-qa')
    stageSSOxkey = funct.getCredential(entry_info, 'nyl-services-x-api-key-stage')
    devSSOhgcode = funct.getCredential(entry_info, 'sso-handle-govid-code-dev')
    qaSSOhgcode = funct.getCredential(entry_info, 'sso-handle-govid-code-qa')
    devMOBILEcid = funct.getCredential(entry_info, 'mobile-client-id-dev')
    qaMOBILEcid = funct.getCredential(entry_info, 'mobile-client-id-qa')
    stageMOBILEcid = funct.getCredential(entry_info, 'mobile-client-id-stage')
    devMOBILExkey = funct.getCredential(entry_info, 'mobile-x-api-key-dev')
    qaMOBILExkey = funct.getCredential(entry_info, 'mobile-x-api-key-qa')
    stageMOBILExkey = funct.getCredential(entry_info, 'mobile-x-api-key-stage')
    devFCMtoken = funct.getCredential(entry_info, 'mobile-fcm-token-dev')
    qaFCMtoken = funct.getCredential(entry_info, 'mobile-fcm-token-qa')
    stageFCMtoken = funct.getCredential(entry_info, 'mobile-fcm-token-stage')
    devSSOuserpool = funct.getCredential(entry_info, 'sso-userpool-id-dev')
    qaSSOuserpool = funct.getCredential(entry_info, 'sso-userpool-id-qa')
    stageSSOuserpool = funct.getCredential(entry_info, 'sso-userpool-id-stage')
    devADMINtestuser = funct.getCredential(entry_info, 'admin-test-user-dev')
    qaADMINtestuser = funct.getCredential(entry_info, 'admin-test-user-qa')
    stageADMINtestuser = funct.getCredential(entry_info, 'admin-test-user-stage')

###==============================================================###
# NYL SSO
###==============================================================###
# [Documentation - Summary] This section creates the variables for
# NYL Single Sign On page objects for testing user flows

# [Documentation - Variables] Objects on Registration page
# Credentials for SSO Web user
class credsSSOWEB:
    # obtain creds file from the 1Password QA vault (contact QA lead on project for access)
    # opens specific local creds file with user data according to confTest variable
    if confTest.NYlottoBASE.testdata == 'iddw':
        notepadfile = open('/Users/Shared/testing/andrewpii1212022.txt', 'r')
    elif confTest.NYlottoBASE.testdata == 'real':
        notepadfile = open('/Users/Shared/testing/nyl1212022.txt', 'r')

    # turns variable into a list of every line in above notepadfile
    entry_info = notepadfile.read().splitlines()
    fname = funct.getCredential(entry_info, 'sso-first-name')
    lname= funct.getCredential(entry_info, 'sso-last-name')
    housenum = funct.getCredential(entry_info, 'sso-house-number')
    street = funct.getCredential(entry_info, 'sso-street-address')
    city = funct.getCredential(entry_info, 'sso-city')
    state = funct.getCredential(entry_info, 'sso-state')
    zip = funct.getCredential(entry_info, 'sso-zip')
    phone = funct.getCredential(entry_info, 'sso-phone')
    ssn4 = funct.getCredential(entry_info, 'sso-ssn')
    dob_month = funct.getCredential(entry_info, 'sso-dob-month')
    dob_date = funct.getCredential(entry_info, 'sso-dob-date')
    dob_year = funct.getCredential(entry_info, 'sso-dob-year')
    password = funct.getCredential(entry_info, 'sso-test-password')
    imapEmail = funct.getCredential(entry_info, 'imap-email')
    imapPW = funct.getCredential(entry_info, 'imap-pw')
    tempPW = funct.getCredential(entry_info, 'temp-pw')


# Reg page elements
class regV:
    fname = [By.NAME, 'firstName', 'fname']
    mname = [By.NAME, 'middleName', 'mname']
    lname = [By.NAME, 'lastName', 'lname']
    suffix_dropdown = [By.NAME, 'suffix', 'suffix_dropdown']
    housenum = [By.NAME, 'streetNumber', 'housenum']
    street = [By.NAME, 'street', 'street']
    add2 = [By.NAME, 'addressLine2', 'add2']
    city = [By.NAME, 'city', 'city']
    state_dropdown = [By.NAME, 'state', 'state_dropdown']
    zip = [By.NAME, 'zip', 'zip']
    phone = [By.NAME, 'phone', 'phone']
    ssn4 = [By.NAME, 'ssn4', 'ssn4']
    ss_check = [By.NAME, 'noSsn4', 'ss_check']
    dob = [By.NAME, 'birthdate', 'dob']
    dob_check = [By.NAME, 'isOver18', 'dob_check']
    email = [By.ID, 'sso-email', 'email']
    password = [By.NAME, 'password', 'password']
    confirmPsw = [By.NAME, 'confirmPassword', 'confirmPsw']
    tos_check = [By.NAME, 'acceptedTermsAndConditions', 'tos_check']
    cnw_check = [By.NAME, 'collectnwin', 'cnw_check']
    nylnews_check = [By.NAME, 'newsletter', 'nylnews_check']
    submit_button = [By.XPATH, '//*[@id="app-container"]/div/div[2]/div/div/form/div[2]/div[7]/button/span', 'submit_button']

# error variables
    fname_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(2) > div.is-error.invalid-feedback', 'fname_error']
    lname_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(4) > div.is-error.invalid-feedback', 'lname_error']
    housenum_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(6) > div.is-error.invalid-feedback', 'housenum_error']
    street_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(7) > div.is-error.invalid-feedback', 'street_error']
    city_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(9) > div.is-error.invalid-feedback', 'city_error']
    state_dropdown_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div.form-group.error > div > div', 'state_dropdown_error']
    zip_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(11) > div.is-error.invalid-feedback', 'zip_error']
    phone_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div.form-group.has-prepend > div.is-error.invalid-feedback', 'phone_error']
    dob_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(15) > div.is-error.invalid-feedback', 'dob_error']
    dob_check_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(16) > div > label', 'dob_check_error']
    email_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(2) > div.form-group.has-prepend > div.is-error.invalid-feedback', 'email_error']
    password_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(2) > div:nth-child(3) > div.is-error.invalid-feedback', 'password_error']
    confirmPsw_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(2) > div:nth-child(4) > div.is-error.invalid-feedback', 'confirmPsw_error']
    tos_check_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(2) > div:nth-child(5) > div > label', 'tos_check_error']
    submit_button_error = [By.XPATH, '//p[@class="submit-error"]', 'submit_button_error']

# error copy
    requiredErrorStub = 'Required'
    submitErrorStub = 'Please see required fields above to complete registration.'
    zipErrorStub = 'Invalid zipcode'
    phoneErrorStub = 'Invalid phone number'
    dobErrorStub = 'Please enter a valid birth date'
    dobErrorUnderageStub = 'You must be 18 years or older to register'
    emailErrorStub = 'Invalid email address'
    passwordErrorStub = 'Your password must follow the password guidelines.'
    confirmPswErrorStub = 'Passwords must match'
    duplicateEmailErrorStub = 'This email is already registered with an account. Please log in or reset your password.'
    duplicatePhoneErrorStub = 'This phone number is already registered with an account. Please log in or reset your password.'

# [Documentation - Variables] Objects on OTP pages
class otpV:
# otp method selection page
    text_button = [By.XPATH, '//*[@id="app-container"]/div/div[2]/div/div/div/button[1]/span', 'text_button']
    call_button = [By.XPATH, '//*[@id="app-container"]/div/div[2]/div/div/div/button[2]/span', 'call_button']
# otp code entry page
    otp_input = [By.NAME, 'otp', 'otp_input']
    otp_continue_button = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div > div:nth-child(4) > button > span', 'otp_continue_button']
    retry_call_button = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div > div:nth-child(5] > p > button:nth-child(1]', 'retry_call_button']
    retry_text_button = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div > div:nth-child(5] > p > button:nth-child(2]', 'retry_text_button']

# [Documentation - Variables] Objects on Gov ID pages
class govIdV:
# gov id and upload method selection page
    gov_id_dropdown = [By.NAME, 'govIdType', 'gov_id_dropdown']
    id_drivers_license = [By.XPATH, '//option[@value="US Drivers License"]', 'id_drivers_license']
    id_passport = [By.XPATH, '//option[@value="International Passport"]', 'id_passport']
    mobile_button = [By.XPATH, '//button[@class="nyl-button"]', 'mobile_button']
    mobile_input = [By.ID, 'intlTelephone', 'mobile_input']
    continue_mobile_btn = [By.ID, 'async-continue', 'continue_mobile_btn']
    browser_link = [By.XPATH, '//a[@class="continue-with-browser-link"]', 'browser_link']

# Drivers license and browser capture method
# Document capture page
    dl_start_button = [By.ID, 'dcui-start-button', 'dl_start_button']
# Driver's license front capture page
    dl_front_capture_button = [By.XPATH, '//button[@id="start-capture"]', 'dl_front_capture_button']
# Driver's license front quality check page
    dl_front_discard_button = [By.XPATH, '//button[@id="discard-capture"]', 'dl_front_discard_button']
    dl_front_save_button = [By.XPATH, '//button[@id="save-capture"]', 'dl_front_save_button']
# Driver's license back capture page
    dl_back_capture_button = [By.XPATH, '//button[@id="start-capture"]', 'dl_back_capture_button']
# Driver's license back quality check page
    dl_back_discard_button = [By.XPATH, '//button[@id=["discard-capture"]', 'dl_back_discard_button']
    dl_back_save_button = [By.XPATH, '//button[@id="save-capture"]', 'dl_back_save_button']
# Facial snapshot capture page
    dl_facial_capture_button = [By.XPATH, '//button[@id="start-capture"]', 'dl_facial_capture_button']
# Facial snapshot quality check page
    dl_facial_discard_button = [By.XPATH, '//button[@id=["discard-capture"]', 'dl_facial_discard_button']
    dl_facial_save_button = [By.XPATH, '//button[@id="save-capture"]', 'dl_facial_save_button']
# Document submission page
    id_submit_button = [By.XPATH, '//button[@id="verify-all"]', 'id_submit_button']

# Passport and browser capture method
# Document capture page
    passport_start_button = [By.ID, 'dcui-start-button', 'passport_start_button']
# Passport front capture page
    passport_capture_button = [By.ID, 'capture-input', 'passport_capture_button']
# Passport front quality check page
    passport_discard_button = [By.ID, 'discard-capture', 'passport_discard_button ']
    passport_save_button = [By.ID, 'save-capture', 'passport_save_button ']
# Facial snapshot capture page
    passport_facial_capture_button = [By.ID, 'capture-input', 'passport_facial_capture_button']
# Facial snapshot quality check page
    passport_facial_discard_button = [By.CSS_SELECTOR, '#discard-capture', 'passport_facial_discard_button']
    passport_facial_save_button = [By.CSS_SELECTOR, '#save-capture', 'passport_facial_save_button']

# TODO at a future date with Appium inspection session
# Drivers license and mobile capture method
# Passport and mobile capture method

# [Documentation - Variables] Objects on Login page
class loginV:
    email = [By.ID, 'sso-email', 'email']
    password = [By.NAME, 'password', 'password']
    login_button = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div > div.button-wrap > button > span', 'login_button']
    forgot_password_link = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div > div.button-wrap > p > a', 'forgot_password_link']

# error variables
    email_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div > div.form-group.has-prepend > div.is-error.invalid-feedback', 'email_error']
    password_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div > div:nth-child(3) > div.is-error.invalid-feedback', 'password_error']
    login_button_error = [By.XPATH, '//p[@class="submit-error"]', 'login_button_error']

# error copy
    requiredErrorStub = 'Required'
    emailErrorStub = 'Invalid email address'
    loginErrorStub = 'There is a problem with the data you entered, please try again.'
    badEmailErrorStub = 'The username and password combination did not match. Users with accounts on the Official NY Lottery Winning Numbers app will need to register a new account.'
    badPasswordErrorStub = 'Your email address and password do not match.'
    # [Documentation - Variables] Objects on Reset Password page
class resetPswV:
    email = [By.NAME, 'email', 'email']
    reset_submit_button = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div > div.button-wrap > button > span', 'reset_submit_button']
    error1 = [By.XPATH, '//*[@class="is-error invalid-feedback"]', 'error_message1']
    error2 = [By.XPATH, '//*[@class="submit-error"]', 'error_message2']
    success = [By.XPATH, '//*[@class="alert alert-success mt-5"]', 'success_message1']
    resetError = [By.XPATH, '//*[@class="submit-error"]', 'error_message3']
    newPwField = [By.XPATH, '//*[@name="password"]', 'confirmPwField']
    confirmPwField = [By.XPATH, '//*[@name="confirmPassword"]', 'confirmPwField']
    resetPwButton = [By.XPATH, '//*[@class="nyl-button"]', 'resetPwButton']
    matchError = [By.XPATH, '//*[@class="is-error invalid-feedback"]', 'passwordMatchError']
    google = [By.XPATH, '//*[@title="Search"]', 'proofOfGoogle']
    gSearchButton = [By.XPATH, '(//input[@value="Google Search"])[2]', 'gSearchButton']
    
    

#error copy
    error1Stub = 'Invalid email address'
    error2Stub = 'All inputs must be valid in order to submit the form.'
    resetErrorStub = "All inputs must be valid in order to submit the form."
    matchErrorStub = "Your password must follow the password guidelines."

# [Documentation - Variables] Objects on Update Profile page
class updateProfV:
    fname = [By.NAME, 'firstName', 'fname']
    mname = [By.NAME, 'middleName', 'mname']
    lname = [By.NAME, 'lastName', 'lname']
    suffix = [By.NAME, 'suffix', 'suffix']
    housenum = [By.NAME, 'streetNumber', 'housenum']
    street = [By.NAME, 'street', 'street']
    add2 = [By.NAME, 'addressLine2', 'add2']
    city = [By.NAME, 'city', 'city']
    state_dropdown = [By.NAME, 'state', 'state_dropdown']
    zip = [By.NAME, 'zip', 'zip']
    phone = [By.NAME, 'phone', 'phone']
    dob = [By.NAME, 'birthdate', 'birthdate']
    email = [By.ID, 'sso-email', 'email']
    update_button = [By.XPATH, '//button[@class="nyl-button"]', 'update_button']
    signout_button = [By.CLASS_NAME, 'sign-out-all-cta', 'signout_button']

# error variables
    fname_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(2) > div.is-error.invalid-feedback', 'fname_error']
    lname_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(4) > div.is-error.invalid-feedback', 'lname_error']
    housenum_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(6) > div.is-error.invalid-feedback', 'housenum_error']
    street_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(7) > div.is-error.invalid-feedback', 'street_error']
    city_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(9) > div.is-error.invalid-feedback', 'city_error']
    state_dropdown_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div.form-group.error > div > div', 'state_dropdown_error']
    zip_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(11) > div.is-error.invalid-feedback', 'zip_error']
    phone_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div.form-group.has-prepend > div.is-error.invalid-feedback', 'phone_error']
    dob_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(1) > div:nth-child(13) > div.is-error.invalid-feedback', 'dob_error']
    update_button_error = [By.CSS_SELECTOR, '#app-container > div > div.container__content > div > div > form > div:nth-child(2) > div.button-group-wrapper > div > p', 'update_button_error']

# error copy
    requiredErrorStub = 'Required'
    fnameErrorStub = 'Must contain only letters'
    lnameErrorStub = 'Must contain only letters'
    cityLengthErrorStub = 'If your town name is over 21 characters, please submit only 20 characters and the form will identify town based on zip code.'
    zipErrorStub = 'Invalid zipcode'
    phoneErrorStub = 'Invalid phone number'
    dobErrorStub = 'Please enter a valid birth date'
    updateErrorStub = 'All inputs must be valid in order to submit the form.'

# [Documentation - Variables] Objects on Confirm Details page
class confirmDetailsV:
    submit_button = [By.XPATH, '//button[@class="nyl-button"]', 'submit_button']

# [Documentation - Variables] Objects on Identity Verification Failed page
class identityVerFailedV:
    failed_body = [By.XPATH, '//div[@class="migration-failed-body"]', 'failed_body']
class loginAWS:
        aws_acctId = [By.CSS_SELECTOR, '.textinput #account', 'account_Id']
        aws_email = [By.ID, 'username', 'aws_email']
        aws_password = [By.CSS_SELECTOR, '.textinput #password', 'aws_password']
        aws_signin_button = [By.ID, 'signin_button', 'login_button']
        aws_forgot_password_link = [By.CSS_SELECTOR, '#link_root_account_signin #root_account_signin',
                       'forgot_password_link']

        # error variables
        aws_account_Id_error = [By.CSS_SELECTOR, '#input_account label[for=\'account\']', 'aws_accountId_error']
        aws_email_error = [By.CSS_SELECTOR, '.textinput.error label[for=\'username\']', 'aws_email_error']
        aws_password_error = [By.CSS_SELECTOR, '.textinput.error label[for=\'password\']', 'aws_password_error']
        aws_login_button_error = [By.ID, 'main_message', 'aws_login_button_error']
        aws_textfield_error_class = [By.CLASS_NAME, 'textinput.error', 'mandatory']
        # error copy
        aws_account_Id_errorstub = 'Account ID (12 digits) or account alias'
        aws_email_errorstub = 'IAM user name'
        aws_password_errorstub = 'Password'
        aws_badCredentials_errorstub = 'Your authentication information is incorrect. Please try again.'

class cloudWatchAWS:
        aws_Logo = [By.ID, 'nav-home-link', 'AWS Logo']
        aws_services = [By.CSS_SELECTOR, 'button[data-testid=\'aws-services-list-button\']', 'Services']
        aws_services_search = [By.CSS_SELECTOR, 'div[class*=\'globalNav-search\'] input[placeHolder=\'Search\']', 'Services search']
        aws_cloudwatch_search = [By.XPATH, '//h3/a[@data-testid="services-search-result-link-cw"]', 'Cloud Watch']
        aws_logs = [By.XPATH, '//div[@class=\'navigation-header\']//span[contains(text(),\'Logs\')]', 'Logs']
        aws_logGroups = [By.XPATH, '//li[@id=\'nav-logsGroups-wrapper\']//a[text()=\'Log groups\']', 'Log Groups']
        aws_searchAllLogStreams = [By.XPATH, '//span[contains(text(),"Search all log streams")]/ancestor::button', 'Search All Log Streams']
        aws_1hLogs = [By.XPATH, '//span[text()="1h"]/ancestor::button', 'One Hour Logs']
        aws_logGroupsSearch = [By.XPATH, '//input[@placeholder="Filter log groups or try prefix search"]', 'Log Groups search']
        aws_logGroupsSearchResults = [By.XPATH, '//table//strong/ancestor::a[contains(@href,\'qa-postSsoRegisterVerify\')]', 'Log Groups Search Results']
        aws_logEventsSearch = [By.XPATH, '//div[@class=\'awsui-input-container\']//input[@placeholder=\'Filter events\']', 'Log Events Search']
        aws_openAll = [By.CSS_SELECTOR, 'thead[class=\'awsui-table-sticky-active\'] label input[id*=\'awsui-checkbox\']', 'Open all Arrow']
        aws_logStatusCode_successCode = [By.XPATH, '//span[@class=\'logs__events__json-number\'][contains(text(),\'200\')]', 'Status Code Success 200']
        aws_logStatus_SUCCESS = [By.XPATH, '//*[@class = \'logs__events__json\']//span[@class=\'logs__events__json-string\'][contains(text(),\'SUCCESS\')][.][2]', 'Status Success is SUCCESS']
        aws_noEventsFound = [By.XPATH, '//table[@role=\'table\']/tbody/tr/td/span', 'No events found']
class cognitoAWS:
        aws_cognito_search = [By.XPATH, '//h3/a[@data-testid="services-search-result-link-c"]', 'Cognito']
        aws_cognito_cognitoPageHeader = [By.XPATH, '//h1[text()=\'Amazon Cognito\']', 'Amazon Cognito']
        aws_cognito_ManageUserPools = [By.XPATH, '//div[@class = \'cog-billboard\']//a[@id = \'btnStart\']', 'Manage User Pools']
        aws_cognito_userPool = [By.XPATH, '//h2[@title=\'qa-nyl-sso-pool\']', 'User Pools']
        aws_cognito_usersAndGroups = [By.XPATH, '//span[text()=\'Users and groups\']/ancestor::a', 'Users and Groups']
        aws_cognito_userNameDropdown = [By.XPATH, '//span[text()=\'User name\']/preceding::div[@class=\'columbia-select__display columbia-select__display--type--primary\']', 'Email Dropdown']
        aws_cognito_selectEmailOption = [By.XPATH, '//div[contains(@data-reactid, \'option_email\')]', 'Select the option Email from UserName dropdown']
        aws_cognito_inputSearch = [By.XPATH, '//input[contains(@placeholder,\'Search for value... \')]', 'Search value']
        aws_cognito_emailRow = [By.XPATH, '//table[@class=\'cog-user-table\']//a', 'Select eMail row']
        aws_cognito_firstName = [By.XPATH, '//td[contains(@data-reactid,\'given_name\')]', 'First Name']
        aws_cognito_lastName = [By.XPATH, '//td[contains(@data-reactid,\'family_name\')]', 'Last Name']
        aws_cognito_address = [By.XPATH, '//td[contains(@data-reactid,\'address.1\')]', 'Address']
        aws_cognito_lexId = [By.XPATH, '//td[contains(@data-reactid,\'lex_id\')]', 'LexId']
        aws_cognito_birthdate = [By.XPATH, '//td[contains(@data-reactid,\'birthdate\')]', 'Birth Date']
        aws_cognito_phoneNumber = [By.XPATH, '//td[contains(@data-reactid,\'phone_number.\')]', 'Phone Number']
        aws_cognito_email = [By.XPATH, '//td[contains(@data-reactid,\'email.\')]', 'Email']

class rdsAWS:
        aws_rds_dashboardrds = [By.XPATH, '//div[contains(@class,\'dashboardWidgetBody\')]//img[@alt=\'RDS\']//parent::div/div/a', 'RDS']
        aws_rds_pageHeader = [By.XPATH, '//a[text()=\'Amazon RDS\']', 'Amazon RDS']
        aws_rds_queryEditorLink = [By.XPATH, '//a[text()=\'Query Editor\']', 'Query Editor']
        aws_rds_connectToDatabasePage = [By.XPATH, '//div[text()=\'Connect to database\']', 'Connect to Database Page']
        aws_rds_chooseDatabaseCluster = [By.XPATH, '//span[text()=\'Choose a database instance or cluster\']', 'Choose a database instance or cluster']
        aws_rds_chooseDatabaseClusterValue = [By.XPATH, '//span[@class=\'awsui-select-option-label\']', 'Select Cluster value from dropdown']
        aws_rds_userName = [By.XPATH, '//div//span[text() = \'Choose a username\']', 'RDS UserName']
        aws_rds_userNameValue = [By.XPATH, '//div[@class="awsui-select-open"]//div[@title=\'postgres\']', 'RDS UserName value']
        aws_rds_passWord = [By.XPATH, '//input[@type="password"]','RDS Password']
        aws_rds_databaseName = [By.XPATH, '//input[@placeholder="Enter database name"]', 'RDS Database Name']
        aws_rds_connectDatabaseBtn = [By.ID, 'qfc-connect-db-modal-connect-btn', 'Connect to RDS Database Button']
        aws_rds_editorTab = [By.XPATH, '//span[text()=\'Editor\']', 'RDS Editor Tab for Queries']
        aws_rds_clearButton = [By.XPATH, '//span[text()=\'Clear\']/parent::button', 'Clear button']
        aws_rds_RunButton = [By.XPATH, '//span[text()=\'Run\']/parent::button', 'Run button']
        aws_rds_statusSuccess = [By.XPATH, '//span[text()=\'Success\']', 'Status Success']
        aws_rds_rowsReturned = [By.XPATH, '//a[text()=\'1 rows returned\']', '1 Row Returned']
