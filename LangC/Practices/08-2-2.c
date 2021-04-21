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
