import os

class CorpusReader:
  """
  This class gives access to the paralysis files in the paralysis format.
  """
  
##############################################################################
  
  def __init__(self,path):
    
    self.path = path
  
##############################################################################
  
  def read_file(self,file):
    """
    This method reads a file and stores its content in a tuple with
    1. the ID as the first element and
    2. the text as the second element.
    Comment lines marked with a hash '#' as the first symbol are ignored.
    """
    
    contents = list()
    
    with open(file) as input_file:
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
          
if __name__ == '__main__':
  
  c = CorpusReader("../../../Tools/UDHR/data/par/")
  c.read_texts()
