import gradio as gr
import requests

API_URL = "http://127.0.0.1:8000"

def upload_pdf(file):
    files = {"file": (file.name, file, "application/pdf")}
    response = requests.post(f"{API_URL}/upload_pdf", files=files)
    return response.json().get("message", "Error uploading PDF")

def ask_question(message, pdf_mode):
    data = {"message": message, "pdf_mode": pdf_mode}
    response = requests.post(f"{API_URL}/ask", json=data)
    return response.json().get("response", "Error getting response")

def toggle_mode(pdf_mode):
    return "📄 PDF Mode Enabled" if pdf_mode else "💬 Direct Chat Mode"

def create_interface():
    with gr.Blocks(title="PDF Chatbot") as demo:
        gr.Markdown("# 📚 PDF Chatbot")
        
        with gr.Row():
            with gr.Column():
                pdf_file = gr.File(label="Upload PDF", file_types=[".pdf"], type="binary")
                upload_button = gr.Button("Upload")
                upload_status = gr.Markdown("No PDF uploaded")
                
                mode_toggle = gr.Checkbox(label="Enable PDF Mode", value=False)
                mode_status = gr.Markdown("💬 Direct Chat Mode")
                
            with gr.Column():
                chatbot = gr.Chatbot(label="Conversation")
                msg = gr.Textbox(label="Ask a question", lines=2)
                clear = gr.Button("Clear Chat")
        
        upload_button.click(upload_pdf, inputs=[pdf_file], outputs=[upload_status])
        mode_toggle.change(toggle_mode, inputs=[mode_toggle], outputs=[mode_status])
        msg.submit(ask_question, inputs=[msg, mode_toggle], outputs=[chatbot])
        clear.click(lambda: None, None, chatbot)
    
    return demo

if __name__ == "__main__":
    demo = create_interface()
    demo.launch()