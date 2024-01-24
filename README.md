[![wemake-python-styleguide](https://img.shields.io/badge/style-wemake-000000.svg)](https://github.com/wemake-services/wemake-python-styleguide)

# Socrat project
Backend web application on FastAPI 

## Description
The application can be launched in 2 ways, using Docker or locally, but for this you will need to create a database.
The application has 2 endpoints post and get(test) 
It is also covered with tests and packaged in Docker containers
Credentials have been added to the .env.example file so that you can deploy the application in 3 clicks.

## Basic Requirements
    - API for user management
    - API for authorization and authentication
    - API for menege reports
    - API for manage contacts
    - API for manage files
    - Custom admin panel

---
## Installation
**1. Clone the repository:**

   ```shell
   git clone https://github.com/baza-trainee/rd2-backend.git
   ```

  Create virtual env.

   ```shell
   python -m venv venv
   ```

**2. Create a `.env` file based on the `.env.example` file:**

   ```shell
   cd rd2-backend
   ```

   ```shell
   cp .env.example .env
   ```
**3. If you want to run using Docker you must have a Docker desktop**
  
   ```shell
   docker compose build --no-cache
   ```
   
   After that, you must run next command, It builds the images if they are not located locally and starts the containers:

   ```shell
   docker compose up
   ```
   Starting development server at  http://127.0.1:8000/
  
	
**4 If you want to run locally without using docker**

   ```shell
   pip install -r requirements.txt
   ```
**5 You also need to create a PostgreSQL database and enter the credentials in the .env file.
 Additionally, you should update the 'HOST' in the .env file  to match your configuration.**

  ```shell
   cd rd2-backend (root)
   ```

  ```shell
   alembic revision -m "test" --autogenerate

   ```

  ```shell
   alembic upgrade head
   ```

  ```shell
   uvicorn main:app --reload
   ```
  Starting development server at  http://127.0.1:8000/

## Technologies

 - Python 3.11
 - FastAPI
 - Pydantic
 - SQLAlchemy
 - Docker 
 - Docker-compose
 - PostgreSQL
 - Swagger


## License
MIT License

Created by Alex Grig
email:alexgrig.cyber@gmail.com
