1.
#include <stdio.h>

int main() {
    float length, breadth, area;
    printf("Enter length: ");
    scanf("%f", &length);
    printf("Enter breadth: ");
    scanf("%f", &breadth);
    area = length * breadth;
    printf("Area of rectangle: %.2f\n", area);
    return 0;
}

2. Integer + Float Addition
#include <stdio.h>

int main() {
    int a;
    float b, result;
    printf("Enter an integer: ");
    scanf("%d", &a);
    printf("Enter a floating-point number: ");
    scanf("%f", &b);
    result = a + b;
    printf("Result: %.2f\n", result);
    printf("Data type of result: float\n");
    printf("Reason: In C, when an int and a float are added, the int is automatically promoted to float. So the result is always float.\n");
    return 0;
}


3. User Details Display
#include <stdio.h>

int main() {
    char name[50], gender[10];
    int age;
    float height;

    printf("Enter name: ");
    scanf("%s", name);
    printf("Enter age: ");
    scanf("%d", &age);
    printf("Enter gender: ");
    scanf("%s", gender);
    printf("Enter height (in cm): ");
    scanf("%f", &height);

    printf("\n--- User Details ---\n");
    printf("Name   : %s\n", name);
    printf("Age    : %d\n", age);
    printf("Gender : %s\n", gender);
    printf("Height : %.2f cm\n", height);

    return 0;
}
