import requests
from requests import get
from bs4 import BeautifulSoup
import pandas as pd

import os
from pprint import pprint 

url = "https://codeup.com/blog/"
headers = {'User-Agent': 'Codeup Data Science'}
response = get(url, headers = headers)
soup = BeautifulSoup(response.content, 'html.parser')
more_links = soup.find_all('a', class_="more-link")
links_list = [link['href'] for link in more_links]
response = get(links_list[3], headers = headers)
title = soup.find('h1')

headers = {'User-Agent': 'Codeup Data Science'}

#follow format
def get_all_articles(url):
    article_list = []
    headers = {"User-Agent": "Chrome/91.0.4472.124"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    # Extract the href attribute from <a> tags with class 'more-link'
    links = soup.find_all('a', class_='more-link')
    link_list = [link['href'] for link in links]
    for link in link_list:
        response = requests.get(link, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1', class_='entry-title').text
        divcont = soup.find('div', class_='entry-content')
        article = [para.text for para in divcont.find_all('p')]
        article_nl = ' '.join(article)
        article_dict = {'title': title, 'content': article_nl}
        article_list.append(article_dict)
        #turn into a dataframe withing get code
    codeup_df = pd.DataFrame(article_list)
    return codeup_df

def get_blog_articles(article_info):
    """
    
    """
    file = "blog_posts.json"
    
    if os.path.exists(file):
        with open(file) as f:
            return json.load(f)
        
    headers = {'User-Agent': 'Codeup Data Science'}

    for article in article_info:
        response = get(article, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')

        info_dict = {
            "title": soup.find("h1").text,
            "link": article,
            "date_published": soup.find('span', class_="published").text,
            "content": soup.find('div', class_="entry-content").text
        }
        article_info.append(info_dict)
    
    with open(file, "w") as f:
        json.dump(article_info, f)
    
    return article_info





def get_articles(article_list):
    """
    
    """
    file = "blog_posts.json"
    
    if os.path.exists(file):
        with open(file) as f:
            return json.load(f)
        
    
    headers = {'User-Agent': 'Codeup Data Science'}
    article_info = []

    for article in article_list:
        response = get(article, headers=headers)

        soup = BeautifulSoup(response.content, 'html.parser')

        info_dict = {"title":soup.find("h1").text,
                    "link": article,
                    "date_published":soup.find('span', class_="published").text,
                    "content": soup.find('div', class_="entry-content").text}
        article_info.append(info_dict)
    
    with open(file, "w") as f:
        json.dump(article_info, f)
    return article_info

"""def get_blog_articles(url):
    headers = {"User-Agent": "Chrome/109.0.0.0"}
    response = get(url, headers=headers)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.find('h1').text if soup.find('h1') else None
        content = [p.text for p in soup.find_all('p')]
        
        return title, content
    else:
        return None, None

url_list = [
    'https://codeup.com/featured/women-in-tech-panelist-spotlight/',
    'https://codeup.com/featured/women-in-tech-rachel-robbins-mayhill/',
    'https://codeup.com/codeup-news/women-in-tech-panelist-spotlight-sarah-mellor/',
    'https://codeup.com/featured/apida-heritage-month/',
    'https://codeup.com/codeup-news/panelist-spotlight-4/'
]

for url in url_list:
    title, content = get_blog_articles(url)
    
    if title and content:
        print('Title:', title)
        print('Content:', content)
        print('---')
    else:
        print('Failed to retrieve title and content from the blog article.')"""
