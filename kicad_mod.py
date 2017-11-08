#!/usr/bin/python
import os
import sys
import re
import math

ModExt=".kicad_mod"
#"thru_hole", "smd","connect", "np_thru_hole"
#"circle","rect","oval"
#(layers F.Cu F.Paste F.Mask)#smd
#(layers *.Cu *.Mask F.SilkS)#thru_hole

#  (at 0 0)
#  (descr "module CMS SOT223 4 pins")
#  (tags "CMS SOT")
#  (attr smd)

#  (model TO_SOT_Packages_SMD.3dshapes/SOT-223.wrl
#    (at (xyz 0 0 0))
#    (scale (xyz 0.4 0.4 0.4))
#    (rotate (xyz 0 0 0))
#  )
#(pad 1 thru_hole rect (at 6.096 0) (size 4.8006 4.8006) (drill oval 1.016 2.54) (layers *.Cu *.Mask F.SilkS))
#(pad "" connect circle (at 9.4996 2.30124) (size 0.65024 0.65024) (layers F.Cu F.Mask))
#(pad 2 thru_hole oval (at 2.54 0) (size 1.1 1.3) (drill 0.74) (layers *.Cu *.Mask F.SilkS))
#(pad Hole np_thru_hole circle (at 5.93852 0) (size 3.64998 3.64998) (drill 3.2512) (layers *.Cu *.SilkS *.Mask))
#(pad ~ smd circle (at 0 0) (size 1 1) (layers B.Cu B.Mask)
#    (solder_mask_margin 0.77) (clearance 0.77))
#  (pad 1 thru_hole rect (at 0 -1.27 90) (size 1.524 1.524) (drill 0.762 (offset 0.2 0)) (layers *.Cu *.Mask F.SilkS)
#    (die_length 2))
#  (pad 2 thru_hole trapezoid (at 1.27 0 45) (size 1.524 1.524) (drill 0.762 (offset 0.2 0)) (layers *.Cu *.Mask F.SilkS))
class Library:
	def __init__(self,name,outdir="./"):
		self.dir=outdir
		self.name=name
		self.current_dir=name + ".pretty"
		self.modules=[]
		self.unit="mm"
		if os.path.isdir(self.current_dir):
			print ("Directory exist")
		else:
			print ("make directory")
			os.mkdir(self.current_dir)
class Module:
	def __init__(self,name,layer="F.Cu"):
		self.name=name
		#for Po
		self.x = 0
		self.y = 0
		self.angle=0
		self.layer=layer
		self.Tedit=""
		self.Tstamp=0
		self.Attributes="~~"
		self.description="test"
		self.Kw="keywords"
		self.LayerType="STD"
		self.AR=""
		self.penalty90=0
		self.penalty180=0
		self.pads=[]
		self.lines=[]
		self.texts=[]
		self.vals=[]
		self.refs=[]
		self.circles=[]
		self.arcs=[]
		self.polygons=[]
class Line:
	def __init__(self,x1=0,y1=0,x2=0,y2=0,PenWidth=1,layer="F.Cu"):
		self.x1 = x1
		self.y1 = y1
		self.x2 = x2
		self.y2 = y2
		self.PenWidth = PenWidth
		self.Layer=layer
class Text:
	def __init__(self,text_type="value",text="",x=0,y=0,h=0.5,w=0.5,PenWidth=0.1,angle=0,layer="F.SilkS"):
		self.type=text_type
		self.x = x
		self.y = y
		self.h = h
		self.w = w
		self.angle=angle
		self.PenWidth = PenWidth
		self.Mirror="N"
		self.Visible="V"
		self.Layer=layer
		self.Italic="N"
		self.Text=text
class ValRef:
	def __init__(self,text="",x=0,y=0,h=0.5,w=0.5,PenWidth=0.1,angle=0):
		self.x = x
		self.y = y
		self.h = h
		self.w = w
		self.angle=angle
		self.PenWidth = PenWidth
		self.Text=text

class Circle:
	def __init__(self,x=0,y=0,r=0,PenWidth=0.1,layer="F.Cu"):
		self.x = x
		self.y = y
		#self.xp = self.x+r
		#self.yp = self.y
		self.xp = self.x
		self.yp = self.y+r
		self.PenWidth = PenWidth
		self.Layer=layer
class Arc:
	def __init__(self,cx=0,cy=0,xp=0,yp=0,angle=0,PenWidth=0.1,layer="F.Cu"):
		self.x = cx
		self.y = cy
		self.xp = xp
		self.yp = yp
		self.angle=angle
		self.PenWidth = PenWidth
		self.Layer=layer
