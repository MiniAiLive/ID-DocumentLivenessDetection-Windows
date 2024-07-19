import gradio as gr
import os
import requests
import json

def check_id_liveness(frame):
    url = "http://127.0.0.1:8093/api/check_id_liveness"
    files = {'image': open(frame, 'rb')}
    try:
        r = requests.post(url=url, files=files)
        r.raise_for_status()
        return json.dumps(r.json(), indent=2) 
    except requests.exceptions.RequestException as e:
        return str(e)

# APP Interface
with gr.Blocks() as MiniAIdemo:
    gr.Markdown(
        """
        <a href="https://miniai.live" style="display: flex; align-items: center;">
            <img src="https://miniai.live/wp-content/uploads/2024/02/logo_name-1-768x426-1.png" style="width: 18%; margin-right: 15px;"/>
            <div>
                <p style="font-size: 50px; font-weight: bold; margin-right: 20px;">ID Document Liveness Detection Web Online Demo</p>
            </div>
        </a>

        <br/>
        <ul>
            <li style="font-size: 18px;">Visit and learn more about our Service : <a href="https://miniai.live" target="_blank" style="font-size: 18px;">https://www.miniai.live</a></li>
            <li style="font-size: 18px;">Check our SDK for cross-platform from Github : <a href="https://github.com/MiniAiLive" target="_blank" style="font-size: 18px;">https://github.com/MiniAiLive</a></li>
            <li style="font-size: 18px;">Quick view our Youtube Demo Video : <a href="https://www.youtube.com/@miniailive" target="_blank" style="font-size: 18px;">MiniAiLive Youtube Channel</a></li>
            <li style="font-size: 18px;">Demo with Android device from Google Play : <a href="https://play.google.com/store/apps/dev?id=5831076207730531667" target="_blank" style="font-size: 18px;">MiniAiLive Google Play</a></li>
        </ul>
        <br/>
        """
    )
    with gr.Tabs():
        with gr.TabItem("ID Document Liveness Detection"):
            with gr.Row():
                with gr.Column():
                    im_idlive_input = gr.Image(type='filepath', height=300)
                    gr.Examples(
                        [
                            os.path.join(os.path.dirname(__file__), "images/demo1.jpg"),
                        ],
                        inputs=im_idlive_input
                    )
                    btn_f_idlive = gr.Button("Analysis Document", variant='primary')
                with gr.Column():
                    txt_idlive_output = gr.Textbox(label="API Response (JSON)")
            btn_f_idlive.click(check_id_liveness, inputs=im_idlive_input, outputs=txt_idlive_output)

if __name__ == "__main__":
    MiniAIdemo.launch(server_port=8083, server_name="0.0.0.0")