class count_inv():
    def __init__(self,file):
        with open(file) as f:
            rows=f.readlines()
        self.arr=[int(i) for i in rows]
    
    def sort_and_count_inv(self):
        if len(self.arr)==1:
            return self.arr,0
        else:
            n=len(self.arr)
            s=n//2
            left=self.arr[:s]
            right=self.arr[s:]
            left_sorted,left_count=sort_and_count_inv(left)
            right_sorted,right_count=sort_and_count_inv(right)
            full_sorted,middle_count=sort_and_merge_count(left_sorted,right_sorted,n)
            return full_sorted, left_count+right_count+middle_count
    
    def sort_and_merge_count(self,left_s,right_s,full_len):
        out=[]
        count=0
        left_ind=0
        right_ind=0
        while len(out) < full_len:
            if left_ind >= len(left_s):
                out=out+ right_s[right_ind:]
            elif right_ind >= len(right_s):
                out=out+left_s[left_ind:]
            elif left_s[left_ind] < right_s[right_ind]:
                out.append(left_s[left_ind])
                left_ind += 1
            elif left_s[left_ind] > right_s[right_ind]:
                out.append(right_s[right_ind])
                count += len(left_s)-left_ind
                right_ind += 1
        return out, count


arr_count=count_inv('array.txt')
arr_sorted,inv_count=arr_count.sort_and_count_inv()
print(inv_count)
print(inv_c)
