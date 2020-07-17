import vector_cal as vc

v1 = vc.Vector2D(2, 3)
v2 = vc.Vector2D(2, 3)

v3 = v1 + v2
print(v3)

v4 = (v1 == v2)
print(v4)

v5 = (v1 % v2)
print(v5)

v6 = v1 - v2
print(v6)