//
// Created by cheyulin on 11/25/16.
//

#ifndef TUPLE_QUERY_UITL_H
#define TUPLE_QUERY_UITL_H

#include <vector>
#include <string>
#include <sstream>

using namespace std;

vector<string> Split(const string &s, char delim) {
    stringstream ss(s);
    string item;
    vector<string> elements;
    while (getline(ss, item, delim)) {
        elements.push_back(move(item));
    }
    return elements;
}

#endif //TUPLE_QUERY_UITL_H
