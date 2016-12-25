#!/usr/bin/python
import os
import sys
import re
import math
class Library:
	def __init__(self,filename,outdir="./"):
		self.dir=outdir
		self.filename=filename
		self.components=[]
class Component:
	def __init__(self,name):
		self.name = name
		self.ref = "U"
		self.unused = "0"
		self.text_offset = 40
		self.draw_pinnumber = "Y"
		self.draw_pinname = "Y"
		self.unit_count = 1
		self.units_locked = "0"
		self.option_flag = "N"
		#for Ref
		self.ref_x = 0
		self.ref_y = -200
		self.ref_text_size = 100
		self.ref_text_orient = "H"
		self.ref_visibile = "V"
		self.ref_htext_justify = "C"
		self.ref_vtext_justify = "C"
		#for Name
		self.name_x = 0
		self.name_y = 200
		self.name_text_size = 100
		self.name_text_orient = "H"
		self.name_visibile = "V"
		self.name_htext_justify = "C"
		self.name_vtext_justify = "C"

		self.pins=[]
		self.polylines=[]
		self.texts=[]
		self.circles=[]
		self.arcs=[]
		self.rectangles=[]
class Polyline:
	def __init__(self,points):
		self.point_count = len(points)
		self.unit = 0
		self.convert = 1
		self.thickness = points
		self.points = points
		self.fill = "N"

class Text:
	def __init__(self,text="",x=0,y=0,size=0.5,direction=0):
		self.direction = direction
		self.x = x
		self.y = y
		self.text_size = size
		self.text_type = ""
		self.unit = 0
		self.convert = 1
		self.text = text
		self.text_italic="Normal"
		self.text_hjustify = "C"
		self.text_vjustify = "C"
class Circle:
	def __init__(self,x=0,y=0,r=0):
		self.x = x
		self.y = y
		self.r = r
		self.unit = 0
		self.convert = 1
		self.thickness = 0
		self.fill = "N"

class Arc:
	def __init__(self,x=0,y=0,r=0,start_angle=0,end_angle=900):
		self.x = x
		self.y = y
		self.r = r
		self.start_angle = start_angle
		self.end_angle = end_angle
		self.unit = 0
		self.convert = 1
		self.thickness = 0
		self.fill = "N"
		self.startx = 0
		self.starty = 0
		self.endx = 0
		self.endy = 0

class Rectangle:
	def __init__(self,startx=0,starty=0,endx=1,endy=1):
		self.startx = startx
		self.starty = starty
		self.endx = endx
		self.endy = endy
		self.unit = 0
		self.convert = 1
		self.thickness = 0
		self.fill = "N"

class point:
	def __init__(self):
		self.x = 0
		self.y = 0
class Pin:
	def __init__(self,name="",num=1,x=0,y=0,direction="L",length=300):
		self.name = name
		self.num = num
		self.x = x
		self.y = y
		self.length = length
		self.direction = direction
		self.name_text_size = 40
		self.num_text_size = 40
		self.unit = 1
		self.convert =  1
		self.electrical_type = "B"
		self.pin_type = ""

def OutLibrary(lib):
	ret="EESchema-LIBRARY Version 2.3  Date:" + " date-here\n"
	for comp in lib.components:
		ret+=DrawComponent(comp)
	ret += "#\n"
	ret += "#End Library\n"
	#return ret
	file_name = os.path.join(lib.dir, lib.filename)

	f = open(file_name, 'w')
	f.write(ret)
	f.close()

def DrawCircle(cir):
	ret="C " + str(cir.x) + " " + str(cir.y) + " " + str(cir.r) + " " + str(cir.unit)  + " " + str(cir.convert) + " " + str(cir.thickness) + " " + cir.fill +"\n"
	return ret
