# Sentiment Analysis on Product Reviews

## Project Overview
This project performs sentiment analysis on product reviews to classify sentiments as positive, negative, or neutral. The analysis pipeline includes data preprocessing, sentiment analysis using the VADER sentiment analyzer, and visualization of the results.

## Installation

### Prerequisites
- Python 3.9 or higher
- pip

### Dependencies
Install the required Python packages using pip:

bash
pip install pandas numpy nltk vaderSentiment matplotlib seaborn


### NLTK Data
Download the required NLTK datasets:

python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
nltk.download('omw-1.4')
nltk.download('averaged_perceptron_tagger')


## Usage

### Data Preparation
Place your dataset in the `data/` directory. The dataset should be a CSV file with columns for `Id`, `ProductId`, `UserId`, `ProfileName`, `HelpfulnessNumerator`, `HelpfulnessDenominator`, `Score`, `Time`, `Summary`, and `Text`.

### Running the Analysis
Execute the main script to start the analysis:

bash
python main.py


### Output
The script will output:
- Sentiment distribution counts
- Visualizations in the `data/` directory:
  - `sentiment_distribution.png`
  - `sentiment_scores.png`
  - `sentiment_by_score.png`
- A CSV file `analyzed_reviews.csv` containing the processed data with sentiment analysis results.

## Project Structure

sentiment-analysis-NLP/
├── data/
│ ├── Reviews.csv # Dataset file
│ ├── sentiment_distribution.png
│ ├── sentiment_scores.png
│ ├── sentiment_by_score.png
│ └── analyzed_reviews.csv
├── src/
│ ├── init.py
│ ├── preprocess.py # Text preprocessing utilities
│ ├── sentiment_analyzer.py # Sentiment analysis utilities
│ └── visualizer.py # Visualization utilities
├── main.py # Main script to run the analysis
└── README.


## Contributing
Contributions to this project are welcome. Please fork the repository and submit a pull request.

## License
This project is open source and available under the [MIT License](LICENSE.md).

## Author
- Fitzroy Meyer-Petgrave

## Acknowledgments
- Thanks to the NLTK team for providing the tools to process and analyze text data.
- Thanks to the creators of the VADER sentiment analysis tool.

