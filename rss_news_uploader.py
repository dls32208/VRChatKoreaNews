import feedparser
import subprocess
import os
import time

# ssh-agent 실행
ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
# ssh-add 실행
subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)
# RSS 피드 URL 설정

rss_url = "http://www.yonhapnewstv.co.kr/browse/feed/"
# feedparser로 RSS 뉴스 기사 파싱
feed = feedparser.parse(rss_url)

# 저장할 파일 경로와 파일명 설정
base_path = "/home/dls32208/Documents/VRChatKoreaNews"
file_name = "news.html"


rss_urls = {
    '조선일보': {
        '전체기사': 'https://www.chosun.com/arc/outboundfeeds/rss/?outputType=xml',
        '정치': 'https://www.chosun.com/arc/outboundfeeds/rss/category/politics/?outputType=xml',
        '경제': 'https://www.chosun.com/arc/outboundfeeds/rss/category/economy/?outputType=xml',
        '사회': 'https://www.chosun.com/arc/outboundfeeds/rss/category/national/?outputType=xml',
        '국제': 'https://www.chosun.com/arc/outboundfeeds/rss/category/international/?outputType=xml',
        '문화라이프': 'https://www.chosun.com/arc/outboundfeeds/rss/category/culture-life/?outputType=xml',
        '오피니언': 'https://www.chosun.com/arc/outboundfeeds/rss/category/opinion/?outputType=xml',
        '스포츠': 'https://www.chosun.com/arc/outboundfeeds/rss/category/sports/?outputType=xml',
        '연예': 'https://www.chosun.com/arc/outboundfeeds/rss/category/entertainments/?outputType=xml'
    },
    '동아일보': {
        '전체기사': 'https://rss.donga.com/total.xml',
        '정치': 'https://rss.donga.com/politics.xml',
        '사회': 'https://rss.donga.com/national.xml',
        '경제': 'https://rss.donga.com/economy.xml',
        '국제': 'https://rss.donga.com/international.xml',
        '사설칼럼': 'https://rss.donga.com/editorials.xml',
        '의학과학': 'https://rss.donga.com/science.xml',
        '문화연예': 'https://rss.donga.com/culture.xml',
        '스포츠': 'https://rss.donga.com/sports.xml',
        '사람속으로': 'https://rss.donga.com/inmul.xml',
        '건강': 'https://rss.donga.com/health.xml',
        '레져': 'https://rss.donga.com/leisure.xml',
        '도서': 'https://rss.donga.com/book.xml',
        '공연': 'https://rss.donga.com/show.xml',
        '여성': 'https://rss.donga.com/woman.xml',
        '여행': 'https://rss.donga.com/travel.xml',
        '생활정보': 'https://rss.donga.com/lifeinfo.xml',
        '스포츠': 'https://rss.donga.com/sportsdonga/sports.xml',
        '야구MLB': 'https://rss.donga.com/sportsdonga/baseball.xml',
        '축구': 'https://rss.donga.com/sportsdonga/soccer.xml',
        '골프': 'https://rss.donga.com/sportsdonga/golf.xml',
        '일반': 'https://rss.donga.com/sportsdonga/sports_general.xml',
        'e스포츠': 'https://rss.donga.com/sportsdonga/sports_game.xml',
        '엔터테인먼트': 'https://rss.donga.com/sportsdonga/entertainment.xml',
    },
    '매일경제': {
        '헤드라인': 'https://www.mk.co.kr/rss/30000001/',
        '전체뉴스': 'https://www.mk.co.kr/rss/40300001/',
        '경제': 'https://www.mk.co.kr/rss/30100041/',
        '정치': 'https://www.mk.co.kr/rss/30200030/',
        '사회': 'https://www.mk.co.kr/rss/50400012/',
        '국제': 'https://www.mk.co.kr/rss/30300018/',
        '기업경영': 'https://www.mk.co.kr/rss/50100032/',
        '증권': 'https://www.mk.co.kr/rss/50200011/',
        '부동산': 'https://www.mk.co.kr/rss/50300009/',
        '문화연예': 'https://www.mk.co.kr/rss/30000023/',
        '스포츠': 'https://www.mk.co.kr/rss/71000001/',
        '게임': 'https://www.mk.co.kr/rss/50700001/',
        'MBA': 'https://www.mk.co.kr/rss/40200124/',
        '머니앤리치스': 'https://www.mk.co.kr/rss/40200003/',
        'English': 'https://www.mk.co.kr/rss/30800011/',
        '이코노미': 'https://www.mk.co.kr/rss/50000001/',
        '시티라이프': 'https://www.mk.co.kr/rss/60000007/'
    }
}


