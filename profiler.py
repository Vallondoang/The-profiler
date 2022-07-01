try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
    print("type <pip install google>")

def reset():
    print("The Profiler 0.1")
    print("pick tools:")
    print("1.google database search")
    print("2.in depth google database search")
    print("00.exit")
    inputcommand = input()
    if inputcommand == "2":
        print("insert keyword")
        keyword = '"' + input() + '"'
        print("insert spesific site")
        print("leave blank if you dont use it")
        insiteword = input()
        insite = "site:" + insiteword
        print("insert what are you looking for in the site")
        print("leave blank if you dont use it")
        inurlword = input()
        inurl = "inurl:" + inurlword
        query = keyword + " " + insite + " " + inurl

        print(query)

        for j in search (query ,tld="co.in", num=20,stop=20 , pause=2):
            print(j)
        
    if inputcommand == "1":
        print("insert keyword")
        print("dont forget to add quotation mark in the sentences for spesific result")
        query = '"' + input() + '"'
 
        print(query)
        for j in search(query, tld="co.in", num=20,stop=20 , pause=2):
            print(j)

    if inputcommand == "00":
        print("good luck")
        exit()
while True:
    reset()
