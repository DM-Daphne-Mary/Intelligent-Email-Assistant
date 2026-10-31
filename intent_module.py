from groq import Groq

client = Groq()


def detect_intent(customer_email):

    prompt = f"""
Classify the following customer email into exactly ONE of these intents:

Delivery Issue
Refund Request
Product Complaint
Technical Support
Order Cancellation
General Inquiry

Customer Email:
{customer_email}

Return only the intent name.
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