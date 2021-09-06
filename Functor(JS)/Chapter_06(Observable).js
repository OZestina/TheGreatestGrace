type DerivedObservable<B> = {
  subscribe: (react: (v: B) => void) => void;
};

type Observable<A> = {
  value: A;
  update: (f: (old: A) => A) => void;
  subscriber: Array<(v: A) => void>;
  subscribe: (react: (v: A) => void) => void;
  // (v)=>{result!.innerHTML = `${v}`;}
  map: <B>(f: (a: A) => B) => DerivedObservable<B>;
};

// 상태를 업데이트 update 하면 ...
// 상태 변화가 derived된 -> map 된 친구들에게 전파
// subscribe 했던 친구들이 dom을 최신화하는 등 effect

function createObservable<A>(initValue: A): Observable<A> {
  return {
    value: initValue,
    update: function (f: (old: A) => A) {
      // value 의 상태를 f함수를 이용해서 업데이트한다
      this.value = f(this.value);
      // 구독하고 있는 함수들(subscriber)을 모두 실행한다. // 부수효과
      this.subscriber.forEach((f) => f(this.value));
    },
    subscriber: [],
    subscribe: function (react: (v: A) => void) {
      // 구독하면 react 라는 함수를 subscriber에 넣는다
      this.subscriber.push(react);
    },
    map: function <B>(f: (a: A) => B): DerivedObservable<B> {
      const derivedObservable = {
        subscribe: (react: (v: B) => void) => {
          //함수 f를 원래 값인 A에 적용해서 새로운 Observable을 만든다.
          // v => v에 f를 적용한 값을 react에 넣고 실행하는
          this.subscriber.push((v) => react(f(v)));
        }
      };
      return derivedObservable;
    }
  };
}

let counter = createObservable(0);
const doubleCounter = counter.map((v) => v * 2);

document.getElementById("app")!.innerHTML = `
<h1>반응형 카운터</h1>
<div>
  <h3 id="result">${0}</h3>
  <h3 id="result2">${0}</h3>
  <button id="incButton">+1</button>
  <button id="resetButton">reset</button>
  <button id="descButton">-1</button>
</div>`;

// 버튼을 만든다
const incButton = document.getElementById("incButton");
const descButton = document.getElementById("descButton");
const resetButton = document.getElementById("resetButton");

const increase = () => counter.update((v) => v + 1);

// 버튼을 클릭하면
incButton?.addEventListener("click", increase);
resetButton?.addEventListener("click", (e) => counter.update((v) => 0));
descButton?.addEventListener("click", (e) => counter.update((v) => v - 1));

const result = document.getElementById("result");
counter.subscribe((v) => {
  result!.innerHTML = `${v}`;
});


const result2 = document.getElementById("result2");
doubleCounter.subscribe((v2) => {
  result2!.innerHTML = `${v2}`;
});

// counter + 1 해주고
// dom에 렌더링해야한다.
