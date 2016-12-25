#!/usr/bin/python
#import library
import kicad_lib as library
import math
OutFile="PINHEAD.lib"
Comp0="PIN70"
#Comp1="DIL12P1"
#Comp2="DIL70"

PinX=800
PinL=300
PinYStep=100


def main():
	lib=library.Library(OutFile)
	comp0=library.Component(Comp0)
	lib.components.append(comp0)
	PinHead(comp0,70)

	#comp1=library.Component(Comp1)
	#lib.components.append(comp1)
	#DilPins(comp1,12)
	#comp1.pins.append(library.Pin(str(13),13,0,-4*PinL/3,"U"))

	#comp2=library.Component(Comp2)
	#lib.components.append(comp2)
	#DilPins(comp2,70)

	library.OutLibrary(lib)
def PinHead(lib,pins):
	starty=PinYStep*(pins/2-1)/2
	for i in range(pins/2):
		tmp_y=starty-i*PinYStep
		if abs(tmp_y) < 1e-10:
			tmp_y=0
		lib.pins.append(library.Pin(str(i*2+1),i*2+1,-PinX,tmp_y,"R"))
		lib.pins.append(library.Pin(str(i*2+2),i*2+2,PinX,tmp_y,"L"))
	lib.rectangles.append(library.Rectangle(-(PinX-PinL),-starty-PinYStep,(PinX-PinL),starty+PinYStep))
if __name__ == '__main__':
	main()
