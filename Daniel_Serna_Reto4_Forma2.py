import json
def lePodemosVender(fichasEnTienda, fichasRequeridas):
  fichasReqList = list(map(str,fichasRequeridas.split()))
  fichasAdquiridasAqui = []
  totalTienda = 0;
  for i in range(0, len(fichasReqList)):
    if fichasReqList[i] in fichasEnTienda:
      totalTienda += fichasEnTienda.get(fichasReqList[i])
      fichasAdquiridasAqui.append(fichasReqList[i])
  print(str(totalTienda))
  print(' '.join(fichasAdquiridasAqui))

lePodemosVender(json.loads(input("")),input(""))