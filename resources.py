def maptokens(data:list[str]) -> tuple[dict]:
  vocabs = list(sorted(set(''.join(data))))
  stoi   = {s:i for i,s in enumerate(vocabs)}
  itos   = {i:s for i,s in enumerate(vocabs)}

  return stoi, itos
