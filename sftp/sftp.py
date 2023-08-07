# [Documentation - Setup] This section lists all dependencies
# that are imported for this test file to work
import pysftp
import unittest, HtmlTestRunner

# [Documentation - Summary] function to grab credentials from locally stored credential file via their label
def getCred(target):
        sftpCreds = open('/Users/Shared/testing/sftpCreds.txt', 'r')
        entry_info = sftpCreds.read().splitlines()
        targ = str(target + ': ')
        credential = [item for item in entry_info if item.startswith(targ)][0]
        cred = credential.replace(targ, '')
        return cred


class NYLsftp(unittest.TestCase):
# [Documentation - Summary] sets variables for all testcases below
    def setUp(self):
        
        self.myHostname = getCred('devHost')
        self.myUsernameNYL = getCred('nylUsername')
        self.myUsernameSSH = getCred('nylUSernameSSH')
        self.myUsernameMc = getCred('mccannUsername')
        self.myUsernameMcSSH = getCred('mccannUsernameSSH')
        self.myPasswordMc = getCred('mccannPassword')
        self.myPasswordNYL = getCred('nylPassword')
        self.localFile = 'testFile.txt'
        self.remoteFileNYL = '/Prod/NYSL/test100.txt'
        self.remoteFileMcCann = '/Prod/McCann/test100.txt'
        self.private_key = "~/.ssh/id_rsa"
        self.cnopts = pysftp.CnOpts()
        self.cnopts.hostkeys = None

 # [Documentation - Summary] functions starting with "test" are recognized bu unittest as test cases, and run in abc 
 # order   
    def test00_checkLoginNoPwNYL(self):
        try:
            # [Documentation - Detail] pysftp.connection takes multiple arguements such as host, username, and password
            # in order to create an sftp connection. For Advanced options such as Private Keys, you can use cnopts 
            # attribute, and define the advanced arguements within that (see test 08 below for example).
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameNYL, password='', cnopts=self.cnopts) as sftp:
                # [Documentation - Detail] raises exception, ignoring the Try/Except soft fail
                raise Exception('E--- Able to log in with incorrect password!')    
        except:
            print("incorrect password test passed")

    def test01_checkLoginNoUnNYL(self):
        try:
            with pysftp.Connection(host=self.myHostname, username='', password=self.myPasswordNYL, cnopts=self.cnopts) as sftp:
                raise Exception('E--- Able to log in with incorrect username!')    
        except:
            print("incorrect username test passed")
    
    def test02_checkFileStructureNYL(self):
        try:
            n = 0
            m = 0
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameNYL, password=self.myPasswordNYL, cnopts=self.cnopts) as sftp:
                print("nyl un/pw logs in correctly")
                # [Documentation - Detail] sftp.cwd navigates user within an sftp connection into the folder path used 
                # as the arguement
                sftp.cwd('/Prod/')
                # [Documentation - Detail] sftp.listdir_attr() returns a list of every entry in the current directory
                directory_structure = sftp.listdir_attr()
                for attr in directory_structure:
                    # [Documentation - Detail] attr.filename, as used here will print the file name of each entry in 
                    # the current directory
                    if 'McCann' in attr.filename:
                        m = 1
                    if 'NYSL' in attr.filename:
                        n = 1
                if m == 0:
                    print("E--- file structure missing Mccann!")
                    if n == 0:
                        raise Exception('E--- file structure missing NYSL!')
                else:
                    pass
                if n == 0:
                    raise Exception('E--- file structure missing NYSL!')
                else:
                    print("correct login for NYL user test passed")
        except:
            raise Exception("E--- Error using correct UN/PW!")
    def test03_checkDownloadMcCannFileNYL(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameNYL, password=self.myPasswordNYL, cnopts=self.cnopts) as sftp:
                # [Documentation - Detail] sftp.get attempts to allow you to download the file in the first arguement 
                # and save it to the location in the second arguement
                sftp.get(self.remoteFileMcCann, '')
                print('Able to DL McCann File as NYL user')
        except:
            raise Exception("E--- Unable to DL McCann File as NYL user!")
    
    def test04_checkDownloadNylFileNYL(self):

        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameNYL, password=self.myPasswordNYL, cnopts=self.cnopts) as sftp:
                sftp.get(self.remoteFileNYL, '')
                print("NYL user DLing Mccann file test passed")
        except:
            raise Exception('E--- Unable to DL NYL File as NYL user!')
    
    def test05_checkUploadMcCannFileNYL(self):
        try:

            with pysftp.Connection(host=self.myHostname, username=self.myUsernameNYL, password=self.myPasswordNYL, cnopts=self.cnopts) as sftp:
                sftp.cwd('/Prod/McCann/')
                # [Documentation - Detail] sftp.put attempts to allow you to upload a file found in the path fo the 
                # first arguement, and save it to the path in the second arguement
                sftp.put(self.localFile, 'testFile.txt')
                print("W--W---If following statement doesn't say 'file deleted', must delete file manually!")
                # [Documentation - Detail] sftp.remove attempts to remove the file found in the path of the arguement
                sftp.remove('testFile.txt')
                print('file deleted')
                raise Exception('E--- Able to Upload McCann File as NYL user!')
        except:
            print("NYL user Uploading Mccann file test passed")

    def test06_checkUploadNylFileNYL(self):  
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameNYL, password=self.myPasswordNYL, cnopts=self.cnopts) as sftp:
                sftp.cwd('/Prod/NYSL/')
                sftp.put(self.localFile, 'testFile.txt')
                sftp.remove('testFile.txt')
                print('file deleted, NYL user Uploading NYL file test passed')
        except:
            print('W--W--- Check for non deleted file')
            raise Exception('E--- Unable to Upload NYL File as NYL user!')

    def test07_checkSshCanNotLoginNYL(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameNYL, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                raise Exception('E--- Able to log in with SSH key with incorrect username!')    
        except:
            print("incorrect username for ssh test passed")

    def test08_checkSshCanLoginSSHnyl(self):
        try:
            # [Documentation - Detail] as states above, using Private_Key and the advanced cnopts arguements, you are 
            # able to sign in with ssh keys instead of passwords
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                print('login passed')    
        except:
            raise Exception('E--- Unable to log in with SSH key with correct username!')

    def test09_checkFileStructureSSHnyl(self):
        try:
            n = 0
            m = 0
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                print("nyl un/pw logs in correctly")
                sftp.cwd('/Prod/')
                directory_structure = sftp.listdir_attr()
                for attr in directory_structure:
                    if 'McCann' in attr.filename:
                        m = 1
                    if 'NYSL' in attr.filename:
                        n = 1
                if m == 0:
                    print("E--- file structure missing Mccann!")
                    if n == 0:
                        raise Exception('E--- file structure missing NYSL!')
                if n == 0:
                    raise Exception('E--- file structure missing NYSL!')
                else:
                    print("correct login for NYL user test passed")
        except:
            raise Exception("E--- Error using correct UN/PW!")

    def test10_checkDownloadMcCannFileSSHnyl(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                sftp.get(self.remoteFileMcCann, '')
                print('Able to DL McCann File as NYL user')
        except:
            raise Exception("E--- Unable to DL McCann File as NYL user!")

    def test11_checkDownloadNylFileSSHnyl(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                sftp.get(self.remoteFileNYL, '')
                print("NYL user DLing Mccann file test passed")
        except:
            raise Exception('E--- Unable to DL NYL File as NYL user!')

    def test12_checkUploadMcCannFileSSHnyl(self):
        try:

            with pysftp.Connection(host=self.myHostname, username=self.myUsernameSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                sftp.cwd('/Prod/McCann/')
                sftp.put(self.localFile, 'testFile.txt')
                print("W--W---If following statement doesn't say 'file deleted', must delete file manually!")
                sftp.remove('testFile.txt')
                print('file deleted')
                raise Exception('E--- Able to Upload McCann File as NYL user!')
                
        except:
            print("NYL user Uploading Mccann file test passed")

    def test13_checkuploadNylFileSSHnyl(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                sftp.cwd('/Prod/NYSL/')
                sftp.put(self.localFile, 'testFile.txt')
                sftp.remove('testFile.txt')
                print('file deleted, NYL user Uploading NYL file test passed')
        except:
            print('W--W--- Check for non deleted file')
            raise Exception('E--- Unable to Upload NYL File as NYL user!')
    
    def test14_checkFileStructureMc(self):
        try:
            n = 0
            m = 0
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMc, password=self.myPasswordMc, cnopts=self.cnopts) as sftp:
                print("nyl un/pw logs in correctly")
                sftp.cwd('/Prod/')
                directory_structure = sftp.listdir_attr()
                for attr in directory_structure:
                    if 'McCann' in attr.filename:
                        m = 1
                    if 'NYSL' in attr.filename:
                        n = 1
                if m == 0:
                    raise Exception("E--- file structure missing Mccann!")
                else:
                    pass
                if n == 0:
                    raise Exception('E--- file structure missing NYSL!')
                else:
                    print("correct login for NYL user test passed")
        except:
            raise Exception("E--- Error using correct UN/PW!")

    def test15_checkDownloadMcCannFileMc(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMc, password=self.myPasswordMc, cnopts=self.cnopts) as sftp:
                sftp.get(self.remoteFileMcCann, '')
                print('Able to DL McCann File as NYL user')
        except:
            raise Exception("E--- Unable to DL McCann File as NYL user!")
    
    def test16_checkDownloadNylFileMc(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMc, password=self.myPasswordMc, cnopts=self.cnopts) as sftp:
                sftp.get(self.remoteFileNYL, '')
                print("NYL user DLing Mccann file test passed")
        except:
            raise Exception('E--- Unable to DL McCann File as NYL user!')

    def test17_checkUploadNylFileMc(self):
        try:

            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMc, password=self.myPasswordMc, cnopts=self.cnopts) as sftp:
                sftp.cwd('/Prod/NYSL/')
                sftp.put(self.localFile, 'testFile.txt')
                print("W--W---If following statement doesn't say 'file deleted', must delete file manually!")
                sftp.remove('testFile.txt')
                print('file deleted')
                raise Exception('E--- Able to Upload NYL File as McCann user!')
                
        except:
            print("McCann user Uploading NYL file test passed")

    def test18_checkUploadMcCannFileMc(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMc, password=self.myPasswordMc, cnopts=self.cnopts) as sftp:
                sftp.cwd('/Prod/McCann/')
                sftp.put(self.localFile, 'testFile.txt')
                sftp.remove('testFile.txt')
                print('file deleted, McCann user Uploading McCann file test passed')
        except:
            print('W--W--- Check for non deleted file')
            raise Exception('E--- Unable to Upload McCann File as McCann user!')
            

    def test19_checkSshCanNotLoginMc(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMc, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                raise Exception('E--- Able to log in with SSH key with incorrect username!')    
        except:
            print("incorrect username for ssh test passed")

    def test20_checkFileStructureMcSSH(self):
        try:
            n = 0
            m = 0
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMcSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                print("nyl un/pw logs in correctly")
                sftp.cwd('/Prod/')
                directory_structure = sftp.listdir_attr()
                for attr in directory_structure:
                    if 'McCann' in attr.filename:
                        m = 1
                    if 'NYSL' in attr.filename:
                        n = 1
                if m == 0:
                    raise Exception("E--- file structure missing Mccann!")
                else:
                    pass
                if n == 0:
                    raise Exception('E--- file structure missing NYSL!')
                else:
                    print("correct login for NYL user test passed")
        except:
            raise Exception("E--- Error using correct UN/PW!")


    def test21_checkDownloadMcCannFileMcSSH(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMcSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                sftp.get(self.remoteFileMcCann, '')
                print('Able to DL McCann File as NYL user')
        except:
            raise Exception("E--- Unable to DL McCann File as NYL user!")

    def test22_checkDownloadNylFileMcSSH(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMcSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                sftp.get(self.remoteFileNYL, '')
                print("NYL user DLing Mccann file test passed")
        except:
            raise Exception('E--- Unable to DL NYL File as NYL user!')

    def test23_checkUploadMcCannFileMcSSH(self):
        try:

            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMcSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                sftp.cwd('/Prod/NYSL/')
                sftp.put(self.localFile, 'testFile.txt')
                print("W--W---If following statement doesn't say 'file deleted', must delete file manually!")
                sftp.remove('testFile.txt')
                print('file deleted')
                raise Exception('Able to Upload NYL File as Mccann user!')
        except:
            print("McCann SSH user unable to Upload NYL file!")

    def test24_checkFileStructureMcSSH(self):
        try:
            with pysftp.Connection(host=self.myHostname, username=self.myUsernameMcSSH, private_key=self.private_key, cnopts=self.cnopts) as sftp:
                sftp.cwd('/Prod/McCann/')
                sftp.put(self.localFile, 'testFile.txt')
                sftp.remove('testFile.txt')
                print('file deleted, NYL user Uploading NYL file test passed')
        except:
            print('W--W--- Check for non deleted file')
            raise Exception('E--- Unable to Upload McCann File as McCann SSH user!')
            
    # McCann cannot login with no or incorrect UN
    def test25_checkLoginNoUnMc(self):
        try:
            with pysftp.Connection(host=self.myHostname, username='', password=self.myPasswordMc, cnopts=self.cnopts) as sftp:
                raise Exception('E--- Able to log in with incorrect McCann username!')
        except:
            print("Incorrect McCann username test passed")
# Boiler plate code to run the test suite

if __name__ == "__main__":
#First runner will enable html logs on your current directory(the one you are running this python script from), 
#Second runner will keep local console logs
        unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='html_report_dir'))
        #unittest.main()