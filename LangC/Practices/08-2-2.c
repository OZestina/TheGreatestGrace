//without Continue & Break

#include <stdio.h>

int main(void)
{
	int a, z;

	for(a=1; a<10; a++)
	{
		for(z=1;z<10;z++)
		{
			if (a+z==9)
				printf("A: %d, Z: %d\n", a, z);
		}
	}

	return 0;
}

//2nd try with Continue & Break

#include <stdio.h>

int main(void)
{
	int a=1, z=1;

	while(1)
	{
		for(z=1; z<10; z++)
		{
			if(a+z != 9)
				continue;
			else
				printf("A: %d, Z: %d\n", a, z);
		}
		a++;
		if(a>9)
			break;
	}

	return 0;
}


//답지

#include <stdio.h>

int main(void)
{
	int a, z;
	int result;
	for(a=0; a<10; a++)
	{
		for(z=0; z<10; z++)
		{
			if(a==z)	//굳이? if(a+z<9) 라고 하면 더 빠른 연산이 가능할듯.
				continue;
			result=(a*10+z)+(z*10+a);
			if(result==99)
				printf("%d%d + %d%d = %d\n", a,z,z,a,result);
		}
	}
	return 0;
}
