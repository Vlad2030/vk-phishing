from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles


app = FastAPI(
    debug=True,
    title="VK phishing",
    version="0.0.1,"
)