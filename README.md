# Fetch Rewards backend take-home assignment
This is a Django Rest Framework API that provides endpoints for Fetch Rewards' backend take-home assignment.
## Installation with Docker
1. Clone repository: `git clone https://github.com/stanleyzzheng/fetch-backend-th [your-directory-name-of-choice]`
2. Build Docker Image: `docker build --t django_project .`
3. Run Docker image on port 8000: `docker run -d -p 8000:8000 django_project`

## Usage
Test your application with Postman or your testing method of choice on `localhost:8000` or `127.0.0.1:8000`.

## API endpoints:
- `GET /receipts/` get all receipts. 
- `GET /receipts/{id}/` get single receipt detail.
- `DELETE /receipts/{id}/` delete single receipt with id.
- `POST /receipts/process/` post receipt with format given, returns JSON response with id.
- `GET /receipts/{id}/points/` return points rewarded for receipt.



## Tech stack/ languages used:
- Python
- Django
- django-rest-framework
- sqlite3 database for testing

