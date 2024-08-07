# Genie Music Chart Scraper

이 Python 스크립트는 Genie Music의 실시간 차트 Top 100을 스크래핑하여 출력하는 프로그램입니다.

## 기능

- Genie Music의 실시간 차트 페이지에서 Top 100 곡의 정보를 가져옵니다.
- 각 곡의 순위, 제목, 아티스트 정보를 출력합니다.

## 사용된 라이브러리

- `requests`: 웹 페이지 요청을 보내기 위해 사용
- `BeautifulSoup`: HTML 파싱을 위해 사용

## 주요 함수

### `song(url)`

- 주어진 URL의 웹 페이지에서 곡 정보를 추출합니다.
- 반환값: 딕셔너리 리스트 (각 딕셔너리는 'title'과 'artist' 키를 가짐)

## 작동 방식

1. Genie Music 차트의 1페이지와 2페이지 URL을 리스트에 저장합니다.
2. 각 URL에 대해 `song()` 함수를 호출하여 곡 정보를 수집합니다.
3. 수집된 모든 곡 정보를 하나의 리스트로 합칩니다.
4. Top 100 곡의 순위, 제목, 아티스트 정보를 출력합니다.

## 주의사항

- 이 스크립트는 교육 및 개인 사용 목적으로만 사용해야 합니다.
- Genie Music의 이용 약관을 준수하여 사용하세요.
- 과도한 요청은 서버에 부담을 줄 수 있으므로 적절한 간격을 두고 사용하세요.

## 사용 방법

1. 필요한 라이브러리를 설치합니다: `pip install requests beautifulsoup4`
2. 스크립트를 실행합니다: `python genie_chart_scraper.py`

