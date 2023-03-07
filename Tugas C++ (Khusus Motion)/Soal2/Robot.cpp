#include "Robot.h"
#include <iostream>


using namespace std;

void Robot::printlocation(int x, int y){
	if(x == 0){
		if(y > 0) cout << "UTARA";
		else cout << "SELATAN";
	}
	
	else if(x > 0){
		if(y == 0) cout << "TIMUR";
		else if(y > 0) cout << "TIMUR LAUT";
		else cout << "TENGGARA";
	}
	
	else if(x < 0){
		if(y == 0) cout << "BARAT";
		else if (y > 0) cout << "BARAT LAUT";
		else cout << "BARAT DAYA";
	}
	
	cout << endl;
}

void Robot::updatelocation(int x, int y){
	x_now+=x;
	y_now+=y;
}

void Robot::getlocation(){
	cout << "KOORDINAT AKHIR: (" << x_now << ", " << y_now <<")" << endl;
}
