from bs4 import BeautifulSoup
import pandas as pd

def extract_posts(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    posts = []
    
    # Find all article elements containing posts
    articles = soup.find_all('article')
    
    for article in articles:
        # Extract post data
        title = article.get('aria-label', '')
        
        # Get author information
        author_elem = article.find('a', {'href': lambda x: x and '/user/' in x})
        author = author_elem.text.strip() if author_elem else ''
        
        # Get timestamp
        timestamp = article.get('created-timestamp', '')
        
        # Get post link
        link_elem = article.find('a', {'data-ks-id': True})
        link = link_elem.get('href', '') if link_elem else ''
        
        # Get score
        score = article.get('score', '0')
        
        posts.append({
            'title': title,
            'author': author,
            'timestamp': timestamp,
            'link': link,
            'score': score
        })
    
    return pd.DataFrame(posts)

def extract_posts2(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    posts = []
    
    articles = soup.find_all('article')
    
    for article in articles:
        # Extracting basic post info
        title_elem = article.find('a', {'id': lambda x: x and 'post-title' in x})
        title = title_elem.get_text(strip=True) if title_elem else ''
        
        author_elem = article.find('span', {'slot': 'authorName'})
        author = author_elem.get_text(strip=True) if author_elem else ''
        
        timestamp_elem = article.find('time')
        timestamp = timestamp_elem.get('datetime', '') if timestamp_elem else ''
        
        # Extracting post body (description or preview)
        description_elem = article.find('div', {'class': 'md feed-card-text-preview'})
        description = ''
        if description_elem:
            paragraphs = description_elem.find_all('p')
            description = '\n'.join(p.get_text(strip=True) for p in paragraphs if p.get_text(strip=True))
        
        # Extracting full body text (if available)
        body_elem = article.find('a', {'slot': 'text-body'})
        body_text = ''
        if body_elem:
            body_text = body_elem.get_text(separator='\n', strip=True)
        
        # Extracting number of comments
        comment_count_elem = article.find('shreddit-post-overflow-menu')
        comment_count = comment_count_elem.get('comment-count', '0') if comment_count_elem else '0'
        
        # Extracting link
        link_elem = article.find('a', {'data-ks-id': True})
        link = link_elem.get('href', '') if link_elem else ''
        
        # Extracting post score
        score = article.get('score', '0')
        
        # Appending data for the post
        posts.append({
            'title': title,
            'author': author,
            'timestamp': timestamp,
            'description': description,
            'body_text': body_text,
            'comment_count': comment_count,
            'link': link,
            'score': score
        })
    
    return pd.DataFrame(posts)

# Usage:
with open('output.html', 'r', encoding='utf-8') as file:
    html_content = file.read()
    
df = extract_posts2(html_content)
df.to_csv('reddit_posts.csv', index=False)