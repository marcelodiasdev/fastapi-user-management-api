from fastapi import FastAPI, status

from car_api.routers.users import router

app = FastAPI()

app.include_router(router=router, prefix="/api/v1/users", tags=["users"])


@app.get("/health_check", status_code=status.HTTP_200_OK)
def health_check():
    return {"status": "ok"}
