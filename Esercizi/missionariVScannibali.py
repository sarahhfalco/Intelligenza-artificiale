from search4e import Problem, path_states, uniform_cost_search

class CannibaliMissionari(Problem):

  def __init__(self,N = 3, BC = 2):
    self.initial = (N,N,1)
    self.goal = (0,0,0)
    self.boatCapacity = BC
    self.numMiss = N

  def action_cost(self, s, action, s1): return 1

  def h(self, node): return 0

  def result(self, state, action):
        "States are represented by (m, c, b) triples, actions by pairs (mb,cb)"
        (m,c,b) = state
        (m1,c1) = action
        if b == 0:
          return (m+m1,c+c1,1)
        else:
          return (m-m1,c-c1,0)

  def actions(self, state):
        res = []
        (ms,cs,bs) = state
        # if the boat is on the right, compute the configuration of people on that river side
        if bs == 0:
          ms = self.numMiss - ms
          cs = self.numMiss - cs
        
        for m in range(min(ms,self.boatCapacity)+1):
          for c in range(min(cs,self.boatCapacity)+1):
            # check if the travel on the boat is ok
            if (m >= c or m == 0) and 0< m+c <= self.boatCapacity:
              (mNew,cNew,bNew) = self.result(state,(m,c))
              # check if the subsequent state would be a feasible one
              if mNew == cNew or (mNew > cNew and mNew == self.numMiss)  or mNew == 0:
                res.append((m,c))
        return res

#####################################
# Try it with some different number of people and of boat capacity
p = CannibaliMissionari(3,2)

print(path_states(uniform_cost_search(p)))

#TODO add some nice printing of what happened...

