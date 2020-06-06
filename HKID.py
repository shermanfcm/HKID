import re

def validate(hkid): # omit parentheses
  weight = [9, 8, 7, 6, 5, 4, 3, 2, 1]
  values = list('0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ') +[None]
  
  match = re.match('^([A-Z])?([A-Z])([0-9]{6})([0-9A])$', hkid)
  if not match: return False
  
  hkidArr = []
  for g in match.groups():
    hkidArr += list(g) if g else [g]

  r = sum([values.index(i) * w for i, w in zip(hkidArr, weight)]) % 11

  return r == 0
