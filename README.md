# msc-virtual-agent

Starter backend for the Murrindindi Shire Council public website chatbot.
Built with FastAPI, containerised for Azure App Service.

## What's here

- `app/main.py` — the API. `/health` for uptime checks, `/chat` for the chatbot
  (currently a placeholder echo — replace with a real Azure OpenAI / AI Foundry call).
- `Dockerfile` — builds and runs the app on port 8000, matching Azure App Service
  for Linux container conventions.
- `requirements.txt` — Python dependencies.

## Run it locally (optional, needs Docker Desktop)

```
docker build -t msc-virtual-agent .
docker run -p 8000:8000 msc-virtual-agent
```

Then visit http://localhost:8000

## Push to GitHub

From inside this folder in Git Bash:

```
git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/Rravary71/msc-virtual-agent.git
git push -u origin main
```

## Next steps

- Wire `/chat` up to Azure OpenAI or Azure AI Foundry
- Add the site-scraping/indexing logic
- Add voice/speech support
- Point Azure App Service's Deployment Center at this repo (GitHub Actions build)
