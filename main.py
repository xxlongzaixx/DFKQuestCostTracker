from fastapi import FastAPI
import uvicorn
import src.dfk as dfk

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/api/v1/quest-cost-breakeven")
async def get_quest_cost_breakeven():
    costs = await dfk.get_quest_cost_breakeven()
    return costs


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
