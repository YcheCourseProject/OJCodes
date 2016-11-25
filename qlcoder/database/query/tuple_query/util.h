//
// Created by cheyulin on 11/25/16.
//

#ifndef TUPLE_QUERY_UITL_H
#define TUPLE_QUERY_UITL_H

#include <vector>
#include <string>
#include <sstream>
#include <regex>
#include <list>
#include <iostream>

#include "prettyprint.h"

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

std::vector<std::string> SplitReg(const string &input, const string &regex) {
    // passing -1 as the submatch index parameter performs splitting
    std::regex re(regex);
    std::sregex_token_iterator first{input.begin(), input.end(), re, -1}, last;
    return {first, last};
}

vector<string> SplitConstraint(const string &input) {
    vector<string> my_strings = move(Split(input, ':'));
    vector<string> tmp_strings;
    if (my_strings[0] != "color") {
        tmp_strings = move(SplitReg(my_strings[1], " TO "));
        my_strings.resize(3);
        my_strings[1] = tmp_strings[0].substr(1, tmp_strings[0].length() - 1);
        my_strings[2] = tmp_strings[1].substr(0, tmp_strings[1].length() - 1);
    }
    return my_strings;
}


#endif //TUPLE_QUERY_UITL_H
