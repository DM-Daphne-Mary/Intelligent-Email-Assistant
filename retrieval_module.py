import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def retrieve_similar_email(customer_email):

    # Load previous customer interactions
    data = pd.read_csv("data/emails.csv")

    # Get historical customer emails
    previous_emails = data["Customer_Email"].fillna("").tolist()

    # Add current email for comparison
    all_emails = previous_emails + [customer_email]

    # Convert emails into TF-IDF vectors
    vectorizer = TfidfVectorizer(stop_words="english")

    vectors = vectorizer.fit_transform(all_emails)

    # Compare current email with previous emails
    similarities = cosine_similarity(
        vectors[-1],
        vectors[:-1]
    )

    # Find most similar email
    index = similarities.argmax()

    previous_email = data.iloc[index]["Customer_Email"]
    previous_reply = data.iloc[index]["Previous_Reply"]

    return previous_email, previous_reply