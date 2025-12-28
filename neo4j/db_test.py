from neo4j import GraphDatabase
from neo4j.exceptions import Neo4jError

NEO4J_URI = "neo4j://127.0.0.1:7687"
NEO4J_USER = "neo4j"
NEO4J_PASSWORD = "passwordneo4j"
NEO4J_DATABASE ="test"
class Neo4jTest:
    def __init__(self, NEO4J_URI, 
                 NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE):
        self.driver = GraphDatabase.driver(NEO4J_URI, auth=(NEO4J_USER, NEO4J_PASSWORD))
        self.database = NEO4J_DATABASE
    def test_connection(self):
        try:
            with self.driver.session(database=self.database) as session:
                result = session.run("RETURN 1 AS test")
                record = result.single()
                if record and record["test"] == 1:
                    print("Connection to Neo4j database successful.")
                else:
                    print("Connection to Neo4j database failed.")
        except Neo4jError as e:
            print(f"An error occurred: {e}")
    def close(self):
        self.driver.close()

if __name__ == "__main__":
    neo4j_test = Neo4jTest(NEO4J_URI, NEO4J_USER, NEO4J_PASSWORD, NEO4J_DATABASE)
    neo4j_test.test_connection()
    neo4j_test.close()