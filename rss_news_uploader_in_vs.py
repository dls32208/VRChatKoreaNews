import feedparser
import ssl

# SSL 인증서 검증 비활성화
if hasattr(ssl, '_create_unverified_context'):
    ssl._create_default_https_context = ssl._create_unverified_context

rss_url = 'https://web.gekisaka.jp/feed'
feed = feedparser.parse(rss_url)


if feed.bozo:
    print("잘못된 RSS 피드입니다.")
    print("오류 메시지: ", feed.bozo_exception)
else:
    print("유효한 RSS 피드입니다.")

for entry in feed.entries:
    print(entry)
    print("\n")
    