#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int binarySearch (vector<int> &v, int val) {
    sort(v.begin(), v.end());
    int l = 0;
    int r = v.size() - 1;
    while (l <= r) {
        int mid = l + (r - l) / 2;
        if (v[mid] == val) {
            cout<<"The number was found at the index "<<mid<<endl;
            return mid;
        }
        else if (v[mid] > val) {
            r = mid - 1;
        }
        else {
            l = mid + 1;
        }
    }
    cout << "The number was not found." << endl;
    return -1;3
    
}
int main() {
    vector <int>v;
    int count,x;
    cout<<"Enter how many numbers you want to put"<<endl;
    cin>>count;
    for(int i=0;i<count;i++) { 
    cout<<"Enter The Numbers"<<endl;
        cin>>v[i];
    }
    cout<<"Enter the number you want to search"<<endl;
    cin>>x;
    binarySearch(v,x);
    return 0;
}
