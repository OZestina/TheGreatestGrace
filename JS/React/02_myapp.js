//터미널에서
npx create-react-app my-app
npm start //실행 파일 경로 my-app으로 되어있는지 확인!


import {useState, useEffect} from 'react';

//useState(초기값) 은 [수, 수 세팅 함수] 의 '튜플'을 리턴한다
const [counter, setCounter] = useState(0)

//setCounter(수): 해당 수로 set
//setCounter(변수 => sth): 변수에는 이전값이 들어있다 (자동)
function handleClick (event) {
  console.log(event)
  setCounter(prev => prev+1)
}

//DOM이 새로 불러와질때마다 (화면이 새로고침될때마다) 실행되는 함수
//중괄호 뒤에 추가 인자를 통해 불리는 기준을 추가할 수도 있다
useEffect(() => {
  const w = window.innerWidth
  const h = window.innerHeight
  console.log(w,h)
})
//line 22 => }, [counter])


//html에는 이렇게
<p>
  {counter}
</p>
