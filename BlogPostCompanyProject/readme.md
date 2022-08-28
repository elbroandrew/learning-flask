## Puppy blog posts project
go into BlogPostCompanyProject from main directory of the repo: `cd BlogPostCompanyProject`

then set up the FLASK_APP var for win 10:

`$env:FLASK_APP="app.py"`

linux:

`export FLASK_APP=app.py`

init DB (before that delete any existing DB and migrations folder):

`flask db init`

`flask db migrate -m "some message here"`

`flask db upgrade`

run flask app on win10:
`py app.py`

linux:
`python3 app.py`