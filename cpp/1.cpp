#include <algorithm>
#include <iostream>
#include <vector>

using namespace std;

int main() {
	int n, m;
	cin >> n;
	long int ans1 = 0, ans2 = 1;
	int flag = 0;
	
	if(n%2==0){
		flag = 0;
		while(n>0) {
			m=n%10;    
			ans1=ans1+m;    
			n=n/10;
		}
	} else {
		flag = 1;
		while(n>0) {
			m=n%10;    
			ans2=ans2*m;    
			n=n/10;
		}
	}
	
	if(flag == 1) {
		cout<<ans2;
	} else {
		cout<<ans1;
	}

	return 0;
}