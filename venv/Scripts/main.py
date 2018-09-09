import xml.etree.ElementTree as ET
from operator import is_not
from functools import partial
import zlib
import base64
import urllib.parse
import commonClasses.classes as classes

def urlencode(str):
  return urllib.parse.quote(str)


def urldecode(str):
  return urllib.parse.unquote(str)

#from urllib.parse import unquote

def decode_base64_and_inflate( b64string ):
    decoded_data = base64.b64decode( b64string )
    return zlib.decompress( decoded_data , -15)


def deflate_and_base64_encode( string_val ):
    zlibbed_str = zlib.compress( string_val )
    compressed_string = zlibbed_str[2:-4]
    return base64.b64encode( compressed_string )

nodos= classes.Nodo_KRL();


#matrimonio = open ('Matrimonio.xml', "rb")
#tree = ET.parse( matrimonio )
tree = ET.parse( '../Matrimonio.xml' )
root = tree.getroot()

xml_codificado= root[0].text
print ( xml_codificado )
#byte_texto= bytes(xml_codificado , 'ascii')

#xml_codificado.text.encode
result64= base64.b64decode( xml_codificado )
result_data = zlib.decompress( result64 , -15)
print ("Inflate")
print ( result_data )
sin_b = result_data.decode( 'utf-8' )
print ( sin_b )

matrimonio = urldecode( sin_b )

print (matrimonio)


'''
NO BORRAR
f = open ('matri.xml' , 'w' ) NO BORRAR
f.write(matrimonio) NO BORRAR
f.close()  NO BORRAR
'''


#decode_base64_and_inflate( contenido )
print( "DESPUES DE LA DECODIFICACIÓN Y CREACIÓN DEL NUEVO XML")
e = ET.parse('../matri.xml').getroot()
i = 0
k = 0
origen = [ ]
destino = [ ]
#verdad= bool
nodoKrl= classes.Nodo_KRL()
'''
Imprime origen  destino
for atype in e.findall('root'):
    for mxCell in e.iter('mxCell'):
        # print(mxCell.get('target')
        if mxCell.get('target') is not None:
            destino = destino + [mxCell.get('target')]
        if mxCell.get('source') is not None:
            origen = origen + [mxCell.get('source')]
    for x in range (len(destino)):
        for cell in atype.findall('object'):
            if (origen[x] == cell.get('id')):
                print('Origen: ', cell.get('label'))
        for cell in atype.findall('object'):
            if (destino[x] == cell.get('id')):
                print('Destino :', cell.get('label'))
'''
for atype in e.findall('root'):
    for mxCell in e.iter('mxCell'):
        # print(mxCell.get('target')
        if mxCell.get('target') is not None:
            destino = destino + [mxCell.get('target')]
        if mxCell.get('source') is not None:
            origen = origen + [mxCell.get('source')]
    for x in range (len(destino)):
        for cell in atype.findall('object'):
            if (origen[x] == cell.get('id')):
                #print('Origen: ', cell.get('label'))
                nodoKrl.Id= cell.get('id')
                nodoKrl.Nombre = cell.get('label')
                #nodoKrl.Rel_KRL.Destino = cell.get('label')
                nodoKrl.Rel_KRL.Tipo = cell.get('ELEMENTO')
                for mxCell in e.iter('mxCell'):
                    # print(mxCell.get('target')
                    if mxCell.get('source') is not None:
                        if (nodoKrl.Id == mxCell.get('source')):
                            for mxCell in e.iter('mxCell'):
                                if mxCell.get('target') is not None:
                                    nodoKrl.Rel_KRL.Target.append([mxCell.get('target')])
                print ("Elementos Nodo")
                print ("Nombre Nodo: "+nodoKrl.Nombre)
                print("ID Nodo: " + nodoKrl.Id)
                print("Tipo Nodo: " + nodoKrl.Rel_KRL.Tipo)
                print("Destinos: ")
                print (nodoKrl.Rel_KRL.Target)
                print ("Fin de Información del nodo")
'''            
                            
        for cell in atype.findall('object'):
            if (destino[x] == cell.get('id')):
                print('Destino :', cell.get('label'))
                nodoKrl.Rel_KRL.Destino=cell.get('label')
                nodoKrl.Rel_KRL.Origen= nodoKrl.GetNombre()
                nodoKrl.Rel_KRL.Tipo= cell.get('ELEMENTO')

'''