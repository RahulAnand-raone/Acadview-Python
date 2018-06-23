      #BFS PROGRAM

#from collections import defaultdict

#class Graph:
#    def __init__(self):
#        self.graph=defaultdict(list)

#    def add_edge(self,u,v):
#        self.graph[u].append(v)
#        self.graph[v].append(u)

#    def BFS(self,arg):
#        visited=[False]*len(self.graph)
#        queue=[]
#        queue.append(arg)
#        visited[arg]=True
#        while queue:
#            l=queue.pop(0)
#            print(l)
#            for i in self.graph[l]:
#                if visited[i]==False:
#                    queue.append(i)
#                    visited[i]=True

#g=Graph()
#g.add_edge(0,1)
#g.add_edge(0,2)
#g.add_edge(1,3)
#g.add_edge(1,4)
#g.add_edge(2,5)
#print(g.graph)
#g.BFS(1)



            #DFS PROGRAM

#from collections import defaultdict

#class Graph:
 #   def __init__(self):
  #      self.graph=defaultdict(list)
#
 #   def add_edge(self,u,v):
  #      self.graph[u].append(v)
   #     self.graph[v].append(u)
    #    
    #def dfs_traverse(self,arg,visited):
     #   visited[arg]=True
     #   print(arg)
      ###        self.dfs_traverse(i,visited)
#
 ##      visited=[False]*len(self.graph)
   #     self.dfs_traverse(arg,visited)
##g=Graph()
#g.add_edge(0,1)
#g.add_edge(0,2)
##g.add_edge(1,3)
#g.add_edge(1,4)
#g.add_edge(2,5)
#print(g.graph)
#g.DFS(1)

         # Pangram program
#l=set(string.ascii_lowercase[:])
#s=input().lower().replace(' ','')
#if(set(s)==l):
#    print('pangram')
#else:
#    print('Not pangram')



       #to display notification on windows

#from win10toast import ToastNotifier
#toaster=ToastNotifier()
#toaster.show_toast("Hello World!!!","Python is 10 seconds awsm!",icon_path="favicon.ico",duration=10)
#toaster.show_toast("Example two","This notification is in its own thread!",icon_path=None,duration=5,threaded=True)



