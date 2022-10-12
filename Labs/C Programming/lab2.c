#include <stdio.h>
void question1(void);
void question2(void);
void question3(void);
void question4(void);


int main()
{
question2();
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

void question2()
{
/*
Purpose of program: if number = 12344 , digit = 3
Call by parameters - printf: DigitPos1(): 3
Call by reference -  printf: DigitPos2(): 3
 */
    
   //Function prototypes
    int digitPos1(int num, int digit);
    void digitPos2(int num, int digit, int *result);
    int number, digit,result=0;
    
    //user-input request : number & digit
   
    printf("Enter the number:\n");
    scanf("%d",&number);
    printf("Enter the digit:\n");
    scanf("%d",&digit);
    
    printf("DigitPos1():%d\n",digitPos1(number,digit));
    
    digitPos2(number,digit,&result);
    printf("DigitPos2():%d\n",result);
    
}

int digitPos1(int num, int digit)
{
    int pos = 0;
    /*
Do - loop : pos initialized at 0 ,num = 1234
first iteration: position = 1   , if-else checks if num = digit and returns pos = 1 if true.
                 else - num = 123 = 1234/10.
                 while condition checks that if num is still greater than 0.
    
second iteration: similar to first iteration
last iteration: when num%10 == digit, if-else statement will return pos back to caller function.
     */
    do
    {
        pos++;
        if (num % 10 == digit)
            return pos;
        num = num/10;
    }
    while (num > 0);
    return 0;
}

void digitPos2(int num, int digit, int *result)
{
    do
    {
        *result+=1;
        if (num%10 == digit)
            break;
        else
            num = num/10;
    }
    while (num > 0);
}
