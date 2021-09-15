H,M = map(int, input().split()) 

if 1 <= H < 24 and M >= 45: 
  print("{} {}".format(H, M-45))
elif 1 <= H < 24 and M < 45:
  print("{} {}".format(H-1, 60-(45-M)))
elif H == 0 and M >= 45:
  print("{} {}".format(H, M-45))
elif H == 0 and M < 45:
  print("{} {}".format(23, 60-(45-M)))




