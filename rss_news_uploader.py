import feedparser
import subprocess
import os
import time
from bs4 import BeautifulSoup
import time
import ssl

def remove_parenthesis(string):
    # 주어진 문자열에서 괄호로 시작하는 부분을 찾아 삭제
    while True:
        start_index = string.find("{")
        end_index = string.find("}")
        if(end_index-start_index<1000):
            if start_index != -1 and end_index != -1:
                string = string[:start_index] + string[end_index+1:]
            else:
                break
    # 삭제된 문자열 반환
    return string


def remove_p_and_img_tags(html_text):
    html_text = str(html_text)
    soup = BeautifulSoup(html_text, 'html.parser')
    for tag in soup(['p', 'img']):
        tag.decompose()
    return remove_parenthesis(str(soup))








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
    },
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

while True:
    for press in rss_urls:
        if hasattr(ssl, '_create_unverified_context'):
            ssl._create_default_https_context = ssl._create_unverified_context
        file_name = f"{press}.html"
        file_path = os.path.join(base_path, file_name)
        press_html = ""
        titleList=""
        for category in rss_urls[press]:
            rss_url = rss_urls[press][category]
            # feedparser로 RSS 뉴스 기사 파싱
            feed = feedparser.parse(rss_url)
            # 기사 정보를 HTML 코드로 변환하여 press_html에 추가
            titleList=titleList+category+"_"
            for entry in feed.entries:
                temp = f"_{entry.title}\n"
                try:
                    if len(remove_p_and_img_tags(entry.content[0])) > len(remove_p_and_img_tags(entry.description)) and len(remove_p_and_img_tags(entry.content[0])) > len(remove_p_and_img_tags(entry.summary)):
                        if len(remove_p_and_img_tags(entry.content[0])) <2:
                            continue
                        temp += f"{remove_p_and_img_tags(entry.content[0])}\n\n"
                    else:
                        if len(remove_p_and_img_tags(entry.summary)) < 2:
                            continue
                        temp += f"{remove_p_and_img_tags(entry.summary)}\n\n"
                except AttributeError:
                    if len(remove_p_and_img_tags(entry.summary)) < 2:
                        continue
                    temp +=f"{remove_p_and_img_tags(entry.summary)}\n\n"
                press_html = press_html+temp
            press_html +="^"; 

        press_html=titleList+'\n'+press_html

        # HTML 파일 생성
        with open(file_path, "w") as f:
            f.write("<html>\n<head>\n<title>News</title>\n</head>\n<body>\n")
            f.write(press_html)
            f.write("</body>\n</html>")

        # 각 언론사별로 commit 및 push
        subprocess.call(f"git add {file_path}", cwd=base_path, shell=True)
        subprocess.call(f"git commit -m 'Update news' && git push", cwd=base_path, shell=True)

    # 1분 대기
    time.sleep(7200)




