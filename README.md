# fastapi_blog
Fast api blog


The **app** folder contains the main application code.

The ***main.py*** file creates the FastAPI instance and includes the routers from the routers folder.

The __*config.py*__ file contains the configuration settings for the app, such as database URL, secret key, etc.

>The db.py file creates the database session and engine using SQLAlchemy.

>The models.py file defines the database models using SQLAlchemy ORM.
The schemas.py file defines the Pydantic schemas for validation and serialization.

The routers folder contains the different API endpoints for each resource, such as auth, blogs and research. Each router file uses dependency injection to access the database session and JWT tokens.

The utils folder contains some utility functions, such as generating and verifying JWT tokens using PyJWT.

The tests folder contains the unit tests for the app using Pytest.

The requirements.txt file lists the dependencies for the app, such as FastAPI, SQLAlchemy, PyJWT, etc.

The README.md file contains the documentation for the app, such as how to run it, how to use the API endpoints, etc.