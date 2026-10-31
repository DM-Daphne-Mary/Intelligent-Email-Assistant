from intent_module import detect_intent
from retrieval_module import retrieve_similar_email
from reply_module import generate_reply
from tone_module import improve_tone
from summary_module import generate_summary
from utils import save_reply


def email_assistant():

    print("\n========================================")
    print("       INTELLIGENT EMAIL ASSISTANT")
    print("========================================")

    customer_name = input("Enter Customer Name: ")
    subject = input("Enter Email Subject: ")
    customer_email = input("Enter Customer Email: ")

    print("\n--- Customer Details ---")
    print("Customer Name :", customer_name)
    print("Subject       :", subject)
    print("Customer Email:", customer_email)

    # Intent Detection
    print("\nDetecting Customer Intent...")
    intent = detect_intent(customer_email)

    print("\nDetected Intent:")
    print(intent)

    # Similar Email Retrieval
    print("\nSearching for Similar Previous Email...")

    previous_email, previous_reply = retrieve_similar_email(
        customer_email
    )

    print("\n--- Similar Previous Interaction ---")
    print("Previous Email:")
    print(previous_email)

    print("\nPrevious Reply:")
    print(previous_reply)

    # Generate Reply
    print("\nGenerating AI Reply...")

    generated_reply = generate_reply(
        customer_name,
        customer_email,
        previous_reply,
        intent
    )

    print("\n--- Generated Reply ---")
    print(generated_reply)

    # Tone Improvement
    print("\nChoose Reply Tone")
    print("1. Friendly")
    print("2. Formal")
    print("3. Empathetic")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        tone = "Friendly"
    elif choice == "2":
        tone = "Formal"
    elif choice == "3":
        tone = "Empathetic"
    else:
        tone = "Formal"

    improved_reply = improve_tone(
        generated_reply,
        tone
    )

    print(f"\n--- {tone} Reply ---")
    print(improved_reply)

    # Conversation Summary
    print("\nGenerating Conversation Summary...")

    summary = generate_summary(customer_email)

    print("\n--- Conversation Summary ---")
    print(summary)

    # Save Final Reply
    save_reply(
        customer_email,
        improved_reply,
        intent
    )

    print("\nReply Saved Successfully!")
    print("Saved in: outputs/generated_reply.txt")


# Continuous Menu
while True:

    print("\n========================================")
    print("       INTELLIGENT EMAIL ASSISTANT")
    print("========================================")
    print("1. Process Customer Email")
    print("2. Exit")
    print("========================================")

    menu_choice = input("Enter your choice: ")

    if menu_choice == "1":
        email_assistant()

    elif menu_choice == "2":
        print("\nThank you for using Intelligent Email Assistant!")
        break

    else:
        print("\nInvalid choice. Please enter 1 or 2.")