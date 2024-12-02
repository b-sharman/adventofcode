#include <bits/stdc++.h>

using namespace std;

bool valid_arr(string s, vector<int> n) {
    vector<int> damaged;
    int current_group = 0;
    for (const char& c : s) {
        if (c == '#') {
            current_group++;
        }
        else {
            if (current_group) damaged.push_back(current_group);
            current_group = 0;
        }
    }
    if (current_group) damaged.push_back(current_group);
    return damaged == n;
}

int main() {
    size_t nl;
    cin>>nl;
    string s, temp;
    long long ans = 0;
    for (size_t i=0; i<nl; i++) {
        cin >> s;
        cin >> temp;
        istringstream ss {temp};
        vector<int> ns;
        for (string temp; getline(ss, temp, ',');) {
            ns.push_back(stoi(temp));
        }

        // compute all possible permutations of s
        // make a queue of current strings
        // while there are ?s in the current string
        // remove the current string and replace it with two more current strings
        deque<string> q;
        q.push_front(s);
        string current_string, next_string;
        size_t next_q;
        while (!q.empty()) {
            current_string = q.front();
            q.pop_front();
            next_q = current_string.find('?');
            if (next_q == current_string.npos) {
                if (valid_arr(current_string, ns)) ans++;
            }
            else {
                next_string = current_string.replace(next_q, 1, 1, '.');
                q.push_front(next_string);
                next_string = current_string.replace(next_q, 1, 1, '#');
                q.push_front(next_string);
            }
        }
    }
    cout << ans << endl;

    return 0;
}
