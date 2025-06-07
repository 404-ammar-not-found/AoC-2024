import requests 
import os 

def download_input(day: int) -> bytes:
    URL = f"https://adventofcode.com/2024/day/{day}/input"
    #Reads in the auth key required to get input data
    with open(".session","r") as f:
        session =f.read().strip()
    #Reads in the auth key required to get input data
    cookies = {"session" :  session}
    
    resp = requests.get(url=URL,
                       cookies=cookies)
    
    return resp.content 

def setup_day(day: int) -> None :
    origin_dir = os.getcwd()  
    dir_name = f"Day_{day:02}"
    TEMPLATE = f"""with open("Day_{day:02}/data.txt") as f:
    lines = f.readlines()

def part_1():
        pass
def part_2():
        pass
    """

    os.mkdir(dir_name)

    data = download_input(day=day).decode()

    os.chdir(dir_name)

    with open("solution.py","w") as f:
        f.write(TEMPLATE)
    with open("data.txt","w") as f:
        f.write(data)

    os.chdir(origin_dir)


for day in range(1,26):
    setup_day(day=day)