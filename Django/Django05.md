# Namespace

### 개요

- 개체를 구분할 수 있는 범위를 나타내는 namespace(이름 공간)에 대한 이해

### Namespace의 필요성

- 두번째 app pages의 index 페이지를 작성해보고 어떤 문제가 발생하는지 확인해보기

```python
# pages/urls.py

from django.urls import path
from . import views

urlpatterns = [
	path('index/', views.index, name='index'),
]
```

```python
# pages/views.py • Namespace의 필요성

def index(request):
	return render(request, 'index.html')
```

```html
<!-- pages/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>두번째 앱의 index</h1>
{% endblock content %}
```

```html
<!-- articles/templates/index.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>만나서 반가워요!</h1>
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'throw' %}">throw</a>

  <a href="{% url 'index' %}">두번째 앱 index로 이동</a>
{% endblock content %
```



- 2가지 문제가 발생..

1. articles app index 페이지에 작성한 두번째 앱 index로 이동하는 하이퍼 링크를 클 릭 시 현재 페이지로 다시 이동
   - URL namespace

2.  pages app의 index url (http://127.0.0.1:8000/pages/index/)로 직접 이동해도 articles app의 index 페이지가 출력됨
   - Template namespace



# URL namespace

### 개요

- URL namespace를 사용하면 서로 다른 앱에서 동일한 URL 이름을 사용하는 경우에도 이름이 지정된 URL을 고유하게 사용 할 수 있음
- app_name attribute를 작성해 URL namespace를 설정

```python
# articles/urls.py

app_name = 'articles'
urlpatterns = [
	...,
]
```

```python
# pages/urls.py

app_name = 'pages'
urlpatterns = [
	...,
]
```



### URL tag의 변화

{% url 'index' %}  ---->  {% url 'articles:index' %}



# Template namespace



### 개요

- Django는 기본적으로 app_name/templates/ 경로에 있는 templates 파일들만 찾 을 수 있으며, settings.py의 INSTALLED_APPS에 작성한 app 순서로 template을 검색 후 렌더링 함
- 바로 이 속성 값이 해당 경로를 활성화

```python
# settings.py

TEMPLATES = [
	{
		...,
		'APP_DIRS': True,
		...
	},
]
```



### 디렉토리 생성을 통해 물리적인 이름공간 구분

- Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해 폴더 구조를 app_name/templates/app_name/ 형태로 변경
- Django templates의 기본 경로 자체를 변경할 수는 없기 때문에 물리적으로 이름 공간을 만드는 것

```html
articles/
	templates/
		articles/
			index.html
			...

pages/
	templates/
		pages/
			index.html
			...
```



### 템플릿 경로 변경

- 폴더 구조 변경 후 변경된 경로로 해당하는 모든 부분을 수정하기

```python
# articles/views.py

return render(request, 'articles/index.html')
```

```python
# pages/views.py

return render(request, 'pages/index.html')
```



### 반드시 Template namespace를 고려해야 할까?

- 만약 단일 앱으로만 이루어진 프로젝트라면 상관없음
- 여러 앱이 되었을 때에도 템플릿 파일 이름이 겹치지 않게 하면 되지만,  앱이 많아지면 대부분은 같은 이름의 템플릿 파일이 존재하기 마련



# Naming  URL patterns



### Naming URL patterns의 필요성

- 만약 “index/”의 문자열 주소를 “new-index/”로 바꿔야 한다고 가정, 그렇다면 “index/” 주소를 사용했던 모든 곳을 찾아서 변경해야 하는 번거로움이 발생.



### Naming URL patterns

- 이제는 링크에 URL을 직접 작성하는 것이 아니라 “path()” 함수의 name 인자를 정의해서 사용
- DTL의 Tag 중 하나인 URL 태그를 사용해서 “path()” 함수에 작성한 name을 사용할 수 있음
- 이를 통해 URL 설정에 정의된 특정한 경로들의 의존성을 제거할 수 있음
- Django는 URL에 이름을 지정하는 방법을 제공함으로써 view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

```python
# articles/urls.py

urlpatterns = [
	path('index/', views.index, name='index'),
	path('greeting/', views.greeting, name='greeting'),
	path('dinner/', views.dinner, name='dinner'),
	path('throw/', views.throw, name='throw'),
	path('catch/', views.catch, name='catch'),
	path('hello/<str:name>/', views.hello, name='hello'),
]
```



### Built-in tag – “url”

```html
{% url '' %}
```

- 주어진 URL 패턴 이름 및 선택적 매개 변수와 일치하는 절대 경로 주소를 반환
- 템플릿에 URL을 하드 코딩하지 않고도 DRY 원칙을 위반하지 않으면서 링크를 출력하는 방법

```html
<!-- catch.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Catch</h1>
  <h2>여기서 {{ message }}를 받았어!!</h2>
   <a href="{% url 'throw' %}">다시 던지러</a>
{% endblock content %}
```

```html
<!-- throw.html -->

{% extends 'base.html' %}

{% block content %}
  <h1>Throw</h1>
  <form action="{% url 'catch' %}" method="GET">
    ...
  </form>

  <a href="{% url 'index' %}">뒤로</a>
{% endblock content %}
```

```html
<!-- index.html -->

{% extends 'base.html' %}

{% block content %}
  ...
  <a href="{% url 'greeting' %}">greeting</a>
  <a href="{% url 'dinner' %}">dinner</a>
  <a href="{% url 'throw' %}">throw</a>
{% endblock content %}

<!-- dinner, greeting.html-->

<a href="{% url 'index' %}">뒤로</a>
```



### url 태그 출력 확인하기

- 마지막으로 개발자 도구를 통해 url 태그가 URL 패턴 이름과 일치하는 절대 경로 주소를 반환하는 것을 확인해보기



### [참고] DRY 원칙

- Don’t Repeat Yourself의 약어
- 더 품질 좋은 코드를 작성하기 위해서 알고, 따르면 좋은 소프트웨어 원칙들 중 하나로 “소스 코드에서 동일한 코드를 반복하지 말자” 라는 의미
- 동일한 코드가 반복된다는 것은 잠재적인 버그의 위협을 증가 시키고 반복되는 코드를 변경해야 하는 경우, 반복되는 모든 코드를 찾아서 수정해야 함
- 이는 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커짐 



### Django의 설계 철학 (Templates System)

1. “표현과 로직(view)을 분리”
   - 템플릿 시스템은 표현을 제어하는 도구이자 표현에 관련된 로직일 뿐
   - 즉, 템플릿 시스템은 이러한 기본 목표를 넘어서는 기능을 지원하지 말아야 함
2. “중복을 배제”
   - 대다수의 동적 웹사이트는 공통 header, footer, navbar 같은 사이트 공통 디자인을 갖음
   - Django 템플릿 시스템은 이러한 요소를 한 곳에 저장하기 쉽게 하여 중복 코드를 없애야 함
   - 템플릿 상속의 기초가 되는 철학



### Framework의 성격

- 독선적(Opinionated)
  - 독선적인 프레임워크들은 어떤 특정 작업을 다루는 ‘올바른 방법’에 대한 분명한 의견(규약)을 가지고 있음
  - 대체로 특정 문제내에서 빠른 개발방법을 제시
  - 어떤 작업에 대한 올바른 방법이란 보통 잘 알려져 있고 문서화가 잘 되어있기 때문
  - 하지만 주요 상황을 벗어난 문제에 대해서는 그리 유연하지 못한 해결책을 제시할 수 있음
- 관용적(Unopinionated)
  - 관용적인 프레임워크들은 구성요소를 한데 붙여서 해결해야 한다거나 심지어 어떤 도구를 써야 한다는 '올바른 방법'에 대한 제약이 거의 없음
  - 이는 개발자들이 특정 작업을 완수하는데 가장 적절한 도구들을 이용할 수 있는 자유도가 높음
  - 하지만 개발자 스스로가 그 도구들을 찾아야 한다는 수고가 필요



### Django Framework의 성격

- '다소 독선적'
  - 양쪽 모두에게 최선의 결과를 준다고 강조
- 결국하고자 하는 말은 현대 개발에 있어서는 가장 중요한 것들 중 하나는 '생산성'
- 프레임워크는 우리가 하는 개발을 방해하기 위해 규칙, 제약을 만들어 놓은 것이 아님
- 우리가 온전히 만들고자 하는 것에만 집중할 수 있게 도와주는 것
- "수레바퀴를 다시 만들지 말라"



# Database

### Database

- 체계화된 데이터의 모임
- 검색 및 구조화 같은 작업을 보다 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템



### Database 기본 구조

1. 스키마(Schema)
2. 테이블(Table)



### 스키마(Schema)

- 뼈대(Structure)
- 데이터베이스에서 자료의 구조, 표현 방법, 관계 등을 정의한 구조

| column | datatype |
| :----: | :------: |
|   id   |   INT    |
|  name  |   TEXT   |
|  age   |   INT    |
| email  |   TEXT   |



### 테이블(Table)

- 필드와 레코드를 사용해 조직된 데이터 요소들의 집합
- 관계(Relation)라고도 부름



1.  필드(field)
   - 속성, 컬럼(Column)
2.  레코드(record)
   - 튜플, 행(Row)



### 필드(field)

- 속성 혹은 컬럼(column)
- 각 필드에는 고유한 데이터 형식이 지정됨
  - INT, TEXT 등



### 레코드(record)

- 튜플 혹은 행(row)
- 테이블의 데이터는 레코드에 저장됨



### PK (Primary Key)

- 기본키
- 각 레코드의 고유한 값 (식별자로 사용)
- 기술적으로 다른 항목과 절대로 중복될 수 없는 단일 값(unique)
- 데이터베이스 관리 및 테이블 간 관계 설정 시 주요하게 활용 됨

- ex) 주민등록번호
  - 데이터베이스에 동일한 이름, 나이를 가진 사람들의 데이터는 존재할 수 있지만 각 사람들이 가진 주민등록번 호는 절대 같을 수 없음
  - 주민등록번호는 그 사람을 나타내는 고유한 값으로써 사용할 수 있음



