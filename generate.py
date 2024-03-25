import os
from dotenv import load_dotenv
from openai import OpenAI
from speak import *
load_dotenv()
key = os.getenv('OPEN_AI_KEY')
client = OpenAI(api_key=key)
print("Please input your character name, class, and a short description")
while(True):
  prompt = input()
  response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
  {
  "role": "system",
  "content": "You are a DM for A Dungeons and Dragons game, you must speak as a wise wizard that is describing things in great detail as a user plays through your story. When a character speaks, before their text place either Male Voice: or Female Voice: depending on the gender of the character being portrayed"
  },
  {
  "role": "user",
  "content": prompt
  }
  ],
  temperature=0,
  max_tokens=1024,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
  )

  print(response.choices[0].message.content)
  process(response.choices[0].message.content)