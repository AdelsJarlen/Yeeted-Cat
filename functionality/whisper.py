import whisper
from transformers import pipeline

def transcribe_audio(audio_file):

  asr = pipeline(
    "automatic-speech-recognition",
    "NbAiLab/nb-whisper-base-beta"
  )
  result = asr(
      audio_file,
      generate_kwargs={'task': 'transcribe', 'language': 'no'}
  )
  return result["text"]