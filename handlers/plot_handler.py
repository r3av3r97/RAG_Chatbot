import matplotlib.pyplot as plt
from utils.prompts import pandas_system_prompt
from utils.database import create_pandas_dataframe_agent

def create_pandas_plot_agent(df, question):
    pandas_agent = create_pandas_dataframe_agent(df)
    plot_code = pandas_agent.run(question)
    return plot_code

def plot_generation_handler(question, df):
    if any(keyword in question.lower() for keyword in ["plot", "graph", "visualization", "visualize", "chart"]):
        plot_code = create_pandas_plot_agent(df, question)

        try:
            exec(plot_code)
            fig = plt.gcf()
            return fig
        except Exception as e:
            return f"An error occurred while generating the plot: {str(e)}"
    return None
