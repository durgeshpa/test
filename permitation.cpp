#include <iostream>
using namespace std;
void permitation(char input[],char output[],bool cheak[],int lavel,int size)
{
	if (lavel==size)
	{
		for(int i=0;i<size;i++)
		{
			cout<<output[i];
			
		}
		cout<<"\n";
	}
	else
	{
		for (int i = 0; i < size; ++i)
		{
			
			if (cheak[i]==0)
			{
				continue;
			}
			else 
			{
				cheak[i]-=1;
				output[lavel]=input[i];
				permitation( input, output, cheak,lavel+1, size);
				cheak[i]+=1;
			}
		}
	}
}
int main(int argc, char const *argv[])
{
	char x[]={'a','b','c'};


	char y[3];
	bool c[3]={1,1,1};
	permitation( x, y, c,0, 3);

	return 0;
}