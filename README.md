![](https://img.shields.io/badge/%E2%9C%A8-Open%20Source-blue)
# UnBillIt-Transform-Your-Bills
UnBillIt Initiate all transaction of Bills online. It uses an End Point API to create provide an authorized way of credentials and enable the users to use the Services.

To run this Flask app, Please follow these instructions:

Execute following commands in the same directory as this project

To make sure you have all the required packages please run:
```pip install -r "requirements.txt"```

For Windows:
```set FLASK_APP=app.py```
For MacOS/Linux:
```export FLASK_APP=app.py```

Next commands are common for all three platforms(i.e. Windows, MacOS and Linux):
```flask db init```
```flask db migrate -m "Any message of your choice"```
```flask db upgrade```

To run the app just execute one of following commands:
Either:
```python3 app.py```
or:
```flask run```

Then copy and paste the localhost site to the web browser.
