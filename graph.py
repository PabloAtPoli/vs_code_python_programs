class Graph:
   def __init__(self,gdict=None):
      if gdict is None:
         gdict = []
      self.gdict = gdict
# Get the keys of the dictionary
   def get_vertices(self):
      return list(self.gdict.keys())
   def edges(self):
      return self.find_edges()
# Find the distinct list of edges
   def find_edges(self):
      edgename = []
      for vrtx in self.gdict:
         for nxtvrtx in self.gdict[vrtx]:
            if {vrtx, nxtvrtx } not in edgename:
                edgename.append({vrtx, nxtvrtx})
      return edgename



# Create the dictionary with graph elements
graph_elements = { 
   "a" : ["b","c"],
   "b" : ["a", "d"],
   "c" : ["a", "d"],
   "d" : ["e"],
   "e" : ["d"]
}

g = Graph(graph_elements)
print(g.get_vertices())
print(g.edges())