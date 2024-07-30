from threads_api.src.threads_api import ThreadsAPI  
import asyncio
from metathreads import MetaThreads  
from get_sheet import get_user_list  
import random  
import nest_asyncio
import json

nest_asyncio.apply()
data = json.load(open("config.json", encoding="utf-8")) 

ACCOUNT = data["ACCOUNT"]
PASSWORD = data["PASSWORD"]
SHEET = data["SHEET"]

print("正在獲取使用者資料...")
user_list = get_user_list(SHEET)

threads = MetaThreads()
threads.login(ACCOUNT, PASSWORD)

async def post():
    api = ThreadsAPI()
    
    await api.login(ACCOUNT, PASSWORD, cached_token_path=".token")
    print(f"成功登入 {ACCOUNT}，開始執行封鎖")

    for user_name in user_list:
        id = threads.get_user_id(user_name)
        try:
            await api.block_user(id)
            print(f"成功封鎖 {user_name}")
        except Exception as e:
            print(f"無法封鎖 {user_name}: {e}")
        await asyncio.sleep(random.randint(2, 5))
    print("封鎖完成")
    
    await api.close_gracefully()

async def main():
    await post()

asyncio.run(main())