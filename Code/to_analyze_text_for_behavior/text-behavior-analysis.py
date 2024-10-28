import pandas as pd
import nltk
from nltk.tokenize import word_tokenize, sent_tokenize
from nltk.sentiment import SentimentIntensityAnalyzer
from collections import Counter
import spacy
from sklearn.feature_extraction.text import TfidfVectorizer
from textblob import TextBlob


def analyze_text(text, user_id=None):
    results = {
        'user_id': user_id,
        'basic_metrics': _get_basic_metrics(text),
        'sentiment_analysis': _analyze_sentiment(text),
        'linguistic_features': _extract_linguistic_features(text),
        'behavioral_indicators': _identify_behavioral_indicators(text),
        'communication_style': _analyze_communication_style(text)
    }
    return results


def _get_basic_metrics(text):
    sentences = sent_tokenize(text)
    words = word_tokenize(text)

    return {
        'word_count': len(words),
        'sentence_count': len(sentences),
        'avg_words_per_sentence': len(words) / len(sentences) if sentences else 0,
        'unique_words': len(set(words)),
        'lexical_diversity': len(set(words)) / len(words) if words else 0
    }


def _analyze_sentiment(text):
    vader_scores = sia.polarity_scores(text)
    blob = TextBlob(text)

    return {
        'vader_compound': vader_scores['compound'],
        'vader_positive': vader_scores['pos'],
        'vader_negative': vader_scores['neg'],
        'vader_neutral': vader_scores['neu'],
        'textblob_polarity': blob.sentiment.polarity,
        'textblob_subjectivity': blob.sentiment.subjectivity
    }


def _extract_linguistic_features(text):
    doc = nlp(text)

    # Analyze parts of speech
    pos_counts = Counter([token.pos_ for token in doc])

    # Extract named entities
    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return {
        'parts_of_speech': dict(pos_counts),
        'named_entities': entities,
        'key_phrases': _extract_key_phrases(doc)
    }


def _identify_behavioral_indicators(text):
    """Identify potential behavioral indicators"""
    doc = nlp(text)

    # Analyze certainty and confidence
    certainty_words = set(
        ['definitely', 'certainly', 'surely', 'always', 'never'])
    uncertainty_words = set(
        ['maybe', 'perhaps', 'possibly', 'probably', 'might'])

    indicators = {
        'certainty_count': sum(1 for token in doc if token.text.lower() in certainty_words),
        'uncertainty_count': sum(1 for token in doc if token.text.lower() in uncertainty_words),
        'personal_pronouns': sum(1 for token in doc if token.pos_ == 'PRON'),
        'action_verbs': sum(1 for token in doc if token.pos_ == 'VERB')
    }

    return indicators


def _analyze_communication_style(text):
    """Analyze communication style patterns"""
    doc = nlp(text)

    # Analyze sentence complexity
    sentence_lengths = [len(sent) for sent in doc.sents]

    style_metrics = {
        'avg_sentence_length': sum(sentence_lengths) / len(sentence_lengths) if sentence_lengths else 0,
        'question_count': sum(1 for sent in doc.sents if sent.text.strip().endswith('?')),
        'exclamation_count': sum(1 for sent in doc.sents if sent.text.strip().endswith('!')),
        'formality_score': _calculate_formality_score(doc)
    }

    return style_metrics


def _extract_key_phrases(doc):
    """Extract important phrases from text"""
    return [chunk.text for chunk in doc.noun_chunks]


def _calculate_formality_score(doc):
    """Calculate a basic formality score based on language patterns"""
    formal_indicators = sum(1 for token in doc if len(
        token.text) > 6)  # longer words
    informal_indicators = sum(1 for token in doc if token.text.lower() in {
        'gonna', 'wanna', 'gotta'})

    return (formal_indicators - informal_indicators) / len(doc) if len(doc) > 0 else 0


def analyze_user_history(texts, user_id):
    """
    Analyze multiple texts from the same user to identify patterns

    Parameters:
    texts (list): List of text samples
    user_id (str): User identifier

    Returns:
    dict: Aggregated analysis results
    """
    analyses = [analyze_text(text, user_id) for text in texts]

    # Aggregate results
    aggregated = {
        'user_id': user_id,
        'total_samples': len(texts),
        'avg_sentiment': {
            'compound': sum(a['sentiment_analysis']['vader_compound'] for a in analyses) / len(analyses),
            'subjectivity': sum(a['sentiment_analysis']['textblob_subjectivity'] for a in analyses) / len(analyses)
        },
        'communication_patterns': {
            'avg_word_count': sum(a['basic_metrics']['word_count'] for a in analyses) / len(analyses),
            'avg_sentence_length': sum(a['communication_style']['avg_sentence_length'] for a in analyses) / len(analyses)
        },
        'behavioral_trends': _identify_trends(analyses)
    }

    return aggregated


def _identify_trends(analyses):
    """Identify behavioral trends across multiple analyses"""
    return {
        'sentiment_stability': _calculate_stability([a['sentiment_analysis']['vader_compound'] for a in analyses]),
        'vocabulary_diversity': _calculate_stability([a['basic_metrics']['lexical_diversity'] for a in analyses])
    }


def _calculate_stability(values):
    """Calculate stability score for a series of values"""
    return pd.Series(values).std() if values else 0


jack_the_ripper_letter = """Dear Boss, I keep on hearing the police have caught me but they won’t fix me just yet. 
        I have laughed when they look so clever and talk about being on the right track. That joke about Leather Apron 
        gave me real fits. I am down on whores and I shan’t quit ripping them till I do get buckled. Grand work the 
        last job was. I gave the lady no time to squeal. How can they catch me now? I love my work and want to start 
        again. You will soon hear of me with my funny little games. I saved some of the proper red stuff in a ginger 
        beer bottle over the last job to write with but it went thick like glue and I can’t use it. Red ink is fit 
        enough I hope ha. ha. The next job I do I shall clip the lady’s ears off and send to the police officers ... 
        My knife’s so nice and sharp I want to get to work right away if I get a chance. Good luck."""

"""Initialize the behavioral analysis framework"""
# Download required NLTK resources
nltk.download('punkt')
nltk.download('vader_lexicon')
nltk.download('averaged_perceptron_tagger')

# Initialize analyzers
nlp = spacy.load('en_core_web_trf')
sia = SentimentIntensityAnalyzer()
vectorizer = TfidfVectorizer()

results = analyze_text(jack_the_ripper_letter)
print(results)
