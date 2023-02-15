# fetch-backend-th
This is a Django Rest Framework API that provides endpoints for Fetch Rewards backend take-home assignment.
## Installation with Docker
1. Clone repository: `git clone https://github.com/stanleyzzheng/fetch-backend-th [your-directory-name-of-choice]`
2. Build Docker Image: `docker build --t django_project .`
3. Run Docker image on port 8000: `docker run -d -p 8000:8000 django_project`

## Usage
Go ahead and test your application with Postman or your testing method of choice.

## API endpoints:
1. `POST /receipts/process/` posts receipt with format given, returns JSON response with id.
2. `GET /receipts/[id]/points/` returns the points for the receipt.
3. `GET /receipts/` gets all receipts. 
4. `GET /receipts/[id]/` gets single receipt detail.


## Tech stack/ languages used:
1. Python/Django/django-rest-framework + built in django sqlite3 database for testing

## Local Testing
You can also test project locally if you have python 3.x installed in your machine
1. git clone repository in your directory of choice
2. `python -m venv venv`
3. `venv/scripsts/activate`
4. `pip install -r requirements.txt`
5. `python manage.py runserver`
