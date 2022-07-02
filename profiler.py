try:
    from googlesearch import search
except ImportError:
    print("no google module detected")

print(" _____ _            ____             __ _ _              ___   _")
print("|_   _| |__   ___  |  _ \ _ __ ___  / _(_) | ___ _ __   / _ \ / |")
print("  | | | '_ \ / _ \ | |_) | '__/ _ \| |_| | |/ _ \ '__| | | | || |")
print("  | | | | | |  __/ |  __/| | | (_) |  _| | |  __/ |    | |_| || |")
print("  |_| |_| |_|\___| |_|   |_|  \___/|_| |_|_|\___|_|     \___(_)_|")
def repeat():
    print("1.google search")
    print("2.help")
    print("00.exit")
    print("insert number:")
    pick = input()
    if pick == "1":
        print("insert keyword")
        query = input()
        print("the last result to retrieve. keep blank to keep searching forever.")
        searchtotal = input()
        if searchtotal == '':
            searchtotal = '0'
        print(query)
        for j in search(query,num=int(searchtotal), pause=3):
            print(j)
    if pick == "2":
        print("use site: in the query to search in spesific site")
        print("use inurl to search spesific thing inside of the url")
        print('Enter " in the beginning and end for spesific keyword order')
        print('example: <"admin" site:microsoft.com inurl:guide filetype:pdf>')
    if pick == "00":
        print("Good bye")
        exit()

while True:
    repeat()
