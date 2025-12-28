from strawberry.fastapi import GraphQLRouter
from fastapi import FastAPI
import strawberry
from reader_data import read_csv_file
@strawberry.type
class Employee:
    id : strawberry.ID

    @strawberry.field
    def Name(self) -> str:
        data = read_csv_file('data_emp.csv')
        return data[int(self.id)]['Name']

    @strawberry.field
    def City(self) -> str:
        data = read_csv_file('data_emp.csv')
        return data[int(self.id)]['City']

    @strawberry.field
    def Designation(self) -> str:
        data = read_csv_file('data_emp.csv')
        return data[int(self.id)]['Designation']

    @strawberry.field
    def Experience(self) -> str:
        data = read_csv_file('data_emp.csv')
        return data[int(self.id)]['Experience']
@strawberry.type
class Query:
    @strawberry.field
    def employee(self, id: strawberry.ID) -> Employee:
        return Employee(id=id)
    
schema = strawberry.Schema(query=Query)
app = FastAPI()
app.include_router(GraphQLRouter(schema), prefix="/graphql")