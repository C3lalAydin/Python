import feedparser


def hava():
    parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|07060|ANTALYA|")
    parse = parse["entries"][0]["summary"]
    parse = parse.split()
    print (parse[4], parse[5])
    return (hava)
