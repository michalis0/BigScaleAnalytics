# Part 1: Introduction to Docker

We will learn about Docker and its advantages. We will answer to the following questions:
- What is Docker? How is it different from a virtual machine?
- What are images and containers and what is their difference?

## Goals

1. Understand the difference between a container and an image
2. How to run a Docker image
3. Practicing some useful Docker commands

# Exercise
- go to the repository https://github.com/samik-saha/rasa-chatbot. It contains an implementation of a simple chatbot.
- Open your terminal and clone the repository. `git clone https://github.com/samik-saha/rasa-chatbot.git`
- Go to the directory of the repository you just cloned and build the dockerfile:
  ```
  cd rasa-chatbot
  docker build -t rasa-chatbot .
  ```
- Wait for the build to finish. Then you will be able to start a container and test the chat bot.
  `docker run -it --rm -p 5005:5005 --env-file $(pwd)/.env-sample rasa-chatbot`
- Open a new terminal tab(window) and test the API as instructed in the readme of the repository, e.g:
  ```
  curl --request POST \
  --url http://localhost:5005/webhooks/rest/webhook \
  --header 'content-type: application/json' \
  --data '{
    "message": "Hi"
  }'
  ```
# Part 2: Building a docker image

We will learn how to build a docker image. We will "dockerize" the Flask app we created in a previous week.

## Goals

1. Understand concepts in building a docker image
2. How to create a dockerfile
3. How to build an image
4. How to publish a container's port to the host

### Related tutorial

https://www.youtube.com/watch?v=prlixoDIfrc
