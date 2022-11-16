# 커피 자판기 만들기
## 요구사항
1. 프롬프트
  - "어떤 커피를 원하세요?" (아메리카노/라떼/카푸치노)
  - 정상적인 입력을 받을 때까지 반복
2. 프롬프트에서 "off" 자판기가 종료됩니다.
3. 프롬프트에서 "report" 입력받을 경우
  - 보고서 출력
    - 재료
      - 물 : xxx ml
      - 우유 : xxx ml
      - 커피 : xxx g
      - 돈 : xxx 원

4. 각 커피를 만들 재료가 충분하지 않으면 "재료가 부족합니다."
5. 재료가 충분할 경우 돈을 받는다.
  - 10,000 원, 5,000 원, 1,000원, 500원, 100원, 50원, 10원
  - 각각 지폐 또는 동전 몇개를 입력 받는다
  - 돈이 충분하지 않으면, 메시지 출력
  - 돈이 충분할 경우 거스름돈 출력

6. "트랜잭션"이 성공적인지 체크
  - 자판기 Money 부분 수익 추가
  - 커피에 해당하는 재료는 줄어든다

7. 커피를 만든다.
  - "맛있는 (아메리카노/라떼/카푸치노) 나왔습니다. 좋은 시간 되세요~"