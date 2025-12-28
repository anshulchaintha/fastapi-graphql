import strawberry
from typing import List, Optional
from neo4j import AsyncGraphDatabase
from db_test import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE

driver = AsyncGraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

# -------------------
# GraphQL Type
# -------------------
@strawberry.type
class Company:
    id: int
    name: str
@strawberry.type
class Person:
    id: int
    name: str
    age: int
    city: str
    @strawberry.field
    async def works_at(self, info) -> Optional["Company"]:
        data = await info.context["company_loader"].load(self.id)
        return Company(**data) if data else None
# -------------------
# Query (READ)
# -------------------
@strawberry.type
class Query:

    @strawberry.field
    async def person(self, id: int) -> Optional[Person]:
        async with driver.session(database=NEO4J_DATABASE) as session:
            result = await session.run(
                """
                MATCH (p:Person {id: $id})
                RETURN p.id AS id,
                       p.name AS name,
                       p.age AS age,
                       p.city AS city
                """,
                id=id
            )

            record = await result.single()
            return Person(**record) if record else None

    @strawberry.field
    async def persons(self) -> List[Person]:
        async with driver.session(database=NEO4J_DATABASE) as session:
            result = await session.run(
                """
                MATCH (p:Person)
                RETURN p.id AS id,
                       p.name AS name,
                       p.age AS age,
                       p.city AS city
                """
            )

            persons = []
            async for record in result:
                persons.append(Person(**record))

            return persons


# -------------------
# Mutation (WRITE)
# -------------------
@strawberry.type
class Mutation:

    @strawberry.mutation
    async def add_person(
        self,
        id: int,
        name: str,
        age: int,
        city: str
    ) -> Person:
        async with driver.session(database=NEO4J_DATABASE) as session:
            await session.run(
                """
                MERGE (p:Person {
                  id: $id,
                  name: $name,
                  age: $age,
                  city: $city
                })
                """,
                id=id,
                name=name,
                age=age,
                city=city
            )

        return Person(id=id, name=name, age=age, city=city)


# -------------------
# Schema
# -------------------
schema = strawberry.Schema(
    query=Query,
    mutation=Mutation
)
