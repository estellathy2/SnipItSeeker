import gradio as gr
import rw_json

def code_response(message, history):
    message = str(message)
    matching_lists = []
    for i in rw_json.reading_json():
        if i and isinstance(i[0], str) and message in i[0]:
            matching_lists.append([i[0], f"```py\n{i[1]}\n```"])

    output = '\n\n'.join(['\n'.join(item) for item in matching_lists])
    return output

gr.ChatInterface(code_response).launch(share=True)
