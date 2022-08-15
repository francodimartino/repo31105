import sys
#    argumentos.py palabra cantidad


if len(sys.argv)==3:

    palabra=sys.argv[1]
    cantidad=int(sys.argv[2])

    for i in range(cantidad):
        print(palabra)
else:
    print("error se utiliza con 2 argumentos!!!!")