from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema

app = FastAPI()

app.include_router(
    GraphQLRouter(schema),
    prefix="/graphql"
)

@app.get("/")
async def root():
    return {"message": "Go to /graphql"}
