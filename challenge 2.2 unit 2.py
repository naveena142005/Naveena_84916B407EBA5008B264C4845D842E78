#define the base class player 

class player:

  def play(self):
  
    print("The player is playing cricket.")

# define the derived class batsman

class Batsman(player):

  def play(self):
    print("The batsman is batting.")
    
# define the derived class bowler

class Bowler(player):

  def play(self):
    print("The Bowler is bowling.")

# define the object of Batsman and Bowler classes

batsman = Batsman()

bowler = Bowler()

# call the play() method for each object 

batsman.play()
bowler.play()