#include <iostream>
#include <vector>
#include <algorithm>

int BruteForceMultiply(int num1, int num2) {
    std::string str1 = std::to_string(num1);
    std::string str2 = std::to_string(num2);
    int n1 = str1.size();
    int n2 = str2.size();
    std::vector<int> result(n1 + n2, 0);
    for (int i = n1 - 1; i >= 0; i--) {
        int carry = 0;
        int n1_digit = str1[i] - '0';
        for (int j = n2 - 1; j >= 0; j--) {
            int n2_digit = str2[j] - '0';
            int sum = n1_digit * n2_digit + result[i + j + 1] + carry;
            carry = sum / 10;
            result[i + j + 1] = sum % 10;
        }
        result[i] += carry;
    }

    std::string result_str;
    bool leading_zero = true;
    for (int i = 0; i < result.size(); i++) {
        if (leading_zero && result[i] == 0) continue;
        leading_zero = false;
        result_str += std::to_string(result[i]);
    }

    if (result_str.empty()) {
        return 0;
    }

    return std::stoi(result_str);
}

int main() {
    int num1 = 1234;
    int num2 = 5678;
    std::cout << "Multiplication result: " << BruteForceMultiply(num1, num2) << std::endl;
    return 0;
}
