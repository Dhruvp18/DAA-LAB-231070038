#include <iostream>
#include <string>
#include <algorithm>

std::string padZeros(const std::string& str, int numZeros) {
    return std::string(numZeros, '0') + str;
}

std::string addStrings(const std::string& num1, const std::string& num2) {
    std::string result = "";
    int carry = 0;
    int n1 = num1.size();
    int n2 = num2.size();
    int maxLen = std::max(n1, n2);
    
    for (int i = 0; i < maxLen || carry; ++i) {
        int digit1 = i < n1 ? num1[n1 - 1 - i] - '0' : 0;
        int digit2 = i < n2 ? num2[n2 - 1 - i] - '0' : 0;
        int sum = digit1 + digit2 + carry;
        carry = sum / 10;
        result += (sum % 10) + '0';
    }

    std::reverse(result.begin(), result.end());
    return result;
}

std::string subtractStrings(const std::string& num1, const std::string& num2) {
    std::string result = "";
    int n1 = num1.size();
    int n2 = num2.size();
    int carry = 0;

    for (int i = 0; i < n1; ++i) {
        int digit1 = num1[n1 - 1 - i] - '0';
        int digit2 = i < n2 ? num2[n2 - 1 - i] - '0' : 0;
        int diff = digit1 - digit2 - carry;
        if (diff < 0) {
            diff += 10;
            carry = 1;
        } else {
            carry = 0;
        }
        result += diff + '0';
    }

    while (result.size() > 1 && result.back() == '0') {
        result.pop_back();
    }

    std::reverse(result.begin(), result.end());
    return result;
}

std::string karatsubaMultiply(const std::string& x, const std::string& y) {
    int n = std::max(x.size(), y.size());

    if (n == 1) {
        return std::to_string((x[0] - '0') * (y[0] - '0'));
    }
    std::string xPadded = padZeros(x, n - x.size());
    std::string yPadded = padZeros(y, n - y.size());

    int half = n / 2;
    std::string a = xPadded.substr(0, n - half); 
    std::string b = xPadded.substr(n - half);   
    std::string c = yPadded.substr(0, n - half);
    std::string d = yPadded.substr(n - half); 
    std::string ac = karatsubaMultiply(a, c);
    std::string bd = karatsubaMultiply(b, d);
    std::string abcd = karatsubaMultiply(addStrings(a, b), addStrings(c, d));

    std::string adbc = subtractStrings(subtractStrings(abcd, ac), bd);

    std::string result = addStrings(
        addStrings(ac + std::string(2 * half, '0'), adbc + std::string(half, '0')),
        bd);
    while (result.size() > 1 && result[0] == '0') {
        result.erase(result.begin());
    }

    return result;
}

int main() {
    std::string num1, num2;

    std::cout << "Enter the first large number: ";
    std::cin >> num1;
    std::cout << "Enter the second large number: ";
    std::cin >> num2;

    std::string result = karatsubaMultiply(num1, num2);

    std::cout << "Multiplication result: " << result << std::endl;

    return 0;
}
