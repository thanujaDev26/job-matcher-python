from fastapi import FastAPI, UploadFile, File, Depends, HTTPException
from parser.auth import verify_token
from parser.extract import extract_text_from_pdf
from parser.keywords import extract_keywords
import uvicorn

app = FastAPI()

@app.post("/parse-resume")
async def parse_resume(token: str = Depends(verify_token), file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    content = await file.read()
    text = extract_text_from_pdf(content)
    keywords = extract_keywords(text)

    return {
        "user": token,  
        "keywords": keywords,
        "summary": text[:300]  
    }

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
