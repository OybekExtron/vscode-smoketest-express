## Begin ControlScript Import --------------------------------------------------
from extronlib import event as EVENT, Version as VERSION
    
from extronlib.device import ProcessorDevice as PROCESSORDEVICE, UIDevice as UIDEVICE
    
from extronlib.interface import (EthernetClientInterface as ETHERNETCLIENTINTERFACE ,
EthernetServerInterface as ETHERNETSERVERINTERFACE, SerialInterface as SERIALINTERFACE, 
IRInterface as IRINTERFACE, RelayInterface as RELAYINTERFACE, ContactInterface as CONTACTINTERFACE, 
DigitalIOInterface as DIGITALIOINTERFACE, FlexIOInterface as FLEXIOINTERFACE, SWPowerInterface as SWPOWERINTERFACE, 
VolumeInterface as VOLUMEINTERFACE)
     
from extronlib.ui import Button as BUTTON, Knob as KNOB, Label as LABEL, Level as LEVEL
    
from extronlib.system import Clock as CLOCK, MESet as MESET, Wait as WAIT   
    
import time as TIME

print("Script Restarted")


# Lists
G_NBA = ["Cavs", "Warriors"]
G_EPL = ["Arsenal", "Spurs"]
G_SportsTeams = [[G_NBA],[G_EPL]]

# Tuples
G_EPL_Champions = ("Leicester City","Chelsea","Man City","Manchester United")
G_NBA_Champions = ("Warriors","Spurs","Spurs")

# Dictionaries
G_EPL_PFA = {"Jamie Vardy":"Forward", "Eden Hazard":"Midfielder", "Luis Suarez":"Forward"}
G_NBA_MVP = {"Steph Curry":"Guard", "Kevin Durant":"Forward"}

#sets
G_UCL_Champions_List = ["Real Madrid","Barcelona", "Real Madrid", "Bayern Munich", "Chelsea", "Barcelona" ]
G_UCL_Champions_Set = set(G_UCL_Champions_List)

# Extron setup code
Processor = PROCESSORDEVICE('pro550')
TLP = UIDEVICE('tlp1020')

btnB1 = BUTTON(TLP,1)
btnB2 = BUTTON(TLP,2)
btnB3 = BUTTON(TLP,3)
btnB4 = BUTTON(TLP,4)
btnB5 = BUTTON(TLP,5)
btnB6 = BUTTON(TLP,6)
btnB7 = BUTTON(TLP,7)
btnB8 = BUTTON(TLP,8)
btnB9 = BUTTON(TLP,9)
btnB10 = BUTTON(TLP,10)

lbl11 = LABEL(TLP, 11)
lbl12 = LABEL(TLP, 12)
lbl13 = LABEL(TLP, 13)
lbl14 = LABEL(TLP, 14)
lbl15 = LABEL(TLP, 15)



def DoB1Action(btn, state):
    print("List of lists")
    global G_NBA
    global G_EPL
    
    print(G_EPL)
    
    
    lbl11.SetText(G_EPL)
    
def DoB2Action(btn, state):
    print("Dictionary")
    global G_NBA
    global G_EPL
    
    #L_AllSportsTeams = [G_NBA,G_EPL]
    print(G_NBA)
    lbl12.SetText(G_NBA)    

def DoB3Action(btn, state):
    lbl11.SetText("")
    lbl12.SetText("")
    x = 1/0
    

################### Device A

@EVENT(btnB1, 'Pressed')
def BtnB1Handler(btn, state):
    DoB1Action(btn, state)

@EVENT(btnB2, 'Pressed')
def BtnB2Handler(btn, state):
    DoB2Action(btn, state)
    
@EVENT(btnB3, 'Pressed')
def BtnB3Handler(btn, state):
    DoB3Action(btn, state)
    
@EVENT(btnB4, 'Pressed')
def BtnB4Handler(btn, state):
    DoB4Action(btn, state)


@EVENT(btnB5, 'Pressed')
def BtnB5Handler(btn, state):
    DoB5Action(btn, state)


@EVENT(btnB6, 'Pressed')
def BtnB6Handler(btn, state):
    DoB6Action(btn, state)   
   

def Initialize():
    version = VERSION()
    PartNumber = Processor.PartNumber
    Hostname = Processor.Hostname
    IPAddress = Processor.IPAddress
    print("Initialized")
    pass

## Event Definitions --------------------------

## End Events Definitions-------------------------------------------------------

Initialize()

x = 1
