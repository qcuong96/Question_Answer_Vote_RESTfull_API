# Goal
Create RESTfull API server with python flask. This server allow:

 1) sign-up and sign-in 
 2) create questions/answers
 3) close question (still see but can't add the answer)
 4) delete questions/answers
 5) create tags
 6) add tags for question
 7) up/down vote for questions/answers

# How to use
This project use docker and the name will be rest_api_server. If you know about docker feel free to do your own style. Otherwise please follow these step:

 1) install docker by follow guide at their [website](https://www.docker.com/)
 2) open terminal, go the locate of the project
 3) run as admin/sudo permission 
    ```
    docker build -t rest_api_server:latest .
    docker run -p 80:5000 rest_api_server 
    ```
 4) read the api guide to know how to use (baseURI: 0.0.0.0:80)

# Update
There are some update later:

 1) email verification
 2) authorized tokens
 3) UI website
 4) user profile
 5) add api document for endpoint /tag

# Contact
If this project have issuses, feel free to contact me. <br/>
Email: quangcuong.nguyen96@gmail.com