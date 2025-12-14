import os
from dotenv import load_dotenv
from groq import Groq
from . import pdf_extractor

load_dotenv()
def generate_cover_letter(file):
    resume_text = pdf_extractor(file)
    client = Groq(
        api_key=os.getenv('GROQ_API_KEY'),
    )
    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": "what makes a good tailored cover letter",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    print(chat_completion.choices[0].message.content)