####convertir un numero decimal, de una
####red a binario en cada octeto.

def ip (primer_octeto, segundo_octeto, tercer_octeto, cuarto_octeto): 
    
    print("=============================")
    print("\tip o mascara de red a binario")
    print("=============================")
    
    print(f"\nip: {primer_octeto}.{segundo_octeto}.{tercer_octeto}.{cuarto_octeto}")
    primer_octeto = bin(primer_octeto)[2:].zfill(8)
    segundo_octeto = bin(segundo_octeto)[2:].zfill(8)
    tercer_octeto = bin(tercer_octeto)[2:].zfill(8)
    cuarto_octeto = bin(cuarto_octeto)[2:].zfill(8)
    #print(f"\nbinario:\n\n{primer_octeto}.{segundo_octeto}.{tercer_octeto}.{cuarto_octeto}")
    return print(f"\nbinario:\n\n{primer_octeto}.{segundo_octeto}.{tercer_octeto}.{cuarto_octeto}")

primer_octeto= int(input("Ingrese Primer octecto 1-255\n"))
segundo_octeto= int(input("Ingres Segundo octecto 1-255\n"))
tercer_octeto= int(input("Ingrese Tercer octeto 1-255\n"))
cuarto_octeto= int(input("Ingrese Cuarto octeto 1-255\n"))

ip (primer_octeto, segundo_octeto, tercer_octeto, cuarto_octeto)
