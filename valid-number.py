def solution(s):
  """
  "0" => true
  " 0.1 " => true
  "abc" => false
  "1 a" => false
  "2e10" => true
  " -90e3   " => true
  " 1e" => false
  "e3" => false
  " 6e-1" => true
  " 99e2.5 " => false
  "53.5e93" => true
  " --6 " => false
  "-+3" => false
  "95a54e53" => false
  """

  import re 
                          # +-   1,1.,1.2   .2 1 11     e,e-,e+,e+1,e-1
  pattern = re.compile(r"^[+-]?((\d+\.?\d*)|(\d*\.?\d+))(e[+-]?\d+)?$")
  return pattern.match(s.strip(" "))
