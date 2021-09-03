//2021.09.03

//iterator: 반복가능한 객체 즉, 반복문을 활용해서 데이터를 순회하면서 처리하는 것
// 인터페이스임^^
// 컬렉션의 요소에 접근할 때 한 방향으로만 이동
//함수가 반복 실행되는 경우, 연산을 순차적으로 하지 않고 마지막에 한 번에 연산하게하는 지연평가(lazy) 가능

const arr = [1,2,3,4] // 4기가

interface IterResult<A> { value: A, done?: boolean }

// () => Try<Option<A>>

interface MyIterator<A> {
    next: () => IterResult<A>,
    map: <A, B>(f: (a: A) => B) => MyIterator<B>
}

function mapIter<A,B>(f: (a: A) => B){
    return {
        next: () => {
            const now = this.next()
            return { value: f(now.value), done: now.done }
        },
        map: mapIter
    }
}

// Generator: Iterator를 반환하는 함수
// function 키워드 다음에 별표 ( * )가 추가되고 새로운 yield 키워드를 사용
// toIterator : Array<T> => MyIterator<T>
function* toIterator<T>(arr: Array<T>){
    for (const item of arr.slice(0, arr.length - 1)){
        yield item
    }

    return arr[arr.length - 1]
}

//...은 뿌려주는 것(..? generator인가..?)
const iter: MyIterator<number> = {
    ...toIterator(arr),
    map: mapIter,
}

const double = (n: number) => n * 2;

const x16Iter = iter.map(double)
    .map(double)
    .map(double)
    .map(double)                  //계획만 세우고 실행(연산)은 노노


// toArray : MyIterator<T> => Array<T>
function toArray<T>(iter: MyIterator<T>): Array<T>{
    const result: Array<T> = [];

    let now = iter.next();
    while (! now.done){
        result.push(now.value);
        now = iter.next();
    }
    result.push(now.value);
    return result;
}


const array1: Array<number> = toArray(x16Iter); //여기에서 한 번에 실행

console.log(array1);    //[ 16, 32, 48, 64 ]

const set = new Set([1,2,3,4]);
console.log([...set])   //[ 1, 2, 3, 4 ]
