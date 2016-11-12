//
// Created by cheyulin on 11/11/16.
//

#include "timeline.h"

void PrintMD5(const string &message) {
    cout << "md5(\"" << message << "\") = " << MD5(message).toStr() << endl;
}

vector<string> my_split(const string &s, char deliminiter) {
    stringstream ss(s);
    string item;
    vector<string> elements;

    while (getline(ss, item, deliminiter)) {
        elements.push_back(move(item));
    }
    return elements;
}

std::string &trim_right_end(std::string &s) {
    s.erase(std::find_if(s.rbegin(), s.rend(), std::not1(std::ptr_fun<int, int>(std::isspace))).base(), s.end());
    return s;
}

TimeLine::TimeLine() {
    prime_number_set_.reserve(PRIME_COUNT);
    global_prime_msg_list_.reserve(PRIME_COUNT);
    global_md5_string_list_.reserve(V_COUNT);
    non_prime_message_lists_.resize(NUM_COUNT + 1);
    idx_pairs_.resize(NUM_COUNT + 1, std::move(pair<int, int>(0, -1)));

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
}

string TimeLine::GetListMd5(vector<string> &string_list) {
    stringstream ss;
    if (string_list.size() > 0) {
        for (auto ele:string_list) {
            ss << ele << '-';
        }
        string tmp_str = ss.str();
        tmp_str.resize(tmp_str.size() - 1);
        return MD5(tmp_str).toStr();
    } else {
        return MD5("").toStr();
    }
}

string TimeLine::GetListMd5(vector<TimeLine::MessageType> &message_list) {
    stringstream ss;
    if (message_list.size() > 0) {
        for (auto ele:message_list) {
            ss << ele.second << '-';
        }
        string tmp_str = ss.str();
        tmp_str.resize(tmp_str.size() - 1);
        return MD5(tmp_str).toStr();
    } else {
        return MD5("").toStr();
    }
}


void TimeLine::PostMessage(int entity_id, string &message) {
    if (prime_number_set_.find(entity_id) != prime_number_set_.end()) {
        global_prime_msg_list_.push_back(make_pair(time_stamp_, message));
        global_prime_msg_mapping_list_.push_back(entity_id);
        for (auto smaller_idx = 1; smaller_idx < entity_id; smaller_idx++) {
            idx_pairs_[smaller_idx].second = static_cast<int>(global_prime_msg_list_.size() - 1);
        }
    }

    for (auto times_count = 2; times_count * entity_id < NUM_COUNT + 1; times_count++) {
        non_prime_message_lists_[times_count * entity_id].push_back(make_pair(time_stamp_, message));
    }
}

void TimeLine::VerboseMessage(int entity_id) {
    if (idx_pairs_[entity_id].second >= idx_pairs_[entity_id].first) {
        vector<pair<int, string>> union_vec;
        vector<pair<int, string>> filtered_vec;
        if (non_prime_message_lists_[entity_id].size() > 0) {
            cout << "attention V" << endl;
        }
//        cout << "V size:" << idx_pairs_[entity_id].second - idx_pairs_[entity_id].first + 1 << endl;
        for (auto i = idx_pairs_[entity_id].first; i < idx_pairs_[entity_id].second + 1; i++) {
            if (global_prime_msg_mapping_list_[i] > entity_id) {
                filtered_vec.push_back(global_prime_msg_list_[i]);
            }
        }
        set_union(non_prime_message_lists_[entity_id].begin(), non_prime_message_lists_[entity_id].end(),
                  filtered_vec.begin(), filtered_vec.end(), back_inserter(union_vec), cmp);
        global_md5_string_list_.push_back(GetListMd5(union_vec));
        idx_pairs_[entity_id].first = static_cast<int>(global_prime_msg_list_.size());
    } else {
        global_md5_string_list_.push_back(GetListMd5(non_prime_message_lists_[entity_id]));
    }
    non_prime_message_lists_[entity_id].clear();
}

string TimeLine::GetAnswer() {
    for (auto &str:global_msg_list_) {
        vector<string> my_vec = my_split(str, ' ');
        if (my_vec[0] == "p") {
            PostMessage(stoi(my_vec[1]), trim_right_end(my_vec[2]));
        } else {
            VerboseMessage(stoi(my_vec[1]));
        }
        if (time_stamp_ == 99 || time_stamp_ == 299 || time_stamp_ == 311 || time_stamp_ == 312 ||
            time_stamp_ == 999 || time_stamp_ == 23030 || time_stamp_ == 50000 - 1 || time_stamp_ == 66665 ||
            time_stamp_ == 100000 - 1) {
//            for(auto& ele:global_md5_string_list_)
//            {
//                cout <<ele<<"-";
//            }
            cout << endl << "timestamp:" << time_stamp_ << ":" << GetListMd5(global_md5_string_list_) << endl;
        } else if (time_stamp_ > 1000)
            return "";
        time_stamp_++;
    }
    return GetListMd5(global_md5_string_list_);
}