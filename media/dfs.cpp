#include<bits/stdc++.h>
using namespace std;

list<int> *adj;

void createGraph(int V)
{
  adj = new list<int>[V];
}

void addEdge(int V1,int V2)
{
  adj[V1].push_back(V2);
  adj[V2].push_back(V1);
}

void DFS(int V,int c)
{
  int isVisited[V];
  for(int j=0;j<V;j++)
  {
    isVisited[j]=0;
  }
  stack<int> dfs;
  int s = c;
  label:
  cout << s << " ";
  dfs.push(s);
  isVisited[s]=1;
  while(!dfs.empty())
  {
    list<int>::iterator i;
    for(i=adj[s].begin();i!=adj[s].end();i++)
    {
      if(isVisited[*i]==0)
      {
        isVisited[*i] = 1;
        s = *i;
        cout << s << " ";
        dfs.push(s);
        break;
      }
    }
    if(i==adj[s].end())
    {
      dfs.pop();
      if(!dfs.empty())
      s = dfs.top();
    }
  }
  for(int k=0;k<V;k++)
  {
    if(isVisited[k]==0)
    {
      s = k;
      goto label;
    }
  }

}

int main()
{
  createGraph(12);
  addEdge(0,2);
  addEdge(2,1);
  addEdge(0,1);
  addEdge(3,4);
  addEdge(4,5);
  addEdge(3,6);
  addEdge(8,10);
  addEdge(10,11);
  DFS(12,0);
}
