import os

from dotenv import load_dotenv

load_dotenv()

EVENT = os.environ.get("EVENT")
TOUR = os.environ.get("TOUR")
UNIVERSITY = os.environ.get("UNIVERSITY")
USER = os.environ.get("USER")

ALLOWED_HOSTS = [
    "77.232.135.31",
    "109.172.81.237"
]
ORIGINS = [
    "http://109.172.81.237:8888",
    "http://109.172.81.237",
    "https://109.172.81.237:8888",
    "https://109.172.81.237",
    "http://77.232.135.31:8000",
    "http://77.232.135.31",
    "https://77.232.135.31:8000",
    "https://77.232.135.31",
]