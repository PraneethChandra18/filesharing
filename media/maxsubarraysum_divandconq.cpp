/*
  Implementation of maximum subarray sum using Divide and Conquer ....
  Time complexity - O(nlogn)
*/

#include<bits/stdc++.h>
#define lli long long int
#define fi(i,s,n) for(lli i=s;i<n;i++)
#define fd(i,s,n) for(lli i=s;i>=n;i--)

using namespace std;

lli max(lli a,lli b,lli c)
{
  if(a>b)
  {
    if(a>c)
      return a;
    else return c;
  }
  else
  {
    if(b>c)
      return b;
    else
      return c;
  }
}

lli maxcrossingsum(lli *a,lli l,lli r,lli m)
{
  lli sum=0;
  lli left_sum=0,right_sum=0;
  fd(i,m,0)
  {
    sum = sum + a[i];
    if(sum > left_sum)
    {
      left_sum = sum;
    }
  }
  sum=0;
  fi(i,m+1,r+1)
  {
    sum = sum + a[i];
    if(sum > right_sum)
    {
      right_sum = sum;
    }
  }
  return left_sum + right_sum;
}

lli maxsubarraysum(lli *a,lli l,lli r)
{
  if(l==r)
  {
    return a[l];
  }
  lli m = l+(r-l)/2;
  return max(maxsubarraysum(a,l,m),maxsubarraysum(a,m+1,r),maxcrossingsum(a,l,r,m));
}

int main()
{
  lli n;
  cin >> n;
  lli a[n];
  fi(i,0,n)
    cin >> a[i];
  cout << maxsubarraysum(a,0,n-1) << endl;
}
