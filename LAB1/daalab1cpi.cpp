#include <iostream>
#include <vector>
using namespace std;
double Spi(const vector<int>& credit, const vector<int>& grades) {
    double num = 0.0;
    double den = 0.0;
    for (int i = 0; i < credit.size(); ++i) {
        num += credit[i] * grades[i];
        den += credit[i];
    }
    return num / den;
}
double Cpi(const vector<double>& Spis) {
    double total = 0.0;
    for (int i=0;i<Spis.size();i++) {
        total += Spis[i];
    }
    return total / Spis.size();
}

int main() {
    int sem;
    cout << "Enter the number of semesters: ";
    cin >> sem;

    vector<double> Spis;

    for (int i = 0; i < sem; ++i) {
        int course;
        cout << "Enter the number of courses in semester " << i + 1 << ": ";
        cin >> course;

        vector<int> credit(course);
        vector<int> grade(course);

        for (int j = 0; j < course; ++j) {
            cout << "Enter the credits for course " << j + 1 << ": ";
            cin >> credit[j];
            cout << "Enter the grade for this course: ";
            cin >> grade[j];
        }

        double spi = Spi(credit, grade);
        Spis.push_back(spi);
        cout << "The SPI for semester " << i + 1 << " is " << spi << endl;
    }

    cout << "The overall CPI is " << Cpi(Spis) << endl;

    return 0;
}
