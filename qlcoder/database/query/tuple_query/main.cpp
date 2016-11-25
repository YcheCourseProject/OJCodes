#include <tuple>
#include <iostream>
#include <fstream>

#include "prettyprint.h"
#include "util.h"

using namespace std;

auto get_tuple_with_str(string &my_tuple_str) {
    auto my_cols = Split(my_tuple_str, ',');
    auto tags = Split(my_cols[my_cols.size() - 1], ' ');
    return make_tuple(stol(my_cols[0]), stoi(my_cols[1]), stoi(my_cols[2]), stoi(my_cols[3]), my_cols[4], my_cols[5],
                      stoi(my_cols[6]), stol(my_cols[7]), stof(my_cols[8]), tags);
}

int main() {
    ifstream input_stream("/home/cheyulin/GitRepos/OJCodes/qlcoder/database/query/solr_data.csv");
    string tmp_str;
    getline(input_stream, tmp_str);
    cout << "table schema" << tmp_str << endl;

    getline(input_stream, tmp_str);
    auto t = get_tuple_with_str(tmp_str);
    vector<decltype(t)> tuple_list;
    tuple_list.reserve(3000000);
    tuple_list.push_back(t);

    while (getline(input_stream, tmp_str)) {
        t = get_tuple_with_str(tmp_str);
        tuple_list.push_back(t);
    }

    cout << "tuple size:" << tuple_list.size() << endl;
    for (auto idx = tuple_list.size() - 10; idx < tuple_list.size(); idx++) {
        cout << tuple_list[idx] << endl;
    }
    return 0;
}