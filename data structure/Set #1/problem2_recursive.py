# python3

import sys, threading
sys.setrecursionlimit(10**7) # max depth of recursion
threading.stack_size(2**27)  # new thread will get stack of such size

class TreeHeight:
        def read(self):
                self.n = int(sys.stdin.readline())   #读取第一行
                self.parent = list(map(int, sys.stdin.readline().split())) #读取第二行

        def compute_height(self):
                # Replace this code with a faster implementation
                maxdepth=0
                for i in range(self.n):
                    height=0
                    child_ind=i
                    while self.parent[child_ind]!=-1:  #一直循环至父节点
                        height += 1
                        child_ind=self.parent[child_ind]
                    maxdepth=max(maxdepth,height) 
                return maxdepth+1   #while停止少一
        
        
def main():
  tree = TreeHeight()
  tree.read()
  print(tree.compute_height())

threading.Thread(target=main).start()
