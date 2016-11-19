//
// Created by cheyulin on 11/2/16.
//

#include "state_space_search.h"

hash<string> yche_hash_func_obj;

vector<string> ModuloSolver::Split(const string &s, char delim) {
    stringstream ss(s);
    string item;
    vector<string> elements;
    while (getline(ss, item, delim)) {
        elements.push_back(move(item));
    }
    return elements;
}


ModuloSolver::ModuloSolver(int modulo_num, string &grid_str, vector<string> &piece_strs) : modulo_num_(modulo_num) {
    modulo_grid_ = ExtractMatrix(grid_str);
    grid_row_ = static_cast<int>(modulo_grid_.size());
    grid_col_ = static_cast<int>(modulo_grid_[0].size());
    for (auto &ele:piece_strs) {
        auto tmp = ExtractMatrix(ele);
        pieces_.push_back(move(tmp));
    }
    pieces_sum_.reserve(pieces_.size());
    for (auto &ele:pieces_) {
        pieces_sum_.push_back(GetMatrixSum(ele));
    }

    check_depth_ = GetStartCheckDepth();
    bottom_depth_ = static_cast<int>(pieces_.size());
    vector<pair<unsigned char, unsigned char>> node_info;
    node_info.reserve(static_cast<unsigned long>(bottom_depth_ - check_depth_));
    MatrixType matrix = modulo_grid_;
    for (auto &row :matrix) {
        for (auto &col:row) {
            col = 0;
        }
    }
    look_up_grids_.reserve(1024 * 1024 * 2);
    DFSBuildMap(check_depth_, matrix, node_info);
    cout << look_up_grids_.size() << endl;

    min_possible_cell_num_ = 99999;
    max_possible_cell_num_ = -99999;
    for (auto &ele_pair:look_up_grids_) {
        auto left_cell_num = GetLeftNumsCount(ele_pair.first);
        if (left_cell_num < min_possible_cell_num_) {
            min_possible_cell_num_ = left_cell_num;
        }
        if (left_cell_num > max_possible_cell_num_) {
            max_possible_cell_num_ = left_cell_num;
        }
    }

    PrintInitInfo();

}

MatrixType ModuloSolver::ExtractMatrix(string &matrix_str) {
    vector<string> rows = std::move(Split(matrix_str, '!'));
    MatrixType matrix;
    matrix.reserve(rows.size());
    for (auto &row:rows) {
        vector<unsigned char> row_vec;
        row_vec.reserve(row.size());
        for (auto ch:row) {
            row_vec.push_back(static_cast<unsigned char>(ch - '0'));
        }
        matrix.push_back(move(row_vec));
    }
    return matrix;
}

void ModuloSolver::PrintMatrix(const MatrixType &matrix, string msg) {
    cout << msg << ": ";
    for (auto &row:matrix) {
        for (auto col:row) {
            cout << static_cast<int>(col);
        }
        cout << ";";
    }
    cout << endl;
}

int ModuloSolver::GetMatrixSum(const MatrixType &matrix) {
    int sum = 0;
    for (auto &row :matrix) {
        for (auto col:row) {
            sum += static_cast<int>(col);
        }
    }
    return sum;
}

int ModuloSolver::GetPieceStateSize(const MatrixType &matrix) {
    auto piece_row = static_cast<int>(matrix.size());
    auto piece_col = static_cast<int>(matrix[0].size());
    return (grid_row_ - piece_row + 1) * (grid_col_ - piece_col + 1);
}

void ModuloSolver::PrintInitInfo() {
    cout << "modulo num:" << modulo_num_ << endl;
    stringstream ss;
    ss << "map, row size:" << grid_row_ << ",col_size:" << grid_col_;
    PrintMatrix(modulo_grid_, ss.str());
    for (auto i = 0; i < pieces_.size(); i++) {
        stringstream ss;
        ss << "piece" << i << "," << " sum is " << pieces_sum_[i] << ", state size:" << GetPieceStateSize(pieces_[i]);
        PrintMatrix(pieces_[i], ss.str());
    }
    cout << "From idx:[" << check_depth_ << "," << bottom_depth_ << ") as the check point" << endl;
    cout << "max cell num:" << max_possible_cell_num_ << ",min cell num:" << min_possible_cell_num_ << endl;
}

int ModuloSolver::GetStartCheckDepth() {
    auto matrix_size = grid_col_ * grid_row_;
    auto whole_size = matrix_size;
    int ret_depth = -1;
    auto depth = static_cast<int>(pieces_.size() - 1);
    long depth_state_size = GetPieceStateSize(pieces_[depth]);

    cout << depth << "," << depth_state_size << "," << whole_size << endl;
    while (depth > 0 && depth_state_size * whole_size < MAX_SIZE) {
        ret_depth = depth;
        whole_size *= depth_state_size;
        depth--;
        depth_state_size = GetPieceStateSize(pieces_[depth]);
        cout << depth << "," << depth_state_size << "," << whole_size << endl;
    }
    cout << "ret_depth:" << ret_depth << endl;
    cout << "lookup map whole_size:" << whole_size << endl;
    return ret_depth;
}

