Requirements 
Python=3.8.2

Setup

Create a virtual environment to install dependencies in and activate it:

$ python3 -m venv env
$ source env/bin/activate

Then clone the repository:

$ git clone https://github.com/bohdanshlyah/MembersClub.git
$ cd MembersClub

Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/main/.


