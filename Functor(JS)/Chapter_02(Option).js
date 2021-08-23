//2021.08.23
//옵션, 트라이

//PowerShell에서 .ts 파일 실행하기
//해당 파일이 있는 디렉토리에서 하기 명령어 실행
//ts-node 파일명.ts

// 순수 함수를 조합해서 풍부한 프로그램을 짠다
// 복잡한 Context에 대한 '처리'를 분리해서 map Functor 같은 친구들로 만든다

// Array   값이 여러 개 (비결정적)다 map(a => b)
// Option  null
// Try     error

// Promise 언제 올지 모른다 -> 어떤 순서로 실행될지 모른다
// Iterator
// Observable


//평균을 내는 함수를 정의해보자
[1,2,3] // 1 + 2 + 3 / 3

//리스트 내 수의 총합을 리턴하는 sum 함수 정의
function sum(arr: Array<number>): number {
    let total = 0;
    for (const n of arr){
        total += n;
    }
    return total;
}

//Option<T>라는 데이터 형을 정의하는데, 그 값은 T이거나, null이다
//T에는 어떤 데이터 형도 올 수 있다
type Option<T> = T | null;

//number 데이터형 Array를 받아 평균값을 리턴하는 average 함수 정의
//리턴형은 Option<number>로, number값이거나 null이다
function average(arr: Array<number>): Option<number> {
    if(arr.length === 0){ //나누는 값이 0일 경우 null 리턴
      return null;
    }
    return sum(arr) / arr.length;
}

//3배를 하는 triple 함수의 정의
//화살표 함수는 값을 리턴해서 함수에 바로 넘기는 것도 가능
const triple = (n: number) => n * 3;


//null값이 대입될 경우를 대비한 camp 선언
function cmap<A,B>(func: (a: A) => B): (optionA: Option<A>) => Option<B>{
    return function(optionA){
        if (optionA === null){
            return null;  // null
        } else {
            return func(optionA); // B
        }
    }
}
// cmap은 (순수)함수를 받아서 => context를 처리할 수 있는 함수 
// f: a: A => B          map =>   Array<A>     =>  Array<B>
//  태그 => 트림한 태그           Array<Tag>   =>  Array<TrimTag>
// (f: (a: A) => B)      map =>   Option<A>    => Option<B>

const optionTriple = cmap(triple)

triple(3) // 9
triple(null) // 할 수 없어 엉엉

optionTriple(3) // 9
optionTriple(null) // null

//cadd 정의
function cadd(a: number): (b: number) => number {
  return b => b + a;
}

const cadd4 = cadd(4) // 4를 더해주는 함수를 만든다...

cadd4(5) // 9
cadd4(3) // 7

const cadd3 = cadd(3) // 3을 더해주는 함수를 만든다...
cadd3(5) // 8

// null undefined NaN Infinity
// console.log(3 / 0) // Infinity
// console.log(0 / 0) //
// console.log([])    // null

// 전체함수 부분함수 -> 일부만 처리할 수 있으면 부분함수.
// (null인 경우 처리 못해... 홀수는 처리 못해... 음수는 처리 못해...)

// curry 은 매개변수 여러 개를 받는 함수를 -> 한 개씩 받아서 새로운 함수를 만들어주는 것
function cadd_2(a){
    return (b) => a+b
}

function cadd_3(a){
    return function(b){ return a+b }
}

function cadd_4(a){
    function addA(b){
        return a+b
    }
    return addA;
}

// map이라는 건 그냥 함수를... 복잡한 Context를 처리할 수 있는 함수로 만들어주는구나