class Polygon:
	def __init__(self,Vertexs=[],PenWidth=0,layer="F.Cu"):
		#self.Count = 0
		self.PenWidth = PenWidth
		self.Layer=layer
		self.Vertexs=Vertexs
class point:
	def __init__(self):
		self.x = 0
		self.y = 0
class Pad:
	def __init__(self,num=1,x=0,y=0,padtype="thru_hole",padfig="circle",xsize=1.0,ysize=1.0,drilld=1.0,drillw=0.0,drillh=0.0):
		self.num = num
		self.x = x
		self.y = y
		self.fig=padfig
		self.type = padtype
		self.xsize = xsize
		self.ysize = ysize
		#self.ybaseincrease=0
		#self.xbaseincrease=0
		self.angle=0
		#self.DrillDia=drilld
		self.DrillXOffset=0
		self.DrillYOffset=0
		self.DrillW=drillw
		self.DrillH=drillh
		self.dfig="circular" #or oval
		if drillw!=drillh:
			self.dfig="oval"
		if drillw<=0.0 or drillh<=0.0:
			if drilld>0.0:
				self.DrillW=drilld
				self.DrillH=drilld
		self.netName=""
		#self.LayerFlag="N"

def OutModule(lib):
	for mod in lib.modules:
		file_name = os.path.join(lib.current_dir, mod.name+ModExt)
		#print file_name
		#print DrawModule(mod)
		f = open(file_name, 'w')
		f.write(DrawModule(mod))
		f.close()

def DrawCircle(cir):
	ret="  (fp_circle (center " + str(cir.x) + " " + str(cir.y) + ") (end " + str(cir.xp) + " " + str(cir.yp)  + ") (layer " + str(cir.Layer) + ") (width " + str(cir.PenWidth) +"))\n"
	return ret
def DrawArc(arc):
	#ret="  (fp_arc (start " + str(arc.y) + " " + str(arc.xp) + ") (end " + str(arc.xp) + " " + str(arc.yp) + ") (angle " + str(arc.angle) + ") (layer " + str(arc.Layer) + ") (width " + str(arc.PenWidth) + "))\n"	
	ret="  (fp_arc (start " + str(arc.x) + " " + str(arc.y) + ") (end " + str(arc.xp) + " " + str(arc.yp) + ") (angle " + str(arc.angle) + ") (layer " + str(arc.Layer) + ") (width " + str(arc.PenWidth) + "))\n"
	return ret
def DrawPolygon(poly):
	ret="  (fp_poly (pts "
	for vert in poly.Vertexs:
		ret+="(xy " + str(vert[0]) + " " + str(vert[1]) + ") "
	ret+=")\n(layer" + str(poly.Layer) + ") (width " + str(poly.PenWidth) + "))\n"
	return ret
def DrawText(txt):
	#(fp_text value WROOM (at 0 -11) (layer F.Fab)
   # (effects (font (size 1 1) (thickness 0.15)))
 # )
	ret="  (fp_text "+str(txt.type) + " " + txt.Text + " (at " + str(txt.x) + " " + str(txt.y) + " " + str(txt.angle)+ ") (layer " + str(txt.Layer) + ")\n"
	ret +="    (effects (font (size "+ str(txt.h) + " " + str(txt.w) + ") (thickness " + str(txt.PenWidth) + ")))\n"
	ret +="  )\n"
	return ret
def DrawVal(txt):
	ret="  (fp_text value " + txt.Text + " (at " + str(txt.x) + " " + str(txt.y) + " " + str(txt.angle)+ ") (layer F.Fab)\n"
	ret +="    (effects (font (size "+ str(txt.h) + " " + str(txt.w) + ") (thickness " + str(txt.PenWidth) + ")))\n"
	ret +="  )\n"
	return ret
def DrawRef(txt):
	ret="  (fp_text reference " + txt.Text + " (at " + str(txt.x) + " " + str(txt.y) + " " + str(txt.angle)+ ") (layer F.SilkS)\n"
	ret +="    (effects (font (size "+ str(txt.h) + " " + str(txt.w) + ") (thickness " + str(txt.PenWidth) + ")))\n"
	ret +="  )\n"
	return ret
