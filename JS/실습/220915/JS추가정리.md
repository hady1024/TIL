# JavaScript

- [HTML](https://developer.mozilla.org/ko/docs/Glossary/HTML)은 웹 콘텐츠의 구조를 짜고 의미를 부여하는 마크업 언어. 예를 들어 페이지의 어디가 문단이고, 헤딩이고, 데이터 표와 외부 이미지/비디오인지 정의.
- [CSS](https://developer.mozilla.org/ko/docs/Glossary/CSS)는 HTML 콘텐츠에 스타일을 적용할 수 있는 스타일 규칙 언어. 배경색을 추가하고, 글꼴을 바꾸고, 콘텐츠를 신문처럼 다열 레이아웃으로 배치할 수 있다.
- [JavaScript](https://developer.mozilla.org/ko/docs/Glossary/JavaScript)는 동적으로 콘텐츠를 바꾸고, 멀티미디어를 제어하고, 애니메이션을 추가하는 등 거의 모든 것을 만들 수 있는 스크립팅 언어. (정말 모든게 가능하지는 않겠지만, JavaScript 코드 몇 줄만으로도 놀라운 결과를 이룰 수 있다)

### HTML

```html
<p>Player 1: Chris</p>
```

### CSS

```css
p {
  font-family: 'helvetica neue', helvetica, sans-serif;
  letter-spacing: 1px;
  text-transform: uppercase;
  text-align: center;
  border: 2px solid rgba(0, 0, 200, 0.6);
  background: rgba(0, 0, 200, 0.3);
  color: rgba(0, 0, 200, 0.6);
  box-shadow: 1px 1px 2px rgba(0, 0, 200, 0.4);
  border-radius: 10px;
  padding: 3px 10px;
  display: inline-block;
  cursor: pointer;
}
```

### JavaScript

```javascript
const para = document.querySelector('p');

para.addEventListener('click', updateName);

function updateName() {
  const name = prompt('Enter a new name');
  para.textContent = `Player 1: ${name}`;
}
```



# 문법과 자료형

### 기본

- JavaScript는 문법의 대부분을 Java와 C, C++로부터 차용하고 있으며, Awk, Perl, Python의 영향도 받음.
- JavaScript는 **대소문자를 구별**하며 **유니코드** 문자셋을 이용하며, 예를 들면, Früh(독일어로 "이른")을 변수명으로 사용할 수도 있다.

```javascript
var 갑을 = "병정";
var Früh = "foobar";
```

- `Früh`는 `früh`와 다르다. 대소문자를 구분하기 때문.
- avaScript에서는 명령을 [명령문(statement) (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Statement)이라고 부르며, 세미콜론(;)으로 구분.

- 명령문이 한 줄을 다 차지할 경우에는 세미콜론이 필요하지 않고, 그러나 한 줄에 두 개 이상의 명령문이 필요하다면 반드시 세미콜론으로 구분해야 함.

- JavaScript의 스크립트 소스는 왼쪽에서 오른쪽으로 탐색하면서 토큰, 제어 문자, 줄바꿈 문자, 주석이나 [공백 (en-US)](https://developer.mozilla.org/en-US/docs/Glossary/Whitespace)으로 이루어진 입력 요소의 시퀀스로 변환. (스페이스, 탭, 줄바꿈 문자는 공백으로 간주.)



### 주석

- **주석**의 구문은 C++ 및 다른 많은 언어와 똑같다.

```javascript
// 한 줄 주석

/* 이건 더 긴,
 * 여러 줄 주석입니다.
 */

/* 그러나, /* 중첩된 주석은 쓸 수 없습니다 */ SyntaxError */
```

- 주석은 공백처럼 행동하며 스크립트 실행 시 버려진다.



### 선언

- [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var)
  - 변수를 선언. 추가로 동시에 값을 초기화.
- [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let)
  - 블록 스코프 지역 변수를 선언. 추가로 동시에 값을 초기화.
- [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const)
  - 블록 스코프 읽기 전용 상수를 선언.



###  변수

- 애플리케이션에서 값에 상징적인 이름으로 변수를 사용. 변수명은 [식별자(identifiers)](https://developer.mozilla.org/ko/docs/Glossary/Identifier)라고 불리며 특정 규칙을 따른다.
- JavaScript 식별자는 문자, 밑줄 (`_`) 혹은 달러 기호 (`$`)로 시작해야 하는 반면 이후는 숫자 (`0`–`9`) 일 수도 있다.
- JavaScript가 대소문자를 구분하기에, 문자는 "`A`"부터 "`Z`" (대문자)와 "`a`"부터 "`z`" (소문자)까지 모두 포함한다.
- ISO 8859-1 혹은 Unicode 문자(가령 `å` 나 `ü`)도 식별자에 사용할 수 있다. (좀 더 상세한 내용은 [이 블로그 글](https://mathiasbynens.be/notes/javascript-identifiers-es6)을 참고.) 또한 [Unicode escape sequences](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Lexical_grammar#문자열_리터럴)도 식별자에 문자로 사용할 수 있다.
- 적절한 이름으로는 `Number_hits`, `temp99`, `$credit` 및 `_name` 등 



### 변수 선언

- `var x = 42`와 같이 [`var`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/var) 키워드로 변수를 선언할 수 있다. 이 구문은 실행 맥락에 따라 **지역 및 전역 변수**를 선언하는데 모두 사용될 수 있다.
- `let y = 13`와 같이 [`const`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/const) 혹은 [`let`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/let) 키워드로 변수를 선언할 수 있다. 이 구문은 블록 스코프 지역 변수를 선언하는데 사용될 수 있다.



### 변수 할당

- 지정된 초기 값 없이 `var` 혹은 `let` 문을 사용해서 선언된 변수는 [`undefined`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/undefined) 값을 갖는다.
- 선언되지 않은 변수에 접근을 시도하는 경우 [`ReferenceError`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/ReferenceError) 예외가 발생한다.

```javascript
var a;
console.log('a 값은 ' + a); // a 값은 undefined

console.log('b 값은 ' + b); // b 값은 undefined
var b;
// 이것은 아래의 '변수 호이스팅'을 읽기 전에는 혼란스러울 수 있음

console.log('c 값은 ' + c); // Uncaught ReferenceError: c is not defined

let x;
console.log('x 값은 ' + x); // x 값은 undefined

console.log('y 값은 ' + y); // Uncaught ReferenceError: y is not defined
let y;
```

- `undefined`를 사용하여 변수 값이 있는지 확인할 수 있습니다. 아래 코드에서, `input` 변수는 값이 할당되지 않았고 [`if`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Statements/if...else)문은 `true`로 평가

```javascript
var input;
if(input === undefined) {
  doThis();
} else {
  doThat();
}
```

- `undefined` 값은 불리언 맥락(context)에서 사용될 때 `false`로 동작합니다. 예를 들어, 아래 코드는 `myArray` 요소가 `undefined`이므로 `myFunction` 함수를 실행

```html
var myArray = [];
if (!myArray[0]) myFunction();
```

- `undefined` 값은 수치 맥락에서 사용될 때 `NaN`으로 변환

```javascript
var a;
a + 2; // NaN으로 평가
```

- [`null`](https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Operators/null) 값을 평가할 때, 수치 맥락에서는 `0`으로, 불리언 맥락에서는 `false`로 동작

```javascript
var n = null;
console.log(n * 32); // 콘솔에 0 으로 로그가 남음
```

