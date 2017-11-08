#!/usr/bin/python3
import kicad_mod as module
import math
inch=25.4
Full=2.54
GroupName="Edison"
Module0="IntelEdisonBoard"
Module1="BreakoutBoard"
#For Edison
EdisonOffsetX=100
EdisonOffsetY=100
EdisonRefH=1
EdisonValH=1
#For BreakoutBoard
def main():
	lib=module.Library(GroupName)
	mod0=module.Module(Module0)
	lib.modules.append(mod0)
	mod1=module.Module(Module1)
	lib.modules.append(mod1)

	#edison
	EdsionConnector(mod0)
	EdisonBis(mod0)
	EdisonArea(mod0)
	#(self,type=0,text="",x=0,y=0,h=0.5,w=0.5,PenWidth=0.1,angle=0,type="value",layer="F.SilkS"):
	#(self,text="",x=0,y=0,h=0.5,w=0.5,PenWidth=0.1,angle=0)
	ref0=module.ValRef("M**",5,-32,EdisonRefH,EdisonRefH,0.1,0)
	mod0.refs.append(ref0)
	val0=module.ValRef(Module0,5,6,EdisonValH,EdisonValH,0.1,0)
	mod0.vals.append(val0)

	#For BreakoutBoard
	BreakoutBoard(mod1)
	ref1=module.ValRef("M**",5,-32,EdisonRefH,EdisonRefH,0.1,0)
	mod1.refs.append(ref1)
	val1=module.ValRef(Module1,5,6,EdisonValH,EdisonValH,0.1,0)
	mod1.vals.append(val1)

	module.OutModule(lib)

def BreakoutBoard(mod):
	Bis=[[0,0],[0.1,-22.4],[42,-22.1],[41.9,-0.3]]
	BisNums=[1,1,1,1]
	BisDrillD=3.0
	BisPadSize=4.0
	module.Pads(mod,Bis,BisNums,"thru_hole","circle",BisPadSize,BisPadSize,BisDrillD)

	PinDrillD=0.8
	PinPadD=1.4
	BatPins=[[-1.13,-17.4],[1.41,-17.4]]
	BatPinNums=["B1","B2"]
	module.Pads(mod,BatPins,BatPinNums,"thru_hole","circle",PinPadD,PinPadD,PinDrillD)

	VinPins=[[52.45,-0.38],[55,-0.38]]
	VinPinNums=["V1","V2"]
	module.Pads(mod,VinPins,VinPinNums,"thru_hole","circle",PinPadD,PinPadD,PinDrillD)

	StartX=5.60
	StartY=-17.4
	Pins=[]
	PinNums=[]
	Names=["J17_","J18_","J19_","J20_"]
	for i in range(4):
		tmpy=StartY+i*Full
		for j in range(14):
			PinNums.append(Names[i]+str(j+1))
			tmpx=StartX+j*Full
			Pins.append([tmpx,tmpy])
	module.Pads(mod,Pins,PinNums,"thru_hole","circle",PinPadD,PinPadD,PinDrillD)
def EdisonArea(mod):
#Thanks
#https://github.com/mogar/IntelEdisonTemplate
	#(fp_line (start 123.53 104.83) (end 98.53 104.83) (layer F.SilkS) (width 0.2))
	#(fp_line (start 123.53 69.33) (end 123.53 104.83) (layer F.SilkS) (width 0.2))
	#(fp_line (start 98.53 69.33) (end 123.53 69.33) (layer F.SilkS) (width 0.2))
	#(fp_line (start 98.53 104.83) (end 98.53 69.33) (layer F.SilkS) (width 0.2))
	mod.lines.append(module.Line(123.53-EdisonOffsetX,104.83-EdisonOffsetY,98.53-EdisonOffsetX,104.83-EdisonOffsetY,0.2,"F.SilkS"))
	mod.lines.append(module.Line(123.53-EdisonOffsetX,69.33-EdisonOffsetY,123.53-EdisonOffsetX,104.83-EdisonOffsetY,0.2,"F.SilkS"))
	mod.lines.append(module.Line(98.53-EdisonOffsetX,69.33-EdisonOffsetY,123.53-EdisonOffsetX,69.33-EdisonOffsetY,0.2,"F.SilkS"))
	mod.lines.append(module.Line(98.53-EdisonOffsetX,104.83-EdisonOffsetY,98.53-EdisonOffsetX,69.33-EdisonOffsetY,0.2,"F.SilkS"))
	#Anntena Keep Out zone
	x0=100-EdisonOffsetX
	y0=100-EdisonOffsetY
	mod.lines.append(module.Line(x0+17.75,y0+4.83,x0+17.75,y0-8.28,0.2,"F.SilkS"))
	mod.lines.append(module.Line(x0+17.75,y0-8.28,x0+23.53,y0-8.28,0.2,"F.SilkS"))
