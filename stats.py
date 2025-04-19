def get_num_words(text: str) -> int:
  return len(text.split())

def get_num_characters(text: str) -> dict:
  dct = {}
  text = text.lower()
  for c in text:
    if c in dct:
      dct[c] += 1
    else:
      dct[c] = 1
  return dct

def sort_on(dict):
    return dict["count"]

def sort_chars(dct: dict) -> list:
  lst = [ {'char': k, 'count': v} for k,v in dct.items() ]
  lst.sort(reverse=True, key=sort_on)
  return lst
