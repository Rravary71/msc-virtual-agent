from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from pydantic import BaseModel

app = FastAPI(title="MSC Virtual Agent")

# Allow the council website (and local testing) to call this API from the browser.
# Tighten this list once you know the exact domain(s) the widget will be embedded on.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


class ChatRequest(BaseModel):
    message: str


class ChatResponse(BaseModel):
    reply: str


@app.get("/health")
def health():
    """Azure App Service / uptime checks hit this to confirm the container is alive."""
    return {"status": "ok"}


@app.get("/", response_class=HTMLResponse)
def root():
    return """
    <html>
        <head><title>MSC Virtual Agent</title></head>
        <body style="font-family: sans-serif; padding: 2rem;">
            <h2>MSC Virtual Agent is running</h2>
            <p>This is a placeholder page. The chatbot widget will call <code>/chat</code>.</p>
        </body>
    </html>
    """


@app.post("/chat", response_model=ChatResponse)
def chat(req: ChatRequest):
    """
    Placeholder chat logic. Replace this with a real call to your chosen LLM
    (Azure OpenAI, Azure AI Foundry, etc.) once you're ready to wire that in.
    """
    return ChatResponse(reply=f"You said: {req.message}. (Real AI logic goes here.)")
