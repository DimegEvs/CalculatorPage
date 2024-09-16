from fastapi import FastAPI


from src.pages.router import router as main_router
app = FastAPI()

app.include_router(main_router)