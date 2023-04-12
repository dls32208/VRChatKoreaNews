import feedparser
import subprocess
import os

# ssh-agent 실행
ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
# ssh-add 실행
subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)

# 언론사 및 분야별 RSS 피드 URL 설정
rss_urls = {
    'NHK': {
        '主要ニュース': 'https://www3.nhk.or.jp/rss/news/cat0.xml',
        '社会': 'https://www3.nhk.or.jp/rss/news/cat1.xml',
        '科学・医療': 'https://www3.nhk.or.jp/rss/news/cat2.xml',
        '政治': 'https://www3.nhk.or.jp/rss/news/cat3.xml',
        '経済': 'https://www3.nhk.or.jp/rss/news/cat4.xml',
        '国際': 'https://www3.nhk.or.jp/rss/news/cat5.xml',
        'スポーツ': 'https://www3.nhk.or.jp/rss/news/cat6.xml',
        '文化・エンタメ': 'https://www3.nhk.or.jp/rss/news/cat7.xml',
    },
    '毎日新聞': {
        'ニュース速報（総合）': 'https://mainichi.jp/rss/etc/mainichi-flash.rss',
        'スポーツ': 'https://mainichi.jp/rss/etc/mainichi-sports.rss',
        'エンタメ':'https://mainichi.jp/rss/etc/mainichi-enta.rss',
        '社説・解説・コラム':'https://mainichi.jp/rss/etc/opinion.rss'
    },
    '朝日新聞': {
        '国内': 'https://www.asahi.com/rss/asahi/newsheadlines.rdf',
        '社会': 'https://www.asahi.com/rss/asahi/national.rdf',
        '政治': 'https://www.asahi.com/rss/asahi/politics.rdf',
        'スポーツ': 'https://www.asahi.com/rss/asahi/sports.rdf',
        'エンタメ': 'https://www.asahi.com/rss/asahi/entertainment.rdf',   
        '経済':'https://www.asahi.com/rss/asahi/business.rdf',
        '国際':'https://www.asahi.com/rss/asahi/international.rdf',
        'カルチャー':'https://www.asahi.com/rss/asahi/culture.rdf',
        'テック＆サイエンス':'https://www.asahi.com/rss/asahi/science.rdf',
        'ファッション':'https://www.asahi.com/rss/asahi/fashion.rdf',
        '健康':'https://www.asahi.com/rss/asahi/health.rdf',
        '愛車':'https://www.asahi.com/rss/asahi/car.rdf',
        '教育': 'https://www.asahi.com/rss/asahi/edu.rdf',
        'デジタル':'https://www.asahi.com/rss/asahi/digital.rdf',
        'トラベル':'https://www.asahi.com/rss/asahi/travel.rdf',
        '環境':'https://www.asahi.com/rss/asahi/eco.rdf',
        'ショッピング':'https://www.asahi.com/rss/asahi/shopping.rdf'
    }

}

# 저장할 파일 경로 설정
file_path = "/home/dls32208/Documents/VRChatKoreaNews/"

# html 파일 생성 및 깃허브에 업로드
for press in rss_urls:
    for category in rss_urls[press]:
        rss_url = rss_urls[press][category]
        if not os.path.exists(file_path+"/"+press):
            os.mkdir(file_path+"/"+press)
        file_name = f"{press}/{category}.html"

        # feedparser로 RSS 뉴스 기사 파싱
        feed = feedparser.parse(rss_url)

        # html 파일 생성
        with open(os.path.join(file_path, file_name), "w") as f:
            f.write("<html>\n<head>\n<title>News</title>\n</head>\n<body>\n")
            # 뉴스 기사 쓰기
            for entry in feed.entries:
                f.write(f"<h2><a href='{entry.link}'>{entry.title}</a></h2>\n")
                f.write(f"<p>{entry.summary}</p>\n\n")
            f.write("</body>\n</html>")

        # 깃허브에 업로드
        subprocess.call(f"cd {file_path} && git add {file_name} && git commit -m 'Update news' && git push", shell=True)

# ssh-agent 종료
ssh_agent.kill()
