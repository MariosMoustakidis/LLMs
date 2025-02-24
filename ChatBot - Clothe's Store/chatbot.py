import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

# Load OpenAI API Key
load_dotenv(override=True)
openai_api_key = os.getenv("OPENAI_API_KEY")

if openai_api_key:
    print(f"OpenAI API Key exists and begins {openai_api_key[:8]}")
else:
    raise ValueError("OpenAI API Key not set. Please check your .env file.")

# Initialize OpenAI client
openai = OpenAI(api_key=openai_api_key)
MODEL = "gpt-4o-mini"

# Define system message
BASE_SYSTEM_MESSAGE = """You are a helpful assistant in a clothes store. 
You should gently encourage the customer to try items that are on sale. 
Hats are 60% off, and most other items are 50% off.
For example, if the customer says 'I'm looking to buy a hat', 
you could reply with something like, 'Wonderful! We have lots of hats—several are part of our sales event!'
Encourage the customer to buy hats if they are unsure what to get.

If the customer asks for shoes, let them know that shoes are not on sale today, 
but remind them to check out our hats!"""

def chat(message, history):
    # Modify system message based on user input
    relevant_system_message = BASE_SYSTEM_MESSAGE

    if "belt" in message.lower():
        relevant_system_message += " The store does not sell belts, but we have a great selection of hats on sale."

    messages = [{"role": "system", "content": relevant_system_message}] + history + [
        {"role": "user", "content": message}
    ]

    response = ""
    stream = openai.chat.completions.create(model=MODEL, messages=messages, stream=True)

    for chunk in stream:
        content = chunk.choices[0].delta.content or ""
        response += content
        yield response  # Stream response to Gradio

# Launch Gradio Chat Interface
gr.ChatInterface(fn=chat, type="messages").launch(share=True)
