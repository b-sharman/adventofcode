#include <bits/stdc++.h>

using namespace std;

vector<int> n_from_s(const string& s) {
    vector<int> ret;
    int current_group = 0;
    for (const char& c : s) {
        if (c == '#') {
            current_group++;
        }
        else {
            if (current_group) ret.push_back(current_group);
            current_group = 0;
        }
    }
    if (current_group) ret.push_back(current_group);
    return ret;
}

bool valid_arr(const string& s, const vector<int>& n) {
    return n_from_s(s) == n;
}

int main() {
    cout << "starting" << endl;
    size_t nl;
    cin>>nl;
    string s, temp;
    long long ans = 0;
    for (size_t i=0; i<nl; i++) {
        cin >> s;
        cin >> temp;
        // temp = temp+","+temp+","+temp+","+temp+","+temp;
        istringstream ss {temp};
        vector<int> ns;
        for (string temp; getline(ss, temp, ',');) {
            ns.push_back(stoi(temp)+1);
        }

        /* if index of the first group of # is <= its size in ns
         * that adds a lot of restriction to where the first group can be
         * look at the next group of # (if it exists) and place restrictions on it
         * do this until no more restrictions can be placed
         * then switch sides
         * keep doing this until both sides are at the point where no more restrictions can be placed
         *
         * next, check for groups of # whose size narrows which ns they correspond to
         *
         * after that, just brute-force the rest
         */
    }
    return 0;
}