for press in rss_urls:
    press_path = os.path.join(base_path, press)
    if not os.path.exists(press_path):
        os.mkdir(press_path)

    for category in rss_urls[press]:
        rss_url = rss_urls[press][category]
        file_name = f"{category}.html"
        file_path = os.path.join(press_path, file_name)

        # 이전에 생성된 파일이 존재하는 경우, 이전 내용을 비교하여 변경된 경우에만 파일을 업데이트
        if os.path.exists(file_path):
            with open(file_path, "r") as f:
                prev_content = f.read()
            # feedparser로 RSS 뉴스 기사 파싱
            feed = feedparser.parse(rss_url)
            print(rss_url)
            # 기사 정보를 HTML 코드로 변환
            content = f"<h1>{category}</h1>\n"
            for entry in feed.entries:
                content += f"<h2><a href='{entry.link}'>{entry.title}</a></h2>\n"
                if entry.summary > entry.description:
                    content += f"<p>{entry.summary}</p>\n\n"
                else:
                    content += f"<p>{entry.description}</p>\n\n"
            # 이전 내용과 변경된 내용이 다른 경우에만 파일을 업데이트
            if prev_content != content:
                with open(file_path, "w") as f:
                    f.write("<html>\n<head>\n<title>News</title>\n</head>\n<body>\n")
                    f.write(content)
                    f.write("</body>\n</html>")
                    # 변경된 파일만 git add
                    subprocess.call(f"git add {file_path}", cwd=base_path, shell=True)
        else:
            # 이전에 생성된 파일이 없는 경우, 새로 파일을 생성
            # feedparser로 RSS 뉴스 기사 파싱
            feed = feedparser.parse(rss_url)
            # 기사 정보를 HTML 코드로 변환
            content = f"<h1>{category}</h1>\n"
            for entry in feed.entries:
                content += f"<h2><a href='{entry.link}'>{entry.title}</a></h2>\n"
                if entry.summary > entry.description:
                    content += f"<p>{entry.summary}</p>\n\n"
                else:
                    content += f"<p>{entry.description}</p>\n\n"
            with open(file_path, "w") as f:
                f.write("<html>\n<head>\n<title>News</title>\n</head>\n<body>\n")
                f.write(content)
                f.write("</body>\n</html>")
                # 새로 생성된 파일만


# ssh-agent 종료
ssh_agent.kill()


"""
# 3분마다 반복 실행
while True:
    # ssh-agent 실행
    ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
    # ssh-add 실행
    subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)

    # feedparser로 RSS 뉴스 기사 파싱
    feed = feedparser.parse(rss_url)

    # html 파일 생성
    with open(os.path.join(base_path, file_name), "w") as f:
        f.write("<html>\n<head>\n<title>News</title>\n</head>\n<body>\n")
        # 뉴스 기사 쓰기
        for entry in feed.entries:
            f.write(f"<h2><a href='{entry.link}'>{entry.title}</a></h2>\n")
            f.write(f"<p>{entry.summary}</p>\n\n")
        f.write("</body>\n</html>")

    # 깃허브에 업로드
    subprocess.call(
        f"cd {base_path} && git add {file_name} && git commit -m 'Update news' && git push", shell=True)

    # ssh-agent 종료
    ssh_agent.kill()
    time.sleep(180)
"""

