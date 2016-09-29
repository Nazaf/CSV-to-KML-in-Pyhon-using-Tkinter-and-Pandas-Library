"""
Created on Sat Jun 04 16:55:36 2016

@author: Nazaf
"""

import simplekml
import pandas
import Tkinter
from tkFileDialog   import askopenfilename 

def browse():
    global infile
    infile=askopenfilename()


def KmlFunction(outfile=DestinationDirectory):
    df = pandas.read_csv(infile)
    kml = simplekml.Kml()
    for lon, lat in zip(df["Longitude"], df["Lattitude"]):
        kml.newpoint(coords=[(lon, lat)])
    kml.save(outfile)



root = Tkinter.Tk()
root.title("KML Generator")
label = Tkinter.Label(root, text = "This Program generates a kml file")
label.pack()
browseButton = Tkinter.Button(root, text="Browse", command=browse)
browseButton.pack()
kmlButton=Tkinter.Button(root, text="Generate KML", command=KmlFunction)
kmlButton.pack()
root.mainloop()
