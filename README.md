## Installation and Start up

```
git clone https://github.com/akshtshrma24/speedTestMonitoring.git
cd speedTestMonitoring

curl --output 10mb.txt 'https://raw.githubusercontent.com/jamesward/play-load-tests/master/public/10mb.txt' \
  -H 'authority: raw.githubusercontent.com' \
  -H 'accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7' \
  -H 'accept-language: en-US,en;q=0.9' \
  -H 'referer: https://github.com/jamesward/play-load-tests/blob/master/public/10mb.txt' \
  -H 'sec-ch-ua: "Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "macOS"' \
  -H 'sec-fetch-dest: document' \
  -H 'sec-fetch-mode: navigate' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-user: ?1' \
  -H 'upgrade-insecure-requests: 1' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36' \
  --compressed

docker-compose up --build -d 
```

Then navigate to `localhost/grafana` to view the metrics 

## Purpose
To monitor internet speeds and connection to the internet


