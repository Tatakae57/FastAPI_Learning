from fastapi import FastAPI
from pydantic import BaseModel

# Estructuras de datos
app = FastAPI()  # Instancia


class Usuario(BaseModel):  # Clase usuario
    name: str
    age: int


users_db = []  # Base de datos de usuarios


# Usuarios
@app.post("/users/")  # Agregar usuarios a la lista
async def add_user(user: Usuario):
    users_db.append(user)
    return {"message": "Usuario creado exitosamente", "user": user}


@app.get("/users/")  # Recibir los usuarios de la lista
async def get_users():
    return {"users": users_db}


@app.get("/users/{user_name}")  # Encontrar el usuario por el nombre
async def get_user_by_name(user_name: str):
    for user in users_db:
        if user.name == user_name:
            return {"user": user}
    return {"user": "Not Found"}
