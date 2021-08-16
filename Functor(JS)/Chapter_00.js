//2021.08.16

//const는 상수형
const message: string = "hello world";
//console.log() 콘솔에 출력
console.log(message);

// PowerShell에서 js&ts 설정을 위해 진행한 내용
// tsc ch1.ts
// Set-ExecutionPolicy RemoteSigned

//상수형 리스트도 만들 수 있다
const priceList = [1000,2000,3000,4000];

//함수형 코딩을 위해 기억해야하는 것 두 가지!
// 1. 순수 함수 조합한다
    // (traditional) (pain points)
    // for            여러 개다 => []   [1]   [1,2,3,4] => Array map
    // if null        값이 null일 수도 있다 Option map
    // try catch      Try
    // async 비동기    Promise
    // 여러번 반복     매번 값이 달라짐 (side effect 부분때문에)

// 2. 복잡한 Context 를 추상화해서 처리한다.
    // 함수와 effect를 분리!

const c = 'hello world';

//type을 만들(지정할) 수도 있다
type Bool = true | false; // 유니온 타입
const f: Bool = true;


function getTotalPrice(price: number): number {
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
function pushArray<T>(arr: Array<T>, value: T): Array<T>{
    //.puch()는 .append()처럼 list에 값을 하나 추가하는 것
    arr.push(value);
    return arr;
}
