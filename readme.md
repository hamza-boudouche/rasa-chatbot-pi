# Rasa Chatbot

## Setup

To be able to setup this projet locally, you will need to install [rasa](https://rasa.com/docs/rasa/installation/) and [docker](https://docs.docker.com/engine/install/ubuntu/).

The steps are as follows: 

1. run the duckling server docker image on you machine

```
docker run -p 8000:8000 rasa/duckling
```

2. train the chatbot

```
rasa train
```

3. run the rasa actions server ( defaults to port 5055 )

```
rasa run actions
```

4. run the chatbot server ( defaults to port 5005 ), giving it a secret token for later use ( here `secret` )

```
rasa run --enable-api --auth-token secret
```

5. test the chatbot by sending a `POST` request with Postman or with cURL, as follows: 

```
curl --location --request POST 'http://localhost:5005/webhooks/rest/webhook?token=secret' \
--header 'Content-Type: application/json' \
--data-raw '{
    "sender": "hamza",
    "message": "hello"
}'
```

The server responds with a json document similar to : 

```
[
    {
        "recipient_id": "hamza",
        "text": "Hey! How can I help you?"
    }
]
```

You can now continue the conversation with the chatbot using HTTP requests to communicate.