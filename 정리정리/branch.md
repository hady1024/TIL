# 3일차 정리

- Git : 분산버전관리 시스템 => repository(저장소)에 여러파일들을 커밋
- commit massage는 지금 하는 작업의 전반적인 과정 설명
- 커밋한 모든 내용은 다시 되돌릴 수 있음 커밋하지 않은 모든 내용은 손 쓸 방법이 없다. 

​        => ex) 게임리셋같은 패치에서 데이터가 사라지지 않은 이유

- 다른사람 TIL이나 깃허브에 올라온 자료를 가져오고 싶으면 **git clone <주소>**
- git hub 압축 : 최선버전의 파일/폴더
- git clone : git 저장소
- git clone : 저장소 전체  pull : 변경된 커밋을 받아오는것

# Git 명령어

```bash
# 로컬
$ git init
$ git add . $ git 파일명
$ git commit -m '커밋메시지'
$ git status
$ git log

# 원격
$ git push origin master
$ git pull origin master
$ git remote add origin URL
$ git clone URL
```



root -commit : 첫번째 커밋

merge : 브랜치 병합 (꼭 마스터에서 해야함) 병합하고 나서 브랜치는 지워도 상관없음 왜냐하면 머지를 했기때문



브랜치 git , git hub => 작업, 협업을 하기위함

브랜치로 협업

# branch, Github Flow

- Github으로 협업하는 흐름
- 여러명의 사람들이 1개의 저장소를 사용하는 환경에서 효과적임
- Github Flow, Git Flow, Gitlab Flow

## 1. branch 관련 명령어

​	1. 브랜치 생성 (branch 뒤에는 branch 이름)

```bash
(master) $ git branch example
```

	2. 브랜치 이동

```bash
(master) $ git checkout example
```

	3.  브랜치 생성 및 이동

```bash
(master) $ git checkout -b example
```

	4. 브랜치 목록

```bash
(master) $ git branch
```

	5. 브랜치 삭제

```bash
(master) $ git branch -d example
```



# Branch merge

- 각 brach에서 작업을 한 이후 이력을 합치기 위해서는 merge 명령어 사용

​	💡 병합을 진행시 서로 다른 commit에서 동일한 파일을 수정한 경우 충돌이 발생할 수 있다. 이 경우 반드시 

​         직접 수정을 진행 해야함.



# Git Flow

- Git을 활용하여 협업하는 흐름으로 branch를 활용하는 전략을 의미.

<img src="branch.assets/git-flow_overall_graph-16572170801432.png" alt="git-flow_overall_graph" style="zoom:33%;" />



# Github Flow 기본원칙



### Github Flow는 Github에서 제안하는 브랜치 전략으로 다음과 같은 기본 원칙을 가지고 있다.



#### 1.  master branch는 반드시 배포 가능한 상태여야 한다.

#### 2. feature branch는 각 기능의 의도를 알 수 있도록 작성한다.

#### 3. Commit message는 매우 중요하며, 명확하게 작성한다.

#### 4. Pull Request를 통해 협업을 진행한다.

#### 5. 변경사항을 반영하고 싶다면, master branch에 병합한다.



> 1) Feature Branch Workflow 
>
>    <u>Shared Repository model (저장소의 소유권이 **있는** 경우)</u>



> 2. Forking Workflow
>
>    <u>Fork & Pull model (저장소의 소유권이 없는 경우)</u>





- git keep : 빈 폴더를 만들기 위해서
- git ignore : git 추적하지 않는 파일 관리
