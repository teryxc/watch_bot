#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 20, 2018

@author: teryx
'''
import scraper
from bs4 import BeautifulSoup
import json
import requests
import common

logger = common.get_logger(__name__)

def main():
    req = scraper.SESSION.post('https://www.furaffinity.net/msg/others/',cookies=scraper.COOKIE)
    get_journals_json(req)

def get_journals_json(req):
    
    logger.info('Parsing Control Panel page for Journals.')
    soup = BeautifulSoup(req.content, 'lxml', from_encoding='utf-8')
    journal_ul = soup.find_all(id='journals')[1]
    journal_li_array = journal_ul.find_all('li')[:-1]
    journals_list = []
    for i in range(len(journal_li_array)):
        journal_li = journal_li_array[i]
        journal = {}
        
        journal['id'] = journal_li.find('input')['value']
        journal['user'] = journal_li.find_all('a')[1].string
        journal['title'] = journal_li.find('a').string
        journal['date'] = journal_li.find('span').string[3:]
        journals_list.append(journal)
        
        logger.debug('journal_li[{}]: {}'.format(i, journal_li_array[i]))
        logger.debug('journal json: {}'.format(journal))
        
    logger.info('Journals extracted - {}'.format(journals_list))
    
if __name__ == '__main__':
    main()