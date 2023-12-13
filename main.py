from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/dfk/getQuestCost")
async def getQuestCost():
    costs = {"cv_fishing": 8, "cv_foraging": 9, "cv_mining": 4}
    return costs


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)