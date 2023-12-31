from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

class Chat(BaseModel):
  id:str
  content:str
  hour:int
  minute:int
  
chats = []

app = FastAPI()

@app.post('/chat')
def create_chat(chat:Chat):
  chats.append(chat)
  return 'chat 추가에 성공했습니다.'

@app.get('/chat')
def read_chat():
  return chats

app.mount("/", StaticFiles(directory='static', html=True), name='static')