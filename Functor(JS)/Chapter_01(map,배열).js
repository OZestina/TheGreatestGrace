//2021.08.20
//map, 배열

type BlogT = {  //BlogT라는 타입 선언 및 어떤 타입인지 정의
  slug: string,
  frontmatter: {
    title: string,
    excerpt: string,
    date: string,
    author: string,
    tag: string
  },    
  html: string,
}

const testBlog: BlogT = { //BlogT 타입의 testBlog를 상수 변수로 선언
    slug: 'customize-elder-blog',
    frontmatter: {
      title: 'Elder 블로그 커스터마이징 하기',
      excerpt: 'Elder 기본 템플릿에 웹 폰트, 날짜 순 정렬, tooltip 같은 기능들을 추가해봅니다.',
      date: '2021-07-08T05:01:27.798Z',
      author: '탐정토끼(Taehee Kim)',
      tag: '작성 중, Svelte ,  Elder.js, Blog'
    },
  html: '...생략합니다'
};

//함수를 파라미터로 전달할 수도 있다 ------------------ 이거 왜 에러뜨지ㅠ
function map1(arr, func){
  const result = [];
  for (let i = 0; i < arr.length; i++){
    result[i] = func(arr[i]);
  }
  return result;
}

//함수 정의 방법_1
function double1(n){ //함수명은 double1, 파라미터가 n
  return n * 2;
}

//함수 정의 방법_2
const double2 = (n: number) => n * 2; //number타입 n을 받아서 n*2를 리턴해라
                                      //(리턴한 값을 double2에 저장)

//map1에 arr과 func을 전달
console.log(map1([1,2,3], (n) => n * n ));


//blogList.json파일 불러와서 blogList에 저장
//json에 저장된 값은 BlogT 데이터 타입의 Array
const blogList: Array<BlogT> = require("./blogList.json");


function getTagList(blog: BlogT): Array<string> {
  return blog.frontmatter.tag //blog의 frontmatter의 tag 값을 가져와라
    .split(",")               //","으로 나눠라 (Array 리턴)
    .map(tag => tag.trim());  //Array에 저장된 tag를 tag.trim()한 값으로 바꿔라
}

//.flat()은 리스트 합치는 것
const allTagList = blogList.map(getTagList).flat();
const allTagList = blogList.flatMap(getTagList);


// Context map -> Functor
const expected = [ 
    '문자열',               '표준 라이브러리',   '작성 중',
    'front-end',           'CSR',             'SPA',
    'SSR',                 'JAM Stack',       '작성 중',
    '개념어',               'Trade Off',       '작성 중',
    'Svelte',              'Elder.js',        'Blog',
    'Svelte',              'Elder.js',        'Github Pages',
    'Blog', // ...
]


//.filter를 이용해 선택적인 값만 배열로 추출할 
[1,2,3,4].filter(n => n % 2 == 1) // [1,3]

// F12에서 실행해볼 수 있다

/*
<참고 자료>
// https://twinstae.github.io/

[모던 자바스크립트 튜토리얼 : while 과 for 반복문]

[모던 자바스크립트 튜토리얼 : 함수 표현식]
[모던 자바스크립트 튜토리얼 : 화살표 함수 기본]
[모던 자바스크립트 튜토리얼 : 화살표 함수 다시 살펴보기]

[모던 자바스크립트 튜토리얼 : 배열과 메서드] map, filter, reduce
*/
