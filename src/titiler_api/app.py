import os
import titiler.core
from titiler.core.factory import TilerFactory
from titiler.core.errors import DEFAULT_STATUS_CODES, add_exception_handlers

from fastapi import FastAPI

# Read environment variables
app_host = str(os.environ["APP_HOST"])
app_port = int(os.environ["APP_PORT"])
reload = bool(os.environ["RELOAD"])

version = titiler.core.__version__

app = FastAPI(
    title="Overstory Titiler Server",
    description=f"Dynamic tile-server for Overstory built on `titiler.core` v{version}.",
    version=f"{version}"
)

cog = TilerFactory()
app.include_router(cog.router, prefix="/cog", tags=["Cloud Optimized GeoTIFF"])

add_exception_handlers(app, DEFAULT_STATUS_CODES)

@app.get("/health", description="Health Check", tags=["Health Check"])
def ping():
    """Health check."""
    return {"ping": "pong!"}


def serve():
    """Serve the app from command line using uvicorn if available."""
    try:
        import uvicorn

        uvicorn.run(
            "titiler_api.app:app",
            host=app_host,
            port=app_port,
            log_level="info",
            reload=reload,
        )
    except ImportError:
        raise RuntimeError("Uvicorn must be installed in order to use command")


if __name__ == "__main__":
    serve()
