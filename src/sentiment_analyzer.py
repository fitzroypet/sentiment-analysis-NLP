from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd

class SentimentAnalyzer:
    def __init__(self):
        self.analyzer = SentimentIntensityAnalyzer()
    
    def analyze_text(self, text):
        """Analyze sentiment of given text using VADER"""
        return self.analyzer.polarity_scores(text)
    
    def classify_sentiment(self, compound_score):
        """Classify sentiment based on compound score"""
        if compound_score > 0.05:
            return 'positive'
        elif compound_score < -0.05:
            return 'negative'
        else:
            return 'neutral'
    
    def analyze_dataframe(self, df, text_column='processed_text'):
        """Analyze sentiment for an entire dataframe"""
        # Get sentiment scores
        df['sentiment'] = df[text_column].apply(self.analyze_text)
        
        # Extract compound score
        df['compound_score'] = df['sentiment'].apply(lambda x: x['compound'])
        
        # Classify sentiment
        df['sentiment_category'] = df['compound_score'].apply(self.classify_sentiment)
        
        return df 