

class CorpusReader:
  """
  This class gives access to the paralysis files in the paralysis format.
  """
  
  def __init__(self):
    
    pass
  
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
        if not line.startswith("#"): # ignore comments
          try:
            id,text = line.split("\t",2)
            contents.append((id,text))
          except ValueError:
            pass
          
    self.pars = contents
          
if __name__ == '__main__':
  
  c = CorpusReader()
  c.read_file("/Users/thommy/Documents/Bible/PBC/corpus/deu-elberfelder_1905.pbt")
