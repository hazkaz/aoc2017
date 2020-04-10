#include<iostream>
#include<stdlib.h>
#include<list>
using namespace std;
//function for printing the elements in a list
void showlist(list <int> g)
{
    list <int> :: iterator it;
    for(it = g.begin(); it != g.end(); ++it)
        cout << '\t' << *it;
    cout << '\n';
}

int main(){

int step_size = 376;
int MAX_LEN = 50000000;
int length = 1;
int current_pos = 0;
list <int> storm;
list <int> :: iterator it;
storm.push_back(0);
it=storm.begin();
//showlist(storm);
int req_number;
for(int i=1;i<MAX_LEN+1;i++){
    it=storm.begin();
    current_pos = (current_pos+step_size)%length+ 1;
//    advance(it,current_pos);
//    storm.insert(it,i);
    if(current_pos==1){
        req_number = i;
    }
    length++;
}
//it = storm.begin();
//advance(it,current_pos+1);
//cout<<*it;
cout<<req_number;
cout<<endl;

return 0;
}