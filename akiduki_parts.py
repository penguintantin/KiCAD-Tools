#!/usr/bin/python3
#import module
import kicad_mod as module
import math
inch=25.4
OutFile="AkidukiParts"
Module0="B1010S"
Module1="KXP84"
Module2="CH224"
Module3="BC2001"
Module4="MPL115"
Module5="FXMA108"
Module6="MAU10X"

SilkScreenFront="F.SilkS"

FullPitch=2.54

RefH=1.0
ValH=1.0

layer=15
play=1.0
AreaLineW=0.5

### B1010S
padsy=2.4
padsx=6.0
PadY=1.0
PadX=2.0
OutX=4.5
OutY=5.0
### KXP84
KXPSize=5.0
KXPPadX=1.0
KXPPadY=0.3
KXPCPadX=3.7
KXPCPadY=4.4
KXPPadPitchX=KXPSize
KXPPadPitchY=0.5

#CH224-2032
CH224D=22.1
CH224R=CH224D/2.0
CH224Bottom=-13.25
CH224BottomW=7.5
CH224PillarsBottom=CH224Bottom+5.4
CH224PillarsTop=CH224PillarsBottom+12.8
CH224PillarsS=16.8
CH224PillarsD=1.2
CH224ElectrodeD=1.5
CH224ElectrodeBottom=CH224Bottom+1.0
CH224ElectrodeTop=CH224ElectrodeBottom+20.0
CH224PadX=2.5
CH224PadY=CH224PadX
#BC-2001
BC2001BisS=25.90
BC2001BottomW=7.5
BC2001SideR=3.0
BC2001CenterR=7.22
BC2001BottomY=-10.45
BC2001Y=19.80
BC2001TopY=BC2001BottomY+BC2001Y
BC2001SideRY=BC2001TopY-BC2001SideR
BC2001CutH=5.75
BC2001CutY=BC2001BottomY+BC2001CutH
BC2001CW=21.1
BC2001OutW=30.5
BC2001BisW=5.1
BC2001PadS=5.5
BC2001BisD=2.5
#MPL115
MPL115X=3.0
MPL115Y=5.0
MPL115PadX=1.60
MPL115PadY=0.8
MPL115PitchX=2.0
MPL115PitchY=1.25
MPL115PitchShiftX=0.4
MPL115HoleY=1.3
MPL115HoleD=1.0
#FXMA108
FXMA108X=2.5
FXMA108Y=4.5
FXMA108PadX=0.9
FXMA108PadY=0.25
FXMA108PitchX=2.6
FXMA108PitchY=0.5
FXMA108PitchY2=4.6
def main():
	lib=module.Library(OutFile)
	mod0=module.Module(Module0)
	mod1=module.Module(Module1)
	mod2=module.Module(Module2)
	mod3=module.Module(Module3)
	mod4=module.Module(Module4)
	mod5=module.Module(Module5)
	mod6=module.Module(Module6)
	lib.modules.append(mod0)
	lib.modules.append(mod1)
	lib.modules.append(mod2)
	lib.modules.append(mod3)
	lib.modules.append(mod4)
	lib.modules.append(mod5)
	lib.modules.append(mod6)

	B1010S(mod0)
	ref0=module.ValRef("M**",0,-RefH,RefH,RefH,0.1,0)
	mod0.refs.append(ref0)
	val0=module.ValRef(Module0,0,ValH,ValH,ValH,0.1,0)
	mod0.vals.append(val0)

	KXP84(mod1,1)
	ref1=module.ValRef("M**",1,-RefH,RefH,RefH,0.1,0)
	mod1.refs.append(ref1)
	val1=module.ValRef(Module1,0,ValH,ValH,ValH,0.1,0)
	mod1.vals.append(val1)

	CH224(mod2)
	ref2=module.ValRef("M**",1,-RefH,RefH,RefH,0.1,0)
	mod2.refs.append(ref2)
	val2=module.ValRef(Module2,0,ValH,ValH,ValH,0.1,0)
	mod2.vals.append(val2)

	BC2001(mod3)
	ref3=module.ValRef("M**",1,-RefH,RefH,RefH,0.1,0)
	mod3.refs.append(ref3)
	val3=module.ValRef(Module3,0,ValH,ValH,ValH,0.1,0)
	mod3.vals.append(val3)

	MPL115(mod4)
	ref4=module.ValRef("M**",1,-RefH,RefH,RefH,0.1,0)
	mod4.refs.append(ref4)
	val4=module.ValRef(Module4,0,ValH,ValH,ValH,0.1,0)
	mod4.vals.append(val4)

	FXMA108(mod5)
	ref5=module.ValRef("M**",1,-RefH,RefH,RefH,0.1,0)
	mod5.refs.append(ref5)
	val5=module.ValRef(Module5,0,ValH,ValH,ValH,0.1,0)
	mod5.vals.append(val5)

	#output
	module.OutModule(lib)
