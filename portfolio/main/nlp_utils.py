import re
import heapq
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize


def summarize_text(text, num_sentences=3):

    if not text:
        return []

    # Clean whitespace
    text = re.sub(r'\s+', ' ', text)

    # Split sentences
    sentences = sent_tokenize(text)

    # If short text, return as-is
    if len(sentences) <= num_sentences:
        return sentences

    # Build frequency table
    stop_words = set(stopwords.words('english'))
    words = word_tokenize(text.lower())

    freq_table = {}
    for word in words:
        if word.isalnum() and word not in stop_words:
            freq_table[word] = freq_table.get(word, 0) + 1

    # Score sentences
    sentence_scores = {}
    for sent in sentences:
        for word in word_tokenize(sent.lower()):
            if word in freq_table:
                sentence_scores[sent] = sentence_scores.get(sent, 0) + freq_table[word]

    # Pick top sentences
    summary = heapq.nlargest(
        num_sentences,
        sentence_scores,
        key=sentence_scores.get
    )

    return summary