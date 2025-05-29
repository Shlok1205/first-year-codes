/*WAP to compute the BMI Index of the person and print the BMI values as per the following 
ranges. You can use the following formula to compute 
BMI=weight(kgs)/Height(Mts)*Height(Mts).*/


#include<stdio.h>
int main()
{
float weight,height,BMI;
printf("Enter your weight in kilograms: ");
scanf("%f", &weight);
printf("Enter your height in meters: ");
scanf("%f", &height);  
BMI=weight/(height*height);
printf("\nBMI=%f7",BMI);
if (BMI<15)
{
printf("\nThe given details lead to starvation");
}
else if (BMI>= 15.1 && BMI<= 17.5)
{
printf("\nThe given details lead to the person being Anorexic");
}
else if (BMI>=17.6 && BMI<=18.5)
{
printf("\nThe given details lead to the person being underweight");
}
else if (BMI>=18.6 && BMI<=24.9)
{
printf("\nThe given details show that the person has an ideal BMI");
}
else if (BMI>=25 && BMI<=25.9)
{
printf("\nThe given details show that the person is overweight");
}
else if (BMI>=30 && BMI<=39.9)
{
printf("\nThe given details show that the person is obese");
}
else
{
printf("\nThe given details show that the person is suffering from morbidity obesity");
}
return 0;
}

/*Enter your weight in kilograms: 40
Enter your height in meters: 1.82
BMI=12.0758357
The given details lead to starvation*/

/*Enter your weight in kilograms: 45
Enter your height in meters: 1.7
BMI=15.5709337
The given details lead to the person being Anorexic*/

/*Enter your weight in kilograms: 55
Enter your height in meters: 1.75
BMI=17.9591837
The given details lead to the person being underweight*/

/*Enter your weight in kilograms: 77
Enter your height in meters: 1.8
BMI=23.7654347
The given details show that the person has an ideal BMI*/

/*Enter your weight in kilograms: 78
Enter your height in meters: 1.75
BMI=25.4693877
The given details show that the person is overweight*/

/*Enter your weight in kilograms: 95
Enter your height in meters: 1.75
BMI=31.0204097
The given details show that the person is obese*/

/*Enter your weight in kilograms: 125
Enter your height in meters: 1.75
BMI=40.8163267
The given details show that the person is suffering from morbidity obesity*/