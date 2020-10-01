from initial import datetime, db, uuid

question_tag = db.Table('question_tag',
                        db.Column('question_id', db.String(50),
                                  db.ForeignKey('question.question_id')),
                        db.Column('tag_id', db.String(50),
                                  db.ForeignKey('tag.tag_id'))
                        )

user_up_vote_question = db.Table('user_up_vote_question',
                                 db.Column('user_id', db.String(50),
                                           db.ForeignKey('user.user_id')),
                                 db.Column('question_id', db.String(50),
                                           db.ForeignKey('question.question_id'))
                                 )

user_up_vote_answer = db.Table('user_up_vote_answer',
                               db.Column('user_id', db.String(50),
                                         db.ForeignKey('user.user_id')),
                               db.Column('answer_id', db.String(50),
                                         db.ForeignKey('answer.answer_id'))
                               )

user_down_vote_question = db.Table('user_down_vote_question',
                                   db.Column('user_id', db.String(50),
                                             db.ForeignKey('user.user_id')),
                                   db.Column('question_id', db.String(50),
                                             db.ForeignKey('question.question_id'))
                                   )

user_down_vote_answer = db.Table('user_down_vote_answer',
                                 db.Column('user_id', db.String(50),
                                           db.ForeignKey('user.user_id')),
                                 db.Column('answer_id', db.String(50),
                                           db.ForeignKey('answer.answer_id'))
                                 )


# User Class/Model
class User(db.Model):
    user_id = db.Column(db.String(50), primary_key=True)
    user_name = db.Column(db.String(50), nullable=False, unique=True)
    user_email = db.Column(db.String(50), nullable=False, unique=True)
    user_password = db.Column(db.String(50), nullable=False)
    answers = db.relationship('Question', backref='owner', lazy=True)
    answers = db.relationship('Answer', backref='owner', lazy=True)
    is_deleted = db.Column(db.Boolean, nullable=False)

    def __init__(self, name, email, password):
        self.user_id = uuid.uuid4().hex
        self.user_name = name
        self.user_email = email
        self.user_password = password
        self.is_deleted = False

    def delete(self):
        self.is_deleted = True


# Question Class/Model
class Question(db.Model):
    question_id = db.Column(db.String(50), primary_key=True)
    question_content = db.Column(db.Text, nullable=False, unique=True)
    up_vote = db.Column(db.Integer, nullable=False)
    down_vote = db.Column(db.Integer, nullable=False)
    date_public = db.Column(db.DateTime, nullable=False)
    last_update = db.Column(db.DateTime, nullable=False)
    is_closed = db.Column(db.Boolean, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey(
        'user.user_id'), nullable=False)
    answers = db.relationship('Answer', backref='question', lazy=True)
    tags = db.relationship('Tag', secondary=question_tag,
                           backref='questions', lazy='dynamic')
    up_vote_users = db.relationship('User', secondary=user_up_vote_question,
                                    backref='up_vote_questions', lazy='dynamic')
    down_vote_users = db.relationship('User', secondary=user_down_vote_question,
                                      backref='down_vote_questions', lazy='dynamic')

    def __init__(self, content, user_id):
        self.question_id = uuid.uuid4().hex
        self.question_content = content
        self.user_id = user_id
        self.up_vote = 0
        self.down_vote = 0
        self.date_public = datetime.now()
        self.last_update = datetime.now()
        self.is_closed = False
        self.is_deleted = False

    def vote_up(self):
        self.up_vote += 1

    def dis_vote_up(self):
        self.up_vote -= 1

    def vote_down(self):
        self.down_vote += 1

    def dis_vote_down(self):
        self.down_vote -= 1

    def edit(self, content):
        self.question_content = content
        self.last_update = datetime.now()

    def delete(self):
        self.is_deleted = True

    def close(self):
        self.is_closed = True

    def add_tags(self, tags):
        for tag in tags:
            self.tags.append(tag)


# Answer Class/Model
class Answer(db.Model):
    answer_id = db.Column(db.String(50), primary_key=True)
    answer_content = db.Column(db.Text, nullable=False, unique=True)
    up_vote = db.Column(db.Integer, nullable=False)
    down_vote = db.Column(db.Integer, nullable=False)
    date_public = db.Column(db.DateTime, nullable=False)
    last_update = db.Column(db.DateTime, nullable=False)
    is_deleted = db.Column(db.Boolean, nullable=False)
    user_id = db.Column(db.String(50), db.ForeignKey(
        'user.user_id'), nullable=False)
    question_id = db.Column(db.String(50), db.ForeignKey(
        'question.question_id'), nullable=False)
    up_vote_users = db.relationship('User', secondary=user_up_vote_answer,
                                    backref='up_vote_answer', lazy='dynamic')
    down_vote_users = db.relationship('User', secondary=user_down_vote_answer,
                                      backref='down_vote_answer', lazy='dynamic')

    def __init__(self, content, user_id, question_id):
        self.answer_id = uuid.uuid4().hex
        self.answer_content = content
        self.user_id = user_id
        self.up_vote = 0
        self.down_vote = 0
        self.date_public = datetime.now()
        self.last_update = datetime.now()
        self.question_id = question_id
        self.is_deleted = False

    def vote_up(self):
        self.up_vote += 1

    def dis_vote_up(self):
        self.up_vote -= 1

    def vote_down(self):
        self.down_vote += 1

    def dis_vote_down(self):
        self.down_vote -= 1

    def edit(self, content):
        self.answer_content = content
        self.last_update = datetime.now()

    def delete(self):
        self.is_deleted = True


# Tag Class/Model
class Tag(db.Model):
    tag_id = db.Column(db.String(50), primary_key=True)
    tag_name = db.Column(db.String(50), nullable=False, unique=True)
    is_deleted = db.Column(db.Boolean, nullable=False)

    def __init__(self, name):
        self.tag_id = uuid.uuid4().hex
        self.tag_name = name
        self.is_deleted = False

    def delete(self):
        self.is_deleted = True
