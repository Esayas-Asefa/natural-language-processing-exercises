def get_blog_articles(url):
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
        print('Failed to retrieve title and content from the blog article.')

        
def scrape_inshorts():
    url = 'https://inshorts.com/en/read'
    response = get(url, headers=headers)

    
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        
        articles = soup.find_all('div', class_='news-card')
        
        for article in articles:
            # Extract title
            title = article.find('span', itemprop='headline').text.strip()
            
            # Extract content
            content = article.find('div', itemprop='articleBody').text.strip()
            
            # Extract category
            category = article.find('a', class_='clickable').text.strip()
            
            # Print the extracted information
            print('Title:', title)
            print('Content:', content)
            print('Category:', category)
            print('---')
    else:
        print('Failed to retrieve data from the Inshorts website.')

scrape_inshorts()
"""In this example, we target the news-card class, which represents each news article on the Inshorts website. Inside the loop, we extract the title, content, and category by using appropriate CSS selectors and methods provided by BeautifulSoup.

Please note that web scraping can be subject to changes in website structure and terms of service. Make sure to review the website's terms of service before scraping and consider the website's policies on data usage and scraping.






Regenerate response"""
