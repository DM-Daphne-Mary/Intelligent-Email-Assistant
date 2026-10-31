from groq import Groq

client = Groq()


def improve_tone(reply, tone):

    prompt = f"""
Rewrite the following customer support email in a {tone} tone.

Keep the original meaning and important information.
Make the email clear, professional and natural.

Email:
{reply}

Return only the rewritten email.
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