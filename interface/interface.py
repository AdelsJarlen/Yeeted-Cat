import gradio as gr
from tabs import clipdrop_tab

def main_window():
    with gr.Blocks() as main_window:
        clipdrop_tab.clipdrop_tab()

    main_window.launch()

main_window()