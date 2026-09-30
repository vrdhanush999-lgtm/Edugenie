# EduGenie: Google Gemini Powered Learning Assistant

EduGenie is a FastAPI-based educational assistant implementing the modules described in the supplied project document:

- Question answering
- Simple concept explanation
- Quiz generation
- Text summarization
- Personalized learning recommendations

## Project structure

```text
EduGenie/
├── main.py
├── gemini_client.py
├── explanation_module.py
├── qna.py
├── quiz_module.py
├── summary_module.py
├── learning_path.py
├── templates/
│   └── index.html
├── static/
│   └── style.css
├── requirements.txt
└── .env.example
```

## Installation

Use Python 3.10+.

```bash
python -m venv venv
```

Windows:

```bash
venv\Scripts\activate
```

macOS/Linux:

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Set the Gemini API key.

Windows PowerShell:

```powershell
$env:GEMINI_API_KEY="YOUR_API_KEY"
```

macOS/Linux:

```bash
export GEMINI_API_KEY="YOUR_API_KEY"
```

## Run

```bash
uvicorn main:app --reload
```

Open:

```text
http://127.0.0.1:8000
```

The PDF specifies the same local run command and address. 

## Notes

The supplied PDF describes the architecture and functionality but does not contain the complete original source-code listings. This package is an implementation based on those specifications, not a claim that it is the exact original source code.
