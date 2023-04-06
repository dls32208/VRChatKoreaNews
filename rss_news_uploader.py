import feedparser
import subprocess
import os

# ssh-agent 실행
ssh_agent = subprocess.Popen(['ssh-agent', '-s'], stdout=subprocess.PIPE)
# ssh-add 실행
subprocess.call('ssh-add ~/.ssh/id_rsa', shell=True)

# RSS 피드 URL 설정
rss_url = "http://www.yonhapnewstv.co.kr/browse/feed/"

# feedparser로 RSS 뉴스 기사 파싱
feed = feedparser.parse(rss_url)

# 저장할 파일 경로와 파일명 설정
file_path = "/home/dls32208/Documents/VRChatKoreaNews"
file_name = "news.txt"

# 파일 열기
with open(os.path.join(file_path, file_name), "w") as f:
    # 뉴스 기사 쓰기
    for entry in feed.entries:
        f.write(entry.title + "\n")
        f.write(entry.link + "\n")
        f.write(entry.summary + "\n\n")

# 깃허브에 업로드
subprocess.call(f"cd {file_path} && git add {file_name} && git commit -m 'Update news' && git push", shell=True)

# ssh-agent 종료
ssh_agent.kill()
