from src.preprocess import TextPreprocessor
from src.sentiment_analyzer import SentimentAnalyzer
from src.visualizer import SentimentVisualizer
import pandas as pd

def process_in_chunks(file_path, chunk_size):
    # Read the CSV in chunks with proper parameters
    chunks = pd.read_csv(file_path, 
                        skiprows=1,  # Skip the "Reviews" row
                        chunksize=chunk_size,
                        low_memory=False,
                        dtype={
                            'Id': str,
                            'ProductId': str,
                            'UserId': str,
                            'ProfileName': str,
                            'HelpfulnessNumerator': int,
                            'HelpfulnessDenominator': int,
                            'Score': int,
                            'Time': int,
                            'Summary': str,
                            'Text': str
                        })
    
    # Process each chunk
    df_list = []
    for chunk in chunks:
        df_list.append(chunk)
    
    # Combine all chunks
    return pd.concat(df_list, ignore_index=True)

def main():
    # Initialize classes
    preprocessor = TextPreprocessor()
    analyzer = SentimentAnalyzer()
    visualizer = SentimentVisualizer()
    
    # Load and process data
    file_path = 'data/Reviews.csv'
    print("Processing data in chunks...")
    df = process_in_chunks(file_path, chunk_size=10000)
    
    print("\nDataset shape:", df.shape)
    print("\nColumns:", df.columns.tolist())
    
    print("\nPreprocessing texts...")
    df['processed_text'] = df['Text'].apply(preprocessor.preprocess)
    
    print("Analyzing sentiment...")
    df = analyzer.analyze_dataframe(df)
    
    print("\nSentiment Distribution:")
    print(df['sentiment_category'].value_counts())
    
    # Create visualizations
    visualizer.plot_sentiment_distribution(df, 'data/sentiment_distribution.png')
    visualizer.plot_sentiment_scores(df, 'data/sentiment_scores.png')
    visualizer.plot_sentiment_by_score(df, 'data/sentiment_by_score.png')
    
    # Save results
    df.to_csv('data/analyzed_reviews.csv', index=False)
    print("\nResults saved to 'analyzed_reviews.csv'")

if __name__ == "__main__":
    main() 