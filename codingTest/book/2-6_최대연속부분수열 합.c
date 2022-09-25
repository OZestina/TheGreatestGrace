// P.104
// 와 너무 재미있었다 (+ 머리 아픔)
// 

#define N 100
#define max(x, y) ((x)>(y)?(x):(y))

int c[N];

# 1st ==========================================

int max_sum2(int s[], int n)
{
	if (n == 1)
		return s[0];
	return max(max_sum2(s, n-1) + s[n-1], s[n - 1]);
}

int max_sum1(int s[], int n)
{
	if (n == 1)
		return s[0];
	return max_sum1(max_sum2(s, n), max_sum1(s, n-1));
}

# 2nd ==========================================

void cal_max_sum2(int s[], int n)
{
	int i;

	c[0] = s[0];
	for (i = 1; i < n; i++)
		c[i] = max(s[i], c[i-1] + s[i]);
}

int new_max_sum1(int s[], int n)
{
	if (n == 1)
		return s[0];
	return new_max_sum1(c[n-1], new_max_sum1(s, n-1));
}

# 3rd ==========================================

void cal_max_sum2(int s[], int n);

int new_new_sum1(int s[], int n)
{
	int max_sum, i;

	max_sum = s[0];
	for (i = 1; i < n; i++)
		if (max_sum < c[i])
			max_sum = c[i];
	return max_sum;
}
