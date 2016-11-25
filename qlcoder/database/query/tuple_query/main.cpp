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
            tag_indices[tag_str].push_back(cur_tuple.good_id_);
        }
    }

    PrintTupleListInfo(tuple_list);
}

void InitQueryList(vector<QueryInfo> &query_list) {
    ifstream input_stream(query_path);
    string tmp_str;
    while (getline(input_stream, tmp_str)) {
        query_list.emplace_back(tmp_str);
    }
}

bool CheckSingleTuple(TupleInfo &tuple, QueryInfo &query_info) {

}

int CheckMatchNumber(vector<TupleInfo> &tuple_list, unordered_map<string, vector<long>> &tag_indices,
                     QueryInfo &query_info) {
    
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

    return 0;
}