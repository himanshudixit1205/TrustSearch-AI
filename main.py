from search import search_web
from llm import generate_answer
from utils import build_context

def validate_answer(answer):
    # If answer contains numbers but context was empty, likely hallucination
    # This is a simple heuristic
    if "Answer:" in answer:
        answer_text = answer.split("Answer:")[1].split("Sources:")[0]
        if any(char.isdigit() for char in answer_text) and "no clear answer" in answer.lower():
            return False
    return True

def web_search_agent(query):
    try:
        results = search_web(query)
        if not results:
            return "No search results found. Please try a different query."
        
        context = build_context(results)
        if not context.strip():
            return "No usable content found from search results."
        
        answer = generate_answer(query, context)
        
        if not validate_answer(answer):
            return "Unable to provide a reliable answer from available sources."
        
        return answer
        
    except Exception as e:
        print(f"Error in web_search_agent: {e}")
        return f"An error occurred while processing your request. Please try again."
    
    
if __name__ == "__main__":
    query = input("Enter your question: ").strip()
    
    if not query:
        print("Please enter a valid question.")
        exit(1)
    
    if len(query) > 500:
        print("Query too long. Please shorten your question.")
        exit(1)
    
    response = web_search_agent(query)
    
    print("\n===== FINAL ANSWER =====\n")
    print(response)