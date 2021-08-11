#include <stdio.h>
#include<math.h>
int main()

{
    int L1,L2,T1,T2;
    double Theta1,Theta2;
    float x,y;
    printf("Enter the Link Lengths,L1 and L2:\n");
    scanf("%d%d",&L1,&L2);
    printf("Enter the Joint Angles,Theta1 and Theta2:\n");
    scanf("%lf%lf",&Theta1,&Theta2);
    double radian1 = Theta1 * (M_PI/180);
    double radian2 = Theta2 * (M_PI/180)
    x=(L1*(cos(radian1))+L2*(sin(radian1+radian2)));
    y=(L1*(sin(radian1))+L2*(sin(radian1+radian2)));
    printf("Position of end arm in World space:\n");
    printf("%f\n",x);
    printf("%f\n",y);
    
    return 0;
}
