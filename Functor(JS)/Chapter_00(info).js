//2021.08.16

//함수형 코딩을 위해 기억해야하는 것 두 가지!
// 1. 순수 함수를 조합해서 풍부한 프로그램을 짠다
    // (traditional)  (pain points)                                     (how to solve) 
    // array (for문)   값이 여러 개(0개, 1개, 여러개)일 가능성(비결정적)   => map(a => b)
    // if null         리턴되는 값이 null일 수도 있다                    => Option
    // try catch       에러가 발생할 수 있다                             => Try
    // async 비동기    언제 리턴될 지 & 어떤 순서로 실행될 지 모른다       => Promise
    // 여러번 반복      매번 값이 달라짐 (side effect 부분때문에)
    // Iterator
    // Observable

// 2. 복잡한 Context를 추상화해서 처리한다 ('처리'를 분리해서 map Functor 같은 친구들로 만든다)
    // 함수와 effect를 분리!
    // 인터페이스와 구현의 분리!



//const는 상수형
const message: string = "hello world";
//console.log() 콘솔에 출력
console.log(message);

// PowerShell에서 js&ts 설정을 위해 진행한 내용
// tsc ch1.ts
// Set-ExecutionPolicy RemoteSigned

//상수형 리스트도 만들 수 있다
const priceList = [1000,2000,3000,4000];

const c = 'hello world';

//type을 만들(지정할) 수도 있다
type Bool = true | false; // 유니온 타입 - Union, 합집합
const f: Bool = true;     // 상수 변수 f는 데이터 타입이 (위에서 선언한) Bool이고, 그 값은 true이다


function getTotalPrice(price: number): number { //getTotalPrice라는 함수를 선언. price라는 number타입의 파라미터와 number타입의 return 값을 가진다
  const discountRate = 0.9;
  const vatRate = 1.1;
  return price * discountRate * vatRate;
}

const 사과_가격 = 5000;
const 오렌지_가격 = "4000";
const 바나나_가격 = 3000;
const result = getTotalPrice(2000);

//<T>는 어떠한 type이 올 수 있다는 것 (어떤 type이던지 상관 없게 되는건 any!)
//하기의 내용에서 T는 모두 동일한 데이터 타입이 와야 한다
function pushArray<T>(arr: Array<T>, value: T): Array<T>{ //pushArray라는 함수를 선언하는데, 이 함수에서는 T라는 데이터 타입을 쓸거다
                                                          //T 데이터 타입의 Array인 arr과 T 데이터 타입의 value를 파라미터로 받아서
                                                          //T 데이터 타입의 Array를 
    //.push()는 .append()처럼 list에 값을 하나 추가하는 함수
    arr.push(value);
    return arr;
}
