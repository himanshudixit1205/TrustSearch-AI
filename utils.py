UNRELIABLE_DOMAINS = [
    "reddit.com", 
    "facebook.com", 
    "twitter.com", 
    "tiktok.com",      
    "youtube.com",   
    "instagram.com"
]

BLOCKED_PHRASES = [
    "turnstile", 
    "captcha", 
    "quick check before you continue", 
    "verify you are human",
    "access denied",
    "cloudflare"
]

def build_context(results):
    context = ""
    seen_urls = set()
    
    for r in results:
        # Check 1: Duplicate URL
        if r['url'] in seen_urls:
            continue
        seen_urls.add(r['url'])
        
        # Check 2: Unreliable domain
        if any(domain in r['url'].lower() for domain in UNRELIABLE_DOMAINS):
            continue
        
        # Check 3: Blocked content (THIS WAS THE BUG)
        content_lower = r['content'].lower()
        if any(phrase in content_lower for phrase in BLOCKED_PHRASES):
            continue
        
        # Check 4: Minimum content length
        if len(r['content'].strip()) < 100:
            continue
        
        # All checks passed
        context += f"Title: {r['title']}\n"
        context += f"Content: {r['content']}\n"
        context += f"URL: {r['url']}\n\n"
    
    return context