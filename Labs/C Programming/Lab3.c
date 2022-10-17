//
//  main.c
//  Lab3
//
//  Created by J'sen Ong on 17/10/22.
//

#include <stdio.h>


void question1(void);
void question2(void);
void question3(void);
void question4(void);


int main()
{
int choice;
    choice = 3;
    switch(choice)
    {
        case 1:
            question1();
        case 2:
            question2();
        case 3:
            question3();
    }
    while (choice <2);
}



void question1()
{
    #define INIT_VALUE -1000
    int findAr1D(int size,int ar[],int target);
    int ar[20];
    int size,i,target,result =INIT_VALUE;


    printf("Enter array size:\n");
    scanf("%d",&size);
    
    printf("Enter %d data:\n",size);
    for (i=0;i<=size-1;i++)
    {
        scanf("%d",&ar[i]);
    }
        
    printf("Enter the target number:\n");
    scanf("%d",&target);

        
    result = findAr1D(size,ar,target);
    if(result==-1)
        printf("findAr1D(): Not found\n");
    else
        printf("findAr1D(): %d",result);
    
}


int findAr1D(int size,int ar[], int target)
{
    for (int i=0;i<=size-1;i++)
        if (target == ar[i])
            return i;

    return -1;
}

void question2()
{
#define SIZE 3
    //the function swaps the row r1 with the row r2 of a 2D array
    void swap2Rows(int ar[][SIZE],int r1, int r2);
    // the function swaps the column c1 with the column c2 of a 2D array
    void swap2Cols(int ar[][SIZE], int c1, int c2);
    void display(int ar[][SIZE]);
    
    int array[SIZE][SIZE];
    int row1,row2,col1,col2;
    int i,j;
    int choice;
    
    // UI display
    printf("Select one of the following options:\n");
    printf("1: getInput()\n");
    printf("2: swap2Rows()\n");
    printf("3: swap2Cols()\n");
    printf("4: display()\n");
    printf("5: exit()\n");
    
    
    do
    {
        printf("Enter your choice:\n");
        scanf("%d",&choice);
        
        switch (choice)
        {
            // matrix population
            case 1:
                printf("Enter the matrix (3x3): \n");
                for (i=0;i<SIZE;i++)
                    for (j=0;j<SIZE;j++)
                        scanf("%d",&array[i][j]);
                break;
                
            // Swap2Rows
            case 2:
                printf("Enter two rows for swapping:\n");
                scanf("%d %d",&row1,&row2);
                swap2Rows(array,row1,row2);
                printf("The new array is:\n");
                display(array);
                break;
                
            // Swap2Cols
            case 3:
                printf("Enter two columns for swapping:\n");
                scanf("%d %d",&col1,&col2);
                swap2Cols(array,col1,col2);
                printf("The new array is:\n");
                display(array);
                break;
                
            // Display
            case 4:
                display(array);
                break;
        }
    } while (choice <5);
    
}

void display(int ar[][SIZE])
{
    int I,m;
    for (I=0;I<SIZE;I++)
    {
        for (m=0;m<SIZE;m++)
            printf("%d ",ar[I][m]);
        printf("\n");
    }
       
}

void swap2Rows(int ar[][SIZE],int r1, int r2)
{
    int temp_term = 0;
    for (int i =0;i<SIZE;i++)
        for (int j=0;j<SIZE;j++)
        {
            temp_term= ar[r1][j];
            ar[r1][j] = ar[r2][j];
            ar[r2][j] = temp_term;
        }
}


void swap2Cols(int ar[][SIZE],int r1, int r2)
{
    int temp_term =0;
    for (int i =0;i<SIZE;i++)
        for (int j=0;j<SIZE;j++)
        {
            temp_term = ar[i][r1];
            ar[i][r1] = ar[i][r2];
            ar[i][r2] = temp_term;
        }
}

void question3()
{
    void printReverse1(int ar[],int size);
    void printReverse2(int ar[], int size);
    void reverseAr1D(int ar[], int size);
    
    int ar[80];
    int size,i;
    
    printf("Enter array size: \n");
    scanf("%d",&size);
    
    printf("Enter %d data: \n",size);
    for (i=0;i<=size-1;i++)
        scanf("%d",&ar[i]);
    
    printReverse1(ar,size);
    printReverse2(ar,size);
    reverseAr1D(ar,size);
    
    printf("\nreverseAr1D():");
    if (size > 0)
        for(i=0;i<size;i++)
            printf("%d ",ar[i]);
    printf("\n");
}

void reverseAr1D(int ar[],int size)
{
    int temp_term = 0;
    for (int i=0;i<size/2 ;++i)
    {
           temp_term = ar[(size-1)-i];
           ar[(size-1)-i] = ar[i];
           ar[i] = temp_term;
            
    }
}

void printReverse1(int ar[],int size)
{
    int i =0;
    
    if (size > 0)
        printf("printReverse2():");
    for(i = size -1; i >=0 ; --i)
        printf("%d ", ar[i]);
    putchar('\n');
}

void printReverse2(int ar[],int size)
{
    int i =0;
    
    if (size > 0)
        printf("printReverse2():");
    for(i = size-1; i >=0 ; --i)
        printf("%d ", *(ar+i));
}