def DrawLine(line):
	#(fp_line (start -5.08 -5.08) (end -5.08 5.08) (layer F.SilkS) (width 0.15))
	ret="  (fp_line (start " + str(line.x1) + " " + str(line.y1) + ") (end " + str(line.x2) + " " + str(line.y2) + ") (layer "+ str(line.Layer) +") (width " + str(line.PenWidth) + "))\n"
	return ret

def DrawModule(mod):
	#Tedit field is a hexadecimal value with the time-stamp of the last edit;
	ret="(module " + mod.name +" (layer F.Cu) (tedit 56DD5100)\n"
	for val in mod.vals:
		ret+=DrawVal(val)
	for ref in mod.refs:
		ret+=DrawRef(ref)
	for text in mod.texts:
		ret+=DrawText(text)
	for line in mod.lines:
		ret+=DrawLine(line)
	for circle in mod.circles:
		ret+=DrawCircle(circle)
	for arc in mod.arcs:
		ret+=DrawArc(arc)
	for polygon in mod.polygons:
		ret+=DrawPolygon(polygon)
	for pad in mod.pads:
		ret+=DrawPad(pad)
	ret +=")\n"
	return ret
def DrawPad(pad):
	#(pad 3 thru_hole circle (at 2.54 -2.54) (size 1.6 1.6) (drill 1) (layers *.Cu *.Mask F.SilkS))
	#(pad 9 smd rect (at -9.3 9.1) (size 1.5 1) (layers F.Cu F.Paste F.Mask))
#"connect", "np_thru_hole"
#drillw=0.0,drillh=0.0
	if pad.type=="thru_hole":
		#layers="*.Cu *.Mask F.SilkS"
		layers="*.Cu *.Mask"
	elif pad.type=="smd":
		layers="F.Cu F.Paste F.Mask"
	elif pad.type=="connect":
		layers="F.Cu F.Paste F.Mask"
	elif pad.type=="np_thru_hole":
		layers="*.Cu *.Mask F.SilkS"
	else:
		print ("Pad Type Error")
		return
	#dfig=""
	#if pad.dfig=="oval":
#		difg="oval "
	ret="  (pad " + str(pad.num) + " " + pad.type + " " + pad.fig +" (at " + str(pad.x) + " " +  str(pad.y) + ") (size " + str(pad.xsize) + " " + str(pad.ysize) +")"
	if pad.type=="thru_hole" or pad.type=="np_thru_hole":
		if pad.dfig=="oval":
			ret+=" (drill oval" + str(pad.DrillW) + " " + str(pad.DrillH) + ")"
		else:
			ret+=" (drill " + str(pad.DrillW) + ")"
	ret+=" (layers " + layers + ")" + ")\n"
	return ret
def rad2deg(angle):
	ret=180*angle/math.pi
	#ret=round(ret, 1)
	ret=round(ret, 5)*10
	return ret

def PadCheck(padtype,padfig):
	if padfig != "circle" and padfig != "rect":
		print ("Pad figure Error:",padfig)
		return 1
	if padtype != "thru_hole" and padtype != "smd" and padtype != "connect" and padtype != "np_thru_hole":
		print ("Pad Type Error:",padtype)
		return 1
	return 0
########## Extra functions ############
#(self,num=1,x=0,y=0,padtype="thru_hole",padfig="circle",xsize=1.0,ysize=1.0,drilld=1.0,drillw=0.0,drillh=0.0)
def Pads(mod,points,nums,padtype,padfig,xsize,ysize,drilld):
	if PadCheck(padtype,padfig):
		return
	if len(points)!=len(nums):
		print("points and nums are not same size")
		return
	for i in range(len(points)):
		mod.pads.append(Pad(nums[i],points[i][0],points[i][1],padtype,padfig,xsize,ysize,drilld=drilld))

#(self,x1=0,y1=0,x2=0,y2=0,PenWidth=1,layer="F.Cu")
def PolyLine(mod,points,linew,layer):
	for i in range(1,len(points)):
		mod.lines.append(Line(x1=points[i-1][0],y1=points[i-1][1],x2=points[i][0],y2=points[i][1],PenWidth=linew,layer=layer))

def Rectangle(mod,xl,yl,xr,yu,linew,layer=15,fill=False):
	points=[[xl,yl],[xl,yu],[xr,yu],[xr,yl],[xl,yl]]
	if fill:	
		rect=Polygon()
		rect.PenWidth = linew
		rect.layer=layer
		rect.Vertexs=points
		mod.polygons.append(rect)
	else:
		PolyLine(mod,points,linew,layer)
if __name__ == '__main__':
	main()
