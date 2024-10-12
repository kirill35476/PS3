from hitbox import Hitbox


#1
hb1 = Hitbox(0,100,100,100)

#2
hb2 = Hitbox(150,100,100,100)

print(f'верхняя граница hb1: {hb1.top},'
      f'верхняя граница hb2: {hb2.top},')
print(f'нижния граница hb1: {hb1.bottom},'
      f'нижния граница hb2: {hb2.bottom},')
print(f'левая граница hb1: {hb1.left},'
      f'левая граница hb2: {hb2.left},')
print(f'правая граница hb1: {hb1.right},'
      f'правая граница hb2: {hb2.right},')

intersects = hb1.intersects(hb2)

print(intersects)