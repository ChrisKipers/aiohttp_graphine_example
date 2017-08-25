import graphene


class Choice(graphene.ObjectType):
    id = graphene.Int()
    choice_text = graphene.String()
    votes = graphene.Int()


class Question(graphene.ObjectType):
    id = graphene.Int()
    question_text = graphene.String()
    pub_date = graphene.String()
    choices = graphene.List(Choice)

    async def resolve_choices(self, args, context, info):
        return context['choice_loader'].load(self.id)


class Query(graphene.ObjectType):

    question = graphene.Field(Question, id=graphene.Int())

    async def resolve_question(self, args, context, info):
        q_id = args['id']
        return context['question_loader'].load(q_id)


schema = graphene.Schema(query=Query)
