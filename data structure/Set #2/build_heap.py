# python3

class HeapBuilder:
  def __init__(self):
    self._swaps = []
    self._data = []
    self.n = 0

  def ReadData(self):
    self.n = int(input())
    self._data = [int(s) for s in input().split()]
    assert self.n == len(self._data)

  def WriteResponse(self):
    print(len(self._swaps))
    for swap in self._swaps:
      print(swap[0], swap[1])

  def GenerateSwaps(self,i):
    # The following naive implementation just sorts 
    # the given sequence using selection sort algorithm
    # and saves the resulting sequence of swaps.
    # This turns the given array into a heap, 
    # but in the worst case gives a quadratic number of swaps.
    #
    # TODO: replace by a more efficient implementation
    size=len(self._data)-1
    lc_ind=2*i+1
    rc_ind=2*i+2
    if rc_ind <= size:
        min_c=min(self._data[lc_ind],self._data[rc_ind])
        if min_c < self._data[i]:
            if min_c==self._data[lc_ind]:
                self._swaps.append([i,lc_ind])
                self._data[lc_ind]=self._data[i]
                self._data[i]=min_c
                self.GenerateSwaps(lc_ind)
            else:
                self._swaps.append([i,rc_ind])
                self._data[rc_ind]=self._data[i]
                self._data[i]=min_c
                self.GenerateSwaps(rc_ind)
    elif lc_ind <= size and rc_ind > size:
        if self._data[lc_ind] < self._data[i]:
            self._swaps.append([i,lc_ind])
            cur_v=self._data[lc_ind]
            self._data[lc_ind]=self._data[i]
            self._data[i]=cur_v
    

  def Solve(self):
    self.ReadData()
    for i in range(self.n//2,-1,-1):
        self.GenerateSwaps(i)
    self.WriteResponse()

if __name__ == '__main__':
    heap_builder = HeapBuilder()
    heap_builder.Solve()
