import openai

def extract_object(text):
    prompt = f"Extract the main object being queried in this sentence: '{text}'"
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response['choices'][0]['message']['content'].strip()