# try ~ except 문 사용 가능
# except 뒤에는 발생오류를 적어 예외에 따라 각기 다른 방식의 처리를 할 수 있다

# 여러 개의 except를 적을 수 있으며,
# 1) 가장 먼저 발생한 에러만
# 2) 그 에러가 가장 먼저 만나는 부합하는 except만 실행된다

try:
    4/0
    with open ("txt.txt", 'r') as f:
        f.readlines()

except ZeroDivisionError as e:  #0으로 나눴다
    pass  #에러가 발생하더라도 그냥 통과해라
    #print(e)

#2개 이상의 오류를 한 번에 처리하는 방법도 있는데, 에러를 괄호로 묶는 것이다    
except (IndexError, FileNotFoundError) as e: #인덱스가 없다, 파일이 없다
    print(e)

#모든 에러는 except
except:
    print("에러 발생!")
    
#에러 발생 여부와 상관 없이 실행해야 하는 것은 finally 안에!    
finally:
    print("그래도 이건 해조")


    
    
#일부러 오류 발생
class Bird:
    def fly(self):
        #Bird 클래스를 상속받는 자식 클래스는 fly 함수를 구현해야한다
        #NotImplementedError: 작성해야 하는 부분이 구현되지 않았을 경우 오류를 일으킨다(raise)
        raise NotImplementedError

class Eagle(Bird):
    #pass
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly() #Bird 클래스의 fly 함수를 사용하는 경우 에러 발생한다




#예외 만들기
#파이썬 내장 클래스인 Exception을 상속해 만든다!
class MyError(Exception):
    def __str__(self):  #as e 구문 사용을 위해 메서드 정의
        return "허용되지 않은 별명입니다."
    #pass

def say_nick(nick):
    if nick == '바보':
        raise MyError()
    print(nick)

#예외 처리
try:
    say_nick("천사")
    say_nick("바보")
except MyError as e:
    print(e)
except:
    print("허용되지 않은 별명입니다")
