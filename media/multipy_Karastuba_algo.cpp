/*
  Implementation of multiplication using Karastuba's algorithm ....
  Time complexity - O(n^(log3))
*/



#include<bits/stdc++.h>
#define lli long long int
#define fi(i,s,n) for(lli i=s;i<n;i++)
#define fd(i,s,n) for(lli i=s;i>=n;i--)

using namespace std;
string add(string p,string q)
{
  int carry=0;
  int k,i;
  string r,s,res;

  int n1=p.length();
  int n2=q.length();
  reverse(p.begin(),p.end());
  reverse(q.begin(),q.end());
  if(n1<n2)
  {
   p.swap(q);
   int t;
   t=n1;
   n1=n2;
   n2=t;
  }
  if(n1!=n2)
  {
  for(i=0;i<n2;i++)
  {
    k=carry+(p[i]-'0')+(q[i]-'0');
    carry=k/10;
    r.push_back(k%10+'0');
  }
  for(i=n2;i<n1;i++)
  {
    if(i!=n1-1)
    {
    k=carry+(p[i]-'0');
    carry=k/10;
    r.push_back(k%10+'0');
    }
    else
    {
      k=carry+(p[i]-'0');
      s = to_string(k);
    }
    }
  }
  else{
    for(i=0;i<n1;i++)
    {
      if(i!=n1-1)
      {
      k=carry+(p[i]-'0')+(q[i]-'0');
      carry=k/10;
      r.push_back(k%10+'0');
      }
      else
      {
        k=carry+(p[i]-'0')+(q[i]-'0');
        s = to_string(k);
      }
    }
  }
    reverse(r.begin(),r.end());
    res=s.append(r);
    return res;
}

string substract(string p,string q)
{
  int i,k;
  string c;

  int d=0;
  while(p[d]=='0')
  {
    p.replace(d,1,"");
    d++;
    if(p[d]!=0){
      break;
    }
  }
  d=0;
  while(q[d]=='0')
  {
    q.replace(d,1,"");
    d++;
    if(q[d]!=0){
      break;
    }
  }
  int n1=p.length();
  int n2=q.length();

  if(n1==n2)
  {
    for(int j=0;j<n1;j++)
    {
      if(p[j]==q[j])
      {
        continue;
      }
      if(p[j]<q[j])
      {
        p.swap(q);
        break;
      }
      if(p[j]>q[j])
      {
        break;
      }
    }
  }
  if(n1<n2)
  {
   p.swap(q);
   int t;
   t=n1;
   n1=n2;
   n2=t;
  }

  reverse(p.begin(),p.end());
  reverse(q.begin(),q.end());

  if(n1!=n2){
  for(i=0;i<n2;i++)
  {
    if(p[i]>=q[i])
    {
      k=p[i]-q[i];
    }
    else
    {
      int l;
      for(l=i+1;l<n1;l++)
      {
        if(p[l]!='0')
        {
          p[l]--;
          break;
        }else
        {
          p.replace(l,1,"9");
          continue;
        }
      }
      k=10+p[i]-q[i];
    }
    c.push_back(k+'0');
  }
    for(i=n2;i<n1;i++)
    {
      k=p[i]-'0';
      c.push_back(k+'0');
    }
 }
 else
 {
   for(i=0;i<n1;i++)
   {
     if(p[i]>=q[i])
     {
       k=p[i]-q[i];
     }
     else
     {
       p[i+1]--;
       k=10+p[i]-q[i];
     }
     c.push_back(k+'0');
  }
 }
  reverse(c.begin(),c.end());
  return c;
}

int multiply(string x,string y)
{
  lli n1 = x.size();
  lli n2 = y.size();
  string x1 = x.substring(0,n1/2);
  string x0 = x.substring(n1/2,n1-(n1/2));
  string y1 = y.substring(0,n2/2);
  string y0 = y.substring(n2/2,n2-(n2/2));
}

int main()
{
  string x,y;
  cout << multiply(x,y) << endl;
}
