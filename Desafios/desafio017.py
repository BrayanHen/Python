from math import cos, tan,sin,radians

a=float(input('Angulo:'))
co=cos(radians(a))
se=sin(radians(a))
ta=tan(radians(a))

print('Cosseno:{:.2f}\nSeno:{:.2f}\nTangente:{:.2f}'.format(co,se,ta))