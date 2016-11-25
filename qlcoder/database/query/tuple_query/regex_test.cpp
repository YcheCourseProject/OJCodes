//
// Created by cheyulin on 11/25/16.
//
#include <unordered_map>
#include "query_info.h"

using namespace std;

void StudyHashMap() {
    unordered_map<string, vector<int>> my_map;
    if (my_map.find("fds") == my_map.end()) {
        cout << "go" << endl;
        my_map["fds"].reserve(50000);
    }
    my_map["fds"].push_back(1);

    if (my_map.find("fds") == my_map.end()) {
        cout << "go" << endl;
        my_map["fds"].reserve(50000);
    }
    my_map["fds"].push_back(2);

    cout << my_map["fds"] << endl;
    cout << my_map["fds"].capacity() << endl << endl;
}

void StudyRegex() {
    string my_str = "(tag:*字母* OR tag:*甜美*) AND saleNum:[13202 TO 43161] AND color:red AND favNum:[67680 TO 97990]";
    QueryInfo query_info(my_str);
    cout << query_info.tags_ << endl;
    cout << query_info.first_constraint_ << endl;
    cout << query_info.second_constraint_ << endl;
    cout << query_info.third_constraint_ << endl << endl;
}

void StudyFloatComp() {
    cout << (stoi("3.5") <= 3.5) << endl;
    cout << (3.6 <= 3.5) << endl;
    cout << true << endl;
}


int main() {
    StudyRegex();
    StudyHashMap();
    StudyFloatComp();
}