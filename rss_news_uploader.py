import feedparser
import subprocess
import os
import time

# ssh-agent 실행
ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
# ssh-add 실행
subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)

# 언론사별 RSS 피드 URL 설정
rss_urls = {
    "조선일보": "http://rssplus.chosun.com/",
    "동아일보": "http://rss.donga.com/",
    "중앙일보": "https://rss.joins.com/",
    "매일경제": "https://www.mk.co.kr/rss/",
    "한국경제": "http://rss.hankyung.com/",
    "경향신문": "http://www.khan.co.kr/help/help_rss.html",
    "한겨레": "http://www.hani.co.kr/arti/RSS/list1.html",
    "연합뉴스tv": "https://www.yonhapnewstv.co.kr/add/rss",
    "머니투데이": "https://www.mt.co.kr/mtm/mtm_rss.htm",
    "뉴시즈": "https://newsis.com/RSS/",
    "SBS": "https://news.sbs.co.kr/news/rss.do",
    "JTBC": "https://news.jtbc.joins.com/Etc/RssService.aspx",
    "The New York Times": "https://rss.nytimes.com/",
    "CNN": "http://edition.cnn.com/services/rss/"
}

# 저장할 파일 경로 설정
file_path = "/home/dls32208/Documents/VRChatKoreaNews"

# 3분마다 반복 실행
while True:
    # ssh-agent 실행
    ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
    # ssh-add 실행
    subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)

    # 모든 언론사 RSS 뉴스 기사 파싱
    for media, rss_url in rss_urls.items():
        # feedparser로 RSS 뉴스 기사 파싱
        feed = feedparser.parse(rss_url)

        # 저장할 파일 경로와 파일명 설정
        file_name = f"{media}.html"

        # html 파일 생성
        with open(os.path.join(file_path, file_name), "w") as f:
            f.write("<html>\n<head>\n<title>News</title>\n</head>\n<body>\n")
            # 뉴스 기사 쓰기
            for entry in feed.entries:
                f.write(f"<h2><a href='{entry.link}'>{entry.title}</a></h2>\n")
                f.write(f"<p>{entry.summary}</p>\n\n")
            f.write("</body>\n</html>")

        # 깃허브에 업로드
        subprocess.call(f"cd {file_path} && git add {file_name} && git commit -m 'Update {media} news' && git push", shell=True)

    # ssh-agent 종료
    ssh_agent.kill()

    # 3분마다 반복 실행
    time.sleep(180)
