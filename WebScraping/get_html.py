NUMBER_OF_SCROLLS = 1000

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd
import time
from tqdm import tqdm


def fetch_data(wd,URL):
    url = URL
    wd.get(url)

    posts = []

    last_height = -1000
    # Scroll to load more posts
    for _ in tqdm(range(NUMBER_OF_SCROLLS)):
        last_height = wd.execute_script("return document.body.scrollHeight")
        wd.find_element(By.TAG_NAME, 'body').send_keys(Keys.END)
        soup = BeautifulSoup(wd.page_source, 'html.parser')
        posts.append(soup.prettify())
        time.sleep(3)  # Wait for content to load
        if  wd.execute_script("return document.body.scrollHeight") == last_height:
            print("No more content to load.")
            break


    # Extract and parse the page
    soup = BeautifulSoup(wd.page_source, 'html.parser')

    def extract_posts2(html_list):
        posts = []
        for html_content in html_list:
            soup = BeautifulSoup(html_content, 'html.parser')
            
            articles = soup.find_all('article')
            
            for article in articles:
                try:
                    title_elem = article.find('a', {'id': lambda x: x and 'post-title' in x})
                    title = title_elem.get_text(strip=True) if title_elem else ''
                except Exception as e:
                    title = ''
                    print(f"Error extracting title: {e}")

                try:
                    author_elem = article.find('span', {'slot': 'authorName'})
                    author = author_elem.get_text(strip=True) if author_elem else ''
                except Exception as e:
                    author = ''
                    print(f"Error extracting author: {e}")

                try:
                    timestamp_elem = article.find('time')
                    timestamp = timestamp_elem.get('datetime', '') if timestamp_elem else ''
                except Exception as e:
                    timestamp = ''
                    print(f"Error extracting timestamp: {e}")

                # Extracting post body (description or preview)
                try:
                    description_elem = article.find('div', {'class': 'md feed-card-text-preview'})
                    description = ''
                    if description_elem:
                        paragraphs = description_elem.find_all('p')
                        description = '\n'.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
                except Exception as e:
                    description = ''
                    print(f"Error extracting description: {e}")

                # Extracting full body text (if available)
                try:
                    body_elem = article.find('a', {'slot': 'text-body'})
                    body_text = ''
                    if body_elem:
                        body_text = body_elem.get_text(separator='\n', strip=True)
                except Exception as e:
                    body_text = ''
                    print(f"Error extracting body text: {e}")

                if not body_text:
                    continue

                # Extracting number of comments
                try:
                    comment_count_elem = article.find('shreddit-post-overflow-menu')
                    comment_count = comment_count_elem.get('comment-count', '0') if comment_count_elem else '0'
                except Exception as e:
                    comment_count = '0'
                    print(f"Error extracting comment count: {e}")

                # Extracting link
                try:
                    link_elem = article.find('a', {'data-ks-id': True})
                    link = link_elem.get('href', '') if link_elem else ''
                except Exception as e:
                    link = ''
                    print(f"Error extracting link: {e}")

                # Extract label
                try:
                    label_elem = article.find('shreddit-post-flair')
                    label = label_elem.find('div').getText().strip() if label_elem else ''
                except Exception as e:
                    label = ''
                    print(f"Error extracting label: {e}")

                # Extracting post score
                try:
                    score = article.get('score', '0')
                except Exception as e:
                    score = '0'
                    print(f"Error extracting score: {e}")

                # Appending data for the post
                posts.append({
                    'title': title,
                    'author': author,
                    'timestamp': timestamp,
                    'description': description,
                    'body_text': body_text,
                    'label': label,
                    'comment_count': comment_count,
                    'link': link,
                    'score': score
                })
            
        return pd.DataFrame(posts)
        
    df = extract_posts2(posts)
    df.to_csv(f'more_subs/reddit_posts{url.split("/")[-2]}.csv', index=False)

url_list = ['https://www.reddit.com/r/enter_your_subreddit/',]
for url_i in tqdm(url_list):
    wd = webdriver.Safari()
    fetch_data(wd, url_i)
    try:
        wd.close()
    except:
        pass

