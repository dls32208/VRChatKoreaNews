
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

for entry in feed.entries:
    print("Title:", entry.title)
    print("Link:", entry.link)
    print("Summary:", entry.summary, "\n")



# 저장할 파일 경로와 파일명 설정
file_path = "/home/dls32208/Documents/VRChatKoreaNews"
file_name = "news.html"

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

# 3분마다 반복 실행
while True:
    time.sleep(180)
    # ssh-agent 실행
    ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
    # ssh-add 실행
    subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)

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

