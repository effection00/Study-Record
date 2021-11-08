# Sprint Challenge 32x

### 주의 사항
1. 여러분이 원하는 Tool과 reference를 사용할 수 있습니다. 

2. 다음의 모듈만 가져오거나 사용할 수 있습니다.
    * 여러분이 작성한 다른 모듈
    * `random` 모듈 (표준 라이브러리)
    * `unittest` 모듈 (표준 라이브러리)
    이외의 것은 허용되지 않습니다!

3. 시간 관리에 신경 써주세요! 
    * 섹션 / 질문에서 "good enough "라고 표시 한 다음 모든 작업을 수행했는지 확인합니다. 언제든지 다시 확인할 수 있습니다.
    * 시간이 남는다면 코드 및 답변을 모두 작성한 후, 마지막에 수정 및 추가하길 권장드립니다.

행운을 빕니다!

# Part 1

파이썬과 더 친숙해집니다.

## Part 1.1 - 필드

여러분은 커피 전문점 CodeBeans의 관리자입니다.
CodeBeans에서는 다양한 상품을 판매하고 있습니다.
여러분은 다양한 상품들을 좀더 나은 방법으로 정리하고 관리하는 방법을 고민하고 있습니다.

CodeBeans에서 판매하는 음료들은 모두 (`Product`)으로 간주되며,
음료들은 기본적으로 다음과 같은 필드(클래스 "내부"에 있는 변수)를 가집니다.

* 이름: `name` (문자열, 기본값: 없음)
* 가격: `price` (정수, 기본값: 30)
* 사이즈: `size` (정수, 기본값: 20)
* 따뜻함: `warmness` (실수, 기본값: 0.5)
* 달달함: `sweetness` (실수, 기본값: 0.5)
* 변수: `identifier` (정수, 기본값: 1000000 ~ 9999999 범위의 임의의 정수)

위 데이터를 모델링하기 위해 Python '클래스'를 작성합니다. 

<!-- 필드 이름과 유형, 클래스에`__init__` 생성자가 있는지 적절한 기본값 (또는 부족)이있는 방법. -->

참고) `random.randint`를 사용하면 랜덤 정수를 반환합니다.
https://docs.python.org/ko/3/library/random.html?highlight=random#module-random

위 내용과 같이 만든 클래스를 `codebeans.py`에 저장하고 나서
다음과 같이 Python repl에서 코드를 테스트할 수 있습니다.

```python
>>> from src.Part_1 import Product
>>> prod = Product('A Cold Drink')
>>> prod.name
'A Cold Drink'
>>> prod.price
30
>>> prod.size
20
>>> prod.warmness
0.5
>>> prod.sweetness
0.5
>>> prod.identifier
2812086  # 이 값은 실행에 따라 달라질 수 있습니다.
```

### Part 1.2 - 메소드

`Part 1`에서 작성한 코드가 정상적으로 수행되었나요?
위 예시와 같이 수행된다면 여러분은 훌륭한 코드를 작성해주신 겁니다!

하지만 이것만 가지고는 여러분이 할 수 있는 것은 아무 것도 없습니다.
메소드가 없기 때문입니다. 

따라서 두 개의 메소드를 추가해봅시다!

* `sellability(self)` (판매 가능성)
    * '사이즈(`size`)'를 '가격(`price`)'으로 나눈 값에 따라 다음 메시지를 반환합니다. 
    * `0.5` 보다 작을 경우: "Not so sellable..."
    * `0.5` 보다 크거나 같고, `1.0` 보다 작을 경우: "Kinda sellable."
    * `1.0` 을 크거나 같은 경우 : "Very sellable!"

* `calory(self)` (칼로리)
    * '사이즈(`size`)'와 '달달함(`sweetness`)'를 곱한 값에 따라 다음 메시지를 반환합니다. 
    * `10` 보다 작을 경우 "...it's light"
    * `10` 보다 크거나 같고, `50` 보다 작을 경우: "It's adequate."
    * `50` 을 초과할 경우: "It's really heavy..!!"

코드를 저장하고 다음과 같이 테스트할 수 있습니다.

```python
>>> from src.Part_1 import Product
>>> prod = Product('A Warm Water')
>>> prod.sellability()
'Kinda sellable.'
>>> prod.calory()
"It's adequate."
```


### Part 1.3 - 상속
CodeBeans에서 판매하는 것은 일반적인 음료만 판매하는 것이 아닌
여러 종류의 음료(커피, 차 등)도 판매합니다.

다음을 수행하는 `Tea`라는 `Product`의 하위 클래스를 만듭니다.

* 기본값 변경
    * 사이즈(`size`) 기본값을 10으로 변경
    * 다른 기본값은 변경하지 않습니다.
* `calory` 메서드 재정의
    * 항상 `"...it's a tea. Only a few calories"`를 반환
* `drink(self)` 메소드 추가
    * '따뜻함`warmness`' 값에 따라 다음 메시지를 반환합니다.
    * 0.5 미만이면 : "it's too cold..."
    * 0.5 보다 크거나 같고, 1.0 보다 작은 경우 : "Oh, it's warm!"
    * 1.0 보다 크거나 같은 경우 : "It's too hot!!"


테스트 실행 예 :
```python
>>> from src.Part_1 import Tea
>>> tea = Tea('Green Tea')
>>> tea.price
30
>>> tea.size
10
>>> tea.drink()
"Oh, it's warm..!"
>>> tea.calory()
"...it's a tea. Only a few calories"
```

## Part 2

> ORM 을 복습합니다.

ORM 문법을 활용해 클래스로 테이블을 만듭니다. 

테이블은 다음 요구사항들을 따릅니다:
    - 테이블 명: 'Animals'
    - 테이블 필드 목록: `id`, `name`, `age`
    - 테이블 필드의 세부사항은 다음과 같습니다:
        - `id`: `INTEGER`, `PRIMARY KEY`
        - `name`: `VARCHAR(32)`, `NOT NULL`
        - `age`: `INTEGER`

### 코드 스타일(선택)

지금까지 여러분이 작성한 코드가 다른 사람도 알아볼 수 있는 스타일로 작성되었는지 확인해보아야 합니다.
이번 챌린지에서는 대표적인 Python 코드 스타일 가이드인 PEP 8에 따른 코드 스타일을 적용하도록 합니다.
[PEP8 style] (https://pep8.org/)

만약 코드 편집기(VS Code 등)에서 코드 스타일을 Linting(소스코드에  문제가 있는지 탐색)하도록 되어있다면
여러분의 코드는 이미 특정 스타일로 변경되어 있을 수 있습니다. 
해당 스타일이 PEP 8 가이드와 동일한지 확인해주세요.

코드 스타일 검사를 위한 코드 편집기의 내장 도구를 사용하지 않은 경우 
다음 링크를 확인해보세요.

[PEP8 online] http://pep8online.com/

코드를 Linting 하여 PEP 8 스타일에 위반 사항은 없는지 체크하고 수정해주세요!
