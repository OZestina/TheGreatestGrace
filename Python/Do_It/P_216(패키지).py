# 모듈을 import
import game.play.playing
game.play.playing.playing_test()

# 모듈이 있는 디렉터리까지 from으로 잡고 .py만 import
from game.play import playing
playing.playing_test()

# .py까지 from으로 잡고 함수만 import
from game.play.playing import playing_test
playing_test()

#__init__.py
#해당 디렉터리가 패키지의 일부임을 알려주는 역할
#__init__.py 파일이 없다면 패키지로 인식되지 않는다

#특정 디렉터리의 모듈을 *를 사용해 import할 때는
#해당 디렉터리의 __init__.py파일에 __all__변수를 설정하고 import 가능한 모듈을 정의해야한다
from game.play import *
playing.playing_test()

#----------------------------------------------------
# __init__.py
# *를 사용해 패키지를 import할 경우
# __all__에 정의된 모듈만 import된다
__all__ = ['playing']
