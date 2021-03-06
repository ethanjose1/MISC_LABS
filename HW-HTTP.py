import requests


# retrieves data from a subreddit in the JSON format using a get request
def getRedditStories(subreddit):
    url = f'https://www.reddit.com/r/{subreddit}.json'
    myheaders = {'User-Agent': 'ist256.lesson10.homework:v1.0 (by /u/edjose)'}
    response = requests.get(url, headers=myheaders)
    response.raise_for_status()
    data = response.json()
    return data


# parses through reddit JSON data to retrieve subreddit titles in a list
def extractTitles(stories):
    titles = ''
    for story in stories['data']['children']:
        titles = titles + story['data']['title'] + '\n'
    return titles


# uses the text-processing api given some text to return a sentiment value as a JSON
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


main('python')
