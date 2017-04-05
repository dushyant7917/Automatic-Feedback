# Automatic-Feedback
Python program to fill the feedback form with just one command!

### Prerequisites before running the script
1. Python
2. Selenium
3. Firefox
4. Geckodriver

### Install selenium
```
pip install selenium
```
### Install geckodriver
1. Download geckodriver package
```
wget https://github.com/mozilla/geckodriver/releases/download/v0.13.0/geckodriver-v0.13.0-linux64.tar.gz
```
2. Extract geckodriver
```
tar -xvzf geckodriver-v0.13.0-linux64.tar.gz
```
3. Make driver executable
```
chmod +x geckodriver
```
4. Add the driver to your path script path
```
export PATH=$PATH:/path-to-extracted-package(geckodriver)
```

### Modify the email and password credentials in the script and run the below command
```
python feedback.py
```
