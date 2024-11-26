#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;
int linearSearch(vector<int> v,int val){
    for(int i=0;i<v.size();i++){
        if(v[i]==val){
            cout<<"The number was found at the index "<<i<<endl;
            return i;
        }
    }
    cout << "The number was not found." << endl;
    return -1;
    
}
int main(){
    vector <int>v;
    int count,x;
    cout<<"Enter how many numbers you want to put"<<endl;
    cin>>count;
    cout<<"Enter The Numbers"<<endl;
    for(int i=0;i<count;i++) { 
        cin>>v[i];
    }
    cout<<"Enter the number you want to search"<<endl;
    cin>>x;
    linearSearch(v,x);
    return 0;
}
