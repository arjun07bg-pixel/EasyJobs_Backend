from fastapi import FastAPI
from database.database import Base, engine
from routers import users, companies, posts, jobs, applications

app = FastAPI(title="EasyJobs Backend API")

# Attempt to create DB tables on startup. Log and continue if DB is unavailable
# to avoid crashing the application on import when DB credentials are misconfigured.
@app.on_event("startup")
async def startup_event():
    try:
        Base.metadata.create_all(bind=engine)
    except Exception as e:
        import logging
        logging.exception("Could not create database tables on startup: %s", e)

app.include_router(users.router)
app.include_router(companies.router)
app.include_router(posts.router)
app.include_router(jobs.router)
app.include_router(applications.router)


from routers import users, admins, companies, posts, jobs, applications

app.include_router(admins.router)





