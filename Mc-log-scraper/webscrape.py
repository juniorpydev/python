import requests, random, string, datetime, os
# Import
def make_log(data): # Making log for save 
    now = datetime.datetime.now().strftime("%Y-%m-%d-%H:%M")
    log_dir = os.path.join(os.getcwd(), 'logs', datetime.datetime.now().strftime('%Y-%m-%d-%H-%M'))
    try:
        os.makedirs(log_dir, exist_ok=True)
    except FileExistsError:
        print(f"Directory {log_dir} already exists.")
    
    with open(os.path.join(log_dir, "log.txt"), "a") as file:
        file.write(f"{data}\n")
def generate(leng): # Generating 7 letter string for scrape
    res = ""
    letters1 = string.ascii_lowercase
    letters2 = string.ascii_uppercase
    letters = letters1 + letters2
    for _ in range(leng):
        x = random.choice(letters)
        res = res + x
    return res

def scrape_text(site): # Simple Scrape here
    r = requests.Session() 
    scraped = r.get(site)
    if "Log not found" in scraped.text:
        return "[] Log Not Found"
    else:
        return scraped.text