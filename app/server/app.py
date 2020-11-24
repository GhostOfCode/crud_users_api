from fastapi import FastAPI, Depends, Security, HTTPException
from fastapi.security import HTTPBasic
from fastapi.security.api_key import APIKeyQuery
from starlette.status import HTTP_403_FORBIDDEN

from .routes.user import router as UserRouter
from .config import API_KEY, API_KEY_NAME


app = FastAPI(title="CRUD_API", version='1.0.0')

security = HTTPBasic()
api_key_query = APIKeyQuery(name=API_KEY_NAME, auto_error=True)


async def get_api_key(api_key: str = Security(api_key_query)):
    if api_key == API_KEY:
        return api_key
    raise HTTPException(status_code=HTTP_403_FORBIDDEN, detail="Could not validate credentials")


#  Main methods of API (routes) with tag "User"
app.include_router(UserRouter, tags=["User"], prefix="/user", dependencies=[Depends(get_api_key)],
                   responses={404: {"description": "Not found"}}, )


#  Welcome
@app.get("/", tags=["Root"])
async def read_root():
    return {"message": "Welcome to this test CRUD app!"}
