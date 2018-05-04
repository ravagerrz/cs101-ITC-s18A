//Usama Bin Haider
//17p-6069
//B
#include<iostream>
#include<string>
using namespace std;
int main()
{
	double length,width,radius,height=0.0;
	 int  a;
	const int pie=3.14;
    cout<<"Enter the shape type(1=rectangle,2=circle,3=cylinder)"<<endl;
	cin>>a;

	switch(a)
	{
	case 1:
		  {
			    cout<<"RECTANGLE :"<<endl;

		   cout<<"Enter the length of rectangle"<<endl;
		   cin>>length;
		   cout<<"Enter the width of rectangle"<<endl;
		   cin>>width;
		   cout<<endl;
		   cout<<"Perimeter of rectangle"<<"="<<2*(length+width)<<endl;
		   cout<<"Area of the rectangle"<<"="<<length*width<<endl;

		   break;
		  }
	case 2:
		{
                   cout<<"CIRCLE :"<<endl;
		  cout<<"Enter the radius of the circle"<<endl;
		  cin>>radius;
		  cout<<endl;
		  cout<<"Area of circle"<<"="<<pie*radius*radius<<endl;
		  cout<<"Circumference of circle"<<"="<<2*pie*radius*radius<<endl;

		  break;
		}

	case 3:
		{
			     cout<<"CYLINDER :"<<endl;
          cout<<"Enter the height of the cylinder"<<endl;
		  cin>>height;
		  cout<<"Enter radius"<<endl;
		  cin>>radius;
		  cout<<endl;
		  cout<<"Volume of cylinder"<<"="<<pie*radius*radius*height<<endl;
		  cout<<"Surface area of the cylinder"<<"="<<(2*pie*radius*height)+(2*pie*radius*radius)<<endl;


          }
	}
	return 0;

}
