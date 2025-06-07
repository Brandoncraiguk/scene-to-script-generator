# 🎬 Scene-to-Script Generator

Generate short screenplay scenes from a description using GPT-3.5 and Streamlit.

## 📌 Features

- Convert a simple scene description into a short film script
- Optional tone/style input (e.g. noir, surreal, romantic)
- Built with Python, Streamlit, and OpenAI's GPT-3.5 Turbo API
- Saves each script to a `.txt` file and provides a download button
- Clean web interface with custom styling

## 🛠 Tech Stack

- Python 3.11+
- OpenAI GPT-3.5 Turbo
- Streamlit
- dotenv

## 🚀 Getting Started

1. **Clone the repo or download the ZIP**
2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Create a `.env` file**

Duplicate `.env.example` and rename it to `.env`. Then add your OpenAI API key:

```
OPENAI_API_KEY=your-api-key-here
```

4. **Run the app**

```bash
streamlit run app.py
```

## 📁 Project Structure

```
scene-to-script/
├── app.py
├── .env.example
├── .gitignore
├── .streamlit/
│   └── config.toml
```

## 📝 License

This project is open source under the [MIT License](https://choosealicense.com/licenses/mit/).