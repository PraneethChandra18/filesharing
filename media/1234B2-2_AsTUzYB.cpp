#include<bits/stdc++.h>
using namespace std;

struct HashNode
{
  int key;
};

int capacity;
HashNode **arr;

void Hashmap()
{
  arr = new HashNode*[capacity];
  for(int i=0 ; i < capacity ; i++)
            arr[i] = NULL;
}
struct HashNode *createNode(int k)
{
  struct HashNode *temp = new HashNode;
  temp->key = k;
  return temp;
}
struct HashNode *dummy = createNode(-1);

int Hashcode(int k)
{
  return k%capacity;
}
/* -----------------------------------------------------------------------------*/

void insert(int k)
{
  struct HashNode *temp = createNode(k);
  int hashindex = Hashcode(k);
  int count=0;
  while(arr[hashindex]!=NULL && arr[hashindex]->key!=k && arr[hashindex]->key!=-1)
  {
    if(count>capacity)
    {
      cout << "Hashtable is full" << endl;
      return;
    }
    count++;
    hashindex++;
    hashindex%=capacity;
  }
  if(arr[hashindex]==NULL || arr[hashindex]->key==-1)
  arr[hashindex]=temp;
}

void deletenode(int k)
{
  int hashindex=Hashcode(k);
  int count=0;
  while(arr[hashindex])
  {
    if(count>capacity)
    {
      cout << "Key doesnt exist" << endl;
      return;
    }
    count++;
    if(arr[hashindex]->key==k)
    {
      arr[hashindex] = dummy;
      return;
    }
    hashindex++;
    hashindex%=capacity;
  }
}

int search(int k)
{
  int hashindex=Hashcode(k);
  int count=0;
  while(arr[hashindex])
  {
    if(count>capacity)
      break;
    count++;
    if(arr[hashindex]->key==k)
    {
      return 1;
    }
    hashindex++;
    hashindex%=capacity;
  }
  return 0;
}


int main()
{
  int n,k;
  cin >> n;
  cin >> k;
  long long int id[n];
  for(int i=0;i<n;i++)
  {
    cin >> id[i];
  }
  capacity=n;
  Hashmap();
  queue<int> r;
  r.push(id[0]);
  insert(id[0]);
   for(int i=1;i<n;i++)
   {
     int num = id[i];
     int flag=0;
      if(search(num))
        flag=1;
      if(flag==0)
      {
        if(r.size()!=k)
        {
          r.push(num);
          insert(num);
        }
        else if(r.size()==k)
        {
          int fi=r.front();
          r.pop();
          deletenode(fi);
          i--;
        }

      }
   }
   int s=r.size();
   int res[s];
      cout << s << endl;
   for(int i=0;i<s;i++)
   {
     res[i]=r.front();
     r.pop();
   }
   for(int i=s-1;i>=0;i--)
   {
     cout << res[i] << " ";
   }


}
