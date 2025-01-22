# Código base para iniciar
def cargar_buffer(entrada, inicio, tamano_buffer):
  buffer = list(entrada[inicio:inicio + tamano_buffer])
  if len(buffer) < tamano_buffer:
    buffer.append("eof")
  return buffer

# Funcionamiento de recorrer
def recorrer(buffer, avance, entrada):
    print('lexema procesado:')
    condition = True
    while condition:
        for i in buffer:
            if(i!=" " and i!="eof"):
                print(*i,end="")
            elif i=="eof":
                condition = False
                break
            else:
                print('\n\nlexema procesado:')
        if condition:
            avance = avance +len(buffer)
            buffer = cargar_buffer(entrada, avance, 10)



# Inicialización
entrada = "diego es supercalifragilisticoespiralidoso y a veces huele mal pues no le gusta bañarse"
inicio = 0
avance = 0
tamano_buffer = 10
buffer = cargar_buffer(entrada, inicio, tamano_buffer)

recorrer(buffer, avance, entrada)
