# fetch-backend-th
This is a Django Rest Framework API that provides endpoints for Fetch Rewards backend take-home assignment.
## Installation with Docker
1. Clone repository: `git clone https://github.com/stanleyzzheng/fetch-backend-th [your-directory-name-of-choice]`
2. Build Docker Image: `docker build --t django_project .`
3. Run Docker image on port 8000: `docker run -d -p 8000:8000 django_project`

## Usage
Go ahead and test your application with Postman or your testing method of choice.

## API endpoints:
--`GET /receipts/` gets all receipts. 
--`GET /receipts/[id]/` gets single receipt detail.
--`POST /receipts/process/` posts receipt with format given, returns JSON response with id.
--`GET /receipts/[id]/points/` returns the points for the receipt.



## Tech stack/ languages used:
1. Python/Django/django-rest-framework + sqlite3 database for testing

