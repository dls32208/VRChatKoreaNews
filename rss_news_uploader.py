import feedparser
import subprocess
import os
import time

# ssh-agent 실행
ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
# ssh-add 실행
subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)

# RSS 피드 URL 설정
rss_urls = {
    "조선일보": "http://rssplus.chosun.com/",
    "동아일보": "http://rss.donga.com/",
    "중앙일보": "https://rss.joins.com/",
    "매일경제": "https://www.mk.co.kr/rss/",
    "한국경제": "http://rss.hankyung.com/",
    "경향신문": "http://www.khan.co.kr/help/help_rss.html",
    "한겨레": "http://www.hani.co.kr/arti/RSS/list1.html",
    "연합뉴스TV": "https://www.yonhapnewstv.co.kr/add/rss",
    "머니투데이": "https://www.mt.co.kr/mtm/mtm_rss.htm",
    "뉴시즈": "https://newsis.com/RSS/",
    "SBS": "https://news.sbs.co.kr/news/rss.do",
    "JTBC": "https://news.jtbc.joins.com/Etc/RssService.aspx",
    "The New York Times": "https://rss.nytimes.com/",
    "CNN": "http://edition.cnn.com/services/rss/"
}

# 저장할 파일 경로와 파일명 설정
file_path = "/home/dls32208/Documents/VRChatKoreaNews"
file_name = "news.html"

# html 파일 생성
def write_html():
    with open(os.path.join(file_path, file_name), "w") as f:
        f.write("<html>\n<head>\n<title>News</title>\n</head>\n<body>\n")
        # 뉴스 기사 쓰기
        for name, url in rss_urls.items():
            feed = feedparser.parse(url)
            f.write(f"<h1>{name}</h1>\n")
            for entry in feed.entries:
                f.write(f"<h2><a href='{entry.link}'>{entry.title}</a></h2>\n")
                f.write(f"<p>{entry.summary}</p>\n\n")
        f.write("</body>\n</html>")

# 최초 실행 시 HTML 파일 생성
write_html()

# 깃허브에 업로드
subprocess.call(f"cd {file_path} && git add {file_name} && git commit -m 'Update news' && git push", shell=True)

# ssh-agent 종료
ssh_agent.kill()

# 3분마다 반복 실행
while True:
    time.sleep(180)
    # ssh-agent 실행
    ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
    # ssh-add 실행
    subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)

    # HTML 파일 생성
    write_html()

    # 깃허브에 업로드
    subprocess
