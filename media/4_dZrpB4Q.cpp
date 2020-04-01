#include<bits/stdc++.h>
using namespace std;

int main()
{
  long long int q;
  cin >> q;
  while(q--)
  {
    long long int n,k;
    cin >> n >> k;
    int a[k][n];
    for(int i=0;i<k;i++)
      for(int j=0;j<n;j++)
        cin >> a[i][j];
    for(int i=0;i<k;i++)
      for(int j=0;j<n;j++)
        a[i][j] = a[i][j]-1;

    int adj[n][n]={0};

    for(int i=0;i<n;i++)
    {
      for(int j=i+1;j<n;j++)
      {
        adj[a[0][i]][a[0][j]]=1;
      }
    }

    for(int p=1;p<k;p++)
    {
      for(int i=0;i<n;i++)
      {
        for(int j=i+1;j<n;j++)
        {
          adj[a[p][j]][a[p][i]]=0;
        }
      }
    }
    int indeg[n]={0};
    for(int i=0;i<n;i++)
    {
      for(int j=0;j<n;j++)
      {
        if(adj[j][i]==1)
          indeg[i]+=1;
      }
    }
    vector<int> outdeg[n];
    for(int i=0;i<n;i++)
    {
      for(int j=0;j<n;j++)
      {
        if(adj[i][j]==1)
          outdeg[i].push_back(j);
      }
    }

    for(int i=0;i<n;i++)
    {
      while(outdeg[i].size()>1)
      {
        
      }
    }
  }
}
