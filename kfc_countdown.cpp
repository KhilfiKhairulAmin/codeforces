#include <bits/stdc++.h>

using namespace std;

int main() {
  int T, c, k, k_min;
  
  scanf("%d", &T);

  while (T--) {
    scanf("%d%d", &k, &c);
    scanf("%d", &k_min);

    while(getchar() != '\n');

    if (c == 0 or k_min == 1) cout << 0;
    else if (c < k_min) printf("%d", c);
    else printf("%d", k_min-1);
    printf("\n");
  }
}