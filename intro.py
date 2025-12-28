import strawberry
from fastapi import FastAPI
from strawberry.fastapi import GraphQLRouter

COURSE_NAME = "Computer Science"
COURSE_DURATION_YEARS = 1

@strawberry.type
class Course:
    id: strawberry.ID

    @strawberry.field
    def name(self) -> str:
        return f"Course Name: {COURSE_NAME}"

    @strawberry.field
    def duration(self) -> int:
        return COURSE_DURATION_YEARS

    @strawberry.field
    def description(self) -> str:
        return "Introductory course"

@strawberry.type
class Query:
    @strawberry.field
    def course(self) -> Course:
        return Course(id="1")

schema = strawberry.Schema(query=Query)

app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")
