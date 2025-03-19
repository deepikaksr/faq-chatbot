# Aadhaar FAQ Chatbot

A simple chatbot that answers Aadhaar-related frequently asked questions using Natural Language Processing (NLP). Built with Flask and scikit-learn.

## Features
- Uses Aadhaar FAQ dataset for accurate responses
- Web-based interface with an interactive chatbox
- NLP-based question matching using TF-IDF and cosine similarity
- Simple and easy-to-use UI

## Project Structure

- **Aadhar_Faq.txt** - Dataset file contains FAQ
- **app.py** - Main backend script
- **templates/index.html** - Web interface
- **README.md** - Project documentation

## Installation

1. Clone the repository:
git clone https://github.com/deepikaksr/faq-chatbot.git cd faq-chatbot

2. Install dependencies: pip install flask scikit-learn

## Usage

Run the chatbot : python3 app.py
Open in a browser : http://localhost:5000

## How It Works
1. User enters an Aadhaar-related question.
2. The chatbot finds the most similar question from the dataset using NLP.
3. It returns the best-matching answer.
4. If no match is found, it suggests visiting the official UIDAI website.
