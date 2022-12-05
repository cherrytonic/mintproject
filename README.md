# README.md

# 0. 사용한 기술 스택

- ##### Backend

​		<img src="https://img.shields.io/badge/python-3776AB?style=for-the-badge&logo=python&logoColor=white"><img src="https://img.shields.io/badge/django-092E20?style=for-the-badge&logo=django&logoColor=white"> 



- ##### Frontend

​		<img src="https://img.shields.io/badge/vue.js-4FC08D?style=for-the-badge&logo=vue.js&logoColor=white"><img src="https://img.shields.io/badge/html5-E34F26?style=for-the-badge&logo=html5&logoColor=white"><img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white"><img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">

​		<img src="https://img.shields.io/badge/node.js-339933?style=for-the-badge&logo=Node.js&logoColor=white"><img src="https://img.shields.io/badge/bootstrap-7952B3?style=for-the-badge&logo=bootstrap&logoColor=white">

   

- ##### 그 외

​		<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">

# 1. 프로젝트 소개

![logowithtitle.png](README%20md%209d1f5de16c0e40e289c93857bd758f4e/logowithtitle.png)

- 사용자의 리뷰를 티켓으로 만들어 소장할 수 있게 합니다.
- 사용자의 리뷰들을 모아 하나의 리스트를 만들어 이에 대해 다른 사용자들이 소통할 수 있게 합니다.
- 사용자가 리뷰한 영화의 장르에 맞는 다른 영화들을 추천합니다.

# 2. 팀원 정보 및 업무 분담 내역

|  | 박상현🎸(팀장) | 원채령🌿 |
| --- | --- | --- |
| 프로젝트 매니징  | - 팀장|- git 전략 수집|
| |일정관리|태스크 리마인드|
| |프로젝트 일정 조율|레퍼런스 수집|
| |협업 도구 관리 | |
| --- | --- |--- |
| 백엔드 | - 백엔드 총괄|- 영화, 장르 data 구성(TMDB)|
||- 백엔드 베이스 구성|- REST API|
||- ERD 설계|- movies, reviews 게시판 구현 |
||- account, articles 게시판 구현 || 
| --- | --- |--- |
| 프론트엔드 | - 기능 구현 | - 디테일 구현|
||- vuex 데이터 관리|- axios 관리 |
||- axios 관리 || 
| --- | --- |--- |
| 기획 및 디자인 | - 기술 스택 조사| - 디자인 총괄|
||- 컨셉 디자인 |- 컨셉 디자인 |
|||- CSS 총괄|
|||- 디자인 레퍼런스 수집 |

# 3. 목표 서비스 구현 및 실제 구현 정도

