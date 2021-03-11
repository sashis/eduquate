import graphene

from accounts.schema import Query as StudentQuery


class Query(StudentQuery, graphene.ObjectType):
    pass


schema = graphene.Schema(query=Query)
