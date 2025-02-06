---
marp: true
---
[HNG Python Developers](https://hng.tech/hire/python-developers)


This API returns the following information in JSON format:
- Your registered email address 
- The current datetime as an ISO 8601 formatted timestamp (UTC).
- The GitHub URL of the project's codebase.
## The API's URL 
-[Api link](https://infoapi-t8bs.onrender.com/api/)

## Create and Activate a Virtual Environment:

python -m venv venv

## On Windows:
venv\Scripts\activate

## On macOS/Linux
source venv/bin/activate


## Install Dependencies:

pip install -r requirements.txt


## Run Database Migrations:

python manage.py migrate

## Start the Development Server:
python manage.py runserver

## Access the API:

Open your browser and navigate to http://127.0.0.1:8000/api/


