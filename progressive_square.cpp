#include <bits/stdc++.h>

using namespace std;

int main() {
  int T;

  scanf("%d", &T);

  while(T--) {
    int n, c, d, minimum = 2147483647;
    scanf("%u%u%u", &n, &c, &d);
    vector<int> bs;

    int i = pow(n, 2);
    while(i--) {
      int b;
      scanf("%d", &b);
      bs.push_back(b);
      if (b < minimum) {
        minimum = b;
      }
    }
    i = n;
    int cur = minimum;
    bool flag = true;
    while(i--) {
      int j = n;
      while(j--) {
        auto k = find(bs.begin(), bs.end(), cur);
        if (k == bs.end()) {
          flag = false;
          break;
        }
        bs.erase(k);
        cur += c;
      }
      if (!flag) {
        break;
      }
      minimum += d;
      cur = minimum;
    }
    if (flag) printf("YES\n");
    else printf("NO\n");
  }
}
