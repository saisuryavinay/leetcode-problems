void merge(int *A,int l,int m,int h)
{
  int result[h-l+1];
  int i=l,j=m+1,k=0;
  while(i<=m && j<=h)
    {
	  	if(A[i]<=A[j])
	  	{
	  	  result[k]=A[i];
	  	  i++;
	  	  k++;
		}
      	else
     	{
		result[k++]=A[j++];
	    }
	}
	    while(i<=m)
	    {
	    	result[k++]=A[i++];
		}
		while(j<=h)
		{
			result[k++]=A[j++];
		}
		k=0;
		for(i=l;i<=h;i++)
		{
			A[i]=result[k++];
        }
}
void merge_sort(int *A,int l,int h)
{
	if(l<h)
	{
		int m=(l+h)/2;
		merge_sort(A,l,m);
		merge_sort(A,m+1,h);
		merge(A,l,m,h);
	}
}
int maximumGap(int *a,int n){
    merge_sort(a,0,n-1);
    int i, v=0;
    for(i=0;i<n-1;i++)
    {
        if(v<a[i+1]-a[i])
        {
            v=a[i+1]-a[i];
        }
        
    } 
    return v;

}