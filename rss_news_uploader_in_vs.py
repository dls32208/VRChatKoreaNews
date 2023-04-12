import feedparser
import ssl

# SSL 인증서 검증 비활성화
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

rss_url = 'https://www3.nhk.or.jp/rss/news/cat0.xml'
feed = feedparser.parse(rss_url)


if not feed.bozo:
    first_entry = feed.entries[0]
    print("제목:", first_entry.title)
    print("링크:", first_entry.link)
else:
    print("잘못된 RSS 피드입니다.")

