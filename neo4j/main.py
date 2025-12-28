from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter
from schema import schema
from context import get_context

app = FastAPI()

app.include_router(
    GraphQLRouter(schema, context_getter=get_context),
    prefix="/graphql"
)

@app.get("/")
async def root():
    return {"message": "Go to /graphql"}
