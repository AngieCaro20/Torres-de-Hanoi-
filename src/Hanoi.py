# Torres de Hanoi con recursividad

paso = 0  # variable global para contar pasos

def hanoi(n, torre1, torre2, torre3):
    global paso
    if n == 1:
        paso += 1
        print(f"Paso {paso}: mover disco desde {torre1} hacia {torre3}")
        return
    
    # mover n-1 discos de torre1 a torre2
    hanoi(n - 1, torre1, torre3, torre2)
    
    # mover el disco más grande
    paso += 1
    print(f"Paso {paso}: mover disco desde {torre1} hacia {torre3}")
    
    # mover n-1 discos de torre2 a torre3
    hanoi(n - 1, torre2, torre1, torre3)


