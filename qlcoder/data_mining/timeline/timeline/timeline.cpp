//
// Created by cheyulin on 11/11/16.
//

#include "timeline.h"

vector<string> my_split(const string &s, char deliminiter) {
    stringstream ss(s);
    string item;
    vector<string> elements;

    while (getline(ss, item, deliminiter)) {
        elements.push_back(move(item));
    }
    return elements;
}

TimeLine::TimeLine() {
    non_prime_message_lists_.resize(10000000);
    ifstream input_stream(TIME_LINE_FILE_NAME);
    string line;
    while (getline(input_stream, line)) {
        global_msg_list_.push_back(line);
    }


    ifstream input_stream2(PRIME_FILE_NAME);
    while (input_stream2.good()) {
        int number_line;
        input_stream2 >> number_line;
        prime_number_set_.insert(number_line);
    }

    idx_pairs_.resize(10000000, std::move(pair<int, int>(0, -1)));
}

string TimeLine::GetAnswer() {
    int time_stamp = 0;
    for (auto &str:global_msg_list_) {
        vector<string> my_vec = my_split(str, ' ');
        if (my_vec[0] == "p") {
            PostMessage(stoi(my_vec[1]), my_vec[2]);
        } else {
            GetMessage(stoi(my_vec[1]));
        }
        time_stamp++;
    }
    return GetListMd5(global_md5_string_list_);
}

string TimeLine::GetListMd5(list <string> &string_list) {
    stringstream ss;
    if (string_list.size() > 0) {
        for (auto ele:string_list) {
            ss << ele << '-';
        }
        string tmp_str = ss.str();
        tmp_str = tmp_str.substr(0, tmp_str.size() - 1);
        return MD5(tmp_str).toStr();
    } else {
        return MD5("").toStr();
    }

}

void TimeLine::PostMessage(int entity_id, string message) {

}

void TimeLine::GetMessage(int entity_id) {

}
