# 필요 소프트웨어

- 런타임 버전 관리: [mise](https://mise.jdx.dev/getting-started.html)
  - 설치 후 .bashrc 및 .zshrc에 mise activate 필요
- 가상 환경 및 종속성 관리: [uv](https://docs.astral.sh/uv/getting-started/installation/)
	- 관련 명령어는 슬라이드 참조
	
# Django 관련
- [Django 튜토리얼](https://docs.djangoproject.com/ko/5.1/intro/tutorial01/)
- Django 종속성 설치 및 초기화 (두 명령어 다 프로젝트 디렉토리에서 실행)
  - `uv add Django`
  - `django-admin startproject mysite .`

# 데이터베이스 관련
- 데이터베이스 클라이언트 [Dbeaver](https://dbeaver.io/download/)
- Django의 PostgreSQL 플러그인 [Psycopg2](https://www.psycopg.org/install/) 
	- `uv add psycopg2-binary` 로 설치

# AWS RDS
- 다음 옵션을 선택할 경우, 많은 요금이 나올 수 있음
  - 프로덕션 수준으로 배포
  - Multi-AZ
  - CloudWatch 모니터링
  - 필요 이상으로 높은 사양의 인스턴스 
    - micro로 끝나는 인스턴스로도 연습은 충분히 가능