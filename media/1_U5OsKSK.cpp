#include<bits/stdc++.h>
using namespace std;

int main()
{
  long long int q;
  cin >> q;
  while(q--)
  {
    long long int n,m;
    cin >> n >> m;
    long long int p[n],f[n];
    for(long long int i=0;i<n;i++)
      cin >> f[i];
    for(long long int i=0;i<n;i++)
      cin >> p[i];

    map<long long int,long long int> typecost;

    for(long long int i=0;i<n;i++)
    {
      if(typecost.find(f[i])!=typecost.end())
        typecost[f[i]]+=p[i];
      else
        typecost[f[i]]=p[i];
    }
    long long int min=INT_MAX;
    for(auto t:typecost)
    {
      if(typecost[t.first]<min)
        min = typecost[t.first];
    }
    cout << min << endl;
  }
}
