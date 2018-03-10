def getSumPercentBonuses(listy):
    return listy[9] + listy[10] + listy[11] + listy[12] + listy[13] + listy[14] + listy[15] + listy[16]

   # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
a = [2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 2, 2]
b = [4, 4, 4, 4, 4, 4, 4, 4, 1, 4, 4, 4, 4, 4, 4, 4, 4]
c = [4, 4, 4, 2, 4, 4, 2, 1, 2, 4, 4, 3, 3, 2, 3, 1, 1]
d = [5, 4, 5, 2, 4, 5, 2, 1, 1, 5, 4, 4, 3, 3, 4, 2, 1]
e = [1, 1, 1, 1, 1, 1, 1, 1, 0, 5, 5, 5, 5, 5, 5, 5, 5]
f = [2, 1, 3, 1, 1, 4, 4, 3, 3, 2, 2, 3, 1, 1, 4, 3, 3]
g = [4, 3, 4, 1, 2, 5, 5, 4, 3, 4, 3, 4, 1, 1, 5, 5, 4]
h = [1, 2, 3, 1, 1, 1, 4, 5, 1, 2, 2, 3, 1, 1, 1, 5, 5]                    
i = [3, 3, 5, 1, 2, 2, 5, 5, 1, 3, 3, 5, 1, 2, 2, 5, 5]
   # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
j = [2, 4, 1, 3, 1, 5, 1, 4, 0, 1, 3, 1, 3, 0, 4, 1, 4]
k = [3, 4, 1, 4, 1, 5, 2, 4, 0, 1, 4, 1, 3, 1, 5, 1, 4]
l = [3, 4, 3, 4, 2, 1, 4, 3, 0, 2, 4, 2, 4, 1, 1, 3, 2]
m = [3, 5, 4, 5, 2, 2, 4, 3, 0, 3, 5, 3, 5, 1, 2, 3, 3]
n = [4, 2, 3, 4, 4, 2, 1, 2, 0, 4, 2, 2, 3, 4, 3, 0, 1]
o = [4, 3, 3, 4, 4, 3, 1, 2, 0, 4, 4, 3, 3, 5, 4, 1, 1]
p = [2, 3, 2, 3, 1, 1, 4, 3, 0, 3, 4, 2, 4, 2, 2, 4, 4]
q = [2, 4, 2, 5, 1, 1, 5, 5, 0, 3, 5, 2, 5, 2, 2, 5, 5]
r = [1, 4, 2, 4, 2, 3, 3, 4, 0, 2, 3, 1, 3, 1, 2, 2, 3]
s = [3, 5, 2, 4, 3, 3, 3, 4, 0, 4, 4, 1, 5, 3, 3, 2, 4]
t = [2, 3, 2, 4, 1, 1, 5, 4, 0, 2, 3, 1, 5, 1, 1, 5, 4]
u = [3, 5, 2, 5, 1, 1, 5, 5, 0, 2, 5, 2, 5, 1, 1, 5, 5]
v = [3, 4, 2, 2, 3, 3, 2, 2, 0, 3, 3, 2, 2, 3, 3, 2, 1]
w = [3, 5, 2, 3, 3, 3, 2, 2, 0, 4, 4, 2, 3, 3, 3, 2, 2]
x = [2, 3, 3, 3, 2, 2, 4, 4, 0, 2, 3, 3, 3, 2, 2, 4, 3]
y = [3, 4, 3, 3, 3, 2, 4, 5, 0, 3, 4, 3, 3, 3, 2, 4, 4]
    # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