### 쿼리(Query)

- 데이터를 조회하기 위한 명령어
- 조건에 맞는 데이터를 추출하거나 조작하는 명령어
  (주로 테이블형 자료구조에서 사용)
- "Query를 날린다."  -----> "데이터베이스를 조작한다"



# Model



### 개요

- Django는 Model을 통해 데이터에 접근하고 조작
- 사용하는 데이터들의 필수적인 필드들과 동작들을 포함
- 저장된 데이터베이스의 구조 (layout)
- 일반적으로 각각의 모델은 하나의 데이터베이스 테이블에 매핑(mapping)
  - 모델 클래스 1개 == 데이터베이스 테이블 1개
- Model을 통해 데이터 관리



### [참고] 매핑

- Mapping
- 하나의 값을 다른 값으로 대응시키는 것



### Model 작성하기 (1/2)

- 새 프로젝트(crud), 앱(articles) 작성 및 앱 등록

```Git
$ django-admin startproject crud . [프로젝트 이름]

$ python manage.py startapp articles
```

```py
# settings.py

INSTALLED_APPS = [
	'articles',
	...
]
```



### Model 작성하기 (2/2)

- models.py 작성
  - 모델 클래스를 작성하는 것은 데이터베이스 테이블의 스키마를 정의하는 것
  - ”모델 클래스 == 테이블 스키마”

