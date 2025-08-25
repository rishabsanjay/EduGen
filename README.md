EduGen — AI Study Builder

EduGen is a sleek web application that transforms any topic into interactive study materials. Simply enter a subject and choose a format — Quiz, Flashcards, Study Guide, or Essay Outline — and EduGen instantly generates structured learning content powered by OpenAI.

The frontend features a modern, glassmorphism-inspired design with animated interactions, while the backend is built in Flask (Python).

✨ Features

🔹 Multiple study formats — Quizzes, Flashcards, Study Guides, and Outlines.

🔹 Interactive quizzes — animated correct/incorrect feedback, keyboard shortcuts (A/B/C/D, arrows, Enter).

🔹 Flip-style flashcards — click to reveal answers.

🔹 Modern UI — gradient background, glassmorphism cards, smooth animations.

🔹 Secure key management — API keys stored in .env, never in source code.

🖼️ Preview


(Replace with your own screenshot from the app)

🚀 Getting Started
1. Clone the repo
git clone https://github.com/rishabsanjay/EduGen.git
cd EduGen

2. Create a virtual environment
python3 -m venv .venv
source .venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Set up environment variables

Copy the example env file and add your OpenAI API Key:

cp .env.example .env


Edit .env to look like:

OPENAI_API_KEY=sk-your-new-key-here

5. Run the app
python app.py


Visit http://127.0.0.1:5000
 in your browser.

📂 Project Structure
EduGen/
│── app.py              # Flask backend
│── generator.py        # OpenAI content generation logic
│── requirements.txt    # Python dependencies
│── .env.example        # Example environment variables
│── templates/
│    └── index.html     # Frontend (HTML + TailwindCSS + JS)

🛡️ Security

.env is excluded via .gitignore to protect your API keys.

If a key is ever exposed, rotate it immediately in your OpenAI dashboard.
