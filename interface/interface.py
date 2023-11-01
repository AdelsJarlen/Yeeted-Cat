import gradio as gr
from interface.tabs import clipdrop_tab, whisper_tab

def main_window():
    with gr.Blocks() as main_window:
        whisper_tab.whisper_tab()
        clipdrop_tab.clipdrop_tab()

    main_window.launch()

main_window()