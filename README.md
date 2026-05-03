# EduGen — AI Study Builder

EduGen is a sleek AI-powered web application that transforms any topic into interactive study materials. Simply enter a subject and choose a format — Quiz, Flashcards, Study Guide, or Essay Outline — and EduGen instantly generates structured learning content using OpenAI.

The backend is built with Flask and integrates Respan as an LLM gateway to route, monitor, and track AI requests. This allows the project to observe prompt behavior, generated outputs, and request activity across different study material formats.

The frontend features a modern, glassmorphism-inspired design with animated interactions.

## ✨ Features

🔹 Multiple study formats — Quizzes, Flashcards, Study Guides, and Essay Outlines.

🔹 OpenAI-powered generation — Creates structured learning content from any user-entered topic.

🔹 Respan integration — Routes and monitors LLM requests through Respan for AI observability.

🔹 Interactive quizzes — Animated correct/incorrect feedback, keyboard shortcuts (A/B/C/D, arrows, Enter).

🔹 Flip-style flashcards — Click to reveal answers.

🔹 Modern UI — Gradient background, glassmorphism cards, and smooth animations.

🔹 Secure key management — API keys stored in `.env`, never in source code.

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/rishabsanjay/EduGen.git
cd EduGen
