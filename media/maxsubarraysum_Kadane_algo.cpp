/*
  Implementation of maximum subarray sum using Kadane’s Algorithm ....
  Time complexity - O(n)
*/

#include<bits/stdc++.h>
#define lli long long int
#define fi(i,s,n) for(lli i=s;i<n;i++)
#define fd(i,s,n) for(lli i=s;i>=n;i--)

using namespace std;

lli maxsubarraysum(lli *a,lli n)
{
    lli max_so_far=0,sum=0;
    lli start,end,s;
    fi(i,0,n)
    {
      sum = sum + a[i];
      if(sum < 0)
      {
        sum = 0;
        s = i+1;
      }
      if(max_so_far < sum)
      {
        max_so_far = sum;
        end = i;
        start = s;
      }
    }
    cout << "start : "<<start <<" | "<< "end : "<<end << endl;
    return max_so_far;
}


int main()
{
  lli n;
  cin >> n;
  lli a[n];
  fi(i,0,n)
    cin >> a[i];
  cout << maxsubarraysum(a,n) << endl;
}
