from transformers import pipeline
import traceback
# import pyaudio as pya

def transcribe_audio(audio_file):
  try:
    asr = pipeline(
        "automatic-speech-recognition",
        model = "NbAiLab/nb-whisper-base-beta"
      )
  except Exception as e:
    traceback.print_exc(e)
    raise e
  
  result = asr(
      audio_file,
      generate_kwargs={'task': 'transcribe', 'language': 'no'}
  )
  return result["text"]

# # Audio Settings
# FORMAT = pya.paFloat32 #paInt16
# CHANNELS = 1
# RATE = 24000
# CHUNK_SIZE = 8192

# SILENCE = chr(0)*CHUNK_SIZE*2

# def transcribe_live(stream_data, new_chunk):
#   audio = pya.PyAudio()

#   stream = audio.open(
#     format=FORMAT,
#     channels=CHANNELS,
#     rate=RATE,
#     output=True,
#     frames_per_buffer=CHUNK_SIZE
#   )

#   stream.write(new_chunk)
  
#   sr, y = new_chunk
#   y = y.astype(np.float32)
#   y /= np.max(np.abs(y))

#   if stream_data is not None:
#       stream_data = np.concatenate([stream_data, y])
#   else:
#       stream_data = y
#   return stream_data, asr({"sampling_rate": sr, "raw": stream})["text"]