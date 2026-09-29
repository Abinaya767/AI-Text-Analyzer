import nltk
import re
import spacy
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.tokenize import sent_tokenize
from sklearn.feature_extraction.text import TfidfVectorizer
nlp = spacy.load("en_core_web_sm")
def preprocess_text(text):
    # Convert text to lowercase
    text = text.lower()

    # Remove special characters and numbers
    text = re.sub(r'[^a-zA-Z\s]', '', text)

    # Tokenize the text
    words = word_tokenize(text)

    # Get English stopwords
    stop_words = set(stopwords.words('english'))

    # Remove stopwords
    filtered_words = []

    for word in words:
        if word not in stop_words:
            filtered_words.append(word)

    return filtered_words
from sklearn.feature_extraction.text import TfidfVectorizer
def extract_keywords(text, number_of_keywords=10):

    doc = nlp(text)

    keywords = []

    # Extract noun phrases
    for chunk in doc.noun_chunks:

        words = []

        for token in chunk:

            if token.is_stop:
                continue

            if not token.is_alpha:
                continue

            if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
                words.append(token.text.lower())

        phrase = " ".join(words)

        if len(words) >= 2 and phrase not in keywords:
            keywords.append(phrase)

    # Add important individual nouns
    for token in doc:

        if token.is_stop:
            continue

        if not token.is_alpha:
            continue

        if token.pos_ in ["NOUN", "PROPN"]:

            word = token.text.lower()

            if word not in keywords:
                keywords.append(word)

    return keywords[:number_of_keywords]
def summarize_text(text, number_of_sentences=3):

    sentences = sent_tokenize(text)

    if len(sentences) <= number_of_sentences:
        return text

    vectorizer = TfidfVectorizer(stop_words='english')

    tfidf_matrix = vectorizer.fit_transform(sentences)

    sentence_scores = tfidf_matrix.sum(axis=1)

    sentence_scores = sentence_scores.A1

    ranked_sentences = sorted(
        range(len(sentences)),
        key=lambda i: sentence_scores[i],
        reverse=True
    )

    selected_sentences = ranked_sentences[:number_of_sentences]

    selected_sentences.sort()

    summary = " ".join(
        sentences[i] for i in selected_sentences
    )

    return summary
def identify_topics(text, number_of_topics=3):

    doc = nlp(text)

    topic_phrases = []

    for chunk in doc.noun_chunks:

        words = []

        for token in chunk:

            if token.is_stop:
                continue

            if not token.is_alpha:
                continue

            if token.pos_ in ["NOUN", "PROPN", "ADJ"]:
                words.append(token.text.lower())

        phrase = " ".join(words)

        if len(words) >= 2:
            if phrase not in topic_phrases:
                topic_phrases.append(phrase)

    return topic_phrases[:number_of_topics]
def extract_entities(text):

    doc = nlp(text)

    entities = []

    for entity in doc.ents:

        entities.append(
            (entity.text, entity.label_)
        )

    return entities