//
// Created by cheyulin on 11/11/16.
//

#ifndef CPP_TIMELINE_TIMELINE_H
#define CPP_TIMELINE_TIMELINE_H

#include <algorithm>
#include <string>
#include <unordered_set>
#include <fstream>
#include <iostream>
#include <sstream>
#include <vector>
#include "md5.h"

using namespace std;

const string TIME_LINE_FILE_NAME = string("/home/cheyulin/GitRepos/OJCodes/qlcoder/data_mining/timeline/timeline.txt");
const string PRIME_FILE_NAME = string("/home/cheyulin/GitRepos/OJCodes/qlcoder/data_mining/timeline/primes.txt");
constexpr int NUM_COUNT = 10000000;
constexpr int PRIME_COUNT = 221374;
constexpr int V_COUNT = 6666666;
constexpr int P_COUNT = 3333334;

vector<string> my_split(const string &s, char deliminiter);

auto cmp = [](pair<int, string> left, pair<int, string> right) -> bool { return left.first < right.first; };

class TimeLine {
public:
    using MessageType=pair<int, string>;

    TimeLine();

    string GetAnswer();

private:
    int time_stamp_{0};

    vector<string> global_msg_list_;
    vector<string> global_md5_string_list_;

    unordered_set<int> prime_number_set_;
    vector<MessageType> global_prime_msg_list_;
    vector<int> global_prime_msg_mapping_list_;

    vector<vector<MessageType>> non_prime_message_lists_;
    vector<pair<int, int>> idx_pairs_;

    void PostMessage(int entity_id, string &message);

    void VerboseMessage(int entity_id);

    string GetListMd5(vector<string> &string_list);

    string GetListMd5(vector<MessageType> &message_list);
};


#endif //CPP_TIMELINE_TIMELINE_H
