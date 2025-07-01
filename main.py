from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routers import signupRouter,loginRouter,promptRouter,historyRouter

app = FastAPI()

# Allow CORS from React frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # or use ["*"] for all origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": " Backend is running!"}

app.include_router(signupRouter.router)
app.include_router(loginRouter.router)
app.include_router(promptRouter.router)
app.include_router(historyRouter.router)
