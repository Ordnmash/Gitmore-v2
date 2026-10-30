def build_dataset(commits: list[str]) -> tuple[list]:
  x = []
  y = []
  for c in commits:
    xx = [] 
    yy = []
    for ic in '^' + c + '^':
      xx.append(stoi[ic])
      yy.append(stoi[ic])
    x.append(torch.tensor(xx[:-1]))
    y.append(torch.tensor(yy[1:]))
  return (x,y)
