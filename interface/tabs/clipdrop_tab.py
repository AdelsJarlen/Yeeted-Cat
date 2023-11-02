import gradio as gr
from functionality.clipdrop import sendPromptToClipdrop
from data.data import Data

class clipdrop_tab:
    def update_data_prompt(self):
            return self.data.prompt

    def __init__(self, data: Data, id: int):
        self.data = data
        self.id = id

        with gr.Tab("Bildegenerering", self.id) as cd_tab:
            tekstboks = gr.Textbox(data.prompt, label="Bildebeskrivelse")
            cd_tab.select(fn=self.update_data_prompt, outputs=tekstboks)
            gallery = gr.Gallery()
            btn = gr.Button("Generer bilder")
            btn.click(fn=sendPromptToClipdrop, inputs=tekstboks, outputs=gallery)