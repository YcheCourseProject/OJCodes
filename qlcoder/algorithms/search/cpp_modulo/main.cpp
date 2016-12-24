#include <iostream>
#include "state_space_search.h"


int main(int argc, char *argv[]) {
    cout << argc << endl;
    auto modulo_num = stoi(argv[1]);
    auto map_str = string(argv[2]);
    vector<string> piece_strs;
    for (auto i = 3; i < argc; i++) {
        if (argv[i][0] == '>')
            break;
        auto piece_str = argv[i];
        piece_strs.push_back(move(piece_str));
    }

    ModuloSolver moduloSolver(modulo_num, map_str, piece_strs);
    moduloSolver.GetAnswer();
    return 0;

}