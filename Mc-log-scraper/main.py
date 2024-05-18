import requests, threading, asyncio, sys
from pystyle import *
from webscrape import scrape_text, generate, make_log # Importing funcs
if __name__ == "__main__":
    def start():
        g = generate(7) # 7
        x = scrape_text(f"https://api.mclo.gs/1/raw/{g}") # You change here
        if x in "[] Log Not Found": # If log not found
            print(f"[] Log Not Found: {g}")
        else:
            print("I found a log!") # If log found
            make_log(x)
    async def main():
        tasks = []
        cCheck = 0
        for _ in range(999): # 999 Loop
            cCheck += 1
            thread = threading.Thread(target=start)
            thread.start()
            System.Title(f"Checked: {cCheck}")
        await asyncio.gather(*tasks)
    while 1:
        asyncio.run(main()) # Asncy with main for fast
        print("Checked") # Checked 999