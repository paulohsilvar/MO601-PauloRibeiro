#include<iostream>
using namespace std;

int main()
{
	
	int size = 100000;
	int next_pos = 4500;
	
	int pos = 0;
	int vector[100000] = {};
	
	
	for(int i=0; i<100; i++){
		vector[pos] = i;
		pos = pos + next_pos;
		if(pos >= size) {
		    pos = pos - size;
		}
	}
	return 0;
}
