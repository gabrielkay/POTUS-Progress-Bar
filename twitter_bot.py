import tweepy
import datetime

consumer_key = CKEY
consumer_secret = CKEYSECRET
access_token = AT
access_token_secret = ATSECRET


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def main():
    inaug = datetime.date(2017, 1, 20)
    today = datetime.date.today()
    diff = today - inaug
    numDiff = float(diff.days)
    yesterDiff = float(numDiff - 1) #will break on inaugeration day
    delta1 = numDiff / 1461
    delta2 = yesterDiff / 1461
    per1 = int(delta1 * 100)
    per2 = int(delta2 * 100)
    print("Yesterday: ")
    print(per2)
    print("Today: ")
    print(per1)
    if per1 != per2:
        numXs = per1 // 4
        numSpaces = 25 - numXs
        c = "[" + ("x" * numXs) + ("_" * numSpaces) + "]"
        tweetString = "The president's term is " + str(per1) + "% complete\n" + c
        api.update_status(tweetString)


if __name__ == "__main__":
    main()
