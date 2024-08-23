from sklearn.metrics.pairwise import cosine_similarity

top_questions_cache = []

def find_similar_question(new_question_embedding):
    if not top_questions_cache:
        return None, None

    similarities = [cosine_similarity(new_question_embedding, cached['embedding'])[0][0] for cached in top_questions_cache]
    max_similarity = max(similarities)
    if max_similarity > 0.8:
        index = similarities.index(max_similarity)
        return top_questions_cache[index]['question'], top_questions_cache[index]['answer']
    
    return None, None

def update_cache(new_question, new_answer, new_embedding, new_plot=None):
    for item in top_questions_cache:
        if cosine_similarity(new_embedding, item['embedding'])[0][0] > 0.8:
            item['counter'] += 1
            return
    if len(top_questions_cache) < 5:
        top_questions_cache.append({
            'question': new_question,
            'answer': new_answer,
            'embedding': new_embedding,
            'plot': new_plot,
            'counter': 1
        })
    else:
        top_questions_cache.sort(key=lambda x: x['counter'])
        top_questions_cache.pop(0)
        top_questions_cache.append({
            'question': new_question,
            'answer': new_answer,
            'embedding': new_embedding,
            'plot': new_plot,
            'counter': 1
        })

def get_top_5_questions():
    if top_questions_cache:
        sorted_cache = sorted(top_questions_cache, key=lambda x: x['counter'], reverse=True)
        top_questions = [f"Q: {item['question']} (Asked {item['counter']} times)" for item in sorted_cache[:5]]
        return "\n".join(top_questions)
    return "No questions asked yet."
