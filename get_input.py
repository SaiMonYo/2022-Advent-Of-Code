import requests
import sys

if len(sys.argv) != 2:
    print('Wrong number of arguments')
    exit(0)

cookie = ""
day = int(sys.argv[1])
headers = {'User-Agent': "...",
    'session': cookie}
url = f'https://adventofcode.com/2022/day/{day}/input'

session = requests.Session()
resp = session.get(url,cookies=headers)
text = resp.text.rstrip("\n")
in_file = open(f'Day{day}.txt','w')
in_file.write(text)
in_file.close()
