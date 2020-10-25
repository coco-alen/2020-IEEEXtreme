T = int(input())
muls = []
for i in range(T):
    muls.append(int(input()))

for mul in muls:
    mul_b = str(bin(mul))[2:]
    print(mul_b)

    if '1' not in mul_b[1:]:
        print("MOV R0, R0, LSL #%d" % (len(mul_b)-1))

    else:
        if mul_b.count('1')>mul_b.count('0') and len(mul_b)<=15  :
            print("MOV R1, R0, LSL #0")
            print("MOV R2, R0, LSL #%d" % len(mul_b))
            mul_b=mul_b.replace('1','2')
            mul_b=mul_b.replace('0','1')
            mul_b=mul_b.replace('2','0')
            mul_b = int(mul_b, 2)
            mul_b+=1
            
            mul_b = str(bin(mul_b))[3:]

            while(mul_b.find('1')!=-1):
                rol = mul_b.find('1')+1
                print("ADD R0, R1, R0, LSL #%d" % rol)
                mul_b = mul_b[rol:]
            print("SUB R0, R2, R0, LSL #%d" % len(mul_b))

        else:
            print("MOV R1, R0, LSL #0")
            mul_b = mul_b[1:]
            while(mul_b.find('1')!=-1):
                rol = mul_b.find('1')+1
                print("ADD R0, R1, R0, LSL #%d" % rol)
                mul_b = mul_b[rol:]

            if mul_b:
                print("MOV R0, R0, LSL #%d" % len(mul_b)) 

    print('END')