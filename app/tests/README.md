# Test 패키지

Application의 품질을 책임질 테스트 패키지

테스트 코드 작성 순서

1. Model(SQLAlchemy ORM, Marshmallow Schema) 작성
2. Model을 이용한 Repository 작성
3. Usecase 작성 (Repository, Schema 사용)