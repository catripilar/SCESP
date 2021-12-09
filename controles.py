import pip,serial
try:import keyboard
except:pip.main(['install','keyboard'])

try:control = serial.Serial('COM7',115200, timeout = 0.2)
except:print("Verificar porta serial ou religar comunicador")
esquerda = False;direita = False;frente = False;tras = False;pare = False
while True:
    if  keyboard.is_pressed('w') and frente == False:
        frente = True;tras = False;pare = False
        try:control.write(('f' + '\n').encode());print('frente')
        except:print("Comando frente ,mas ,comunicação nula")
        
    if  keyboard.is_pressed('a')  and esquerda == False:
        esquerda = True;direita = False;pare = False
        try:control.write(('e' + '\n').encode());print('esquerda')
        except:print("Comando esquerda ,mas ,comunicação nula")
        
    if  keyboard.is_pressed('d')  and direita == False:
        direita = True;esquerda = False;pare = False
        try:control.write(('d' + '\n').encode());print('direita')
        except:print("Comando direita ,mas ,comunicação nula")

    if  keyboard.is_pressed('s')  and tras == False:
        tras = True;frente = False;pare = False
        try:control.write(('t' + '\n').encode());print('tras')
        except:print("Comando tras ,mas ,comunicação nula")
    if  esquerda == False and direita == False and frente == False and tras == False and pare == False:
        pare = True;esquerda = False;direita = False;frente = False;tras = False;
        try:control.write(('p' + '\n').encode())
        except:print("parado")