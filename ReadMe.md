Front End: https://frontend.nopcommerce.com/
Back End: https://admin-demo.nopcommerce.com/login?ReturnUrl=%2Fadmin%2F

Step 1: Create new project and install required Packages/Plugins

pip install selenium pytest pytest-html pytest-xdist openpyxl

Step 2: Create folder structure

    Project name
            |
            pageObjects(Package)
            |
            testCases(Package)
            |
            utilities(Package)
            |
            TestData{folder}
            |
            Configurations(Folder)
            |
            Logs(Folder)
            |
            Screenshots(Folder)
            |
            Reports(Folder)
            |
            Run.bat
Step 3:
    Create LoginPage poage object
    Create Login test under testcases foldre
    create conftest.py under testcases

Step 4: 
    Capture the screenshot on failures

Step 5:Read common values from ini file
    add config.ini inn configurations folder
    create readProperties.py utilities file 
    replace the hardcoded values in login test case

Step 6: Adding logs to the test case
    Add customlogger.py under utlities package
    add logs to login test case

Step 7: Run Tests on Desired Browser/Cross Browser/Parallel
    Update conftest.py with required fisxtures which will accept command line arguement
    Pass browser name as argument in command line: pytest -v -s .\testCases\test_login.py --browser chrome (or firefox)
    Use pytest-xdist to run tests in parallel

Inorder to run tests in parallel instances of browsers install pytest-xdist and use the command
pytest -v -s -n=2 .\testCases\test_login.py
where n is the number of instances required
    
