def solution(s):
  x = sorted(set(s))
  res = "
  
  while s:
    for i in x:
      if i in s:
        res += i
        s = s.replace(i, '', 1)
    
    for i in x[::-1]:
      if i in s:
        res += i
        s = s.replace(i, '', 1)

  return res