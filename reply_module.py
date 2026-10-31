from groq import Groq

client = Groq()


def generate_reply(customer_name, customer_email, previous_reply, intent):

    prompt = f"""
Generate a professional customer support email reply.

Customer Name: {customer_name}
Customer Email: {customer_email}
Detected Intent: {intent}

A similar previous customer received this reply:
{previous_reply}

Use the previous reply only as helpful context.
Write a clear, polite and professional response to the current customer.

Start with:
Dear {customer_name},

End with:
Regards,
Support Team

Return only the email reply.
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

    return response.choices[0].message.content