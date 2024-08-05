from fastapi import Depends, FastAPI 

app = FastAPI(
    title=" app DX application",
    description="This app allows you to manage orders, supplements, inventory, and vending machines.",
)



if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
