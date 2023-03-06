from fastapi.staticfiles import StaticFiles 
from backend.fastapi_app import app

async def staticPage() -> None:
    return app.mount(
        path="/",
        app=StaticFiles(
            directory="../site",
            html=True,
        ),
    ),