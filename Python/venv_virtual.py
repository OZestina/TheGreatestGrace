#프로그램이나 프로젝트 별로 가상환경을 구축해 관리할 수 있다

#가상환경 구축
python -m venv {가상환경 경로}
ex) python -m venv myVenv1
    => (현재 디렉토리에) myVenv1 이름의 가상환경 구축

#가상환경 전환
#만들어진 가상환경 디렉터리 아래 ./bin/activate 파일 생성됨
unix 계열: (가상환경 디렉터리에서) source ./bin/activate
ex) source myVenv1/bin/activate

#가상환경 종료
deactivate 명령어 실행
