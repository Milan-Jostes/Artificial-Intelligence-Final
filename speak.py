from openai import OpenAI
#import vlc
import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('OPEN_AI_KEY')
client = OpenAI(api_key=key)
speech_file = "savedInfo\speech"
num = 1
# Load the environment variables from .env file

# Access the OPEN_AI_KEY environment variable


def process(info):
    #print(info)
    lines = info.splitlines()
    #print(lines)
    for line in lines:
        #print(line)
        if len(line)<=1:
            continue
        if "Female Voice:" in line:
            print("Woman")
            female(line)
        elif "Male Voice:" in line:
            print("Male")
            male(line)
        else:
            print("Narrator")
            narrator(line)
    no_gender = info.replace("Male Voice:","")
    no_gender = info.replace("Female Voice:","")
    no_gender = info.replace("Narrator Voice:","")
    return no_gender
def male(info):
    response = client.audio.speech.create(
    model="tts-1",
    voice="echo",
    input=info
    )
    global num
    speech_save = f"{speech_file}{num}.mp3"
    response.stream_to_file(speech_save)
    num+=1

def narrator(info):
    response = client.audio.speech.create(
    model="tts-1",
    voice="onyx",
    input=info
    )
    global num
    speech_save = f"{speech_file}{num}.mp3"
    response.stream_to_file(speech_save)
    num+=1

def female(info):
    response = client.audio.speech.create(
    model="tts-1",
    voice="alloy",
    input=info
    )
    global num
    speech_save = f"{speech_file}{num}.mp3"
    response.stream_to_file(speech_save)
    num+=1





# from gtts import gTTS
# import os

# from elevenlabs import play
# from elevenlabs.client import ElevenLabs

# ELEVEN_LABS_KEY = os.getenv('ELEVEN_LABS_KEY')

# client = ElevenLabs(
#   api_key=ELEVEN_LABS_KEY, # Defaults to ELEVEN_API_KEY
# )

# from elevenlabs.client import ElevenLabs

# client = ElevenLabs(
#   api_key="YOUR_API_KEY", # Defaults to ELEVEN_API_KEY
# )

# response = client.voices.get_all()
# audio = client.generate(text="Hello there!", voice=response.voices[0])
# print(voices)



# audio = client.generate(
#   text="Hello! 你好! Hola! नमस्ते! Bonjour! こんにちは! مرحبا! 안녕하세요! Ciao! Cześć! Привіт! வணக்கம்!",
#   voice="Rachel",
#   model="eleven_multilingual_v2"
# )
# play(audio)


# def text_to_wizard_voice(text, output_file="savedInfo\wizard_voice.mp3"):
#     # Initialize gTTS object
#     tts = gTTS(text=text, lang='en', slow=False)  # slow=False for a normal speech rate

#     # Save the audio file
#     tts.save(output_file)

#     print(f"Wizard voice saved as {output_file}")

# # Example usage
# wizard_text = "It is I, James Moriarty"
# text_to_wizard_voice(wizard_text)