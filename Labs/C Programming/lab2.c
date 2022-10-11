#include <stdio.h>
void question1();
void question2();
void question3();
void question4();


int main()
{
question1();
return 0;
}

void question1()
{
   int numDigits1(int num);
   void numDigits2(int num, int *result);

   int number, result=0;
   printf("Enter the number: \n");
   scanf("%d", &number);
   printf("numDigits1(): %d\n", numDigits1(number));
   numDigits2(number,&result);
   printf("numDigits2(): %d\n", result);
   return 0;
}

int numDigits1(int num)
{
   int count = 0;
//do - while condition function to check number of digits in a integer
   while (num > 0)
    {
      count++;
      num = num/10;
    }
   return count;
}

void numDigits2(int num, int *result)
{
  while (num > 0)
    {
      *result+=1;
      num = num/10;
    }
}



