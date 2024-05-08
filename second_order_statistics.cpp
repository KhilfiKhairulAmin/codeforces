#include <bits/stdc++.h>

using namespace std;

int main() {
  int n;
  
  set<int> a;

  scanf("%d", &n);

  getchar();
  int temp;
  while(n--) {
    scanf("%d", &temp);
    a.insert(temp);
  }

  int minimum = *a.begin();
  auto maximum = --a.end();

  if (*maximum == minimum) {
    printf("NO");
  }
  else {
    auto maximum = --a.end();
    while (*(--maximum) != minimum);
    printf("%d", *(++maximum));
  }
}
