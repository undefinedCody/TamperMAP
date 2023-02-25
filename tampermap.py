import argparse
import requests
import threading



print("""
  _______                                __  __          _____  
 |__   __|                              |  \/  |   /\   |  __ \ 
    | | __ _ _ __ ___  _ __   ___ _ __  | \  / |  /  \  | |__) |
    | |/ _` | '_ ` _ \| '_ \ / _ \ '__| | |\/| | / /\ \ |  ___/ 
    | | (_| | | | | | | |_) |  __/ |    | |  | |/ ____ \| |     
    |_|\__,_|_| |_| |_| .__/ \___|_|    |_|  |_/_/    \_\_|     
                      | |                                       
                      |_|                   \033[0;31mversion: 0.1
        \033[1;33mhttps://github.com/undefinedcody/TamperMAP\033[0m
""")
firstTime = True

def check_url(url, verb, ignore_ssl, showHttpCodes, hideHttpCodes, save):
    global firstTime
    try:
        response = requests.request(verb, url, timeout=5, verify=not ignore_ssl)
        size = len(response.content)
        color = "\033[32m\033[1m" if response.status_code == 200 else ("\033[1;30m" if response.status_code == 404 or response.status_code == 405 else "\033[33m")
        #result = f"{color}[{verb}] {url} - {response.status_code} ({size} bytes)\033[0m"
        result = f"{color}[{verb}] => Status Code: {response.status_code}  -  Size: {size} bytes\033[0m"
        resultPrint = f"[{verb}] => Status Code: {response.status_code}  -  Size: {size} bytes"
        if (not showHttpCodes or response.status_code in showHttpCodes) and (not hideHttpCodes or response.status_code not in hideHttpCodes):
            if firstTime:
                print("")
                print(f"[*]Initializing the service...\n\033[1m[*] Starting to test the url:  {url}\n \033[0m")
            print(result)
            if save:
                with open("result.txt", "a") as f:
                    if firstTime:
                        f.write(f"\n------------\nTamperMAP's Test result for: {url}\n\n")
                    f.write(f"{resultPrint}\n")
            firstTime = False        
    except Exception as err:
        print(f"\033[33m[{verb}] {url} - Error: {err.message}\033[0m")


def __main__():
    parser = argparse.ArgumentParser(description="Check HTTP verbs for the given URL")

    parser.add_argument("-u", "--url", type=str, required=True, help="URL to check")
    parser.add_argument("-t", "--threads", type=int, default=5, help="Threads to use. Default=5")
    parser.add_argument("-i", "--ignore-ssl", action="store_true", help="Ignore SSL errors")
    parser.add_argument("--save", action="store_true", help="Save the result to a file named result.txt")

    groupShowHide = parser.add_mutually_exclusive_group()
    groupShowHide.add_argument("-s", "--show", type=str, help="Only show results that match the specified HTTP status code(s) (comma-separated)")
    groupShowHide.add_argument("-x", "--hide", type=str, help="Hide results that match the specified HTTP status code(s) (comma-separated)")

    groupAllMain = parser.add_mutually_exclusive_group()
    groupAllMain.add_argument("--all", action="store_true", help="Test the 9 common HTTP methods. DEFAULT")
    groupAllMain.add_argument("--main", action="store_true", default=True, help="Only test the 9 main HTTP methods")
    args = parser.parse_args()

    url = args.url
    verbs = ["GET", "HEAD", "POST", "PUT", "DELETE", "CONNECT", "OPTIONS", "TRACE", "PATCH"]
    if args.all:
        verbs = ["ACL", "BASELINE-CONTROL", "BIND", "CHEKIN", "CHECKOUT", "CONNECT", "COPY", "DELETE", "GET", "HEAD", "LABEL", "LINK", "LOCK", "MERGE", "MKACTIVITY", "MKCALENDAR", "MKCOL", "MKREDIRECTREF", "MKWORKSPACE", "MOVE", "OPTIONS", "ORDERPATH", "PATCH", "POST", "PRI", "PROPFIND", "PROPPATCH", "PUT", "REBIND", "REPORT", "SEARCH", "TRACE", "UNBIND", "UNCHECKOUT", "UNLINK", "UNLOCK", "UPDATE", "UPDATEREDIRECTREF", "VERSION-CONTROL", "GIBBERISH", ""]
    elif not args.main:
        verbs = args.main.split(",")
    threads = []

    showHttpCodes = None
    if args.show:
        showHttpCodes = set(map(int, args.show.split(",")))

    hideHttpCodes = None
    if args.hide:
        hideHttpCodes = set(map(int, args.hide.split(",")))

    for verb in verbs:
        t = threading.Thread(target=check_url, args=(url, verb, args.ignore_ssl, showHttpCodes, hideHttpCodes, args.save))
        threads.append(t)

    for i in range(0, len(threads), args.threads):
        batch = threads[i:i+args.threads]
        for t in batch:
            t.start()

        for t in batch:
            t.join()

__main__()
