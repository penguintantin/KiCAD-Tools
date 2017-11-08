#!/usr/bin/python3
#import module
import kicad_mod as module
import math
inch=25.4
OutFile="DIP"
Module0="DIP16W500mil"

FrontLayer=15
BackLayer=0
EdgeLayer=28
SilkScreenFront=21

FullPitch=2.54

RefH=1.0
ValH=1.0

layer=15
play=1.0
AreaLineW=0.5
def main():
	lib=module.Library(OutFile)
	mod0=module.Module(Module0)
	lib.modules.append(mod0)

	DIP(mod0,16,FullPitch,5*FullPitch)

	#output
	module.OutModule(lib)
def DIP(mod,PinN,Pitch,Width,PadX=1.4,PadY=1.4,DrillD=0.8,LineW=0.2,RefH=1.0,ValH=1.0):
	PadPoints=[]
	ArcR=0.5*FullPitch
	ytop=-Pitch*(PinN/2.0-1)/2.0
	ybottom=-ytop
	xleft=-Width/2.0+0.5*FullPitch
	xright=Width/2.0-0.5*FullPitch
	#Texts
	ref=module.ValRef("M**",0,ytop-RefH,RefH,RefH)
	mod.refs.append(ref)
	val=module.ValRef(mod.name,0,ybottom+ValH,ValH,ValH)
	mod.vals.append(val)

	#Lines
	mod.lines.append(module.Line(xleft,ytop,xleft,ybottom,LineW,"F.SilkS"))
	mod.lines.append(module.Line(xright,ytop,xright,ybottom,LineW,"F.SilkS"))
	mod.lines.append(module.Line(xleft,ybottom,xright,ybottom,LineW,"F.SilkS"))
	mod.lines.append(module.Line(xleft,ytop,-ArcR,ytop,LineW,"F.SilkS"))
	mod.lines.append(module.Line(ArcR,ytop,xright,ytop,LineW,"F.SilkS"))
	mod.arcs.append(module.Arc(0,ytop,ArcR,ytop,180,LineW,"F.SilkS"))
	#Pads
	for i in range(PinN):
		if i < PinN/2.0:
			tmpx=-Width/2.0
			tmpy=ytop + i*Pitch
		else:
			tmpx=Width/2.0
			tmpy=ybottom - (i-PinN/2.0)*Pitch
		PadPoints.append([tmpx,tmpy])
	Nums=range(1,PinN+1)
	module.Pads(mod,PadPoints,Nums,"thru_hole","circle",PadX,PadY,DrillD)

if __name__ == '__main__':
	main()
