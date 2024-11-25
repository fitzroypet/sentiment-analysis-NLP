import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

class SentimentVisualizer:
    def __init__(self):
        pass
    
    def plot_sentiment_distribution(self, df, save_path=None):
        """Plot distribution of sentiment categories"""
        plt.figure(figsize=(10, 6))
        sns.countplot(data=df, x='sentiment_category')
        plt.title('Distribution of Sentiments')
        plt.xlabel('Sentiment Category')
        plt.ylabel('Count')
        
        if save_path:
            plt.savefig(save_path)
        plt.close()
    
    def plot_sentiment_scores(self, df, save_path=None):
        """Plot distribution of compound scores"""
        plt.figure(figsize=(10, 6))
        sns.histplot(data=df, x='compound_score', bins=50)
        plt.title('Distribution of Sentiment Scores')
        plt.xlabel('Compound Score')
        plt.ylabel('Count')
        
        if save_path:
            plt.savefig(save_path)
        plt.close()
    
    def plot_sentiment_by_score(self, df, save_path=None):
        """Plot average sentiment for each review score"""
        avg_sentiment = df.groupby('Score')['compound_score'].mean().reset_index()
        
        plt.figure(figsize=(10, 6))
        sns.barplot(data=avg_sentiment, x='Score', y='compound_score')
        plt.title('Average Sentiment Score by Review Rating')
        plt.xlabel('Review Score')
        plt.ylabel('Average Sentiment Score')
        
        if save_path:
            plt.savefig(save_path)
        plt.close() 