from fastapi import APIRouter, Body
from fastapi.encoders import jsonable_encoder

from ..db import (
    add_user,
    delete_user,
    retrieve_user,
    retrieve_users,
    update_user,
)
from ..models.user import (
    error_response_model,
    response_model,
    UserSchema,
    UpdateUserModel,
)

router = APIRouter()


@router.post("/", description="Add new User")
async def add_user_data(user: UserSchema = Body(...)):
    user = jsonable_encoder(user)
    new_user = await add_user(user)
    if new_user:
        return response_model(new_user, "User added successfully.")
    return error_response_model("An error occurred.", 404, "user already exist.")


@router.get("/", description="Return data of all users")
async def get_users():
    users = await retrieve_users()
    if users:
        return response_model(users, "Users data retrieved successfully")
    return response_model(users, "Empty list returned")


@router.get("/{id}", description="Return all User's data")
async def get_user_data(id: str):
    user = await retrieve_user(id)
    if user:
        return response_model(user, "User data retrieved successfully")
    return error_response_model("An error occurred.", 404, "user doesn't exist.")


@router.put("/{id}", description="Update User data by using User ID")
async def update_user_data(id: str, req: UpdateUserModel = Body(...)):
    req = {k: v for k, v in req.dict().items() if v is not None}
    updated_user = await update_user(id, req)
    if updated_user:
        return response_model(
            "User with ID: {} name update is successful".format(id),
            "User name updated successfully",
        )
    return error_response_model(
        "An error occurred",
        404,
        "There was an error updating the User data.",
    )


@router.delete("/{id}", description="Remove User by using User ID")
async def delete_user_data(id: str):
    deleted_user = await delete_user(id)
    if deleted_user:
        return response_model(
            "User with ID: {} removed".format(id), "User deleted successfully"
        )
    return error_response_model(
        "An error occurred", 404, "user with id {0} doesn't exist".format(id)
    )
