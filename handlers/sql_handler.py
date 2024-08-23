import json
import pandas as pd
from utils.database import db, agent_executor
from utils.prompts import standard_sql_query_prompt

def standard_sql_query_handler(question):
    """Handle standard SQL queries using the SQL agent."""
    response = agent_executor.run(question)

    try:
        cleaned_response = response.strip('```json').strip()
        output_data = json.loads(cleaned_response)

        if isinstance(output_data, list):
            df = pd.DataFrame(output_data)
        elif isinstance(output_data, dict):
            flattened_data = []
            for key, value in output_data.items():
                if isinstance(value, dict):
                    for sub_key, sub_value in value.items():
                        flattened_data.append({"Category": f"{key} - {sub_key}", "Value": sub_value})
                else:
                    flattened_data.append({"Category": key, "Value": value})
            df = pd.DataFrame(flattened_data)
        else:
            raise ValueError("Data is not in the expected format for DataFrame conversion.")

        return df, None

    except (json.JSONDecodeError, ValueError) as e:
        return None, f"An error occurred: {str(e)}"
