from dotenv import load_dotenv
import os

ENV = os.getenv("ENV", "dev") # Get the environment from an environment variable or default to dev


if ENV == "prod":
    load_dotenv(".env.prod")
else:
    load_dotenv(".env")

DATABASE_URL = os.getenv("DATABASE_URL") # get the database from environment variable
