# from openai import OpenAI
# import os
# from dotenv import load_dotenv
# import vlc

# # Load the environment variables from .env file
# load_dotenv()

# # Access the OPEN_AI_KEY environment variable
# OPEN_AI_KEY = os.getenv('OPEN_AI_KEY')

# # Now you can use OPEN_AI_KEY in your code
# print(OPEN_AI_KEY)  # For demonstration purposes; remove this in production

# client = OpenAI(api_key=OPEN_AI_KEY)
# speech_file = "speech.mp3"
# response = client.audio.speech.create(
# model="tts-1",
# voice="alloy",
# input="The dark wizard raises his staff over his head.... and casts fire ball"
# )
# #response.with_streaming_response.method(speech_file)
# response.stream_to_file(speech_file)
# player = vlc.MediaPlayer("speech.mp3")
# player.play()



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


def text_to_wizard_voice(text, output_file="savedInfo\wizard_voice.mp3"):
    # Initialize gTTS object
    tts = gTTS(text=text, lang='en', slow=False)  # slow=False for a normal speech rate

    # Save the audio file
    tts.save(output_file)

    print(f"Wizard voice saved as {output_file}")

# Example usage
wizard_text = "It is I, James Moriarty"
text_to_wizard_voice(wizard_text)
