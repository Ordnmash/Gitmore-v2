def build_dataset(commits):
  x, y = [],[]
  for c in commits:
    xx = []
    yy = []
    for ch in '^' + c + '^':
      xx.append(stoi[ch])
      yy.append(stoi[ch])
  
    x.append(torch.tensor(xx[:-1]))
    y.append(torch.tensor(yy[1:]))
  
  return x, y
