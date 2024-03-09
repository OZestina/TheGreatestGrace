#로그를 출력하는 표준 라이브러리 logging import
import logging

#로그 포맷 정하기 (로그 설정)
# 설정 이후 생성한 모든 logger에 대해 해당 설정이 반영된다
# logging.basicConfig(format='포맷 문자열', level=로그레벨)
# 변수 %(변수명)s 의미
# %(name)s         logger명
# %(levelno)s      로그 레벨 번호
# %(levelname)s    로그 레벨 이름
# %(pathname)s     (이용 가능 시) 소스 코드 파일의 전체 경로
# %(filename)s     소스 코드 파일명
# %(module)s       모듈명
# %(lineno)s       (이용 가능 시) 행 번호
# %(funcName)s     함수, 메서드명
# %(asctime)s      logRecord가 만들어진 시간
# %(thread)s       (이용 가능 시) 스레드 ID
# %(threadName)s   (이용 가능 시) 스레드명
# %(process)s      (이용 가능 시) 프로세스 ID
# %(message)s      (메서드 실행 시 전달된) 메시지

# 시간 - 로거명 - 로그레벨 - 로그메시지
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

#로그 레벨: 로그 내용의 심각도를 레벨로 나타냄
# 로거 또는 로그 핸들러 별로 로그 레벨을 설정할 수 있다
# 설정하지 않을 시 default 값은 warning 레벨
# level             |  method(message로 출력할 내용)
logging.DEBUG       |  debug()
logging.INFO        |  info()
logging.WARNING     |  warning()
logging.ERROR       |  error()
logging.CRITICAL    |  critical()  #치명적인 에러 출력

#로그 얻기
# logging.getLoggger("로거명")
# 로그를 출력하는 객체인 logger 생성
# 생성 시 로거명을 설정할 수 있으며, 보통 모듈명으로 설정하는 경우가 많다. 특수변수 __name__을 사용하면 모듈명으로 세팅된다
logger = logging.getLogger(__name__)


#로거 출력 메서드
logger.debug("디버그")    #출력 레벨 info 이상이므로 해당 로그는 출력되지 않는다
logger.info("정보 출력")
logger.warning("경고 발생")
logger.error("에러 발생!!!!")




#로그 핸들러 설정

# 출력위치를 설정할 때는 기본 제공되는 핸들러를 지정한다.
# logging.basicConfig(handlers=[핸들러1, 핸들러2, ...])

# 표준 출력과 파일 출력을 같이 하고 싶을 때는 핸들러를 2개 생성해 지정하면 된다
# logging.StreamHandler()             #표준 출력
# logging.FileHandler("출력 위치 경로")  #파일 출력
std_handler = logging.StreamHandler()
file_handler = logging.FileHandler("tmp.log")  #현재 디렉토리 아래에 tmp.log 파일이 생성되고 표준출력과 같은 로그가 기록된다

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    handlers=[std_handler, file_handler])
