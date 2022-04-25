from scipy.stats import bernoulli
from scipy.stats import beta
import math

class agent:
    
    def __init__(self, q):
        self.quality     = q
        self.num_pulled  = 0
        self.num_rewards = 0
    
    def pull(self):
        self.num_pulled +=1
        reward = bernoulli.rvs(size=1,p=self.quality)[0]
        self.num_rewards += reward
        return reward

#class environment:
    
  #  def __init__(self):
  #      self.agents = []
  #  
  #  def pull(self, i):
        # pull agent i
        
