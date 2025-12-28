from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError
from db_test import NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE
driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
def add_person(id: int, name: str, age: int, city: str) -> int:
    try:
        with driver.session(database=NEO4J_DATABASE) as session:
            result = session.run(
                "MERGE (p:Person {id: $id, name: $name, age: $age, city: $city}) RETURN elementId(p) AS person_id",
                name=name,
                age=age,
                city=city,
                id=id
            )
            record = result.single()
            return record['person_id']
    except Neo4jError as e:
        print(f"An error occurred while adding a person:", e)
if __name__ == "__main__":
    person_id = add_person(4,'Ram', 34, "Ayodhya")
    print(f"Added person with ID: {person_id}")