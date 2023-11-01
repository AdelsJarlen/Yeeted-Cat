import gradio as gr
from functionality import *

def whisper_tab():
    with gr.TabItem("Tale-til-tekst", id=0):
        audio_input = gr.inputs.Audio(source="upload", type="filepath")
        output_text = gr.Textbox(show_copy_button = True)

        iface = gr.Interface(
            fn=whisper.transcribe_audio, 
            inputs=audio_input,             
            outputs=output_text, 
            title="Audio Transcription App",    
            description="Upload an audio file and hit the 'Submit' button"
        )