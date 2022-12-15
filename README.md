# openai chat server
This project uses the api of openai to implement the chat bot

# useage  
## step 1:
* Fill in your openai key in `server.py` -> openai.api_key
* set a accessid in `server.py` ->accessid
## step 2:
Run the following command 
```bash
pip install -r requirements.txt
uvicorn server:app --reload --host 0.0.0.0
```
## Step3:
using curl send a request
```bash
curl --location --request POST 'http://43.134.181.21:8000/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "auth":"your accessid",
    "conversation":"The following is a conversation with an AI assistant. The assistant is helpful, creative, clever, and very friendly.\n\nHuman: Hello, who are you?\nAI: I am an AI created by OpenAI. How can I help you today?\nHuman: 红烧肉的做法?\nAI:",
    "userInfo":"XXX"
}'

```
# roadmap
- [ ] add log
- [ ] support `Notes to summary`
- [ ] support `Classification`

# attention
using openai api you need pay a bill for it, but you have 18$ default.

# lience
MIT

