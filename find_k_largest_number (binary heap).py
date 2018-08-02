### Q：You are given as input an unsorted array of n distinct numbers, where n is a power of 2. 
### Give an algorithm that identifies the second-largest number in the array, and that uses at most 
### n +log_2 n-2 comparisions

### Idea: use binary max-heap to solve this problem

def buildheap(arr):
    
    ### Input: Array with n elements
    ### Output: Heap
    ### Transfer array to heap
    
    n=len(arr)
    ind=n//2
    for i in range(ind,-1,-1):
        arr=list(siftdown(arr,i))
    return arr

def siftdown(arr,i):
    
     ### Input: Array with n elements, index of an element
     ### Output: New Array 
     
     size=len(arr)-1
     lc_ind=2*i+1
     rc_ind=2*i+2
     if rc_ind <=size:
         max_c=max(arr[lc_ind],arr[rc_ind])
         if max_c > arr[i]:
             if max_c==arr[lc_ind]:
                 arr[lc_ind]=arr[i]
                 arr[i]=max_c
                 arr=siftdown(arr,lc_ind)  #check if new child_node has to be siftdown 
             else:
                 arr[rc_ind]=arr[i]
                 arr[i]=max_c
                 arr=siftdown(arr,rc_ind)  #check if new child_node has to be siftdown 
     elif lc_ind <= size and rc_ind > size:
         if arr[lc_ind] > arr[i]:
             cur_v=arr[i]
             arr[i]=arr[lc_ind]
             arr[lc_ind]=cur_v
             arr=siftdown(arr,lc_ind)  #check if new child_node has to be siftdown 
     return arr
         
 
def partialsort(arr,k):
    
     ### Input: Array with n elements, top-k elements that we want
     ### Output: Top-k sorted version of array
     
    arr=buildheap(arr)
    arr_ps=[0]*k
    for i in range(k):
        arr_ps[i],arr=extractmax(arr)
    return arr_ps[-1]

def extractmax(arr):
    
    ### Input: Array with n elements
    ### Output: maximum value of array and a new array with size-1
     
    max_v=arr[0]
    arr[0]=arr.pop()
    arr=siftdown(arr,0)
    
    return max_v, arr
    


### More clean code
class find_k_largest_number():
    
    def __init__(self,arr,k):
        self.arr=arr
        self.k=k
        self.max_v = -1  #base case
        
    def buildheap(self):
        n=len(self.arr)
        ind=n//2
        for i in range(ind,-1,-1):
            self.siftdown(i)
            
    def siftdown(self,i):
        size=len(self.arr)-1
        lc_ind=2*i+1
        rc_ind=2*i+2
        if rc_ind <= size:
            max_c=max(self.arr[lc_ind],self.arr[rc_ind])
            if max_c > self.arr[i]:
                if max_c==self.arr[lc_ind]:
                    self.arr[lc_ind]=self.arr[i]
                    self.arr[i]=max_c
                    self.siftdown(lc_ind)  
                else:
                    self.arr[rc_ind]=self.arr[i]
                    self.arr[i]=max_c
                    self.siftdown(rc_ind)  
        elif lc_ind <= size and rc_ind > size:
            if self.arr[lc_ind] > self.arr[i]:
                cur_v=self.arr[i]
                self.arr[i]=self.arr[lc_ind]
                self.arr[lc_ind]=cur_v
                self.siftdown(lc_ind)   
    
    def extractmax(self):
        self.max_v=self.arr[0]
        self.arr[0]=self.arr.pop()
        self.siftdown(0)
    
    def partialsort(self):
         self.buildheap()  #use other function in the class
         for i in range(self.k):
             self.extractmax()  #use other function in the class
    
out=find_k_largest_number(arr,k=2)
out.partialsort()
out.arr
out.max_v





                 
                 