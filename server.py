import openai
from fastapi import FastAPI
from pydantic import BaseModel

openai.api_key = 'you openai api_key'
accessid = ['a reamdom value']

app = FastAPI()

class Item(BaseModel):
    conversation: str
    auth: str

@app.post("/chat")
async def root(item: Item):
    if item.auth in accessid:
        return {"message":"暂无权限"}
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=f"{item.converstion}",
        temperature=0.9,
        max_tokens=2666,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )
    return {"message": response.choices[0].text}