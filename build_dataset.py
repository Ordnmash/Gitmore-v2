def build_dataset(commits):
  x = []
  y = []
  for c in commits:
    xx = [] 
    yy = []
    for ch in '^' + c + '^': # wrap each commit between special tokens for training efficiency
      xx.append(stoi[ch])
      yy.append(stoi[ch])
    x.append(torch.tensor(xx[:-1]))
    y.append(torch.tensor(yy[1:]))
  return x, y # return the dataset as list of variable sequence length
