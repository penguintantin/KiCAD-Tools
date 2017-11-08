#!/usr/bin/python3
#import library
import kicad_lib as library
import math
OutFile="Edison.lib"
Comp="Edison"
Comp2="EdisonBB"
#
PinNum=70
PinYStep=100
PackageSize=(PinNum/2+2)*PinYStep
PackageSizeX=1200
PinL=300
PinX=PackageSizeX/2+PinL
PinY=PackageSize/2+PinL
StartPoint=(PinNum/2-1)*PinYStep/2
FirstPinMarkR=100
def main():
	lib=library.Library(OutFile)
	#PIN
	comp=library.Component(Comp)
	lib.components.append(comp)
	Edison(comp)
	#Break Board
	comp2=library.Component(Comp2)
	lib.components.append(comp2)
	EdisonBB(comp2)
	library.OutLibrary(lib)
def EdisonBB(comp):
	pins=[#
		"GND",			#1
		"VSYS",			#2
		"USB_ID",		#3
		"VSYS",			#4
		"GND",			#5
		"VSYS",			#6
		"MSIC_SLP_CLK3",	#7
		"3.3V",			#8
		"GND",			#9
		"3.3V",			#10
		"GND",			#11
		"1.8V",			#12
		"GND",			#13
		"DCIN",			#14
		"GND",			#15
		"USB_DP",		#16
		"PWRBTN#",		#17
		"USB_DN",		#18
		"FAULT",		#19
		"USB_VBUS",	#20
		"PSW",			#21
		"GP134",		#22
		"V_VBAT_BKUP",	#23
		"GP44",			#24
		"GP165",		#25
		"GP45",			#26
		"GP135",		#27
		"GP46",			#28
		"Unused",		#29
		"GP47",			#30
		"RCVR_MODE",	#31
		"GP48",			#32
		"GP13_PWM1",	#33
		"GP49",			#34
		"GP12_PWM0",	#35
		"RESET_OUT#",	#36
		"GP182_PWM2",	#37
		"Unused",		#38
		"GP183_PWM3",	#39
		"Unused",		#40
		"GP19",			#41
		"GP15",			#42
		"GP20",			#43
		"GP84",			#44
		"GP27",			#45
		"GP131",		#46
		"GP28",			#47
		"GP14",			#48
		"Unused",		#49
		"GP42",			#50
		"GP111",		#51
		"GP40",			#52
		"GP110",		#53
		"GP41",			#54
		"GP109",		#55
		"GP43",			#56
		"GP115",		#57
		"GP78",			#58
		"GP114",		#59
		"GP77",			#60
		"GP130",		#61
		"GP79",			#62
		"GP129",		#63
		"GP82",			#64
		"GP128",		#65
		"GP80",			#66
		"OSC_CLK_OUT_0",	#67
		"GP83",			#68
		"FW_RCVR",		#69
		"GP81",			#70
]



def Edison(comp):
	pins=[#
		"GND",			#1
		"VSYS",			#2
		"USB_ID",		#3
		"VSYS",			#4
		"GND",			#5
		"VSYS",			#6
		"MSIC_SLP_CLK3",	#7
		"3.3V",			#8
		"GND",			#9
		"3.3V",			#10
		"GND",			#11
		"1.8V",			#12
		"GND",			#13
		"DCIN",			#14
		"GND",			#15
		"USB_DP",		#16
		"PWRBTN#",		#17
		"USB_DN",		#18
		"FAULT",		#19
		"USB_VBUS",	#20
		"PSW",			#21
		"GP134",		#22
		"V_VBAT_BKUP",	#23
		"GP44",			#24
		"GP165",		#25
		"GP45",			#26
		"GP135",		#27
		"GP46",			#28
		"Unused",		#29
		"GP47",			#30
		"RCVR_MODE",	#31
		"GP48",			#32
		"GP13_PWM1",	#33
		"GP49",			#34
		"GP12_PWM0",	#35
		"RESET_OUT#",	#36
		"GP182_PWM2",	#37
		"Unused",		#38
		"GP183_PWM3",	#39
		"Unused",		#40
		"GP19",			#41
		"GP15",			#42
		"GP20",			#43
		"GP84",			#44
		"GP27",			#45
		"GP131",		#46
		"GP28",			#47
		"GP14",			#48
		"Unused",		#49
		"GP42",			#50
		"GP111",		#51
		"GP40",			#52
		"GP110",		#53
		"GP41",			#54
		"GP109",		#55
		"GP43",			#56
		"GP115",		#57
		"GP78",			#58
		"GP114",		#59
		"GP77",			#60
		"GP130",		#61
		"GP79",			#62
		"GP129",		#63
		"GP82",			#64
		"GP128",		#65
		"GP80",			#66
		"OSC_CLK_OUT_0",	#67
		"GP83",			#68
		"FW_RCVR",		#69
		"GP81",			#70
]
	#DIL(comp,pins)
	Para(comp,pins)
	rect=library.Rectangle(-PackageSizeX/2,-PackageSize/2,PackageSizeX/2,PackageSize/2);
	comp.rectangles.append(rect)
	fpmx=int(-PackageSizeX/2+1.5*FirstPinMarkR)
	fpmy=int(PackageSize/2-1.5*FirstPinMarkR)
	FirstPinMark=library.Circle(fpmx,fpmy,FirstPinMarkR)
	comp.circles.append(FirstPinMark)
def Para(comp,pins):
	SidePinNum=len(pins)
	for i in range(SidePinNum):
		#name,num=1,x=0,y=0,direction="R")
		if i % 2:
			tmpPin=library.Pin(pins[i],i+1,PinX,StartPoint-int(i/2)*PinYStep,"L")
			comp.pins.append(tmpPin)
			comp.pins.append(tmpPin)
		else:
			tmpPin=library.Pin(pins[i],i+1,-PinX,StartPoint-int(i/2)*PinYStep,"R")
			comp.pins.append(tmpPin)
			comp.pins.append(tmpPin)
	#tmpPin=library.Pin(str(2*ElectrodeN+1),2*ElectrodeN+1,0,-PinStartY-PinYStep-PinL,"U")
	comp.pins.append(tmpPin)
def DIL(comp,pins):
	SidePinNum=len(pins)/2
	for i in range(SidePinNum):
		#name,num=1,x=0,y=0,direction="R")
		tmpPin=library.Pin(pins[i],i+1,-PinX,StartPoint-i*PinYStep,"R")
		comp.pins.append(tmpPin)
	for i in range(SidePinNum):
		tmpPin=library.Pin(pins[i+SidePinNum],i+SidePinNum+1,PinX,-StartPoint+i*PinYStep,"L")
		comp.pins.append(tmpPin)

	#tmpPin=library.Pin(str(2*ElectrodeN+1),2*ElectrodeN+1,0,-PinStartY-PinYStep-PinL,"U")
	comp.pins.append(tmpPin)
if __name__ == '__main__':
	main()
