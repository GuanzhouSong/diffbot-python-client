from client import DiffbotClient, DiffbotCrawl
from config import API_TOKEN
import pprint
import time
import json


def main():
    diffbot = DiffbotClient()
    token = API_TOKEN
    url = "https://newtonfreelibrary.libcal.com/event/4924168"
    api = "product"
    response = diffbot.request(url, token, api)
    print response
    print type(response)
    print response["objects"][0]["title"]


if __name__ == '__main__':
    main()
