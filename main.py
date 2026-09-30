from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from explanation_module import explain_topic
from qna import answer_question
from quiz_module import generate_quiz
from summary_module import summarize_text
from learning_path import get_learning_recommendations

app = FastAPI(title="EduGenie - Google Gemini Powered Learning Assistant")
templates = Jinja2Templates(directory="templates")


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})


@app.post("/process", response_class=HTMLResponse)
async def process(
    request: Request,
    task: str = Form(...),
    text: str = Form(...)
):
    text = text.strip()

    if not text:
        result = "Please enter some text."
    elif task == "explain":
        result = explain_topic(text)
    elif task == "qa":
        result = answer_question(text)
    elif task == "quiz":
        result = generate_quiz(text)
    elif task == "summarize":
        result = summarize_text(text)
    elif task == "learn":
        result = get_learning_recommendations(text)
    else:
        result = "Invalid task selected."

    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result}
    )


@app.post("/qa")
async def qa_api(text: str = Form(...)):
    return {"answer": answer_question(text)}


@app.post("/explain")
async def explain_api(text: str = Form(...)):
    return {"explanation": explain_topic(text)}


@app.post("/quiz")
async def quiz_api(text: str = Form(...)):
    return generate_quiz(text)


@app.post("/summarize")
async def summarize_api(text: str = Form(...)):
    return {"summary": summarize_text(text)}


@app.post("/learn/recommendations")
async def learning_api(text: str = Form(...)):
    return {"recommendations": get_learning_recommendations(text)}
