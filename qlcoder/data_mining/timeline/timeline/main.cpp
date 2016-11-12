#include <iostream>

#include "md5.h"
#include "timeline.h"
#include <list>
#include <parallel/algorithm>

using namespace std;

void PrintMD5(const string &message) {
    cout << "md5(\"" << message << "\") = " << MD5(message).toStr() << endl;
}

void TestMD5() {
    PrintMD5("");
    PrintMD5("a");
    PrintMD5("abc");
    PrintMD5("message digest");
    PrintMD5("abcdefghijklmnopqrstuvwxyz");
    PrintMD5("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz");
}

void TestSetUnion() {
    std::vector<pair<int, string>> my_pair = {{1, "xd"},
                                              {2, "dsa"},
                                              {4, "23"}};
    std::vector<pair<int, string>> my_pair2 = {{3, "dsfd"}};
    std::vector<pair<int, string>> my_pair3;
    auto cmp = [](pair<int, string> left, pair<int, string> right) -> bool { return left.first < right.first; };

    set_union(my_pair.begin()+1, my_pair.end(), my_pair2.begin(), my_pair2.end(), back_inserter(my_pair3), cmp);
    cout << my_pair3.size() << endl;
    for (auto &ele: my_pair3) {
        cout << ele.first << " " << ele.second << endl;
    }
}

void TestStrUsage() {
    string str = "123";
    str = str.substr(0, str.size() - 1);
    cout << str << endl;
}

int main() {
    TestSetUnion();
    TimeLine time_line;
    cout << time_line.GetAnswer()<<endl;
    return 0;
}