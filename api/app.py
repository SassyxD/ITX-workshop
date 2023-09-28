import uvicorn


if __name__ == "__main__":
    uvicorn.run("src.p1:app", port=3000, reload=True)