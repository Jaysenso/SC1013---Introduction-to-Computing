#include <stdio.h>
#include <math.h>

//Function definitions
void question1();
void question2();
void question3();
void question4();

//main function to execute specific question function
int main()

{
    question4();
    return 0;
}

//Question 1 - Grades benchmark 
void question1()
{
 int studentNumber = 0, mark;

    printf("Enter Student ID:");
    scanf("%d",&studentNumber);
    while (studentNumber!= -1)
    {
        printf("Enter Mark:");
        scanf("%d",&mark);
        switch(mark)
        {
            case 75 ... 100:
                printf("Grade = A\n");
                break;
            case 65 ... 74:
                printf("Grade = B\n");
                break;
            case 55 ... 64:https://github.com/Jaysenso/SC1013
                printf("Grade = C\n");
                break;
            case 45 ... 54:
                printf("Grade = D\n");
                break;
            default:
                 printf("Grade = F\n");
                 break;
        }
    }
return 0;
}

//Question 2 - Average calculation w. quit functionality
void question2()
{
    int user_lines = 0 ,lines;
    printf("Enter number of lines:");
    scanf("%d",&user_lines);
    int input = 0, index = 0;
    float sum = 0;
    for (lines=0;lines<user_lines;lines++)
    {
        printf("Enter line %d (end with -1):\n",lines+1);
        while (input != -1)
        {
            scanf("%d",&input);
            if (input != -1)
            {
                sum = sum + input;
                index++;
            }
        }
    }

    float average = sum / index;
    printf("Average = %.2f",average);

return 0;
}

//pattern printing with modulus (1-2-3-1-2-3)
void question3()
{
//height is user defined
int height = 0;

//prompt for user_input 
printf("Enter the Height:");
scanf("%d",&height);

//nested for loop for 2D array
//Loop for rows
for (int row=1;row<height+1;++row)    
{
    //Loops for columns
    for (int column=0;column<row;++column)
    {
        //conditional operator : it prints according to the number of rows (1-2-3-1-2-3-1-2)
        printf("%d" , row % 3 == 0 ? 3 : row % 3);
    }
    printf("\n");
}
return 0;
}

//Factorial calculation with for loop
void question4()
{
//declarations
int fact = 1;
float y= 0,x = 0, result = 0;

//Prompt for user_input of pow(x)
printf("Enter x:");
scanf("%f",&x);

//Generate 10! factorial using for loop
for (int i=1;i<=10;i++)
{
    fact = fact*i;
    result = result + pow(x,i)/fact;
    //Debug prompt to check values of x and fact loop
    printf("x:%.3f fact:%d \n",x,fact);
}
printf("Result = %.2f",result+1);
return 0;
}