z =  [1, 2, 3, 1, 1, 2, 4, 4, 1, 2, 2, 3, 1, 1, 2, 4, 4]
ab = [2, 3, 4, 1, 1, 2, 5, 5, 1, 2, 3, 3, 1, 1, 2, 5, 5]
cd = [2, 2, 3, 1, 3, 2, 2, 3, 0, 3, 2, 3, 1, 3, 2, 2, 3]
ef = [3, 2, 4, 1, 4, 2, 2, 4, 0, 4, 2, 4, 1, 4, 2, 2, 4]
gh = [1, 1, 3, 1, 2, 2, 3, 4, 0, 2, 1, 3, 1, 2, 2, 3, 4]
ij = [2, 2, 4, 1, 2, 2, 4, 5, 0, 2, 3, 4, 1, 3, 2, 5, 5]
kl = [2, 1, 3, 0, 3, 3, 2, 1, 0, 3, 1, 4, 0, 3, 3, 3, 1]
mn = [3, 2, 5, 0, 4, 3, 3, 2, 0, 3, 2, 5, 0, 4, 3, 3, 2]
op = [4, 1, 3, 0, 5, 0, 1, 1, 0, 4, 1, 3, 0, 5, 0, 1, 2]
qr = [5, 1, 3, 0, 5, 0, 1, 2, 0, 5, 1, 4, 0, 5, 0, 1, 2]
st = [3, 2, 3, 1, 2, 2, 3, 2, 0, 3, 2, 3, 1, 2, 2, 3, 2]
uv = [4, 3, 4, 2, 3, 3, 4, 3, 0, 4, 3, 4, 2, 3, 3, 4, 3]
wx = [2, 2, 2, 1, 1, 2, 3, 4, 0, 2, 2, 2, 1, 1, 2, 3, 4]
yz = [3, 3, 3, 1, 2, 2, 4, 5, 0, 3, 3, 4, 1, 2, 2, 5, 5]
aa = [3, 1, 4, 1, 1, 2, 2, 1, 2, 3, 1, 4, 1, 2, 2, 3, 1]
bb = [4, 2, 5, 2, 2, 2, 3, 2, 2, 4, 2, 5, 2, 2, 2, 3, 1]
    # HP MP ST MG DF RS SP SK MV HP MP ST MG DF RS SP SK
cc = [4, 3, 2, 2, 3, 4, 2, 2, 0, 4, 3, 2, 2, 3, 4, 2, 2] 
dd = [5, 4, 3, 3, 3, 5, 2, 3, 0, 5, 4, 3, 3, 3, 5, 2, 3]
ee = [1, 2, 1, 2, 1, 3, 2, 3, 0, 1, 2, 1, 2, 1, 3, 2, 3]
ff = [3, 5, 3, 5, 3, 5, 2, 4, 0, 3, 5, 3, 5, 3, 5, 2, 4]
gg = [2, 3, 2, 3, 1, 3, 1, 4, 0, 2, 3, 2, 3, 1, 3, 1, 4]
hh = [3, 4, 4, 3, 3, 4, 3, 5, 0, 3, 4, 4, 3, 3, 4, 3, 5]
ii = [2, 3, 1, 2, 2, 3, 2, 4, 0, 2, 3, 1, 2, 2, 3, 2, 4]
jj = [3, 4, 4, 2, 2, 4, 5, 5, 1, 3, 4, 4, 2, 2, 4, 5, 5]
kk = [2, 2, 2, 3, 2, 4, 4, 4, 2, 2, 2, 2, 3, 2, 4, 4, 4]
ll = [3, 3, 3, 3, 3, 4, 5, 4, 3, 3, 3, 3, 3, 3, 4, 5, 4]
mm = [2, 2, 2, 3, 4, 3, 1, 5, 0, 2, 2, 2, 3, 4, 3, 1, 5]
nn = [3, 3, 3, 4, 5, 3, 2, 5, 0, 3, 3, 3, 4, 5, 3, 2, 5]
oo = [3, 3, 3, 2, 2, 2, 1, 2, 0, 3, 3, 3, 2, 2, 2, 1, 2]
pp = [4, 4, 4, 3, 3, 2, 2, 2, 0, 4, 4, 4, 3, 3, 2, 2, 2]
qq = [3, 3, 3, 2, 2, 2, 1, 2, 0, 3, 3, 3, 2, 2, 2, 1, 2]
rr = [4, 4, 4, 3, 3, 2, 2, 2, 0, 4, 4, 4, 3, 3, 2, 2, 2]

