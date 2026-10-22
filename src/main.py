from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi.middleware.cors import CORSMiddleware

import config
import utils

templates = Jinja2Templates(directory="static")

desc = """
Download API
"""

app = FastAPI(
        title="DL-api",
        description=desc,
        docs_url=None,    # 關閉 Swagger UI (預設路徑為 /docs)
        redoc_url=None,   # 關閉 ReDoc (預設路徑為 /redoc)
        openapi_url=None  # 徹底關閉 OpenAPI 結構描述 (預設路徑為 /openapi.json)
    )

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],     # 允許所有網域跨域請求
    allow_credentials=False, # 當 origins 為 "*" 時，此項必須為 False
    allow_methods=["*"],     # 允許所有 HTTP 方法 (GET, POST, OPTIONS 等)
    allow_headers=["*"],     # 允許所有 HTTP 標頭
)

app.mount("/assets", StaticFiles(directory="static/assets"), name="assets")
app.mount("/images", StaticFiles(directory="static/images"), name="images")
app.mount("/download", StaticFiles(directory=config.F_FILE_DIR_PATH), name="download")

@app.get("/")
def get_root(request: Request):
    '''
    預設頁面
    '''
    file_list = utils.get_file_names(config.F_FILE_DIR_PATH)
    file_latest = file_list[0] if file_list else ""
    context = {
        "title": config.F_TITLE,
        "files": file_list,
        "latest": file_latest,
        "desc": config.F_DESC
    }
    return templates.TemplateResponse(request, "index.html.j2", context)

@app.get("/latest")
def get_latest(request: Request):
    '''
    下載最新檔案
    '''
    file_latest = utils.get_latest_file(config.F_FILE_DIR_PATH)
    if not file_latest:
        raise HTTPException(status_code=404, detail="目前沒有任何檔案")
    return FileResponse(path=file_latest, filename=file_latest.name)