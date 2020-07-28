/*
  Implementation of gcd ....
  Time complexity - O(log b)
*/

#include<bits/stdc++.h>
#define lli long long int
#define fi(i,s,n) for(lli i=s;i<n;i++)
#define fd(i,s,n) for(lli i=s;i>=n;i--)

using namespace std;

lli gcd(lli a,lli b)
{
  if(b==0)
    return a;
  else return gcd(b,a%b);
}

int main()
{
  lli a,b;
  cin >> a >> b;
  cout << gcd(a,b) << endl;
}
