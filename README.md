# NLP Text Insight Analyzer

An NLP-based web application that analyzes articles and paragraphs using Text Summarization, Keyword Extraction, and Named Entity Recognition (NER).

## Features

* **Text Summarization** — Generates a concise summary from the input text.
* **Keyword Extraction** — Identifies important words and phrases.
* **Named Entity Recognition** — Detects entities such as people, organizations, locations, and dates.
* **Text Statistics** — Displays original word count, summary word count, and keyword count.
* **Interactive Streamlit UI** — Provides a simple and user-friendly interface.

## Technologies Used

* Python
* Streamlit
* spaCy
* NLTK
* Scikit-learn
* TF-IDF
* Natural Language Processing (NLP)

## How It Works

```text
User Input
    |
    v
Text Processing
    |
    +-------------------+---------------------+
    |                   |                     |
    v                   v                     v
Summarization     Keyword Extraction      NER
    |                   |                     |
    +-------------------+---------------------+
                        |
                        v
                 NLP Analysis Results
```

## Installation

Clone the repository:

```bash
git clone https://github.com/Abinaya767/NLP-Text-Insight-Analyzer.git
```

Go to the project folder:

```bash
cd NLP-Text-Insight-Analyzer
```

Install the required packages:

```bash
pip install -r requirements.txt
```

Download the spaCy English model:

```bash
python -m spacy download en_core_web_sm
```

## Run the Application

```bash
streamlit run app.py
```

The application will open in your browser.

## Project Structure

```text
NLP-Text-Insight-Analyzer/
|
├── app.py
├── nlp_processor.py
├── requirements.txt
└── README.md
```

## Project Objective

The objective of this project is to demonstrate how Natural Language Processing techniques can be used to analyze unstructured text and extract meaningful information.

## Author

**Abinaya S**
