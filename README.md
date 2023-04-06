# VRChatKoreaNews

<!DOCTYPE html>
<html>
  <head>
    <meta charset="utf-8">
    <title>RSS Feed Example with Proxy Server</title>
  </head>
  <body>
    <h1>RSS Feed Example with Proxy Server</h1>
    <div id="feed"></div>
    <script>
      // RSS 피드 URL을 입력하세요.
      const feedUrl = "https://www.yonhapnewstv.co.kr/browse/feed/";

      // Proxy 서버 URL을 입력하세요.
      const proxyUrl = "https://cors-anywhere.herokuapp.com/";

      // RSS 피드를 가져옵니다.
      fetch(proxyUrl + feedUrl)
        .then(response => response.text())
        .then(data => {
          // RSS 피드의 제목을 가져옵니다.
          const parser = new DOMParser();
          const xmlDoc = parser.parseFromString(data, "text/xml");
          const title = xmlDoc.getElementsByTagName("title")[0].childNodes[0].nodeValue;

          // RSS 피드의 아이템을 가져와서 HTML에 적용합니다.
          const items = xmlDoc.getElementsByTagName("item");
          let html = "<h2>" + title + "</h2><ul>";
          for (let i = 0; i < items.length; i++) {
            const itemTitle = items[i].getElementsByTagName("title")[0].childNodes[0].nodeValue;
            const itemLink = items[i].getElementsByTagName("link")[0].childNodes[0].nodeValue;
            html += "<li><a href='" + itemLink + "'>" + itemTitle + "</a></li>";
          }
          html += "</ul>";

          // HTML에 RSS 피드를 적용합니다.
          document.getElementById("feed").innerHTML = html;
        })
        .catch(error => console.log(error));
    </script>
  </body>
</html>
