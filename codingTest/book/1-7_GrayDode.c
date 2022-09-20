// P.68
// 그레이코드: 연속된 수를 한 비트만 다르게 인코딩하는 방법
// 연속적으로 변하는 양을 나타낼 때, 변화폭이 작아 오류를 줄일 수 있어 데이터 전송에서 많이 쓰인다

// binary -> gray
// 가장 앞자리는 이진코드와 같게
// 그레이 코드의 i번째 자리는 이진코드의 i-1, i자리를 xor 연산한 값이다

// gray -> binary
// 가장 앞자리는 같게
// 이진코드의 i번째 자리는 이진코드의 i-1, 그레이코드의 i자리를 xor 연산한 값이다



// 기가막히다... 멋져... 읽는데 한참 걸렸지만 내가 다음에 짜보지는 못할듯...

#include <stdio.h>
#include <limits.h>

void print_g(int code[], int n, int idx);
void print_r(int code[], int n, int idx);

void print_code(int code[], int len)
{
    int i;

    for (i = 0; i < len; i++)
        printf("%d", code[i]);
    printf("\n");
}

void print_g(int code[], int n, int idx)
{
    if (idx == n) {
        print_code(code, n);
        return;
    }

    code[idx] = 0;
    print_g(code, n, idx+1);
    code[idx] = 1;
    print_r(code, n, idx+1);
}

void print_r(int code[], int n, int idx)
{
    if (idx == n) {
        print_code(code, n);
        return;
    }

    code[idx] = 1;
    print_g(code, n, idx+1);
    code[idx] = 0;
    print_r(code, n, idx+1);
}

int main(void)
{
    int num[100000];
    print_g(num, 3, 0);
    return 0;
}


// 근데 이걸 또 줄이네... awesome..!

void print_gray(int code[], int n, int idx, int reverse)
{
    if (idx == n) {
        print_code(code, n);
        return;
    }

    code[idx] = reverse;
    print_gray(code, n, idx+1, 0);
    code[idx] = 1-reverse;
    print_gray(code, n, idx+1, 1);
}
