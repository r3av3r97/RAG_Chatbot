import gradio as gr
from handlers.query_router import handle_query
from handlers.cache_handler import get_top_5_questions

def launch_app():
    with gr.Blocks() as demo:
        gr.Markdown("# Healthcare RAG System with SQL Agent")

        top_5_questions = gr.Markdown(get_top_5_questions(), label="Top 5 Frequently Asked Questions")

        with gr.Row():
            with gr.Column():
                question_input = gr.Textbox(label="Enter your Question")
                submit_button = gr.Button("Submit")

            with gr.Column():
                output_text = gr.HTML(label="Output")
                plot_output = gr.Plot(label="Plot")

        submit_button.click(handle_query, inputs=question_input, outputs=[output_text, plot_output])

    demo.launch()
