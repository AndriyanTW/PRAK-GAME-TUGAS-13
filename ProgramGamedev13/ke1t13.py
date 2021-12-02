import direct.directbase.DirectStart
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectGui import *
from panda3d.core import *
from panda3d.core import TextNode

from direct.gui.DirectGui import DirectFrame




def setText(status=None):

    bk_text = "CurrentValue : %s" % v
    textObject.setText(bk_text)
    


def itemSel(arg):
    if arg == "Pilih Anggota Kelompok":
        l1 = DirectLabel(text="Tugas Game Dev", text_scale=0.07)
        l2 = DirectLabel(text="Kelas TI-D", text_scale=0.08)
        l3 = DirectLabel(text="UNS", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="klik (-) untuk geser ke atas",
            decButton_text_scale=0.07,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="klik (+) untuk geser ke bawah",
            incButton_text_scale=0.07,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(-0.09, 0.81, -0.08, 0.61),
            frameColor=(1, 0, 0, 0.5),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.41, 0.41, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in []:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='kelompok01.jpg', pos=(0.45, 7, 0.57), scale=0.3,)
        #scale besar foto
        #pos meletakkan foto

    if arg == "Anggota 1":
        
        

        l1 = DirectLabel(text="Nama : Andrean L N A", text_scale=0.07)
        l2 = DirectLabel(text="NIM : V3920007", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),


            frameSize=(-0.08, 0.80, -0.05, 0.59),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.41, 0.41, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'Makanan Favorit', 'Bakso,']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='anan.jpeg', pos=(0.45, 0, -0.45), scale=0.35,)


    if arg == "Anggota 2":
        l1 = DirectLabel(text="Nama  : Andriyan T W", text_scale=0.07)
        l2 = DirectLabel(text="NIM : V3920008", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
             decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(-0.08, 0.80, -0.05, 0.59),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.41, 0.41, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'Makanan Favorit', 'Mie Ayam']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='andrian.jpeg', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Anggota 3":
        l1 = DirectLabel(text="Nama : Arin D P", text_scale=0.07)
        l2 = DirectLabel(text="Nim : V3920010", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
             decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(-0.08, 0.80, -0.05, 0.59),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.41, 0.41, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'Makanan Favorit', 'Nasi Goreng']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='arin.jpeg', pos=(0.45, 0, -0.45), scale=0.35,)

    if arg == "Anggota 4":
        l1 = DirectLabel(text="Nama : Dandi D T", text_scale=0.07)
        l2 = DirectLabel(text="Nim : V3920016", text_scale=0.08)
        l3 = DirectLabel(text="Kelas : TI D", text_scale=0.08)

        numItemsVisible = 3
        itemHeight = 0.11

        myScrolledList = DirectScrolledList(
            decButton_pos=(0.35, 0, 0.53),
            decButton_text="-",
            decButton_text_scale=0.10,
            decButton_borderWidth=(0.005, 0.005),

            incButton_pos=(0.35, 0, -0.02),
            incButton_text="+",
            incButton_text_scale=0.10,
            incButton_borderWidth=(0.005, 0.005),

            frameSize=(-0.08, 0.80, -0.05, 0.59),
            pos=(-1, 0, 0),
            numItemsVisible=numItemsVisible,
            forceHeight=itemHeight,
            itemFrame_frameSize=(-0.41, 0.41, -0.37, 0.11),
            itemFrame_pos=(0.35, 0, 0.4),
        )

        myScrolledList.addItem(l1)
        myScrolledList.addItem(l2)
        myScrolledList.addItem(l3)

        for fruit in ['', 'Makanan Favorit', 'Rawon']:
            l = DirectLabel(text=fruit, text_scale=0.1)
            myScrolledList.addItem(l)
        imageObject = OnscreenImage(
            image='da.jpg', pos=(0.45, 0, -0.45), scale=0.35,)



# Create a frame
menu = DirectOptionMenu(text="options", scale=0.1, initialitem=2,
                        items=["Pilih Anggota Kelompok", "Anggota 1",
                               "Anggota 2", "Anggota 3", "Anggota 4"],
                        highlightColor=(0.99, 0.99, 0.99, 99),
                        command=itemSel, textMayChange=1)


def showValue():
    return menu


# Procedurally select a item
menu.set(0)

# Run the program
base.run()
