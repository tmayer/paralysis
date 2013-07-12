import os

class Corpus:
  """
  This class gives access to the paralysis files in the paralysis format.
  """
  
##############################################################################
  
  def __init__(self,path=""):
    
    if os.path.isdir(path):
        self.path = path
    # check for Paralleltext bibles
    else:
        self.path = "/Users/thommy/paralleltext.info/v0.52/clean/"

    self.get_texts()
  

    
##############################################################################

  def read_texts(self):
    """
    This method reads all the files in the specified folder and collects the
    parallel texts in a list of tuples.
    """
    
    corpus_files = [f for f in os.listdir(self.path) if f.endswith(".txt")]
    
    self.texts = list()
    
    for corpus_file in corpus_files:
      curr_text = self.read_file(self.path + corpus_file)
      self.texts.append((corpus_file[:-4],curr_text))
      
##############################################################################

  def get_texts(self):
    """
    This method reads all the files in the specified folder and collects the
    parallel texts in a list of tuples.
    """
    
    self.texts  = {count+1:f for count,f in 
                    enumerate(os.listdir(self.path)) if f[-4:] == ".txt"}
    
##############################################################################

  def show_texts(self):
    """
    This method prints all texts of the corpus_reader object.
    """
    
    texts = [(t,self.texts[t][:3] + self.texts[t][11:-4]) for t in self.texts]
    
    for nr,text in sorted(texts):
        print("{:>3}: {}".format(nr,text))
    
    #print("".join(texts))
    
##############################################################################

  def __len__(self):
    """
    This method returns the number of texts in the corpus object.
    """
    
    return len(self.texts)
    

##############################################################################
# class TEXT
##############################################################################

class Text:
    """
    This class provides all necessary functionalities to access the parallel
    text from the corpus.
    """
    
    def __init__(self,file_name):
        
##############################################################################
  
  def read_file(self,file_name):
    """
    This method reads a file and stores its content in a tuple with
    1. the ID as the first element and
    2. the text as the second element.
    Comment lines marked with a hash '#' as the first symbol are ignored.
    """
    
    contents = list()
    
    with open(file_name) as input_file:
      lines = input_file.readlines()
      for line in lines:
        line = line.strip()
        if not line[0] == "#": # ignore comments
          try:
            id,text = line.split("\t",2)
            contents.append((id,text))
          except ValueError:
            pass
          
    return contents
        
          
if __name__ == '__main__':
  
  c = Corpus()
  c.show_texts()
