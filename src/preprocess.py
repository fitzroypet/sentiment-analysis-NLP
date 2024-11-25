import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class TextPreprocessor:
    def __init__(self):
        # Download all required NLTK data
        try:
            nltk.download('punkt')
            nltk.download('stopwords')
            nltk.download('wordnet')
            nltk.download('omw-1.4')  # Open Multilingual Wordnet
            nltk.download('averaged_perceptron_tagger')
            nltk.download('punkt_tab')
        except Exception as e:
            print(f"Warning: Some NLTK downloads failed but we'll continue: {e}")
        
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()
    
    def preprocess(self, text):
        """
        Preprocess text by performing:
        - Lowercase conversion
        - Tokenization
        - Stop word removal
        - Lemmatization
        """
        try:
            # Convert to lowercase and tokenize
            tokens = word_tokenize(str(text).lower())
            
            # Remove stopwords and lemmatize
            tokens = [self.lemmatizer.lemmatize(token) 
                     for token in tokens 
                     if token.isalnum() and token not in self.stop_words]
            
            return ' '.join(tokens)
        except Exception as e:
            print(f"Warning: Error processing text: {e}")
            return text  # Return original text if processing fails