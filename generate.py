import os
from dotenv import load_dotenv
from openai import OpenAI
from speak import *
import requests
from flask import Flask, render_template, request
from CustomLanguage import basic_command


from PIL import Image
load_dotenv()
key = os.getenv('OPEN_AI_KEY')
client = OpenAI(api_key=key)

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
UPLOAD_FOLDER = 'C:/Users/mjostes/Documents/GitHub/ChatGPT-Final/savedInfo'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

global img_num
img_num = 0
def createScene(prompt):
    responseScene = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
    {
    "role": "system",
    "content": "You are a DM for A Dungeons and Dragons game, you must speak as a wise wizard that is describing things in great detail as a user plays through your story.When a character speaks, before their text place either Male Voice: or Female Voice: depending on the gender of the character being portrayed. You may not portray the user's character, instead prompt the user to respond. Make sure to connect this to the previous scene. When the user wants to do something that would require skill, ask for them to roll and use the result to determine the outcome. The success should be based on the difficulty of the task. The user will input a number between 1 and 20, The higher the number, the more successful they are at the task"
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
    global img_num
    img_num+=1
    with open('static\Image\image'+str(img_num)+'.png', 'wb') as f:
        f.write(response.content)
    #img = Image.open('static\Image\image.png')
    #img.show()

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/get")
def get_bot_response():
    prompt = request.args.get('msg')
    print(prompt)
    if(prompt.startswith("!")):
        print("Command Detected")
        prompt = prompt[1:]
        print(prompt)
        resp = basic_command.run(prompt)
        print(resp)
        ret_str = "["
        if type(resp) == list:
            string_list = [str(element) for element in resp]
            delimiter = ", "
            ret_str += delimiter.join(string_list)
        else:
            ret_str += str(resp)
        ret_str += "]"
        return str("Command Detected: "+ret_str)
        #return ("Command Detected",data)
    else:
        answer = createScene(prompt)
        return str(answer)
    #answer = "blah blah blah"
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


