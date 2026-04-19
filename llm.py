from groq import Groq
import os

client = Groq(api_key = os.getenv("GROQ_API_KEY"))
MODEL_NAME = "llama-3.1-8b-instant"

def generate_answer(query, context):
    
    prompt = f"""
        You are a factual AI assistant.

        Answer the question ONLY using the given context.

        Rules:
        - If the answer is unclear or not found, say exactly: "No clear answer found from sources."
        - Do NOT guess or infer.
        - Do NOT use Reddit, Facebook, or any social media as sources.

        Question: {query}

        Context:
        {context}

        Output format (strictly follow this):

        Output format (strictly follow this):

        Answer: <clear, specific comparison with numbers for each item>

        Sources:
        <url1>
        <url2>
    """
    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages = [{'role': 'user', 'content':prompt}]
        )
    
    return response.choices[0].message.content
