//
// Created by cheyulin on 11/18/16.
//

#include <iostream>
#include <sstream>
#include <vector>
#include <unordered_set>
#include <unordered_map>

using namespace std;

hash<string> yche_hash_func_obj;

namespace std {
    template<>
    struct hash<vector<vector<unsigned char>>> {
        size_t operator()(const vector<vector<unsigned char>> &my_arr) const {
            stringstream ss;
            for (auto &row:my_arr) {
                for (auto &col:row) {
                    ss << col;
                }
            }
            return yche_hash_func_obj(ss.str());
        }
    };
}


void StudyHashSet() {
    vector<vector<unsigned char >> my_arr = {{1, 0},
                                             {0, 1}};

    vector<vector<unsigned char>> my_arr2 = {{1, 0},
                                             {0, 1}};

    vector<vector<unsigned char>> my_arr3 = {{1, 1},
                                             {0, 1}};

    auto my_arr4 = my_arr;

    unordered_set<vector<vector<unsigned char>>> my_arr_set;
    my_arr_set.emplace(my_arr);
    if (my_arr_set.find(my_arr2) != my_arr_set.end()) {
        cout << "ok" << endl;
    } else {
        cout << "not ok" << endl;
    }
    if (my_arr_set.find(my_arr3) != my_arr_set.end()) {
        cout << "ok" << endl;
    } else {
        cout << "not ok" << endl;
    }
    if (my_arr_set.find(my_arr3) != my_arr_set.end()) {
        cout << "ok" << endl;
    } else {
        cout << "not ok" << endl;
    }

    cout << "equal demo:" << (my_arr == my_arr2) << endl;
}

void StudyHashMap() {
    cout << "Hash Map Study" << endl;
    unordered_map<vector<vector<unsigned char>>, int> my_map;
    vector<vector<unsigned char >> my_arr = {{1, 0},
                                             {0, 1}};
    auto my_arr2 = my_arr;

    my_map.emplace(my_arr, 5);
    auto iter = my_map.find(my_arr2);
    if (iter != my_map.end()) {
        cout << "ok value:" << iter->second << endl;
    } else {
        cout << "not ok" << endl;
    }
}

void StudyVector() {
    vector<int> my_vec;
    my_vec.reserve(10);
    for (auto i = 0; i < 5; i++)
        my_vec.push_back(i);
    my_vec.pop_back();
    for (auto ele:my_vec) {
        cout << ele << endl;
    }
}

int main() {
    StudyHashSet();
    StudyHashMap();
    StudyVector();
}