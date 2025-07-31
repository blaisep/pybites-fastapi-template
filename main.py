from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.api_route("/", methods=["GET", "POST"], response_class=HTMLResponse)
def index(request: Request, input: str = Form(None)):
    if request.method == "GET":
        return templates.TemplateResponse("index.html", {"request": request})
    else:
        return templates.TemplateResponse("index.html", {"request": request, "input": input})