def EdisonBis(mod):
	padtype="thru_hole"
	padfig="circle"
	DrillD=2
	PadX=3.5
	PadY=3.5
	x1=100-EdisonOffsetX
	y1=100-EdisonOffsetY
	x2=120.6-EdisonOffsetX
	y2=71.31-EdisonOffsetY
	#(pad 1 thru_hole circle (at 120.6 71.31) (size 2 2) (drill 2) (layers F.Cu))
	#(pad 1 thru_hole circle (at 100 100) (size 2 2) (drill 2) (layers F.Cu))
	mod.pads.append(module.Pad(1,x1,y1,padtype,padfig,PadX,PadY,drilld=DrillD))
	mod.pads.append(module.Pad(1,x2,y2,padtype,padfig,PadX,PadY,drilld=DrillD))
def EdsionConnector(mod):
	OffsetX=120.23-EdisonOffsetX
	OffsetY=81.7-EdisonOffsetY
	xr=1.175
	xl=-1.175
	pitchy=0.4
	PadX=1.43
	PadY=0.2
	starty=6.8
	padtype="smd"
	padfig="rect"
	for i in range(35):
		tmp_y=starty-i*pitchy
		if abs(tmp_y) < 1e-10:
			tmp_y=0
		mod.pads.append(module.Pad(i*2+1,OffsetX+xr,OffsetY+tmp_y,padtype,padfig,PadX,PadY,drilld=0.0))
		mod.pads.append(module.Pad(i*2+2,OffsetX+xl,OffsetY+tmp_y,padtype,padfig,PadX,PadY,drilld=0.0))
	#Line(x1=0,y1=0,x2=0,y2=0,PenWidth=1,layer="F.Cu")
	mod.lines.append(module.Line(OffsetX+1.39,OffsetY+7.4,OffsetX+2.39,OffsetY+6.4,0.2,"F.SilkS"))
	mod.lines.append(module.Line(OffsetX+2.39,OffsetY+6.4,OffsetX+2.39,OffsetY-7.4,0.2,"F.SilkS"))
	mod.lines.append(module.Line(OffsetX+2.39,OffsetY-7.4,OffsetX-2.39,OffsetY-7.4,0.2,"F.SilkS"))
	mod.lines.append(module.Line(OffsetX-2.39,OffsetY-7.4,OffsetX-2.39,OffsetY+7.4,0.2,"F.SilkS"))
	mod.lines.append(module.Line(OffsetX-2.39,OffsetY+7.4,OffsetX+1.39,OffsetY+7.4,0.2,"F.SilkS"))
	#Circle(x=0,y=0,r=0,PenWidth=0.1,layer="F.Cu")
	mod.circles.append(module.Circle(OffsetX+1.6,OffsetY+7.975,0.15,0.15,"F.SilkS"))
def EdsionConnector_old(mod):
	OffsetX=120.23-EdisonOffsetX
	OffsetY=81.7-EdisonOffsetY
	xr=1.175
	xl=-1.175
	pitchy=0.4
	PadX=1.43
	PadY=0.2
	starty=-6.8
	padtype="smd"
	padfig="rect"
	for i in range(35):
		tmp_y=starty+i*pitchy
		if abs(tmp_y) < 1e-10:
			tmp_y=0
		mod.pads.append(module.Pad(i+1,OffsetX+xl,OffsetY+tmp_y,padtype,padfig,PadX,PadY,drilld=0.0))
		mod.pads.append(module.Pad(i+2,OffsetX+xr,OffsetY+tmp_y,padtype,padfig,PadX,PadY,drilld=0.0))
	#Line(x1=0,y1=0,x2=0,y2=0,PenWidth=1,layer="F.Cu")
	mod.lines.append(module.Line(OffsetX-1.39,OffsetY-7.4,OffsetX-2.39,OffsetY-6.4,0.2,"F.SilkS"))
	mod.lines.append(module.Line(OffsetX-2.39,OffsetY-6.4,OffsetX-2.39,OffsetY+7.4,0.2,"F.SilkS"))
	mod.lines.append(module.Line(OffsetX-2.39,OffsetY+7.4,OffsetX+2.39,OffsetY+7.4,0.2,"F.SilkS"))
	mod.lines.append(module.Line(OffsetX+2.39,OffsetY+7.4,OffsetX+2.39,OffsetY-7.4,0.2,"F.SilkS"))
	mod.lines.append(module.Line(OffsetX+2.39,OffsetY-7.4,OffsetX-1.39,OffsetY-7.4,0.2,"F.SilkS"))
	#Circle(x=0,y=0,r=0,PenWidth=0.1,layer="F.Cu")
	mod.circles.append(module.Circle(OffsetX-1.6,OffsetY-7.975,0.15,0.15,"F.SilkS"))
if __name__ == '__main__':
	main()
