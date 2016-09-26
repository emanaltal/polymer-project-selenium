# polymer-project-selenium
Write a Selenium Automated test suite for the following site: https://shop.polymer-project.org/


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
python$> nosetests -xv testsuite --tc-file=config.ini 2>testresults.log
```

See test results:
--------------
```
python$> cat testresults.log
```