```python
# articles/models.py

class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
```



### Model 이해하기 (1/4)

- 각 모델은 django.models.Model 클래스의 서브 클래스
  - 즉, 각 모델은 django.db.models 모듈의 Model 클래스를 상속받아 구성됨
  - 클래스 상속 기반 형태의 Django 프레임워크 개발
  - 프레임워크에서는 잘 만들어진 도구를 가져다가 잘 쓰는 것

```python
# articles/models.py

class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
```



### Model 이해하기 (2/4)

- models 모듈을 통해 어떠한 타입의 DB 필드(컬럼)을 정의할 것인지 정의
  - Article에는 어떤 데이터 구조가 필요한지 정의
  - 클래스 변수 title과 content은 DB 필드를 나타냄

```python
# articles/models.py

class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
```



### Model 이해하기 (3/4)

1. 클래스 변수(속성)명
   - DB 필드의 이름

```python
# articles/models.py

class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
```



### Model 이해하기 (4/4)

2. 클래스 변수 값 (models 모듈의 Field 클래스)
   - DB 필드의 데이터 타입



### Django Model Field

- Django는 모델 필드를 통해 테이블의 필드(컬럼)에 저장할 데이터 유형 (INT, TEXT 등)을 정의
- 데이터 유형에 따라 다양한 모델 필드를 제공
  - DataField(), CharField(), IntegerField() 등
  - [[Model field reference | Django documentation | Django (djangoproject.com)](https://docs.djangoproject.com/en/3.2/ref/models/fields/)]



### 사용한 모델 필드 알아보기 (1/2)

- CharField(max_length=None, **options)
  - 길이의 제한이 있는 문자열을 넣을 때 사용
  - max_length
    - 필드의 최대 길이(문자)
    - CharField의 필수 인자
    - 데이터베이스와 Django의 유효성 검사(값을 검증하는 것)에서 활용됨



### 사용한 모델 필드 알아보기 (2/2)

- TextField(**options)
  - 글자의 수가 많을 때 사용
  - max_length 옵션 작성 시 사용자 입력 단계에서는 반영 되지만,  모델과 데이터베이스 단계에는 적용되지 않음 (CharField를 사용해야 함)
    - 실제로 저장될 때 길이에 대한 유효성을 검증하지 않음



### 데이터베이스 스키마

- 지금까지 작성한 models.py는 다음과 같은 데이터베이스 스키마를 정의한 것
- 이제 이러한 모델의 변경사항을 실제 데이터베이스에 반영하기 위한 과정이 필요

| Column  |  Data Type  |
| :-----: | :---------: |
|  title  | VARCHAR(10) |
| content |    TEXT     |



# Migrations

### Migrations 관련 주요 명령어

1. makemigrations
2. migrate



### makemigrations (1/2)

- 모델의 변경사항에 대한 새로운 migration을 만들 때 사용

```
$ python manage.py makemigrations
```



### makemigrations (2/2)

- 명령어 실행 후 migrations/0001_initial.py가 생성된 것을 확인
- "파이썬으로 작성된 설계도”



### migrate 

- makemigrations로 만든 설계도를 실제 데이터베이스에 반영하는 과정
   (db.sqlite3 파일에 반영)
- 결과적으로 모델의 변경사항과 데이터베이스를 동기화

```
$ python manage.py migrate
```

- 설계도(migration)를 실제 db.sqlite3 DB 파일에 반영



### [참고] Migrations 기타 명령어

1. showmigrations

```
$ python manage.py showmigrations
```

- migrations 파일들이 migrate 됐는지 안됐는지 여부를 확인하는 용도
- [X] 표시가 있으면 migrate가 완료되었음을 의미



2. sqlmigrate

```
$ python manage.py sqlmigrate articles 0001
```

- 해당 migrations 파일이 SQL 문으로 어떻게 해석 될 지 미리 확인 할 수 있음



# 추가 필드 정의

### Model 변경사항 반영하기 (1/6)

- models.py에 변경사항이 생겼을 때 어떤 과정의 migration이 필요할까?
- 추가 모델 필드 작성 후 다시 한번 makemigrations 진행

``` python
# articles/models.py

class Article(models.Model):
	title = models.CharField(max_length=10)
	content = models.TextField()
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
```

```
$ python manage.py makemigrations
```



### Model 변경사항 반영하기 (2/6)

- 기존에 id, title, content 필드를 가진 테이블에 2개의 필드가 추가되는 상황
- Django 입장에서는 이미 존재하는 테이블에 새로운 컬럼이 추가되는 요구 사항을 받 았는데, 이러한 컬럼들은 기본적으로 빈 값을 갖고 추가될 수 없음
  - Django는 우리에게 추가되는 컬럼에 대한 기본 값을 설정해야 하니 어떤 값을 설정할 것인지를 물어보는 과정을 진행

```
You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs 
something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 
```



### Model 변경사항 반영하기 (3/6)

- 각 보기 번호의 의미
  1. 다음 화면으로 넘어가서 새 컬럼의 기본 값을 직접 입력하는 방법
  2. 현재 과정에서 나가고 모델 필드에 default 속성을 직접 작성하는 방법
- “1”을 입력 후 Enter (created_at 필드에 대한 default 값 설정)

```
You are trying to add the field 'created_at' with 'auto_now_add=True' to article without a default; the database needs 
something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
```

