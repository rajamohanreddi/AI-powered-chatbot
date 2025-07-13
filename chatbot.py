from transformers import pipeline

# Load model once
chatbot_pipeline = pipeline("text-generation", model="microsoft/DialoGPT-medium")

def get_bot_response(user_input):
    response = chatbot_pipeline(user_input, max_length=1000, num_return_sequences=1)
    return response[0]['generated_text']
