import asyncio
import os
import sys

def get_application_root():
    """Get the application root directory whether running as script or frozen executable"""
    if getattr(sys, 'frozen', False):
        # Running as compiled executable
        return os.path.dirname(sys.executable)
    else:
        # Running as script
        return os.path.dirname(os.path.abspath(__file__))

# Add the application root directory to Python path
application_root = get_application_root()
sys.path.append(application_root)

from storage.database import Database
from collectors.appData_collector import appData_collector
# from src.collectors.browser_collector import browser_collector
from collectors.technology_collector import technology_collector
from api.routes import app
import uvicorn

async def main():
    db = Database()
    tasks = [
        # browser_collector(db)-
        appData_collector(db),
        technology_collector(db)
    ]
    await asyncio.gather(*tasks)

if __name__ == "__main__":
    import multiprocessing  

    def run_api():
        uvicorn.run(app, host="0.0.0.0", port=8000)

    api_process = multiprocessing.Process(target=run_api)
    api_process.start()

    asyncio.run(main())
    api_process.terminate()
