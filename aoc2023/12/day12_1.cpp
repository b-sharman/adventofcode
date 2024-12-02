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
        istringstream ss {temp};
        vector<int> ns;
        for (string temp; getline(ss, temp, ',');) {
            ns.push_back(stoi(temp));
        }

        deque<string> q;
        q.push_front(s);
        string current_string, next_string;
        size_t next_q;
        while (!q.empty()) {
            current_string = q.front();
            // cout << current_string << endl;
            q.pop_front();
            // cout << "current_string: " << current_string << endl;
            next_q = current_string.find('?');
            if (next_q != current_string.npos) {
                q.push_front(current_string.replace(next_q, 1, 1, '.'));

                bool same_so_far = true;
                int current_group = 0;
                size_t group_index = 0;
                if (next_q) {
                    next_string = current_string.substr(0, next_q) + "#";
                    // cout << "next_string: " << next_string << endl;
                    for (const char& c : next_string) {
                        if (c == '#') {
                            current_group++;
                        }
                        else if (current_group) {
                            if (group_index >= ns.size() || ns.at(group_index) < current_group) {
                                same_so_far = false;
                                break;
                            }
                            group_index++;
                            current_group = 0;
                        }
                    }
                }
                if (same_so_far && (!current_group || (group_index < ns.size() && ns.at(group_index) >= current_group))) {
                    q.push_front(current_string.replace(next_q, 1, 1, '#'));
                }
                /*
                else {
                    cout << "next_string failed; ns = ";
                    for (const auto& n : ns) cout << n << " ";
                    cout<<endl;
                }
                */
            }
            else if (valid_arr(current_string, ns)) {
                 ans++;
            }
            /*
            else {
                cout << "failed; ns = ";
                for (const auto& n : ns) cout << n << " ";
                cout<<endl;
            }
            */
        }
        // cout << endl;
    }
    cout << ans << endl;

    return 0;
}
