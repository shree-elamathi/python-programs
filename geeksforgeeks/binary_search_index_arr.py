##n= 65
##arr= 
##k= 15
###print(arr[4])
##class Solution:
##    def binarysearch(self, arr, n, k):
##        if k>(arr[0]):
##            if k<(arr[len(arr)-1]):
##                i=int(n/2)
##                if (k==arr[i]):
##                    return (i)
##                elif k<arr[i]:
##                    return ob.binarysearch(arr, i, k)
##                elif k>arr[i]:
##                    return (ob.binarysearch(arr,2*(i+int(i/2)), k))
##            else:
##                return ("-1")
##        else:
##            return ("-1")
##
##ob=Solution()
##print(ob.binarysearch(arr,n,k))
n=4
