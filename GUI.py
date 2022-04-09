
import time
import PySimpleGUI as pg
from shift import ceaser_shift


main_window_layout=[[pg.Text("Ceaser cipher Encoder and Decoder")],[pg.Button("Encode")],[pg.Button("Decode")]]



encode_window_layout=[[pg.Text("Encode")],[pg.Text("Enter the String")],[pg.In(size=(25,1),enable_events=True,key="-Encode-")],[pg.Text("Enter the key")],[pg.In(size=(25,1),enable_events=True,key="-Shift-")],[pg.In(size=(20,1),enable_events=True,key="-OUTPUT-")],[pg.Button("Process")]]

decode_window_layout=[[pg.Text("Decode")],[pg.Text("Enter the String")],[pg.In(size=(25,1),enable_events=True,key="-Decode-")],[pg.Text("Enter the key")],[pg.In(size=(25,1),enable_events=True,key="-Shift-")],[pg.In(size=(20,1),enable_events=True,key="-OUTPUT-")],[pg.Button("Process")]]


main_window=pg.Window("Main",main_window_layout)


#Event Loop
running=True
process=""
while running:
    event,value=main_window.read()
    if event==pg.WIN_CLOSED:
        running=False
    if(event=="Encode"):
        print("Encode")
        main_window.close()
        main_window=pg.Window("Main",encode_window_layout)
        process="encode"
    if(event=="Decode"):
        print("Decode")
        main_window.close()
        main_window=pg.Window("Main",decode_window_layout)
        process="decode"
    if(event=="Process" and process=="encode"):
        string=value["-Encode-"]
        shift=int(value["-Shift-"])
        main_window["-OUTPUT-"].update(ceaser_shift(string,shift,process))
    if(event=="Process"and process=="decode"):
        string=value["-Decode-"]
        shift=int(value["-Shift-"])
        main_window["-OUTPUT-"].update(ceaser_shift(string,shift,process))

        

main_window.close()