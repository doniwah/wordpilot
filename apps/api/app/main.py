from fastapi import FastAPI

app = FastAPI(
    title="WordPilot API",
    description="Open-source AI writing assistant API",
    version="0.1.0",
)


@app.get("/health")
async def health_check():
    return {
        "status": "ok",
        "service": "wordpilot-api",
        "version": "0.1.0",
    }