void ModuloSolver::DFSBuildMap(int depth, MatrixType &tmp_grid,
                               vector<pair<unsigned char, unsigned char>> &path_list) {
    if (depth == bottom_depth_) {
        if (look_up_grids_.find(tmp_grid) == look_up_grids_.end()) {
            look_up_grids_.emplace(tmp_grid, path_list);
        }
        return;
    } else {
        //DFS and mark the path
        auto &current_piece = pieces_[depth];
        auto current_piece_row_num = static_cast<int>(current_piece.size());
        auto current_piece_col_num = static_cast<int>(current_piece[0].size());
        for (auto start_row_idx = 0; start_row_idx < grid_row_ + 1 - current_piece_row_num; start_row_idx++) {
            for (auto start_col_idx = 0; start_col_idx < grid_col_ + 1 - current_piece_col_num; start_col_idx++) {
                path_list.emplace_back(start_row_idx, start_col_idx);
                //do overlapping
                for (auto local_row_idx = 0; local_row_idx < current_piece_row_num; local_row_idx++) {
                    for (auto local_col_idx = 0; local_col_idx < current_piece_col_num; local_col_idx++) {
                        tmp_grid[start_row_idx + local_row_idx][start_col_idx + local_col_idx] +=
                                modulo_num_ - current_piece[local_row_idx][local_col_idx];
                        tmp_grid[start_row_idx + local_row_idx][start_col_idx + local_col_idx] %= modulo_num_;
                    }
                }
                DFSBuildMap(depth + 1, tmp_grid, path_list);
                path_list.pop_back();
                //revert overlapping
                for (auto local_row_idx = 0; local_row_idx < current_piece_row_num; local_row_idx++) {
                    for (auto local_col_idx = 0; local_col_idx < current_piece_col_num; local_col_idx++) {
                        tmp_grid[start_row_idx + local_row_idx][start_col_idx + local_col_idx] +=
                                current_piece[local_row_idx][local_col_idx];
                        tmp_grid[start_row_idx + local_row_idx][start_col_idx + local_col_idx] %= modulo_num_;
                    }
                }
            }
        }
    }
}

bool ModuloSolver::DFSLookup(int depth, int left_cells, vector<pair<unsigned char, unsigned char>> &path_list,
                             MatrixType &my_map_arr) {
    if (depth == check_depth_) {
        if (look_up_grids_.find(my_map_arr) != look_up_grids_.end()) {
            cout << "find it" << endl;
            auto &left_path = look_up_grids_[my_map_arr];
            for (auto &ele:left_path) {
                path_list.push_back(ele);
            }
            return true;
        } else {
            return false;
        }
    } else {
        auto possible_cells = GetLeftNumsCount(my_map_arr);
        if (possible_cells + left_cells < min_possible_cell_num_ ||
            possible_cells - left_cells > max_possible_cell_num_) {
            return false;
        }
    }

    //DFS and mark the path
    auto &current_piece = pieces_[depth];
    auto current_piece_row_num = static_cast<int>(current_piece.size());
    auto current_piece_col_num = static_cast<int>(current_piece[0].size());
    for (auto start_row_idx = 0; start_row_idx < grid_row_ + 1 - current_piece_row_num; start_row_idx++) {
        for (auto start_col_idx = 0; start_col_idx < grid_col_ + 1 - current_piece_col_num; start_col_idx++) {
            path_list.emplace_back(start_row_idx, start_col_idx);
            //do overlapping
            for (auto local_row_idx = 0; local_row_idx < current_piece_row_num; local_row_idx++) {
                for (auto local_col_idx = 0; local_col_idx < current_piece_col_num; local_col_idx++) {
                    my_map_arr[start_row_idx + local_row_idx][start_col_idx + local_col_idx] +=
                            current_piece[local_row_idx][local_col_idx];
                    my_map_arr[start_row_idx + local_row_idx][start_col_idx + local_col_idx] %= modulo_num_;

                }
            }
            if (DFSLookup(depth + 1, left_cells - pieces_sum_[depth], path_list, my_map_arr)) {
                return true;
            } else {
                path_list.pop_back();
                //revert overlapping
                for (auto local_row_idx = 0; local_row_idx < current_piece_row_num; local_row_idx++) {
                    for (auto local_col_idx = 0; local_col_idx < current_piece_col_num; local_col_idx++) {
                        my_map_arr[start_row_idx + local_row_idx][start_col_idx + local_col_idx] +=
                                modulo_num_ - current_piece[local_row_idx][local_col_idx];
                        my_map_arr[start_row_idx + local_row_idx][start_col_idx + local_col_idx] %= modulo_num_;
                    }
                }
            }
        }
    }
    if (depth == 2) {
        cout << "backtrack depth" << depth << endl;
    }
    return false;
}

int ModuloSolver::GetLeftNumsCount(const MatrixType &my_map_arr) {
    int count = 0;
    for (auto &row:my_map_arr) {
        for (auto col:row) {
            count += (modulo_num_ - col) % modulo_num_;
        }
    }
    return count;
}

void ModuloSolver::GetAnswer() {
    cout << "go get answer" << endl;
    auto left_cells = 0;
    for (auto i = 0; i < check_depth_; i++) {
        left_cells += pieces_sum_[i];
    }
    cout << left_cells << endl;
    vector<pair<unsigned char, unsigned char>> path_list;
    path_list.reserve(pieces_.size());
    auto map_matrix = modulo_grid_;
    DFSLookup(0, left_cells, path_list, map_matrix);
    cout << endl;
    cout << "[";
    for (auto i = 0; i < path_list.size(); i++) {
        cout << "(" << static_cast<int>(path_list[i].first) << "," << static_cast<int>(path_list[i].second) << ")";
        if (i == path_list.size() - 1)
            break;
        else
            cout << ",";
    }
    cout << "]";
    cout << endl;
}
