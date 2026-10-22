from pathlib import Path

def get_latest_file(directory_str_path: str):
    directory = Path(directory_str_path)
    # 取得資料夾內所有的「檔案」（排除子資料夾）
    files = [f for f in directory.iterdir() if f.is_file()]
    
    if not files:
        return None  # 如果資料夾是空的，回傳 None
        
    # 透過檔案的修改時間 (st_mtime) 找出最新的一個檔案
    latest_file = max(files, key=lambda f: f.stat().st_mtime)
    return latest_file

def get_file_names(directory_str_path: str):
    download_dir = Path(directory_str_path)
    files = [f for f in download_dir.iterdir() if f.is_file()]

    # 2. 依照修改時間 (st_mtime) 排序，reverse=True 代表由新到舊
    sorted_files = sorted(files, key=lambda f: f.stat().st_mtime, reverse=True)

    # 3. 如果只要檔名列表，可以再轉換成字串
    return [f.name for f in sorted_files]
