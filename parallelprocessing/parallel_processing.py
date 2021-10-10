"""
This file downloads a month's worth of reports (pages 1-100 per day for one site) from the Highways England to demostrate using asyncio in python
I chose asyncio over multiprocessing as most of the time is spent on waiting for the io requests not on cup intensive processing.
Threads would also have been a option but asyncio using async await seemed the simplet way to implement making multiple requests un python in a way that was familiar to async await with promises in node.js 
It also seemed much easier to make async loops for each day and page compared to threads with Semaphore acting as a limit on concurrent api calls
"""
from aiohttp import ClientSession
import aiofiles
import asyncio


REPORT_API = "https://webtris.highwaysengland.co.uk/api/v1/reports/{start}/to/{end}/Monthly"

async def store_report(file, json: str):
    """Writes the json reports to a file."""
    await file.write(json)

async def download_report(sem: asyncio.Semaphore, session: ClientSession, start: str, end:str, site:str, page:str, page_size:str):#
    """Calls the api to download a report and returns the json if a valid response is returned, else None."""
    url = REPORT_API.format(start=start, end=end)
    query = {"sites":site, "page":page, "page_size":page_size}
     
    async with sem:
        async with session.get(url, params=query) as response:
            if response.status == 200:
                return str(response.json)
            else:
                return None

async def download_and_store_reports(sem: asyncio.Semaphore, session: ClientSession, file, start: str, end:str, site:str, page:str, page_size:str):
    """Downloads the report json and stored them if there is a result."""
    result_json = await download_report(sem, session, start, end, site, page, page_size)
    if result_json != None:
        await store_report(file, result_json)

async def dowload_reports_for_day(sem: asyncio.Semaphore, session: ClientSession, file, date: str, site: str):
    """Downloads pages 1 to 100 for all reports for given day."""
    page_size = 10
    for page in range(1, 100):
        await download_and_store_reports(sem, session, file, date, date,  site, str(page), page_size)

async def main():
    """Download a months for of reports for a specific site."""
    max_concurrent = 10
    sem = asyncio.Semaphore(max_concurrent) # limit how many api requests can happen at once
    site = "2"

    print("Downloading report data to output.txt")
    async with ClientSession() as session:
        async with aiofiles.open("output.txt", mode="a") as file:
            for day in range(1,31):
                dateStr = f"{day:02d}082021"
                await dowload_reports_for_day(sem, session, file, dateStr, site)
    print("Download complete")

asyncio.run(main())
