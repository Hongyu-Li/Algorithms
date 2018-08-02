# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())   #读取第一行
                self.parent = list(map(int, sys.stdin.readline().split())) #读取第二行
                self.depth=[0]*self.n

        def get_height(self,ind):
                if self.depth[ind]!=0:
                    depth=self.depth[ind]
                else:
                    if self.parent[ind]==-1:
                        depth=1
                    else:
                        depth=self.get_height(self.parent[ind])+1 #类内引用
                return depth
        
        def compute_height(self):
            for i in range(self.n):
                self.depth[i]=self.get_height(i)
            return max(self.depth)
        
            
        
        
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
