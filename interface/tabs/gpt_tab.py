import gradio as gr
import os
import tempfile
from functionality.gpt import *
from data.data import Data

class gpt_tab:
    def update_data_transcription(self):
        return self.data.transcription

    def __init__(self, data: Data, id: int):
        self.data = data

        self.prompt_placeholder = "Fill in text here"
        with gr.Tab("Tekst-til-bildebeskrivelse", id) as main_tab:
            gr.Markdown("""<h1><center>ChatGPT ChatBot  
            with Gradio and OpenAI</center></h1> 
            """)

            self.state = gr.State()
            with gr.Row():
                with gr.Column():
                    with gr.Tab("Last opp tekstfil"):
                        file_output = gr.File()
                        opplast = gr.UploadButton("Last opp fil", file_types=["image", "video", "text", "audio"], file_count="single", visible = False)
                        with gr.Row():
                            file_prompt = gr.Button("Prompt")
                            file_sammendrag = gr.Button("Sammendrag")
                    with gr.Tab("Transkribering fra opptak"):
                        tekstboks = gr.Textbox(data.transcription, label="Transkribering")
                        main_tab.select(fn=self.update_data_transcription, outputs=tekstboks)
                        with gr.Row():
                            transcript_prompt = gr.Button("Prompt")
                            transcript_sammendrag = gr.Button("Sammendrag")
                with gr.Column():
                    chatbot = gr.Chatbot()
                    with gr.Row():
                        send_svar = gr.Button("Generer bilde")
            with gr.Row():
                opplast.upload(last_opp, opplast, file_output)
                file_prompt.click(fn = create_prompt_from_file, inputs = file_output, outputs = [chatbot])
                file_sammendrag.click(fn = create_summary_from_file, inputs = file_output, outputs = [chatbot])
                send_svar.click(hent_svar, inputs = [file_output])
                transcript_prompt.click(fn = self.create_text, inputs = tekstboks, outputs = [chatbot])
                transcript_sammendrag.click(fn = create_summary_from_text, inputs = tekstboks, outputs = [chatbot])

    def create_text(self, text: str):
        t = create_prompt_from_text(text)
        self.data.prompt = t[0][1]
        return t