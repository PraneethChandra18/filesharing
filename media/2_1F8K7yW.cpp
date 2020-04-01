#include<bits/stdc++.h>
using namespace std;

int main()
{
  ios_base::sync_with_stdio(false);
  cin.tie(NULL);

  int t;
  cin >> t;
  while(t--)
  {
    int n,q;
    cin >> n >> q;

    int a[n];

    for(int i=0;i<n;i++)
      cin >> a[i];

    int even=0;

    for(int i=0;i<n;i++)
    {
      int count=0;
      while(a[i]!=0)
      {
        if(a[i]%2==1)
          count++;
        a[i]=a[i]/2;
      }
      if(count%2==0)
        even++;
    }

    while(q--)
    {
      int p;
      cin >> p;
      int count=0;
      int flag=1;
      while(p!=0)
      {
        if(p%2==1)
          count++;
        p=p/2;
      }
      if(count%2==0)
        flag=0;
      if(flag==0)
        cout << even << " " << n-even << endl;
      else
        cout << n-even << " " << even << endl;
    }

  }
}
