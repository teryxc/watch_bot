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
import pandas as pd

import common
import db
import db.setup as db_setup

logger = common.get_logger(__name__)

def main():
    
    journals_df = get_from_control_panel()
    common.dump_df(logger.info, journals_df, 'journals_df')
    
    db_setup.write_df('journals', journals_df)

def get_from_control_panel():
    
    req = scraper.SESSION.post(common.CONTROL_PANEL_URL,cookies=scraper.COOKIE)
    
    logger.info('Parsing Control Panel page for Journals.')
    soup = BeautifulSoup(req.content, 'lxml', from_encoding='utf-8')
    journal_ul = soup.find_all(id='journals')[1]
    journal_li_array = journal_ul.find_all('li')[:-1]
    
    journals_list = []
    journals_df = pd.DataFrame(columns={'id', 'user', 'title', 'date'})
    
    for i in range(len(journal_li_array)):
        journal_li = journal_li_array[i]
        journal = {}
        
        journal['id'] = journal_li.find('input')['value']
        journal['user'] = journal_li.find_all('a')[1].string
        journal['title'] = journal_li.find('a').string
        journal['date'] = journal_li.find('span').string[3:] #TODO: convert to number
        
        journals_list.append(journal)
        journals_df = journals_df.append(journal, ignore_index=True)
        
        logger.debug('journal_li[{}]: {}'.format(i, journal_li_array[i]))
        logger.debug('journal json: {}'.format(journal))
        
    logger.info('Journals extracted - {}'.format(journals_list))
    return journals_df
    
if __name__ == '__main__':
    main()