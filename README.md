# selenium-ui-testing-sample
Example of testing a ui with selenium and python

## Installation
For this project you will python 3, selenium and firefox driver

### Install Firefox driver
#### Linux:
1. Download the geckodriver from the project on Github: https://github.com/mozilla/geckodriver
2. Extract the file: `tar -xvzf geckodriver*`
3. Make it executable: `chmod +x geckodriver`
4. Add driver to your PATH: `export PATH=$PATH:path-to-extracted-file/.`

#### OSX
1. Use homebrew to install: `brew install geckodriver`

### Install python requirements:
    pip install -r requirements.txt

## Usage

The site under test is `https://automationintesting.online/#/` and we are using selenium with the firefox geckodriver to test it.  Tests files will be located in the tests folder and page objects will be kept in the modal folder of the project.  The project structure, currently, looks like this:

    selenium-ui-testing-sample/
    ---> modal/
    -------->webtester.py
    ---> tests/
    -------->test_app.py

To add a new tests, created an object of the page you want to test and save it in `modal/`.  The object will have selenium functions needed to click and navigate the page.  Then create a test file and save it in the `tests` folder.  The name of the test file sould start with `test_`.

Running the tests after that should only require typing:

    pytest

The geckodriver will write a log, which is currently saved to the root of the project and named `geckodriver.log`