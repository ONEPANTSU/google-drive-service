import os
from shutil import copyfileobj

from fastapi import APIRouter, FastAPI, UploadFile, Request
from starlette import status
from starlette.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse

from config import ORIGINS, ALLOWED_HOSTS
from directories import Directory
from google_drive import Driver

app = FastAPI(title="Education Tour Files (Google Drive Service)")


app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["GET", "POST", "OPTIONS", "DELETE", "PATCH", "PUT"],
    allow_headers=[
        "Content-Type",
        "Set-Cookie",
        "Access-Control-Allow-Headers",
        "Access-Control-Allow-Origin",
        "Authorization",
    ],
)

router = APIRouter(prefix="/app/v1/images", tags=["image"])

google_driver = Driver()


@router.post("/upload")
def upload_image(image: UploadFile, directory: Directory):
    with open("temp/" + image.filename, "wb") as file:
        copyfileobj(image.file, file)
    result = google_driver.upload_file(filename=image.filename, directory=directory)
    os.remove("temp/" + image.filename)
    return result


@router.delete("/delete_by_id")
def delete_image_by_id(image_id: str, directory: Directory):
    return google_driver.delete_file_by_id(file_id=image_id, directory=directory)


@router.delete("/delete_by_name", )
def delete_image_by_name(image_name: str, directory: Directory):
    return google_driver.delete_file(filename=image_name, directory=directory)


app.include_router(router)


@app.middleware("http")
async def add_ip_checker(request: Request, call_next):
    ip = str(request.client.host)
    if ip not in ALLOWED_HOSTS:
        return JSONResponse(
            status_code=status.HTTP_403_FORBIDDEN, content={"status": "403 Access Denied"}
        )
    else:
        return await call_next(request)
