def maptokens(data:list[str]) -> tuple[dict]:
  vocabs = list(sorted(set(''.join(data))))
  stoi   = {s:i for i,s in enumerate(vocabs)}
  itos   = {i:s for i,s in enumerate(vocabs)}

  return stoi, itos

def encode(cmmt:str) -> list[int]:
  token_ids = [stoi[x] for x in cmmt]
  return token_ids
