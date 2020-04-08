# 0011 - vote 서비스 코드. 


Boilerplate project using Django and Django REST Framework.
Currently supporting only Python 3.x.

**IMPORTANT**:

혹시 궁금하신 내용이 있으시면, team0011kr@gmail.com 으로 연락주세요. 
마이그레이션 파일과 중간에 이슈가 있는 부분까지 먼저 업데이트 후 차례로 정리할 예정입니다.

이걸 처리하는 것도 중요하다고 생각되기에 공유합니다. 

.env 파일을 만들어서 시작할 수 있습니다. 
.env 파일의 샘플은 다음과 같습니다. DB 샘플의 경우 위의 메일로 연락주시면 좋겠습니다. 

지금은 (2020년 4월 8일기준으로) docker와 테라폼을 사용하고 있지는 않습니다.

```
COMPOSE_PROJECT_NAME=vote21
DJANGO_DEBUG=False
DB_NAME=
DB_HOST=
DB_PORT=
DB_USER=
DB_PASSWORD=
```