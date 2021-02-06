# returns the first link in a google search
def googleSearch(query):
    try:
        from googlesearch import search
    except ImportError:
        print("No module named 'google' found")

    for result in search(query, tld="com", num=1, stop=1, pause=2):
        return result
