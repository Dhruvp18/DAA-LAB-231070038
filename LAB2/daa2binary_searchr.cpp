#include <iostream>
#include <vector>

using namespace std;

int binary_search(const vector<int>& arr,int left,int right, int target) {
  if (left > right) {
    return -1; 
  }

  int mid = left + (right - left) / 2;

  if (arr[mid] == target) {
    return mid;  
  }
   else if (arr[mid] > target) {
    return binary_search(arr, left, mid - 1, target); 
  } 
  else {
    return binary_search(arr, mid + 1, right, target); 
  }
}
int main() {
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
  int result =binary_search(v, 0, v.size() - 1, x);
  if (result != -1) {
    cout << "Element found at index " << result << endl;
  } else {
    cout << "Element not found in the array" << endl;
  }

  return 0;
}
