import gradio as gr
import rw_json

def code_response(message, history):
    for i in rw_json.reading_json():
        for j in i:
            if j == message:
                return i

gr.ChatInterface(code_response).launch()