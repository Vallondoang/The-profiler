try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")

def reset():
    print("The Profiler 0.1")
    print("pick tools:")
    print("1.google dorking")
    print("00.exit")
    inputcommand = input()
    if inputcommand == "1":
        print("insert keyword")
        print("dont forget to add quotation mark in the sentences")
        query = input()
 
        for j in search(query, tld="co.in", num=10, stop=10, pause=2):
            print(j)
        

    if inputcommand == "00":
        print("good luck")
        exit()
while True:
    reset()