## 디버깅
- print 함수 활용
    - 특정 함수 결과, 반복/조건 결과 등 나눠서 생각, 코드를 bisection으로 나눠서 생각
- 개발 환경(text editor, IDE) 등에서 제공하는 기능 활용
    - breakpoint, 변수 조회 등
- Python tutor 활용 (단순 파이썬 코드인 경우)
- 뇌컴파일, 눈디버깅

---

## 예외
실행 중에 감지되는 에러들을 *예외*라고 지칭
- ZeroDivisionError
    - 0으로 나누고자 할 때 발생
- NameError
    - namespace 상에 이름이 없는 경우
- TypeError
    - 타입 불일치, argument 누락, argument 개수 초과, argument type 불일치
- ValueError
    - 타입은 올바르나 값이 적절하지 않거나 없는 경우
- IndexError
    - 인덱스가 존재하지 않거나 범위를 벗어나느 경우
- KeyError
    - 해당 키가 존재하지 않는 경우
- ModuleNotFoundError
    - 해당 모듈이 존재하지 않는 경우
- ImportError
    - 모듈은 있으나 존재하지 않는 클래스/함수를 가져오는 경우
- KeyboardInterrupt
    - 임의로 프로그램을 종료하였을 때
- IndentationError
    - Indentation이 적절하지 않는 경우
---

## 예외처리

try 문
- 오류가 발생할 가능성이 있는 코드를 실행
- 예외가 발생하지 않으면, except 없이 실행 종료
except 문
- 예외가 발생하면, except 절이 실행
- 예외 상황을 처리하는 코드를 받아서 적절한 조치를 취함

## 에러 메시지 처리 (as)

## 예외 처리 종합
- try
    - 코드를 실행
- except
    - try 문에서 예외가 발생 시 실행함
- else
    - try 문에서 예외가 발생하지 않으면 실행함
- finally
    - 예외 발생 여부와 관계없이 항상 실행함
