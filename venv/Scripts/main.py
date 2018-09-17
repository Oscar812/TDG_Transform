import xml.etree.ElementTree as ET
from operator import is_not
from functools import partial
import zlib
import base64
import commonClasses.classes as clases
import urllib.parse

def urlencode(str):
  return urllib.parse.quote(str)


def urldecode(str):
  return urllib.parse.unquote(str)


def decode_base64_and_inflate( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)


def deflate_and_base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )


'''
tree = ET.parse( 'Matrimonio.xml' )
root = tree.getroot()

xml_codificado= root[0].text
print ( xml_codificado )
result64= base64.b64decode( xml_codificado )
result_data = zlib.decompress( result64 , -15)
print ("Inflate")
print ( result_data )
sin_b = result_data.decode( 'utf-8' )
print ( sin_b )

matrimonio = urldecode( sin_b )

#print (matrimonio)'''

print( "DESPUES DE LA DECODIFICACIÓN Y CREACIÓN DEL NUEVO XML")
e = ET.parse('../Transformacion.xml')
root = e.getroot()
i = 0
k = 0
origen = [ ]
destino = [ ]


Nod = clases.NodoKRL
Ids = [Nod.Nombre,Nod.Id,Nod.Parent]

i = 0
data = ' '
Ids.clear()
for atype in e.findall('root'):
    for cell in atype.findall('object'):
        if cell.get('Transformador'):
            Nod.Nombre = cell.get('Transformador')
            Nod.Id = cell.get('id')
            Ids.insert(i,[Nod.Nombre, Nod.Id, Nod.Parent])
            i += 1
        else:
            if cell.get('Regla'):
                Nod.Nombre = cell.get('Regla')
                Nod.Id = cell.get('id')
                Ids.insert(i, [Nod.Nombre, Nod.Id, Nod.Parent])
                i += 1
            else:
                if cell.get('Elemento'):
                    Nod.Nombre = cell.get('Elemento')
                    Nod.Id = cell.get('id')
                    Ids.insert(i, [Nod.Nombre, Nod.Id, Nod.Parent])
                    i += 1
                else:
                    if cell.get('Desc_Class'):
                        Nod.Nombre = cell.get('Desc_Class')
                        Nod.Id = cell.get('id')
                        Ids.insert(i, [Nod.Nombre, Nod.Id, Nod.Parent])
                        i += 1
                    else:
                        if cell.get('Desc_Atributo'):
                            Nod.Nombre = cell.get('Desc_Atributo')
                            Nod.Id = cell.get('id')
                            Ids.insert(i, [Nod.Nombre, Nod.Id, Nod.Parent])
                            i += 1
                        else:
                            if cell.get('RelacionE'):
                                Nod.Nombre = cell.get('RelacionE')
                                Nod.Id = cell.get('id')
                                Ids.insert(i, [Nod.Nombre, Nod.Id, Nod.Parent])
                                i += 1


'''    for object in root.iter('object'):
        if cell.get('Transformador'):
            Nod.Nombre = cell.get('Transformador')
            Nod.Id = cell.get('id')
            Ids.insert(i,[Nod.Nombre, Nod.Id, Nod.Parent])
            i += i
        else:
            Nod.Nombre = cell.get('Transformador')
            Nod.Id = cell.get('id')
            Ids.insert(i, [Nod.Nombre, Nod.Id, Nod.Parent])
            i += i'''

#for object in root.iter('object'):
print(Ids)
    #print(object.attrib.find("': '"))