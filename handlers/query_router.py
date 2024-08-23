from sentence_transformers import SentenceTransformer
from handlers.sql_handler import standard_sql_query_handler
from handlers.plot_handler import plot_generation_handler
from handlers.cache_handler import update_cache, cached_response_handler

model = SentenceTransformer('all-MiniLM-L6-v2')

def query_router(question):
    question_embedding = model.encode([question])

    cached_answer = cached_response_handler(question_embedding)
    if cached_answer:
        return cached_answer

    df, plot_response = standard_sql_query_handler(question)
    update_cache(question, df, question_embedding, plot_response)
    return df, plot_response

def handle_query(question):
    df, plot_response = query_router(question)
    
    if df is not None:
        return df.to_html(), None
    elif plot_response is not None:
        return None, plot_response
    else:
        return "No response generated.", None
