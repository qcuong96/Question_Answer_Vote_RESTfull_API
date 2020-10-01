from initial import app, db, jsonify, ma, request
from model import User, Question, Answer, Tag
from model import question_tag
from model import user_down_vote_answer, user_down_vote_question
from model import user_up_vote_answer, user_up_vote_question
from schema import answer_schema, answers_schema
from schema import question_schema, questions_schema
from schema import tag_schema, tags_schema
from schema import user_schema, users_schema


# Register
@app.route('/register', methods=['POST'])
def register():
    name = request.json['username']
    email = request.json['email']
    password = request.json['password']

    new_user = User(name, email, password)

    try:
        db.session.add(new_user)
        db.session.commit()
    except:
        return 'Username or Email was registed!'

    return user_schema.jsonify(new_user)


# Login
@app.route('/user', methods=['POST'])
def login():
    name = request.json['username']
    password = request.json['password']

    user = User.query.filter_by(user_name=name).first()

    if user.is_deleted:
        return 'This user was delete, please contact the admin!'

    if user.user_password == password:
        return user_schema.jsonify(user)

    return 'Wrong password!'


# Delete user
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    user = User.query.get(id)

    user.delete()
    try:
        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return 'User was deleted'


# Create question
@app.route('/question', methods=['POST'])
def create_question():
    user_id = request.json['user_id']
    content = request.json['content']

    user = User.query.filter_by(user_id=user_id).first()

    if not user:
        return 'This account have been not registed!'

    question = Question(content, user_id)

    try:
        db.session.add(question)
        db.session.commit()
    except:
        return 'Error! Fail to create question!'

    return question_schema.jsonify(question)


# Get all questions
@app.route('/question/all', methods=['GET'])
def get_all_questions():
    questions = Question.query.filter_by(is_deleted=False)
    result = questions_schema.dump(questions)

    return jsonify(result)


# Get question
@app.route('/question/<id>', methods=['GET'])
def get_question(id):
    question = Question.query.get(id)

    if question.is_deleted:
        return 'This question was deleted!'

    return question_schema.jsonify(question)


# Edit question
@app.route('/question/<id>', methods=['PUT'])
def edit_question(id):
    content = request.json['content']
    user_id = request.json['user_id']

    question = Question.query.get(id)

    if question.user_id != user_id:
        return 'You are not the owner of this question!'

    if question.is_deleted:
        return 'This question was deleted!'

    if question.is_closed:
        return 'This question was closed!'

    question.edit(content)
    try:
        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return question_schema.jsonify(question)


# Up vote question
@app.route('/question/<id>/up_vote', methods=['PUT'])
def up_vote_question(id):
    user_id = request.json['user_id']

    user = User.query.get(user_id)
    question = Question.query.get(id)
    up_vote_users = question.up_vote_users.all()
    down_vote_users = question.down_vote_users.all()

    try:
        if user in up_vote_users:
            question.dis_vote_up()
            question.up_vote_users.remove(user)
        else:
            question.vote_up()
            question.up_vote_users.append(user)
            if user in down_vote_users:
                question.dis_vote_down()
                question.down_vote_users.remove(user)

        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return question_schema.jsonify(question)


# Down vote question
@app.route('/question/<id>/down_vote', methods=['PUT'])
def down_vote_question(id):
    user_id = request.json['user_id']

    user = User.query.get(user_id)
    question = Question.query.get(id)
    up_vote_users = question.up_vote_users.all()
    down_vote_users = question.down_vote_users.all()

    try:
        if user in down_vote_users:
            question.dis_vote_down()
            question.down_vote_users.remove(user)
        else:
            question.vote_down()
            question.down_vote_users.append(user)
            if user in up_vote_users:
                question.dis_vote_up()
                question.up_vote_users.remove(user)

        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return question_schema.jsonify(question)


# Close question
@app.route('/question/<id>/close', methods=['DELETE'])
def close_question(id):
    user_id = request.json['user_id']

    question = Question.query.get(id)

    if question.user_id != user_id:
        return 'You are not the owner of this question!'

    question.close()
    try:
        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return 'Question is closed'


# Delete question
@app.route('/question/<id>', methods=['DELETE'])
def delete_question(id):
    user_id = request.json['user_id']

    question = Question.query.get(id)

    if question.user_id != user_id:
        return 'You are not the owner of this question!'

    question.delete()
    try:
        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return 'Question is deleted'


