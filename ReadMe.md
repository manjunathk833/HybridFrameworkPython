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
    create conftest.py underr testcases

Step 4: 
    Capture the screenshot on failures