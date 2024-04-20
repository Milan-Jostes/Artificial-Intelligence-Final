import os
from pydub import AudioSegment

def stitch():
  # Path to the folder containing the audio files
  folder_path = 'static/Voices'
  # Get a list of all the audio files in the folder
  audio_files = [file for file in os.listdir(folder_path) if (file.endswith('.mp3') and file.startswith('speech'))]

  # Sort the audio files based on their names
  audio_files.sort()
  print(audio_files)

  # Create an empty AudioSegment object to store the combined audio
  combined_audio = AudioSegment.empty()

  # Iterate over the audio files and append them to the combined audio
  for file in audio_files:
    path_find = os.path.join(folder_path, file)
    print(path_find)
    audio = AudioSegment.from_file(path_find, format='mp3')
    combined_audio += audio

  # Export the combined audio to a new file
  combined_audio.export('static/Voices/output.mp3', format='mp3')