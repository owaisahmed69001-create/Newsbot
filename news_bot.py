"""
Personal Market News Bot
Har news -> Gemini (free AI) se simple Roman Urdu explanation -> Telegram notification

Install:   pip install feedparser requests
Run:       python news_bot.py
"""
import os, time, json, hashlib
import feedparser, requests

# ====== SETTINGS (environment variables mein rakhein) ======
NTFY_TOPIC = os.environ["NTFY_TOPIC"]              # ntfy app wala random topic naam
GEMINI_API_KEY = os.environ["GEMINI_API_KEY"]      # aistudio.google.com se free key
MODEL = "gemini-flash-lite-latest"   # free tier model
MAX_NEWS_PER_CYCLE = 8   # free limit se bachne ke liye
SECONDS_BETWEEN_AI_CALLS = 6
CHECK_EVERY_SECONDS = 60
SEEN_FILE = "seen.json"

# Agar sirf market-related chahiye to True, warna har cheez aayegi
SKIP_NON_MARKET_NEWS = True

FEEDS = [
    # Markets / business
    "https://feeds.content.dowjones.io/public/rss/mw_realtimeheadlines",
    "https://www.cnbc.com/id/100003114/device/rss/rss.xml",
    "https://www.cnbc.com/id/10000664/device/rss/rss.xml",
    "https://www.fxstreet.com/rss/news",
    "https://www.forexlive.com/feed/news",
    # World / war / politics
    "https://feeds.bbci.co.uk/news/world/rss.xml",
    "https://feeds.bbci.co.uk/news/business/rss.xml",
    # Official sources
    "https://www.federalreserve.gov/feeds/press_all.xml",
    "https://www.whitehouse.gov/feed/",
    # Trump posts (third-party mirror, kabhi band ho sakta hai)
    "https://www.trumpstruth.org/feed",
    # Gold specific
    "https://news.google.com/rss/search?q=gold+price+OR+XAUUSD+when:1h&hl=en-US&gl=US&ceid=US:en",
]
