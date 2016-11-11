//
// Created by cheyulin on 11/11/16.
//

#ifndef CPP_TIMELINE_TIMELINE_H
#define CPP_TIMELINE_TIMELINE_H

#include <algorithm>
#include <list>
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

vector<string> my_split(const string &s, char deliminiter);

class TimeLine {
public:
    using MessageType=pair<int, string>;

    TimeLine();

    string GetAnswer();

private:

    list <string> global_msg_list_;
    list <string> global_md5_string_list_;
    list <MessageType> prime_number_msg_list_;

    vector<std::list<MessageType>> non_prime_message_lists_;
    vector<pair<int, int>> idx_pairs_;

    unordered_set<int> prime_number_set_;


    void PostMessage(int entity_id, string message);

    void GetMessage(int entity_id);

    string GetListMd5(list <string> &string_list);
};


#endif //CPP_TIMELINE_TIMELINE_H
