
import requests

subreddits = ['ama', 'aww', 'news', 'worldnews', 'politics', 'todayilearned', 'explainlikeimfive', 'writingprompts',
              'upliftingnews', 'wholesomememes', 'freecompliments', 'happy', 'financialadvice', 'breadit']


def getRedditStories(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}.json'
    myheaders = {'User-Agent': 'ist256.lesson10.homework:v1.0 (by /u/edjose)'}
    response = requests.get(url, headers=myheaders)
    response.raise_for_status()
    data = response.json()
    return data


def extractTitles(stories):
    titles = ''
    for story in stories['data']['children']:
        titles = titles + story['data']['title'] + '\n'
    return titles


def getSentiment(text):
    url = 'http://text-processing.com/api/sentiment/'
    payload = {'text': f'{text}'}
    response = requests.post(url, data=payload)
    sentiment = response.json()
    return sentiment


def main(subreddit):
    stories = getRedditStories(subreddit)
    titles = extractTitles(stories)
    sentiment = getSentiment(titles)
    print(titles)
    print(sentiment)
    print(f"Overall sentiment of subreddit {subreddit} is {sentiment['label']}")


main('News')


