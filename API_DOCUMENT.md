# User
This endpoint all about user control

## 1) [POST] /user/register
    Use to create user

    Body:
    {
        "username":"", <String with maximum is 50 char>
        "password":"", <String with maximum is 50 char>
        "email":"" <String with maximum is 50 char>
    }

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "user_name":"", <String with maximum is 50 char>
            "user_email":"", <String with maximum is 50 char>
            "user_password":"" <String with maximum is 50 char>
        }
        2) Fail
        <String> "Username or Email was registed!"

## 2) [POST] /user/login
    Use to login

    Body:
    {
        "username":"", <String with maximum is 50 char>
        "password":"" <String with maximum is 50 char>
    }

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "user_name":"", <String with maximum is 50 char>
            "user_email":"", <String with maximum is 50 char>
            "user_password":"", <String with maximum is 50 char>
        }
        2) Fail
        <String> "This user was delete, please contact the admin!"
        or
        <String> "Wrong password"
        or
        <String> "This account have been not registed!"

## 3) [DELETE] /user/[user_id]
    Use to delete user

    Return:
        1) Success
        <String> "User was deleted"
        2) Fail
        <String> "Error! Please contact the admin!"

# Question
This endpoint all about question control

## 1) [POST] /question
    Use to create question

    Body:
    {
        "user_id":"", <Hex uuid string>
        "content":"", <String>
    }

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "question_content":"", <Text>
            "isclosed":"", <Boolean format>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "This account have been not registed!"
        or
        <String> "Error! Please contact the admin!"

## 2) [GET] /question/all
    Use to get all questions

    Return: list of question
        [
            {
                "user_id": "", <Hex uuid string>
                "question_id":"", <Hex uuid string>
                "question_content":"", <Text>
                "isclosed":"", <Boolean format>
                "up_vote":"", <Integer>
                "down_vote":"", <Integer>
                "date_public":"" <Datetime format>
            }, ...
        ]


## 3) [GET] /question/[question_id]
    Use to get question by question id

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "question_content":"", <Text>
            "isclosed":"", <Boolean format>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "This question was deleted!"
        or
        <String> "This question is not existed!"


## 4) [PUT] /question/[question_id]
    Use to edit content of the question

    Body:
    {
        "user_id":"", <Hex uuid string>
        "content":"", <String>
    }

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "question_content":"", <Text>
            "isclosed":"", <Boolean format>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "You are not the owner of this question!"
        or
        <String> "Error! Please contact the admin!"
        or
        <String> "This question was deleted!"
        or
        <String> "This question was closed!"
        or
        <String> "This question is not existed!"

## 5) [PUT] /question/[question_id]/up_vote
    Use to vote/disvote up vote

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "question_content":"", <Text>
            "isclosed":"", <Boolean format>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "Error! Please contact the admin!"
        or
        <String> "This question was deleted!"
        or
        <String> "This question is not existed!"

## 6) [PUT] /question/[question_id]/down_vote
    Use to vote/disvote down vote

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "question_content":"", <Text>
            "isclosed":"", <Boolean format>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "Error! Please contact the admin!"
        or
        <String> "This question was deleted!"
        or
        <String> "This question is not existed!"


## 7) [DELETE] /question/[question_id]/close
    Use to close the question

    Return:
        1) Success
        <String> "Question is closed"
        2) Fail
        <String> "You are not the owner of this question!"
        or
        <String> "Error! Please contact the admin!"
        or
        <String> "This question was deleted!"
        or
        <String> "This question was closed!"
        or
        <String> "This question is not existed!"

## 8) [DELETE] /question/[question_id]
    Use to delete the question

    Return:
        1) Success
        <String> "Question is delete"
        2) Fail
        <String> "You are not the owner of this question!"
        or
        <String> "Error! Please contact the admin!"
        or
        <String> "This question was deleted!"
        or
        <String> "This question was closed!"
        or
        <String> "This question is not existed!"

## 9) [POST] /question/[question_id]/answer
    Use to create an answer for the question

    Body:
    {
        "user_id":"", <Hex uuid string>
        "content":"", <String>
    }

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "answer_id":"", <Hex uuid string>
            "answer_content":"", <Text>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "This account have been not registed!"
        or
        <String> "Error! Please contact the admin!"
        or
        <String> "This question was deleted!"
        or
        <String> "This question was closed!"
        or
        <String> "This question is not existed!"

## 10) [GET] /question/[question_id]/answers
    Use to get all answers of the question
    Return:
        1) Success
        [
            {
                "user_id": "", <Hex uuid string>
                "question_id":"", <Hex uuid string>
                "answer_id":"", <Hex uuid string>
                "answer_content":"", <Text>
                "up_vote":"", <Integer>
                "down_vote":"", <Integer>
                "date_public":"" <Datetime format>
            }, ...
        ]
        2) Fail
        <String> "This question was deleted!"
        or
        <String> "This question is not existed!"

# Answer
This endpoint all about answer control

## 1) [GET] /answer/[answer_id]
    Use to get answer by answer id

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "answer_id":"", <Hex uuid string>
            "answer_content":"", <Text>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "This answer was deleted!"
        or
        <String> "This answer is not existed!"


## 2) [PUT] /answer/[answer_id]
    Use to edit content of the answer

    Body:
    {
        "user_id":"", <Hex uuid string>
        "content":"", <String>
    }

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "answer_id":"", <Hex uuid string>
            "answer_content":"", <Text>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "You are not the owner of this answer!"
        or
        <String> "Error! Please contact the admin!"
        or
        <String> "This answer was deleted!"
        or
        <String> "This answer is not existed!"

## 3) [PUT] /answer/[answer_id]/up_vote
    Use to vote/disvote up vote

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "answer_id":"", <Hex uuid string>
            "answer_content":"", <Text>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "Error! Please contact the admin!"
        or
        <String> "This answer was deleted!"
        or
        <String> "This answer is not existed!"

## 4) [PUT] /answer/[answer_id]/down_vote
    Use to vote/disvote down vote

    Return:
        1) Success
        {
            "user_id": "", <Hex uuid string>
            "question_id":"", <Hex uuid string>
            "answer_id":"", <Hex uuid string>
            "answer_content":"", <Text>
            "up_vote":"", <Integer>
            "down_vote":"", <Integer>
            "date_public":"" <Datetime format>
        }
        2) Fail
        <String> "Error! Please contact the admin!"
        or
        <String> "This answer was deleted!"
        or
        <String> "This answer is not existed!"

## 5) [DELETE] /answer/[answer_id]
    Use to delete the answer

    Return:
        1) Success
        <String> "Answer is delete"
        2) Fail
        <String> "You are not the owner of this answer!"
        or
        <String> "Error! Please contact the admin!"