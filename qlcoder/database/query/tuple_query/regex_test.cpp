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
    for (auto &constraint: query_info.constraints_) {
        cout << constraint << endl;
    }
    cout << endl;

    string pattern= "聚酯";
    std::regex txt_regex(".*" + pattern + ".*");
    if(regex_match("聚酯纤维",txt_regex)){
        cout <<"Okay"<<endl;
    }
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