#Anton and Polyhedrons
d = {"Tetrahedron": 4, "Cube": 6, "Octahedron": 8, "Dodecahedron": 12, "Icosahedron": 20 }
t = int(input())
suM = 0
for _ in range(t):
    suM += d[input()]
print(suM)