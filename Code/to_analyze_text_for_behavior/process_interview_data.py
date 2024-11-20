import re
import pandas as pd
import spacy
from sklearn.model_selection import train_test_split
from collections import Counter
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


nlp = spacy.load("en_core_web_sm")


def load_text(filename):
    base_text = ""
    with open(filename, 'r') as f:
        lines = f.readlines()
        for line in lines:
            if not "Speaker 2" in line or "Speaker 3" in line:
                line = re.sub(
                    r'^\d{2}:\d{2}:\d{2}\s*', '', line)

                base_text += line.strip().replace("Speaker 1", "").replace("Speaker 2",
                                                                           "").replace("Speaker 3", "")
    f.close()
    return base_text


def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'\s+', ' ', text)  # remove extra spaces
    text = re.sub(r'[^\w\s]', '', text)  # remove punctuation
    doc = nlp(text)
    lemmatized = " ".join([token.lemma_ for token in doc if not token.is_stop])
    return lemmatized


def explore_text(pre_text):
    all_words = ' '.join([text for text in pre_text.split()])
    wordcloud = WordCloud(width=800, height=400,
                          background_color='black').generate(all_words)

    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis('off')
    plt.show()

    # Print the most common words
    word_counts = Counter(all_words.split())
    print(word_counts.most_common(20))


def sentiment_analysis(pre_text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(pre_text)
    print(score)


if __name__ == "__main__":
    filename = "Elizabeth.txt"
    # base_text = load_text(filename)
    # text_preprocessed = preprocess_text(base_text)
    file = open("Elizabeth_Preprocessed.txt", 'r')
    text_preprocessed = file.readline()
    explore_text(text_preprocessed)
    sentiment_analysis(text_preprocessed)

    # og_file = open("Elizabeth_OG.txt", 'w')
    # og_file.write(base_text)
    # og_file.close()

    # process_file = open("Elizabeth_Preprocessed.txt", 'w')
    # process_file.write(text_preprocessed)
    # process_file.close()