# Create answer
@app.route('/question/<id>/answer', methods=['POST'])
def create_answer(id):
    user_id = request.json['user_id']
    content = request.json['content']

    user = User.query.filter_by(user_id=user_id).first()
    question = Question.query.get(id)

    if question.is_deleted:
        return 'This question was deleted!'

    if question.is_closed:
        return 'This question was closed!'

    if not user:
        return 'This account have been not registed!'

    answer = Answer(content, user_id, id)

    try:
        db.session.add(answer)
        db.session.commit()
    except:
        return 'Error! Fail to create answer!'

    return answer_schema.jsonify(answer)


# Get all answers of the question
@app.route('/question/<id>/answers', methods=['GET'])
def get_all_answers(id):
    answer = Answer.query.filter_by(question_id=id, is_deleted=False)
    result = answers_schema.dump(answer)

    return jsonify(result)


# Get answer
@app.route('/answer/<ans_id>', methods=['GET'])
def get_answer(ans_id):
    answer = Answer.query.get(ans_id)

    if answer.is_deleted:
        return 'This answer was delete!'

    return answer_schema.jsonify(answer)


# Edit answer
@app.route('/answer/<ans_id>', methods=['PUT'])
def edit_answer(ans_id):
    content = request.json['content']
    user_id = request.json['user_id']

    answer = Answer.query.get(ans_id)

    if answer.user_id != user_id:
        return 'You are not the owner of this question!'

    answer.edit(content)
    try:
        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return answer_schema.jsonify(answer)


# Up vote answer
@app.route('/answer/<ans_id>/up_vote', methods=['PUT'])
def up_vote_answer(ans_id):
    user_id = request.json['user_id']

    user = User.query.get(user_id)
    answer = Answer.query.get(ans_id)
    up_vote_users = answer.up_vote_users.all()
    down_vote_users = answer.down_vote_users.all()

    try:
        if user in up_vote_users:
            answer.dis_vote_up()
            answer.up_vote_users.remove(user)
        else:
            answer.vote_up()
            answer.up_vote_users.append(user)
            if user in down_vote_users:
                answer.dis_vote_down()
                answer.down_vote_users.remove(user)

        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return answer_schema.jsonify(answer)


# Down vote answer
@app.route('/answer/<ans_id>/down_vote', methods=['PUT'])
def down_vote_answer(ans_id):
    user_id = request.json['user_id']

    user = User.query.get(user_id)
    answer = Answer.query.get(ans_id)
    up_vote_users = answer.up_vote_users.all()
    down_vote_users = answer.down_vote_users.all()

    try:
        if user in down_vote_users:
            answer.dis_vote_down()
            answer.down_vote_users.remove(user)
        else:
            answer.vote_down()
            answer.down_vote_users.append(user)
            if user in up_vote_users:
                answer.dis_vote_up()
                answer.up_vote_users.remove(user)

        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return answer_schema.jsonify(answer)


# Delete answer
@app.route('/answer/<ans_id>', methods=['DELETE'])
def delete_answer(ans_id):
    user_id = request.json['user_id']

    answer = Answer.query.get(ans_id)

    if answer.user_id != user_id:
        return 'You are not the owner of this Answer!'

    answer.delete()
    try:
        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return 'Answer is deleted'


# Create tag
@app.route('/tag', methods=['POST'])
def create_tag():
    tag_name = request.json['tag_name']

    new_tag = Tag(tag_name)

    try:
        db.session.add(new_tag)
        db.session.commit()
    except:
        return 'Tag have already existed!'

    return tag_schema.jsonify(new_tag)


# Get all tags
@app.route('/tag/all', methods=['GET'])
def get_all_tags():
    tags = Tag.query.filter_by(is_deleted=False)
    result = tags_schema.dump(answer)

    return jsonify(result)


# Get tag
@app.route('/tag/<id>', methods=['GET'])
def get_tag(id):
    tag = Tag.query.get(id)

    if tag.is_deleted:
        return 'This tag was deleted!'

    return tag_schema.jsonify(tag)


# Delete tag
@app.route('/tag/<id>', methods=['DELETE'])
def delete_tag(id):
    tag = Tag.query.get(id)

    tag.delete()
    try:
        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return 'Tage is deleted'


# Add tags into question
@app.route('/question/<id>/tags', methods=['PUT'])
def add_tags(id):
    user_id = request.json['user_id']
    question = Question.query.get(id)

    if question.user_id != user_id:
        return 'You are not the owner of this question!'

    if question.is_deleted:
        return 'This question was deleted!'

    if question.is_closed:
        return 'This question was closed!'

    tag_ids = request.json['tag_ids']
    tags = Tag.query.filter(Tag.tag_id.in_(tag_ids)).all()

    question.add_tags(tags)

    try:
        db.session.commit()
    except:
        return 'Error! Please contact the admin!'

    return question_schema.jsonify(question)


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, host='0.0.0.0')
