from initial import ma


# User Schema
class UserSchema(ma.Schema):
    class Meta:
        fields = ('user_id', 'user_name', 'user_email', 'user_password')


# Question Schema
class QuestionSchema(ma.Schema):
    class Meta:
        fields = ('question_id', 'question_content', 'isclosed',
                  'up_vote', 'down_vote', 'date_public', 'user_id')


# Answer Schema
class AnswerSchema(ma.Schema):
    class Meta:
        fields = ('answer_id', 'answer_content', 'up_vote',
                  'down_vote', 'date_public', 'user_id')


# Tag Schema
class TagSchema(ma.Schema):
    class Meta:
        fields = ('tag_id', 'tag_name')


user_schema = UserSchema()
users_schema = UserSchema(many=True)
question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
answer_schema = AnswerSchema()
answers_schema = AnswerSchema(many=True)
tag_schema = TagSchema()
tags_schema = TagSchema(many=True)
