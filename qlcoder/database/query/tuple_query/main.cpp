#include <unordered_map>
#include <fstream>

#include "tuple_info.h"
#include "query_info.h"

using namespace std;

const string data_path = string("/home/cheyulin/GitRepos/OJCodes/qlcoder/database/query/solr_data.csv");
const string query_path = string("/home/cheyulin/GitRepos/OJCodes/qlcoder/database/query/solr_query.txt");

void PrintTupleListInfo(vector<TupleInfo> &tuple_list) {
    for (auto idx = tuple_list.size() - 10; idx < tuple_list.size(); idx++) {
        tuple_list[idx].Print();
    }
}

void InitTupleList(vector<TupleInfo> &tuple_list, unordered_map<string, vector<long>> &tag_indices) {
    ifstream input_stream(data_path);
    string tmp_str;
    getline(input_stream, tmp_str);
    while (getline(input_stream, tmp_str)) {
        tuple_list.emplace_back(tmp_str);
        auto &cur_tuple = tuple_list.back();
        for (auto &tag_str:cur_tuple.tag_list_) {
            if (tag_indices[tag_str].size() > 0 && tag_indices[tag_str].back() == cur_tuple.good_id_) {
                continue;
            }
            tag_indices[tag_str].push_back(cur_tuple.good_id_);
        }
    }

    PrintTupleListInfo(tuple_list);
    cout << "tuple size:\t" << tuple_list.size() << endl;
    cout << "tag size:\t" << tag_indices.size() << endl;
}

void InitQueryList(vector<QueryInfo> &query_list) {
    ifstream input_stream(query_path);
    string tmp_str;
    while (getline(input_stream, tmp_str)) {
        query_list.emplace_back(tmp_str);
    }
}

bool CheckSingleTuple(TupleInfo &tuple, vector<vector<string>> &constraints) {
    for (auto &constraint:constraints) {
        if (constraint[0] == COLOR) {
            if (tuple.color_ != constraint[1])
                return false;
        } else if (constraint[0] == PRICE) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.price_ < left || tuple.price_ > right)
                return false;
        } else if (constraint[0] == SALE_NUM) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.sale_num_ < left || tuple.sale_num_ > right)
                return false;
        } else if (constraint[0] == FAV_NUM) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.fav_num_ < left || tuple.fav_num_ > right)
                return false;
        } else if (constraint[0] == SIZE) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.size_ < left || tuple.size_ > right)
                return false;
        } else if (constraint[0] == ITEM_NUM) {
            int left = stoi(constraint[1]);
            int right = stoi(constraint[2]);
            if (tuple.item_num_ < left || tuple.item_num_ > right)
                return false;
        } else if (constraint[0] == CREATE_AT) {
            long left = stol(constraint[1]);
            long right = stol(constraint[2]);
            if (tuple.create_at_ < left || tuple.create_at_ > right)
                return false;
        } else if (constraint[0] == DSR) {
            float left = stof(constraint[1]);
            float right = stof(constraint[2]);
            if (tuple.dsr_ < left || tuple.dsr_ > right)
                return false;
        } else {
            cerr << "something wrong" << endl;
            cout << "something wrong" << endl;
        }
    }
    return true;
}

int CheckMatchNumber(vector<TupleInfo> &tuple_list, unordered_map<string, vector<long>> &tag_indices,
                     QueryInfo &query_info) {
    auto &first_set = tag_indices[query_info.tags_[0]];
    auto &second_set = tag_indices[query_info.tags_[1]];
    vector<long> union_set;
    union_set.reserve(first_set.size() + second_set.size());
    auto filtered_count = 0;

    set_union(first_set.begin(), first_set.end(), second_set.begin(), second_set.end(), back_inserter(union_set));

    for (auto ele: union_set) {
        if (CheckSingleTuple(tuple_list[ele], query_info.constraints_)) {
            filtered_count++;
        }
    }
    return filtered_count;
}

int main() {
    unordered_map<string, vector<long>> tag_indices;
    vector<TupleInfo> tuple_list;
    tuple_list.reserve(3000000);
    vector<QueryInfo> query_list;
    query_list.reserve(3000000);

    InitTupleList(tuple_list, tag_indices);
    cout << "Finish Tuple Init" << endl;

    InitQueryList(query_list);
    cout << "Finish Query Init" << endl;
    long long total = 0;
#pragma omp parallel for
    for (auto i = 0; i < query_list.size(); i++) {
        auto tmp = CheckMatchNumber(tuple_list, tag_indices, query_list[i]);
//        cout << tmp << endl;
#pragma omp critical
        total += tmp;
    }
    cout << "Total:" << total << endl;
    return 0;
}