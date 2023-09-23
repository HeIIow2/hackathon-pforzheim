import nltk

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


# download nltk corpus (first time only)
import nltk

nltk.download('all')


nltk.download('vader_lexicon')
sia = SIA()

def rate_token(rate_token: str) -> float:
    pol_score = sia.polarity_scores(rate_token)
    return pol_score["compound"]


def rate(rating: str) -> float:
    _keywords: dict = {}

    for token in word_tokenize(rating):
        _keywords[rate_token(token)] = token


    pol_score = sia.polarity_scores(rating)
    pol_score['text'] = rating
    print()
    print(pol_score)
    return pol_score["compound"], _keywords
