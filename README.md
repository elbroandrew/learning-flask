## Flask Udemy tutorial

To run Flask app use `python main.py` on win 10 run `py basic.py`

To remove .idea folder `git rm -r --cached .idea`

Install Flask migrate:

`pip install Flask-Migrate`

For Flask `migrations` set up the env or you will get an error:

Linux: `export FLASK_APP=app.py`

Win: `set FLASK_APP=app.py` or for PowerShell `$env:FLASK_APP="app.py"`

then set up the migrations directory:

`flask db init`

setup the migration file:

`flask db migrate -m "some message"`

update the db:

`flask db upgrade`