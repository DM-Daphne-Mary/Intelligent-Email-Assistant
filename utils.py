from datetime import datetime


def save_reply(customer_email, generated_reply, intent):

    date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    with open("outputs/generated_reply.txt", "a", encoding="utf-8") as file:

        file.write("\n====================================\n")
        file.write(f"Date: {date}\n")
        file.write(f"Intent: {intent}\n")
        file.write(f"Customer Email: {customer_email}\n")
        file.write("\nGenerated Reply:\n")
        file.write(generated_reply)
        file.write("\n====================================\n")