def DrawArc(arc):
	ret="A " + str(arc.x) + " " + str(arc.y) + " " + str(arc.r) + " " + str(arc.start_angle) + " " + str(arc.end_angle) + " " + str(arc.unit) + " " + str(arc.convert)+ " " + str(arc.thickness) + " " + arc.fill + " " + str(arc.startx) + " " + str(arc.starty)+ " " + str(arc.endx) + " " + str(arc.endy)+"\n"
	return ret
def DrawPolyline(poly):
	ret="P " + " " + str(poly.point_count) + " " + str(poly.unit) + " " + str(poly.convert)+ " " + str(poly.thickness)
	for point in poly.points:
		ret+=" ("+ str(point[0]) + " " + str(point[1]) + ")"
	ret += " " + poly.fill
	return ret
def DrawText(txt):
	ret="T"+str(txt.type) + " " + str(txt.x) + " " + str(txt.y) + " " + str(txt.h) + " " + str(txt.w) + " " + str(txt.angle) + " " + str(txt.PenWidth) + " " + txt.Mirror + " " + txt.Visible + " " + str(txt.Layer) + " " + txt.Italic + " \"" + txt.Text +"\"\n"
	return ret
def DrawRectangle(rect):
	ret="S " + str(rect.startx) + " " + str(rect.starty) + " " + str(rect.endx) + " " + str(rect.endy) + " " + str(rect.unit) + " " + str(rect.convert) + " " + str(rect.thickness) + " " + str(rect.fill)+"\n"
	return ret
def DrawLib(library):
	ret="EESchema-LIBRARY Version 2.3  Date:" + " date-here\n"
	ret+="# encoding utf-8\n"
	for comp in library.components:
		ret+=DrawModule(comp)
	ret+="#EndLIBRARY"
	return ret

def DrawComponent(comp):
	ret="#\n"
	ret+="# " + comp.name + "\n"
	ret+="#\n"
	ret+="DEF " + comp.name + " " + comp.ref + " " + str(comp.unused) + " " + str(comp.text_offset) + " " + comp.draw_pinnumber  + " " + comp.draw_pinname + " " + str(comp.unit_count) + " " + comp.units_locked + " " + comp.option_flag+"\n"
	ret+="F0 \""+  comp.ref + "\" " +  str(comp.ref_x) + " " +  str(comp.ref_y)	 + " " +  str(	comp.ref_text_size)	 + " " +  comp.ref_text_orient + " " +  comp.ref_visibile + " " + comp.ref_htext_justify + " " +comp.ref_vtext_justify +"\n"
	ret+="F1 \""+  comp.name + "\" " +  str(comp.name_x) + " " +  str(comp.name_y)	 + " " +  str(	comp.name_text_size)	 + " " +  comp.name_text_orient + " " +  comp.name_visibile + " " + comp.name_htext_justify + " " +comp.name_vtext_justify +"\n"
	ret+="DRAW\n"
	for text in comp.texts:
		ret+=DrawText(text)
	for line in comp.polylines:
		ret+=DrawPolyline(line)
	for circle in comp.circles:
		ret+=DrawCircle(circle)
	for arc in comp.arcs:
		ret+=DrawArc(arc)
	for rect in comp.rectangles:
		ret+=DrawRectangle(rect)
	for pin in comp.pins:
		ret+=DrawPin(pin)
	ret +="ENDDRAW\n"
	ret +="ENDDEF\n"
	return ret
def DrawPin(pin):
	ret ="X "+ pin.name + " "  + str(pin.num) + " " + str(pin.x) + " " + str(pin.y) + " " + str(pin.length) + " " + pin.direction + " " + str(pin.name_text_size) + " " + str(pin.num_text_size) + " " + str(pin.unit) + " " + str(pin.convert) + " " + pin.electrical_type + " " + pin.pin_type + "\n"
	return ret
def rad2deg(angle):
	ret=180*angle/math.pi
	#ret=round(ret, 1)
	ret=round(ret, 5)*10
	return ret
if __name__ == '__main__':
	main()
