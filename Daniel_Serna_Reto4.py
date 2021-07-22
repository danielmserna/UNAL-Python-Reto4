import json
def lePodemosVender(fichasEnTienda, fichasRequeridas):
  fichasReqList = list(map(str,fichasRequeridas.split()))
  fichasAdquiridasAqui = []
  totalTienda = 0;
  for k,v in fichasEnTienda.items():
    if k in fichasReqList:
      totalTienda += v
      fichasAdquiridasAqui.append(k)
  print(str(totalTienda))
  print(' '.join(fichasAdquiridasAqui))

lePodemosVender(json.loads(input("")),input(""))