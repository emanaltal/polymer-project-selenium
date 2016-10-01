# polymer-project-selenium
Write a Selenium Automated test suite for the following site: https://shop.polymer-project.org/

# Task Requirements: 
Test Case should include:
* Clicking on the home page the “Men’s outwear” and verify the list of items
* Clicking on the home page the “Ladies outwear” and verify the list of items
* Add Ladies Colorblock Wind Jacket (From Ladies Outwear) & Inbox - Subtle Actions T-shirt (From Men’s
T-Shirt) to the Cart
* Checkout The cart by filling in with some fake details and Place order?

# Files and Folders:
--------------------
* config.cfg: The testsuite configuration file.
* requirements.txt: The testsuite python packages requirements file.
* testsuite: The testsuite folder holding testcases files and testframework.
* testsuite/test_task: The testcase file for the task.
* testframework: The testframework folder for base testcase classes and utilities.
* testframework/base.py: The testframework base file for testcase classes and utilities.
* logs: The testsuite logging folder will be created during operations containing the log file.

# Requirements:
1- linux machine with gui (Ubuntu Desktop) and browser (Firefox)
----------------------------------------------------------
2- If you don't have python 2.7 use this commands to install:
-----------------------------------------------------------
```
sudo add-apt-repository ppa:fkrull/deadsnakes
sudo apt-get update
sudo apt-get install python2.7
sudo apt-get install python-pip
```

Install Python Packages:
------------------------
```
python$> pip install -r requirements.txt
```

Run the tests:
--------------
```
python$> nosetests -v testsuite --tc-file=config.ini
```

See test results:
--------------
```
python$> cat logs/portal_testsuite.log
```
