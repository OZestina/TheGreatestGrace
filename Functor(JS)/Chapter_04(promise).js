//2021.08.30

// 언제 값이 리턴될 지 & 어던 순서로 실행될 지 모르는 상황이 발생
// sync(동기) 방식, 즉 순차적으로 일을 스스로 끝내 나가는 방식은 비효율 발생!
// => 해야 할 일을 위임하고 기다리는 방식인 Async(비동기) 방식으로 코딩을 해보자

function createWaitPromise(duration: number): Promise<null>{
    return new Promise((resolve) => {
        setTimeout(resolve, duration);
    })
}

//async 함수 선언 방법
async function getAsyncOne(){
    await createWaitPromise(500);
    return 1;
}

const onePromise2 = getAsyncOne();

//12~17을 이렇게 코딩할 수도 있다
function getOne(): Promise<number>{
    return createWaitPromise(500).then(() => 1);
}

const p = Promise.resolve(3) // Promise<3>
const p2 = Promise.resolve() // Promise<void>
              .then(() => 3) // Promise<3>

// Array<A> => Array<B>
// 0.5초 기다린다 Promise<void>  =>  Promise<number> 
const ninePromise = createWaitPromise(500)
    .then(() => 3)   // promise<3>
    .then(a => a * a); // promise<9>

function getPromiseOne(): Promise<number>{
    return new Promise((resolve) => {
        setTimeout(()=> {
            resolve(1);
        }, 500);
    })
}


const onePromise = getOne();

const wait1SecondPromise = createWaitPromise(1000)
    .then(() => "i am here")
    .then(message => message + ". taehee...");

console.log(wait1SecondPromise) //Promise { <pending> } 라고뜨는데 왜인지 모르겠슴..

wait1SecondPromise
    .then(async ()=>{
        console.log("hello promise!");
        await createWaitPromise(1000);

        console.log("hello promise2!");
        await createWaitPromise(500);

        console.log("end!" + 1);
    })
    .then(()=>{
        console.log(wait1SecondPromise);
    })
