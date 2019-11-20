# Autor: Aline Capucho
# Data: 19/11/19


def isCollisionDetected(ret1, ret2):
    BL1 = ret1["bottomLeft"]
    BL2 = ret2["bottomLeft"]
    TR1 = ret1["topRight"]
    TR2 = ret2["topRight"]
    BLX1 = BL1[0]
    BLY1 = BL1[1]
    TRX1 = TR1[0]
    TRY1 = TR1[1]
    BLX2 = BL2[0]
    BLY2 = BL2[1]
    TRX2 = TR2[0]
    TRY2 = TR2[1]
    if(((BLX1<=BLX2<=TRX1)or(BLX1<=TRX2<=TRX1))and((BLY1<=BLY2<=TRY1)or(BLY1<=TRY2<=TRY1))):
        return True
    else:
        return False

def main():
    BLX1 = float(input("Entre com BLX1: "))
    BLY1 = float(input("Entre com BLY1: "))
    TRX1 = float(input("Entre com TRX1: "))
    TRY1 = float(input("Entre com TRY1: "))
    BLX2 = float(input("Entre com BLX2: "))
    BLY2 = float(input("Entre com BLY2: "))
    TRX2 = float(input("Entre com TRX2: "))
    TRY2 = float(input("Entre com TRY2: "))
    print("\n")
    BL1 = (BLX1,BLY1)
    TR1 = (TRX1,TRY1)
    BL2 = (BLX2,BLY2)
    TR2 = (TRX2,TRY2)
    ret1={
        "bottomLeft":BL1,
        "topRight":TR1}
    ret2={
        "bottomLeft":BL2,
        "topRight":TR2}
    col = isCollisionDetected(ret1, ret2)
    if col:
        print("Colisão detectada.")
    else:
        print("Colisão não detectada.")

main()
