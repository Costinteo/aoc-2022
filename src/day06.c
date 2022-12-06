#include<stdio.h>
main(){
	int w=4,i=0,x=1;
	char a[123]={},b[8192],*p=b;
	gets(b);
	++a[*p];++a[p[1]];++a[p[2]];
	for(;x;p++)x=a[*p]+a[p[1]]+a[p[2]]+ ++a[p[3]]-w,a[*p]--;
	--a[*p];--a[p[1]];--a[p[2]];
	printf("%d",(p-b)+3);
	w=13,p=b,x=1;
	for(;x;p++){
		for(;i++<w;)
			++a[p[i]];
		i=0;x=0;
		for(;i++<w;)
			x+=a[p[i]];
		x+=++a[p[w]]-w;
		a[*p]--;
	}
	printf("%d",(p-b)+w);
}
