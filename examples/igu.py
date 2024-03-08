
from glass_model import MonoGlass, LaminatedGlass, InsulatedGlass, HeatTreatment, Interlayer, GasLayer, Support,GlassBuildup

w=3000
h=4000

igu_outer = MonoGlass(HeatTreatment.ANNEALED,6)


lam_inner = MonoGlass(HeatTreatment.ANNEALED,6)
interlayer = Interlayer(Interlayer.PVB,t=0.76)
lam_outer = MonoGlass(HeatTreatment.ANNEALED,6)
igu_inner = LaminatedGlass(plies=[lam_outer,lam_inner],interlayers=[interlayer])
igu_outer.igdbcode = 20

gas = GasLayer(GasLayer.AIR,t=12)
igu = InsulatedGlass([igu_outer,igu_inner],[gas])
igu.support = Support.FOUR_SIDE
igu.width = 3000
igu.height = 4000
#igu.igdbcode = 20
igu.igdbflip = False
gs = igu.to_gstr()
print (gs)

igu2 = GlassBuildup.make_glass(gs)
print(igu_outer.igdbcode)
