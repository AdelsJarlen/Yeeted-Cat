import gradio as gr
from data.data import Data
from functionality.whisper import transcribe_audio

class whisper_tab:
    def __init__(self, data: Data, id: int):
        self.data = data
        self.id = id

        with gr.Tab("Tale-til-tekst", id):
            audio_input = gr.Audio(sources=["upload","microphone"], type="filepath")
            transcript_output = gr.Textbox(label="Transkribering",placeholder="Tekst fra intervjuet vil vises her", interactive=False, show_copy_button=True)
            submit_audio_btn = gr.Button("Transkriber lydklipp")
            submit_audio_btn.click(fn=self.transcribe, inputs=audio_input, outputs=transcript_output)

    def transcribe(self,audio):
        transcription = transcribe_audio(audio)
        self.data.transcription = transcription
        return transcription
    
   