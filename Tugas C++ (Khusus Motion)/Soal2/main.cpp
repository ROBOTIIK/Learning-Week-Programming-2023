#include "Robot.h"
#include <iostream>


using namespace std;

int main(){
	Robot alpha;
	
	int q; cin >> q;
	
	for(int i = 1; i<= q; i++){
		int x,y;
		cin >> x >> y;
		
		alpha.printlocation(x,y);
		alpha.updatelocation(x,y);
		
	}
	alpha.getlocation();
	system("pause");
	
}
