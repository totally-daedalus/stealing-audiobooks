def printgreen(text):
    print("\033[1;32;40m" + text + "\033[0;37;40m")

def request(flow):
    url = flow.request.url.split('.') 
    host = "api.findawayworld.com"
    extension = "mp3"

    if url[len(url) - 1] == extension and flow.request.pretty_host == host:
        printgreen(flow.request.url)