print("\nFIRST LEVEL CLASSES: \n")

print("Lord =          ", getSumPercentBonuses(a))
print("Manakete =      ", getSumPercentBonuses(c))
print("Villager =      ", getSumPercentBonuses(e))
print("PegasusRider =  ", getSumPercentBonuses(f))
print("Archer =        ", getSumPercentBonuses(h))
print("Shaman =        ", getSumPercentBonuses(j))
print("FireMage =      ", getSumPercentBonuses(l))
print("EarthMage =     ", getSumPercentBonuses(n))
print("WindMage =      ", getSumPercentBonuses(p))
print("IceMage =       ", getSumPercentBonuses(r))
print("Blitzer =       ", getSumPercentBonuses(t))
print("Monk =          ", getSumPercentBonuses(v))
print("Dryad =         ", getSumPercentBonuses(x))
print("Thief =         ", getSumPercentBonuses(z))
print("Mercenary =     ", getSumPercentBonuses(cd))
print("Swordsman =     ", getSumPercentBonuses(gh))
print("Warrior =       ", getSumPercentBonuses(kl))
print("Knight =        ", getSumPercentBonuses(op))
print("Spearman =      ", getSumPercentBonuses(st))
print("Duelist =       ", getSumPercentBonuses(wx))
print("Cavalier =      ", getSumPercentBonuses(aa))
print("Crusader =      ", getSumPercentBonuses(cc))
print("StormCaller =   ", getSumPercentBonuses(ee))
print("Druid =         ", getSumPercentBonuses(gg))
print("Poisoner =      ", getSumPercentBonuses(ii))
print("Falconer =      ", getSumPercentBonuses(kk))
print("Trenchman =     ", getSumPercentBonuses(mm))
print("FlameKnight =   ", getSumPercentBonuses(oo))
print("FrostKnight =   ", getSumPercentBonuses(qq))

print("\nPROMOTED CLASSES: \n")

print("Hero =          ", getSumPercentBonuses(b))
print("Dragon =        ", getSumPercentBonuses(d))
print("PegasusKnight = ", getSumPercentBonuses(g))
print("Sniper =        ", getSumPercentBonuses(i))
print("Necromancer =   ", getSumPercentBonuses(k))
print("Pyromancer =    ", getSumPercentBonuses(m))
print("Geomancer =     ", getSumPercentBonuses(o))
print("Aeromancer =    ", getSumPercentBonuses(q))
print("Hydromancer =   ", getSumPercentBonuses(s))
print("Electromaster = ", getSumPercentBonuses(u))
print("Hierophant =    ", getSumPercentBonuses(w))
print("Floromancer =   ", getSumPercentBonuses(y))
print("Rogue =         ", getSumPercentBonuses(ab))
print("Veteran =       ", getSumPercentBonuses(ef))
print("Swordmaster =   ", getSumPercentBonuses(ij))
print("Berserker =     ", getSumPercentBonuses(mn))
print("General =       ", getSumPercentBonuses(qr))
print("Lancer =        ", getSumPercentBonuses(uv))
print("Duelmaster =    ", getSumPercentBonuses(yz))
print("Paladin =       ", getSumPercentBonuses(bb))
print("HolyKnight =    ", getSumPercentBonuses(dd))
print("MageGeneral =   ", getSumPercentBonuses(ff))
print("DarkConqueror = ", getSumPercentBonuses(hh))
print("Assassin =      ", getSumPercentBonuses(jj))
print("SkyRider =      ", getSumPercentBonuses(ll))
print("Trapmaster =    ", getSumPercentBonuses(nn))
print("LordofFlame =   ", getSumPercentBonuses(pp))
print("LordofFrost =   ", getSumPercentBonuses(rr))


