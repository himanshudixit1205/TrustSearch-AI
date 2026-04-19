from tavily import TavilyClient
import os
from dotenv import load_dotenv

load_dotenv()
tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))

def is_content_blocked(content):
    blocked_indicators = [
        "captcha", "turnstile", "verify you are human", 
        "quick check before you continue", "access denied",
        "please confirm you are human", "cloudflare"
    ]
    content_lower = content.lower()
    return any(indicator in content_lower for indicator in blocked_indicators)

def is_unreliable_domain(url):
    unreliable_domains = [
        "reddit.com", "facebook.com", "twitter.com", "x.com",
        "tiktok.com", "instagram.com", "youtube.com", "twitch.tv"
    ]
    url_lower = url.lower()
    return any(domain in url_lower for domain in unreliable_domains)

def search_web(query, MAX_RESULTS=3):
    try:
        # Use deeper search for better content
        response = tavily.search(
            query=query, 
            max_results=MAX_RESULTS,
            search_depth="advanced"  # Get more complete content
        )
        results = []
        
        for r in response['results']:
            # Skip unreliable domains
            if is_unreliable_domain(r['url']):
                print(f"Skipping unreliable source: {r['url']}")
                continue
            
            # Skip blocked content
            if is_content_blocked(r['content']):
                print(f"Skipping blocked content: {r['url']}")
                continue
            
            results.append({
                'title': r['title'],
                'content': r['content'],
                'url': r['url']
            })
        
        return results
        
    except Exception as e:
        print(f"Search error: {e}")
        return []