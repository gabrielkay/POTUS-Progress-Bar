import requests
import tweepy
import datetime

consumer_key = "1N6H8rNDBpESzRbkMVvAmN2dT"
consumer_secret = "uSLriaRH22X1CmpCJ0wKj1NWpGLqKQTvBd5n2LNDPl0XWB6qoT"
access_token = "1087484913685880832-kuaM1ZHiwGfsgqtIYAY6T2zOLQJ6hr"
access_token_secret = "RQTmLaFXoY8VkgAFD9N33hRUR7OrX7aqgaX3SHl1MuABR"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    inaug = datetime.date(2017, 1, 20)
    today = datetime.date.today()
    diff = today - inaug
    numDiff = diff.days
    yesterDiff = numDiff - 1 #will break on inaugeration day
    delta1 = numDiff / 1461
    delta2 = numDiff / 1461
    p1 = float(delta1)
    p2 = float(delta2)
    per1 = int(p1 * 100)
    per2 = int(p2 * 100)
    if per1 != per2:
        numXs = per1 // 4
        numSpaces = 25 - numXs
        c = "[" + ("x" * numXs) + ("_" * numSpaces) + "]"
        tweetString = "The president's term is " + str(per1) + "% complete\n" + c
        api.update_status(tweetString)


if __name__ == "__main__":
    main()
