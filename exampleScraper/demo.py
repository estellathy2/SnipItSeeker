import gradio as gr
import py_examples

def code_response(message, history):
    message = str(message)
    matching_lists = py_examples.search_similarity(message)
    output = '\n\n'.join(['\n'.join(item) for item in matching_lists])
    return output

gr.ChatInterface(code_response).launch(share=True)