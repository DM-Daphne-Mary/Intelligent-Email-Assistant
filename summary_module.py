from groq import Groq

client = Groq()


def generate_summary(customer_email):

    prompt = f"""
Summarize the following customer issue in approximately 50 words.

Customer Email:
{customer_email}

Keep the summary clear, short and professional.
Return only the summary.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-20b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content.strip()