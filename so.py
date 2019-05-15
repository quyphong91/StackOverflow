#!/usr/bin/env python3


import requests
import argparse
import json


def stack_over_flow(number, label):
    # get the data
    api_link_prefix = '''
    https://api.stackexchange.com/questions?order=desc&sort=votes
    '''
    site = 'site=stackoverflow'
    tag = 'tagged=' + str(label)
    num = 'pagesize=' + str(number)
    api_full_link = '&'.join([api_link_prefix, tag, num, site])
    resp = requests.get(api_full_link)
    data = json.loads(resp.text)

    # print the request
    data2 = data['items']
    index = 0

    for item in data2:
        index += 1
        item_title = item['title']
        item_score = item['score']
        item_url = item['link']
        print('Question number', index)
        print('Question title:', item_title)
        print('Question vote:', item_score)
        print('Link to question:', item_url)


def main():
    parser = argparse.ArgumentParser("Get number of post and label")
    parser.add_argument('number', type=str)
    parser.add_argument('label', type=str)
    input_data = parser.parse_args()
    stack_over_flow(input_data.number, input_data.label)


if __name__ == '__main__':
    main()
