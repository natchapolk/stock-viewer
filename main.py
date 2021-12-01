from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
app = FastAPI()
@app.get("/")
async def getIndex():
	return RedirectResponse("index.html")
app.mount("/", StaticFiles(directory="web"), name="web")