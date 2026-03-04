
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
gs = igu.to_gstr(inc_meta=False)
print (gs)


my_gs = "#20(6A)_12.0AIR_6A&0.76PVB&6A"
my_gs = "#7211(6MONO)_12.0AIR_#103(6MONO)"

igu2 = GlassBuildup.make_glass(my_gs)
print (igu2.gases[0].gas_mix)