def MAU10X(mod):	#DCDC
	w=19.5
	y1=1.3
	y2=6.7-y1
	PadPoints=[]
	PadPoints.append([-3*FullPitch,0])
	PadPoints.append([-2*FullPitch,0])
	PadPoints.append([0,0])
	PadPoints.append([FullPitch,0])
	PadPoints.append([-2*FullPitch,0])
	Nums=["1","2","4","5","6"]
	module.Pads(mod,PadPoints,Nums,"thru_hole","circle",1.4,1.4,0.8)
	points=[[-w/2.0,-y1],[w/2.0,-y1],[w/2.0,y2],[-w/2.0,y2],[-w/2.0,-y1]]
	module.PolyLine(mod,points,AreaLineW,SilkScreenFront)
def FXMA108(mod):
	#Pads
	PadPoints=[]
	PX=FXMA108PitchX/2
	PYS=FXMA108PitchY*3.5
	for i in range(8):
		PadPoints.append([-PX,-PYS+i*FXMA108PitchY])
	for i in range(8):
		PadPoints.append([PX,PYS-i*FXMA108PitchY])
	Nums=["2","3","4","5","6","7","8","9","12","13","14","15","16","17","18","19"]
	module.Pads(mod,PadPoints,Nums,"smd","rect",FXMA108PadX,FXMA108PadY,0.0)
	#pads2
	PadPoints2=[[-FXMA108PitchY/2,-FXMA108PitchY2/2],[-FXMA108PitchY/2,FXMA108PitchY2/2],[FXMA108PitchY/2,FXMA108PitchY2/2],[FXMA108PitchY/2,-FXMA108PitchY2/2]]
	Nums2=["1","10","11","20"]
	module.Pads(mod,PadPoints2,Nums2,"smd","rect",FXMA108PadY,FXMA108PadX,0.0)
	module.Rectangle(mod,-FXMA108X/2,FXMA108Y/2,FXMA108X/2,-FXMA108Y/2,AreaLineW,SilkScreenFront)
def MPL115(mod):
	#Pads
	PadPoints=[[-MPL115PitchX/2-MPL115PitchShiftX,-1.5*MPL115PitchY],[-MPL115PitchX/2-MPL115PitchShiftX,-0.5*MPL115PitchY],[-MPL115PitchX/2-MPL115PitchShiftX,0.5*MPL115PitchY],[-MPL115PitchX/2-MPL115PitchShiftX,1.5*MPL115PitchY],
	[MPL115PitchX/2+MPL115PitchShiftX,1.5*MPL115PitchY],[MPL115PitchX/2+MPL115PitchShiftX,0.5*MPL115PitchY],[MPL115PitchX/2+MPL115PitchShiftX,-0.5*MPL115PitchY],[MPL115PitchX/2+MPL115PitchShiftX,-1.5*MPL115PitchY]]
	Nums=["1","2","3","4","5","6","7","8"]
	module.Pads(mod,PadPoints,Nums,"smd","rect",MPL115PadX,MPL115PadY,0.0)
	#Outline
	module.Rectangle(mod,-MPL115X/2,MPL115Y/2,MPL115X/2,-MPL115Y/2,AreaLineW,SilkScreenFront)
	mod.circles.append(module.Circle(0,MPL115Y/2-MPL115HoleY,MPL115HoleD/2,AreaLineW,SilkScreenFront))

