//
// Created by cheyulin on 11/2/16.
//

#include "state_space_search.h"


vector<string> ModuloSolver::Split(const string &s, char delim) {
    stringstream ss(s);
    string item;
    vector<string> elements;
    while (getline(ss, item, delim)) {
        elements.push_back(move(item));
    }
    return elements;
}


ModuloSolver::ModuloSolver(int modulo_num, string &grid_str, vector<string> &piece_strs) :
        modulo_num_(modulo_num) {
    cout << "modulo num:" << modulo_num << endl;
    modulo_grid_ = ExtractMatrix(grid_str);
    grid_row_ = static_cast<int>(modulo_grid_.size());
    grid_col_ = static_cast<int>(modulo_grid_[0].size());
    for (auto &ele:piece_strs) {
        auto tmp = ExtractMatrix(ele);
        pieces_.push_back(move(tmp));
    }
    stringstream ss;
    ss << "map, row size:" << grid_row_ << ",col_size:" << grid_col_;
    PrintMatrix(modulo_grid_, ss.str());


    pieces_sum_.reserve(pieces_.size());
    for (auto &ele:pieces_) {
        pieces_sum_.push_back(GetMatrixSum(ele));
    }
    for (auto i = 0; i < pieces_.size(); i++) {
        stringstream ss;
        ss << "piece" << i << "," << " sum is " << pieces_sum_[i] << ", state size:" << GetPieceStateSize(pieces_[i]);
        PrintMatrix(pieces_[i], ss.str());
    }

}

MatrixType ModuloSolver::ExtractMatrix(string &matrix_str) {
    vector<string> rows = std::move(Split(matrix_str, ';'));
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
