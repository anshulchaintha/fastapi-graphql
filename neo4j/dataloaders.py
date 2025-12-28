from typing import List, Optional
from neo4j import AsyncGraphDatabase
from db_test import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE

driver = AsyncGraphDatabase.driver(
    NEO4J_URI,
    auth=(NEO4J_USER, NEO4J_PASSWORD)
)

async def batch_load_companies(person_ids: List[int]):
    async with driver.session(database=NEO4J_DATABASE) as session:
        result = await session.run(
            """
            MATCH (p:Person)-[:WORKS_AT]->(c:Company)
            WHERE p.id IN $ids
            RETURN p.id AS person_id,
                   c.id AS id,
                   c.name AS name
            """,
            ids=person_ids
        )

        mapping = {pid: None for pid in person_ids}

        async for record in result:
            mapping[record["person_id"]] = {
                "id": record["id"],
                "name": record["name"]
            }

        return [mapping[pid] for pid in person_ids]
