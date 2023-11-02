import gradio as gr
from data.data import Data
from interface.tabs import whisper_tab, gpt_tab, clipdrop_tab

def interface():
    data = Data()

    with gr.Blocks() as b:
        whisper_tab.whisper_tab(data, 0)    
        gpt_tab.gpt_tab(data, 1)
        clipdrop_tab.clipdrop_tab(data, 2)

    b.launch()