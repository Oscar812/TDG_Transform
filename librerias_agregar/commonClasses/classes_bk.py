#Mod de las clases common

class Relacion_KRL:
  Nombre  =''
  Tipo    =''
  Origen  =''
  Target = [ ]
  def GetNom (self):
    return (self.Nombre)
  def GetDest (self):
    return (self.Destino)

class Nodo_KRL:
  Id      =''
  Nombre  = ''
  Rel_KRL = Relacion_KRL()
  def GetNom (self):
    return (self.Nombre)
  def GetId(self):
    return self.Id


#A = Nodo_KRL()
#A.Nombre='Matrimonio'
#A.Id='1'
#A.Rel_KRL.Nombre='Tiene'
#A.Rel_KRL.Origen='Matrimonio'
#A.Rel_KRL.Destino='Esposa'

#A.SetNom()
#A.Rel_KRL.SetNom()
#A.Rel_KRL.SetDest()