def BC2001(mod):
	#Pads
	PadPoints=[[-BC2001BisS/2,0],[BC2001BisS/2,0],[0,0]]
	Nums=["1","1","2"]
	module.Pads(mod,PadPoints,Nums,"smd","rect",BC2001PadS,BC2001PadS,0.0)
	#Outline
	points=[[-BC2001CW/2,BC2001SideRY],[-BC2001CW/2,BC2001CutY],[-BC2001BottomW/2,BC2001BottomY],[BC2001BottomW/2,BC2001BottomY],[BC2001BottomW/2,BC2001BottomY],[BC2001CW/2,BC2001CutY],[BC2001CW/2,BC2001SideRY]]
	module.PolyLine(mod,points,AreaLineW,SilkScreenFront)
	mod.arcs.append(module.Arc(-BC2001CW/2+BC2001SideR,BC2001SideRY,-BC2001CW/2,BC2001SideRY,-1200,AreaLineW,SilkScreenFront))
	mod.arcs.append(module.Arc(BC2001CW/2-BC2001SideR,BC2001SideRY,BC2001CW/2,BC2001SideRY,1200,AreaLineW,SilkScreenFront))
	#
	tmp_d=BC2001CW/2-1.5*BC2001SideR
	tmp_ang=math.asin(tmp_d/BC2001CenterR)
	tmp_dy=BC2001CenterR*math.cos(tmp_ang)
	tmp_ang=tmp_ang*3600/math.pi

	mod.arcs.append(module.Arc(0,BC2001SideRY+math.sqrt(3)*BC2001SideR/2+tmp_dy,BC2001CW/2-1.5*BC2001SideR,BC2001SideRY+math.sqrt(3)*BC2001SideR/2,-tmp_ang,AreaLineW,SilkScreenFront))
def CH224(mod):
	tmp=CH224R*CH224R-CH224BottomW*CH224BottomW/4
	bottomy=math.sqrt(tmp)
	tmp_ang=math.asin(CH224BottomW/(2*CH224R))
	angle=(2*math.pi-2*tmp_ang)*180/math.pi
	#Pads
	PadPoints=[[0,CH224ElectrodeBottom],[0,CH224ElectrodeTop]]
	Nums=["1","2"]
	module.Pads(mod,PadPoints,Nums,"thru_hole","circle",CH224PadX,CH224PadY,CH224ElectrodeD)
	#Holes
	HolePoints=[[0,CH224PillarsBottom],[-CH224PillarsS/2,CH224PillarsTop],[CH224PillarsS/2,CH224PillarsTop]]
	HoleNums=["~","~","~"]
	module.Pads(mod,HolePoints,HoleNums,"thru_hole","circle",CH224ElectrodeD,CH224ElectrodeD,CH224ElectrodeD)
	#Outline
	mod.arcs.append(module.Arc(0,0,CH224BottomW/2,-bottomy,int(angle*10),AreaLineW,SilkScreenFront))
	points=[[CH224BottomW/2,-bottomy],[CH224BottomW/2,CH224Bottom],[-CH224BottomW/2,CH224Bottom],[-CH224BottomW/2,-bottomy]]
	module.PolyLine(mod,points,AreaLineW,SilkScreenFront)
def KXP84(mod,sw=1):
	#Pads
	px=KXPPadPitchX/2.0
	py=KXPPadPitchY
	PadPoints=[[-px,-3*py],[-px,-2*py],[-px,-py],[-px,0.0],[-px,py],[-px,2*py],[-px,3*py],
				[px,3*py],[px,2*py],[px,py],[px,0.0],[px,-py],[px,-2*py],[px,-3*py]]
	Nums=["1","2","3","4","5","6","7","8","9","10","11","12","13","14"]
	module.Pads(mod,PadPoints,Nums,"smd","rect",KXPPadX,KXPPadY,0.0)
	#Center pad
	if sw:
		CPadPoints=[[0.0,0.0]]
		CNums=["1"]
		module.Pads(mod,CPadPoints,CNums,"smd","rect",KXPCPadX,KXPCPadY,0.0)
	#Outline
	ox=KXPSize/2.0
	oy=KXPSize/2
	points=[[-ox,-oy],[-ox,oy],[ox,oy],[ox,-oy],[-ox,-oy]]
	module.PolyLine(mod,points,AreaLineW,SilkScreenFront)

def B1010S(mod):
	#Pads
	px=padsx/2.0
	py=padsy/2.0
	PadPoints=[[-px,-py],[-px,py],[px,py],[px,-py]]
	Nums=["1","2","3","4"]
	module.Pads(mod,PadPoints,Nums,"smd","rect",PadX,PadY,0.0)
	#Outline
	ox=OutX/2.0
	oy=OutY/2
	points=[[-ox,-oy],[-ox,oy],[ox,oy],[ox,-oy],[-ox,-oy]]
	module.PolyLine(mod,points,AreaLineW,SilkScreenFront)

def rect(mod,xl,yl,xr,yu):
	rect=module.Polygon()
	rect.PenWidth = 0
	rect.Vertexs=[[xl,yl],[xl,yu],[xr,yu],[xr,yl],[xl,yl]]
	mod.polygons.append(rect)

if __name__ == '__main__':
	main()
