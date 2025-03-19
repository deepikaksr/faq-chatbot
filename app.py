from flask import Flask, request, jsonify, render_template
import json
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

app = Flask(__name__)

# Load Aadhaar FAQ dataset
with open('Aadhar_Faq.txt', 'r', encoding='utf-8') as f:
    faqs = json.load(f)

questions = [item['question'] for item in faqs]
answers = [item['answer'] for item in faqs]

# Vectorize the questions
vectorizer = TfidfVectorizer()
question_vectors = vectorizer.fit_transform(questions)

def get_answer(user_question):
    """Find the most relevant answer using cosine similarity."""
    user_vec = vectorizer.transform([user_question])
    similarity = cosine_similarity(user_vec, question_vectors)
    max_sim_index = similarity.argmax()
    if similarity[0, max_sim_index] > 0.3:  # Adjust threshold if needed
        return answers[max_sim_index]
    else:
        return "Sorry, I don't have an answer for that. Please visit the official UIDAI website."

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    user_question = data.get('question')
    answer = get_answer(user_question)
    return jsonify({"answer": answer})

if __name__ == "__main__":
    app.run(debug=True)
