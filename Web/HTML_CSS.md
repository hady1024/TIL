# HTML: Hypertext Markup Language

### **HTML**(HyperText Markup Language)

- **HTML**(HyperText Markup Language)은 웹을 이루는 가장 기초적인 구성 요소로, 웹 콘텐츠의 의미와 구조를 정의할 때 사용. 
- HTML 이외의 다른 기술은 일반적으로 웹 페이지의 모양/표현 ([CSS](https://developer.mozilla.org/ko/docs/Web/CSS)), 또는 기능/동작 ([JavaScript](https://developer.mozilla.org/ko/docs/Web/JavaScript))을 설명하는 데 사용.



### Hypertext(하이퍼텍스트)

- 웹 페이지를 다른 페이지로 연결하는 링크



### HTML 요소

|                             요소                             |                             내용                             |
| :----------------------------------------------------------: | :----------------------------------------------------------: |
| [`head`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/head) | **HTML `<head>` 요소**는 기계가 식별할 수 있는 문서 정보(메타데이터)를 담는다.<br />정보로는 문서가 사용할 [제목](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title), [스크립트](https://developer.mozilla.org/ko/docs/Web/HTML/Element/script), [스타일 시트](https://developer.mozilla.org/ko/docs/Web/HTML/Element/style) 등이 있습니다.<br />`<head>`의 주 목적은 기계 처리를 위한 정보이고, 사람이 읽을 수 있는 정보가 아님. |
| [`title`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/title) | **HTML `<title>` 요소**는 브라우저의 제목 표시줄이나 페이지 탭에 보이는 문서 제목을 정의.<br />텍스트만 포함할 수 있으며 태그를 포함하더라도 무시. |
| [`body`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/body) | **HTML `<body>` 요소**는 HTML 문서의 내용을 나타낸다. <br />한 문서에 하나의 `<body>` 요소만 존재할 수 있다. |
| [`header`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/header) | **HTML `<header>` 요소**는 소개 및 탐색에 도움을 주는 콘텐츠를 나타낸다. <br />제목, 로고, 검색 폼, 작성자 이름 등의 요소도 포함할 수 있다. |
| [`footer`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/footer) | **HTML `<footer>` 요소**는 가장 가까운 [구획 콘텐츠](https://developer.mozilla.org/ko/docs/Web/HTML/HTML5_문서의_섹션과_윤곽)나 [구획 루트](https://developer.mozilla.org/ko/docs/Web/HTML/HTML5_문서의_섹션과_윤곽)의 푸터를 나타낸다. <br />푸터는 일반적으로 구획의 작성자, 저작권 정보, 관련 문서 등의 내용을 담는다. |
| [`article`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/article) | **HTML `<article>` 요소**는 문서, 페이지, 애플리케이션, 또는 사이트 안에서 독립적으로 구분해 배포하거나 재사용할 수 있는 구획을 나타낸다. <br />사용 예제로 게시판과 블로그 글, 매거진이나 뉴스 기사 등이 있다. |
| [`section`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/section) | **HTML `<section>` 요소**는 HTML 문서의 독립적인 구획을 나타내며, 더 적합한 의미를 가진 요소가 없을 때 사용한다. <br />보통 `<section>`은 제목을 포함하지만, 항상 그런 것은 아니다. |
| [`<p>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/p) | **HTML `<p>` 요소**는 하나의 문단을 나타낸다. <br />시각적인 매체에서, 문단은 보통 인접 블록과의 여백과 첫 줄의 들여쓰기로 구분하지만, HTML에서 문단은 이미지나 입력 폼 등 서로 관련있는 콘텐츠 무엇이나 될 수 있다.<br />문단은 블록 레벨 요소이며, 자신의 닫는 태그(`</p>`) 이전에 다른 블록 레벨 태그가 분석되면 자동으로 닫는다. |
| [`<div>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div) | **HTML `<div>` 요소**는 플로우 콘텐츠를 위한 통용 컨테이너이다.<br /> [CSS](https://developer.mozilla.org/ko/docs/Glossary/CSS)로 꾸미기 전에는 콘텐츠나 레이아웃에 어떤 영향도 주지 않는다. |
| [`span`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/span) | **HTML `<span>` 요소**는 구문 콘텐츠를 위한 통용 인라인 컨테이너로, 본질적으로는 아무것도 나타내지 않는다.<br /> 스타일을 적용하기 위해서, 또는 [`lang`](https://developer.mozilla.org/ko/docs/Web/HTML/Global_attributes#attr-lang) 등 어떤 특성의 값을 서로 공유하는 요소를 묶을 때 사용할 수 있다.<br /> 적절한 의미를 가진 다른 요소가 없을 때에만 사용해야 합니다. `<span>`은 [`div`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div)와 매우 유사하지만, [`div`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/div)는 [블록 레벨 요소](https://developer.mozilla.org/ko/docs/Web/HTML/Block-level_elements)인 반면 `<span>`은 [인라인 요소](https://developer.mozilla.org/ko/docs/Web/HTML/Inline_elements). |
| [`<img>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/img) |       **HTML `<img>` 요소**는 문서에 이미지를 넣는다.        |
| [`aside`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/aside) | **HTML `<aside>` 요소**는 문서의 주요 내용과 간접적으로만 연관된 부분을 나타냅니다. 주로 사이드바 혹은 콜아웃 박스로 표현한다. |
| [`<audio>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/audio) | **HTML `<audio>` 요소**는 문서에 소리 콘텐츠를 포함할 때 사용한다.<br /> `src` 특성 또는 [`source` (en-US)](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/source) 요소를 사용해 한 개 이상의 오디오 소스를 지정할 수 있으며, 다수를 지정한 경우 가장 적절한 소스를 브라우저가 고르다. [`MediaStream` (en-US)](https://developer.mozilla.org/en-US/docs/Web/API/MediaStream)을 사용하면 미디어 스트림을 바라볼 수도 있다. |
| [`canvas`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/canvas) | **HTML `<canvas>` 요소**는 [캔버스 스크립팅 API](https://developer.mozilla.org/ko/docs/Web/API/Canvas_API) 또는 [WebGL API](https://developer.mozilla.org/ko/docs/Web/API/WebGL_API)와 함께 사용해 그래픽과 애니메이션을 그릴 수 있다. |
| [`datalist`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/datalist) | **HTML `<datalist>` 요소**는 다른 컨트롤에서 고를 수 있는 가능한, 혹은 추천하는 선택지를 나타내는 [`option`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/option) 요소 여럿을 담는다. |
| [`<details>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/details) | **HTML `<details>` 요소**는 "열림" 상태일 때만 내부 정보를 보여주는 정보 공개 위젯을 생성. <br />요약이나 레이블은 [`summary`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/summary) 요소를 통해 제공할 수 있다.<br />정보 공개 위젯은 보통 레이블 옆의 작은 삼각형이 돌아가면서 열림/닫힘 상태를 나타낸다. <br />`<details>` 요소의 첫 번째 자식이 `<summary>` 요소라면, `<summary>`의 콘텐츠를 위젯의 레이블로 사용. |
| [`emved`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/embed) | **HTML `<embed>` 요소**는 외부 어플리케이션이나 대화형 컨텐츠와의 통합점을 나타낸다. |
| [`nav`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/nav) | **HTML `<nav>` 요소**는 문서의 부분 중 현재 페이지 내, 또는 다른 페이지로의 링크를 보여주는 구획을 나타냅니다. 자주 쓰이는 예제는 메뉴, 목차, 색인이다. |
| [`output`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/output) | **HTML `<output>` 요소**는 웹 사이트나 앱에서 계산이나 사용자 행동의 결과를 삽입할 수 있는 컨테이너 요소이다. |
| [`progress`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/progress) | **HTML `<progress>` 요소**는 어느 작업의 완료 정도를 나타내며, 주로 진행 표시줄의 형태를 띈다. |
| [`<video>`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/Video) | **HTML `<video>` 요소**는 비디오 플레이백을 지원하는 미디어 플레이어를 문서에 삽입한다. <br />오디오 콘텐츠에도 사용할 수 있으나, [`audio`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/audio) 요소가 사용자 경험에 좀 더 적합함. |
| [`ul`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul) | **HTML `<ul>` 요소**는 정렬되지 않은 목록을 나타낸다. <br />보통 불릿으로 표현한다. |
| [`ol`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol) | **HTML `<ol>` 요소**는 정렬된 목록을 나타냅니다. 보통 숫자 목록으로 표현한다. |
| [`li`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/li) | **HTML `<li>` 요소**는 목록의 항목을 나타냅니다. 반드시 정렬 목록([`ol`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ol)), 비정렬 목록([`ul`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/ul), 혹은 메뉴([`menu`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/menu)) 안에 위치해야 한다. <br />메뉴와 비정렬 목록에서는 보통 불릿으로 항목을 나타내고, 정렬 목록에서는 숫자나 문자를 사용한 오름차순 카운터로 나타낸다. |
| [`blockquote`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/blockquote) | **HTML `<blockquote>` 요소**는 안쪽의 텍스트가 긴 인용문임을 나타낸다. <br />주로 들여쓰기를 한 것으로 그려진다. <br />(외형을 바꾸는 법은 [사용 일람](https://developer.mozilla.org/ko/docs/Web/HTML/Element/blockquote#사용_일람)을 참고) 인용문의 출처 URL은 [`cite`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/blockquote#attr-cite) 특성으로, 출처 텍스트는 [`cite`](https://developer.mozilla.org/ko/docs/Web/HTML/Element/cite) 요소로 제공할 수 있다. |

> [참고](https://developer.mozilla.org/ko/docs/Web/HTML)



# CSS: Cascading Style Sheets

### CSS

- **Cascading Style Sheets**(**CSS**)는 [HTML](https://developer.mozilla.org/ko/docs/Web/HTML)이나 [XML](https://developer.mozilla.org/ko/docs/Web/XML)(XML의 방언인 [SVG](https://developer.mozilla.org/ko/docs/Web/SVG), [XHTML](https://developer.mozilla.org/ko/docs/Glossary/XHTML) 포함)로 작성된 문서의 표시 방법을 기술하기 위한 [스타일 시트](https://developer.mozilla.org/ko/docs/Web/API/StyleSheet) 언어
- CSS는 요소가 화면, 종이, 음성이나 다른 매체 상에 어떻게 렌더링되어야 하는지 지정합니다.
- CSS는 **오픈 웹**의 핵심 언어 중 하나이며, [W3C 명세](https://w3.org/Style/CSS/#specs)가 다양한 브라우저의 표준으로 작동하고 있다.



### CSS 기초

- CSS (Cascading Style Sheets)는 웹페이지를 꾸미려고 작성하는 코드
- HTML와 같이 CSS는 실제로 프로그래밍 언어는 아니다. 
- *마크업(markup) 언어* 도 아니고. *Style sheet 언어* 이다. 
- HTML 문서에 있는 요소들에 선택적으로 스타일을 적용할 수 있다는 말임.

```css
p {
  color: red;
}
```

> [CSS기초](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/CSS_basics)



### 스타일 규칙 예제

```css
strong {
  color: red;
}

div.menu-bar li:hover > ul {
  display: block;
}
```

- 규칙 정의에서 [구문](https://developer.mozilla.org/ko/docs/Web/CSS/Syntax) 오류가 하나라도 발생하면 규칙 전체가 유효하지 않다는 점
- CSS 규칙 정의는 모두 (ASCII) [텍스트에 기반](https://www.w3.org/TR/css-syntax-3/#intro)하지만, DOM-CSS / CSSOM (규칙 관리 시스템)은 [객체에 기반](https://www.w3.org/TR/cssom/#introduction)

> [규칙구문](https://developer.mozilla.org/ko/docs/Web/CSS/At-rule)



### [CSS의 구성 블록](https://developer.mozilla.org/ko/docs/Learn/CSS/Building_blocks)

- [텍스트 스타일링](https://developer.mozilla.org/ko/docs/Learn/CSS/Styling_text)
  - 글꼴 설정, 굵기, 기울임꼴, 행간과 자간, 그림자 등 다양한 텍스트 기능
  - 사용자 지정 글꼴을 페이지에 적용
  - 리스트와 링크 스타일로 모듈
- [CSS 레이아웃](https://developer.mozilla.org/ko/docs/Learn/CSS/CSS_layout)



- [일반적인 CSS 문제 해결하기](https://developer.mozilla.org/ko/docs/Learn/CSS/Howto)