- [x]  회원가입 - username, password 형식 제한, 장르 선택
- [x]  로그인 - 인증된 사용자만 사용 가능한 기능 제한(영화 추천, 리뷰 작성 / 수정 / 삭제,  댓글 등록, 리스트 작성 / 수정 / 삭제, 좋아요, 팔로우
- [x]  좋아요 기능 - 티켓 리스트에 대한 좋아요
- [x]  팔로우 기능 - 티켓 리스트 작성자의 프로필 페이지에서 팔로우
- [x]  TMDB API로 영화 정보 100개와 장르 정보 가져와서 DB에 저장
- [x]  TMDB API로  최고 평점 영화 정보를 가져와서 HomeView에 띄움
- [x]  DB에 저장된 영화 정보 소개
- [x]  DB에 저장된 영화 검색
- [x]  영화 추천 - 회원 가입 시 선택한 장르의 영화 세 개 추천, 티켓 리스트 작성 후 리뷰한 영화들의 장르에 맞는 영화 세 개 추천
- [x]  영화 리뷰를 티켓으로 만들기
- [x]  리뷰를 모아 리스트로 만들기
- [x]  리스트에 대한 댓글 소통(생성, 삭제)
- [ ]  댓글 수정
- [ ]  리뷰한 영화 수에 따른 칭호 부여
- [ ]  TMDB API로 axios 요청해서 Home을 새로고침할 때마다 현재 상영중인 영화 보여주기

# 4. 데이터베이스 모델링(ERD)

- 💛 : 모델 테이블
- 💙 : 중계 테이블

![제목 없는 다이어그램.drawio.png](README%20md%209d1f5de16c0e40e289c93857bd758f4e/%25EC%25A0%259C%25EB%25AA%25A9_%25EC%2597%2586%25EB%258A%2594_%25EB%258B%25A4%25EC%259D%25B4%25EC%2596%25B4%25EA%25B7%25B8%25EB%259E%25A8.drawio.png)

# 5. 영화 추천 알고리즘에 대한 기술적 설명

1. Home 화면의 영화 추천
    
    전체 영화에서 사용자가 회원가입 할 때 선택한 장르를 포함하고 있는 영화들 중 3개의 영화를 랜덤으로 추천합니다. 랜덤을 뽑은 알고리즘은 lodash의 sampleSize를 사용하였습니다.
    
    ![HomeView_Logined.gif](README%20md%209d1f5de16c0e40e289c93857bd758f4e/HomeView_Logined.gif)

    - 사용 코드(HomeView.vue)
    ![rec1.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/rec1.PNG)
    
2. TicketList의 영화 추천
    
     TicketList에 등록한 영화들의 장르들을 포함하고 있는 영화들 중 3개의 영화를 랜덤으로 추천합니다. 랜덤을 뽑은 알고리즘은 lodash의 sampleSize를 사용하였습니다.
    
    ![TicketList_Detail.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/TicketList_Detail.png)

     - 사용 코드(TicketListDetail.vue)
    ![rec2.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/rec2.PNG)
    

# 6. 서비스 대표 기능에 대한 설명

- Django App 이름 기준으로 기능 분류
- vue(url) 형식으로 기재
1. Accounts
    1. SignUp(/accounts/signup)
        - 회원가입 시 아이디, 비밀번호, 비밀번호 확인, 선호 장르 입력
        
        ![SignupAnimation.gif](README%20md%209d1f5de16c0e40e289c93857bd758f4e/SignupAnimation.gif)
        
    2. LogIn(/accounts/login)
        - 인증된 사용자는 홈 화면과 네브 바 변경됨
        - 인증된 사용자는 리뷰 작성/수정/삭제, 리스트 작성/수정/작성, 댓글 작성/삭제, 좋아요, 팔로우 기능 이용 가능
        
        ![SigninAnimation.gif](README%20md%209d1f5de16c0e40e289c93857bd758f4e/SigninAnimation.gif)
        
    3. LogOut
        - 로그아웃시 홈페이지 이동
        - 로그아웃한 사용자는 권한이 필요한 기능 클릭시 로그인 페이지로 이동
    4. ProfileView(/accounts/<user_id>)
        - 사용자를 팔로우하고, 해당 사용자가 작성한 리뷰들과 리스트들 조회 가능
        
        ![FollowAnimation.gif](README%20md%209d1f5de16c0e40e289c93857bd758f4e/FollowAnimation.gif)
        
2. Movies
    1. MovieListView(/movies)
        - 영화의 포스터, 이름 조회
        
        ![Movies.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/Movies.png)
        
    2. MovieDetailView(/movies/moviedetail/<movie_pk>)
        - 영화 디테일 조회
        
        ![Movies_Detail.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/Movies_Detail.png)
        
    3. SearchView(/search)
        - 영화 검색 기능
        
        ![Searched_complete.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/Searched_complete.png)
        
3. Reviews
    1. ReviewListView(/reviews)
        - 리뷰의 제목, 작성자, 해당하는 영화 조회
        
        ![Reviews.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/Reviews.png)
        
    2. ReviewCreateView(/reviews/<movie_pk>/create)
        - 영화 디테일 페이지에서 리뷰 작성시 이동
        - 제목, 내용, 별점 입력
        
        ![Review_Create.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/Review_Create.png)
        
    3. ReviewDetailView(/reviews/reviewdetail/<review_pk>)
        - 리뷰 디테일 조회(작성자에게만 수정, 삭제 버튼 보이기)
        
        ![Review_Detail_Animation.gif](README%20md%209d1f5de16c0e40e289c93857bd758f4e/Review_Detail_Animation.gif)
        
4. Articles
    1. TicketListView(/ticketLists)
        - 리스트의 제목, 작성자, 리스트를 구성한 리뷰들 조회
        - 좋아요 기능
        
        ![LikeAnimation.gif](README%20md%209d1f5de16c0e40e289c93857bd758f4e/LikeAnimation.gif)
        
    2. createTicketList(/ticketLists/create)
        - 리스트의 제목, 내용 입력, 작성한 리뷰(2-8개)들 선택해서 입력
        
        ![TicketList_Create.PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/TicketList_Create.png)
        
    3. TicketListDetailView(/ticketLists/<ticketlist_pk>)
        - 작성자 클릭 시 프로필 페이지로 이동
        - 리스트 디테일 조회
        - 리스트를 구성한 리뷰와 리뷰한 영화 페이지 이동
        - 리뷰한 영화를 기반으로 한 추천 영화 제시(클릭 시 영화 디테일 페이지 이동)
        - 댓글 생성, 삭제
        - 작성자에게만 수정, 삭제 버튼 보이기
        
        ![TicketList_Detail(other).PNG](README%20md%209d1f5de16c0e40e289c93857bd758f4e/TicketList_Detail(other).png)
        

# 7. 후기

- **박상현🎸 :웹 개발에 대해 배훈 후 시도해보는 첫 프로젝트를 무사히 마칠 수 있어서 좋았다. 웹의 기획부터 풀스택 개발을 진행해 보았다는 것이 앞으로 해나갈 개발에 있어 큰 도움이 될 것 이라고 생각한다. 
  첫 프로젝트였던 만큼 시간 관리가 힘들었다. 처음에 계획했던 기능들 대부분을 완성 시켰지만 몇몇개의 기능은 완성시키지 못하였다. 15가지의 기능 중 12가지를 완성시켰는데 앞으로 프로젝트를 진행하는데 있어 시간관리를 어떻게 해야하는지 경험을 쌓게 해주는 좋은 기회였다고 생각한다. 또한, 처음 기획했던 기능을 그대로 구현하지 못하고 다른 방식으로 바뀌는 것을 경험하며 기획 단계부터 완벽하지 않아도 된다는 것을 깨달았다. 좋은 팀원을 만나 서로 부족한 부분들을 채워줄 수 있는 것이 좋았다. 내가 디자인적인 부분이 부족하다는 것을 깨달았고 이 부분을 팀원이 채워줄 수 있어서 좋았다. 그리고 팀원이 부족했던 서버 쪽 개발을 내가 도맡아서 진행하여 서로 협업이 잘 되었다고 생각한다. 팀원과의 소통을 통해 더 좋은 결과물을 만들어 낼 수 있어서 좋았다.
  이번 프로젝트를 통해 2학기 때 진행될 여러 프로젝트들을 잘 헤쳐 나갈 수 있는 기초 체력을 다질 수 있었다고 생각한다. 방학동안 여러 스택들을 다루어보며 2학기를 준비해야겠다는 생각을 가지게 되었다.

- **원채령🌿 :  개발자가 되기로 다짐한 후 처음으로 만들어낸 온전한 프로젝트라 더욱 의미가 있고 뿌듯했다. 프로젝트의 초기 아이디어부터 데이터베이스의 구조, 웹페이지의 구성과 디자인까지 모두 참여했기 때문에 1학기 동안 배운 기술 스택들을 복습하는 좋은 기회가 되었다고 생각한다. 1학기 동안 9번의 관통 프로젝트를 한 것이 모두 이 마지막 최종 프로젝트를 온전히 구현해내기 위한 밑거름이 되었다는 생각이 들었다. 또 처음인 만큼 완벽히 해내지 못한 부분들에 대해서도 아쉬움이 남았다. 추천 알고리즘을 조금 더 정교화하지 못한 것, 처음에 생각했던 기능인 리뷰를 한 것에 대해 리워드를 부여하기 위해 사용자에게 칭호를 만들기로 한 것들을 시간상의 이유로 해내지 못했다. 그렇지만 이러한 아쉬움을 바탕으로 다음에 더 좋은 프로젝트를 만들어낼 것을 생각하니 더욱 기대가 된다. 혼자였다면 절대 주어진 시간 안에 프로젝트를 완성하지 못했을 텐데, 좋은 팀원을 만나 계획했던 기능들을 거의 다 구현할 수 있었고, 막혔던 부분들에 대해서도 큰 도움을 받았다. 개발자에게 가장 필요한 역량 중 하나인 소통능력과 협업 툴 관리 능력 또한 성장시킬 수 있는 좋은 기회였다.**
