from fastapi import FastAPI
from agents.data_analysis_agent import DataAnalysisAgent

app = FastAPI(title="Agentic PM Prototype API")

# Instantiate worker agent
analysis_agent = DataAnalysisAgent()

@app.get("/")
def read_root():
    return {"status": "ok", "message": "Agentic PM prototype running"}

@app.get("/analyze-latest")
def analyze_latest():
    result = analysis_agent.analyze_latest()
    return result
