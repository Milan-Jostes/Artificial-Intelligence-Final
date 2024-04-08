import os
from dotenv import load_dotenv
from openai import OpenAI
from speak import *
import requests
from flask import Flask, render_template, request


from PIL import Image
load_dotenv()
key = os.getenv('OPEN_AI_KEY')
client = OpenAI(api_key=key)

app = Flask(__name__)
UPLOAD_FOLDER = 'C:/Users/mjostes/Documents/GitHub/ChatGPT-Final/savedInfo'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

def createScene(prompt):
    responseScene = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
    "role": "system",
    "content": "You are a DM for A Dungeons and Dragons game, you must speak as a wise wizard that is describing things in great detail as a user plays through your story. When a character speaks, before their text place either Male Voice: or Female Voice: depending on the gender of the character being portrayed. You may not portray the user's character, instead prompt the user to respond."
    },  {
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

    info = responseScene.choices[0].message.content
    #print(info)
    no_gen = process(info)
    createImage(info)
    return no_gen


def createImage(prompt):
    responseImage = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
    "role": "system",
    "content": "You are an environmental artist for a movie. You must describe the location of a scene in the movie without describing anything that happens in the location."
    },
    {
    "role": "user",
    "content": "Describe only one of the locations of the following scene:"+prompt
    }
    ],
    temperature=0,
    max_tokens=1024,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
    )
    imageDesc = responseImage.choices[0].message.content
    # print("\n\n\n\nImage Description:")
    # print(imageDesc)

    model = "dall-e-3"
    # Generate an image based on the prompt
    image = client.images.generate(prompt=imageDesc, model=model)
    #print(image)
    image_url = image.data[0].url
    response = requests.get(image_url)
    with open('/savedInfo/image.png', 'wb') as f:
        f.write(response.content)
    img = Image.open('/savedInfo/image.png')
    img.show()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    #prompt = request.args.get('msg')
    #answer = createScene(prompt)
    answer = "blah blah blah"
    return str(answer)
    # issue_prompt = (f"You are a online service chatbot. Be courteous and explain a solution to the following problem: "
    #               f"\n\n{userText}")
    # response = openai.chat.completions.create(
    #     model="gpt-3.5-turbo",
    #     messages=[
	  #   {
		#     "role": "user",
		#     "content": issue_prompt
	  #   }
	  #   ],
    #     max_tokens=1024,
    #     n=1,
    #     stop=None,
    #     temperature=1,
    # )
    #answer = response.choices[0].message.content
    #return str(answer)


if __name__ == "__main__":
    app.run(port=80)


