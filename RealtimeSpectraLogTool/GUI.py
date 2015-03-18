# -*- coding: utf-8 -*-
# generated by wxGlade 0.6.3 on Wed Dec 15 19:12:49 2010

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

import sys
import queVars
import time


import GraphPanel as vizFrame




class SpectrumFrame(wx.Frame):

	VizEnable = True



	def __init__(self, *args, **kwds):
		# begin wxGlade: ThermFrame.__init__
		kwds["style"] = wx.CAPTION|wx.CLOSE_BOX|wx.MINIMIZE_BOX|wx.MAXIMIZE_BOX|wx.SYSTEM_MENU|wx.RESIZE_BORDER|wx.TAB_TRAVERSAL|wx.CLIP_CHILDREN
		wx.Frame.__init__(self, *args, **kwds)





		self.__set_properties()
		self.__do_layout()


		# end wxGlade
		self.filterTimer = wx.Timer(self)
		self.tbUpdate = wx.Timer(self)



		self.Bind(wx.EVT_CLOSE, self.quitApp)
		self.Bind(wx.EVT_TIMER, self.updateGUI, self.tbUpdate)



	def __set_properties(self):
		# begin wxGlade: ThermFrame.__set_properties
		self.SetTitle("SignalHound Spectrum Monitoring tool")
		self.SetBackgroundColour(wx.SystemSettings_GetColour(wx.SYS_COLOUR_BTNFACE))

		self.SetSize((1000, 685))
		self.SetMinSize((1000,600))

		# end wxGlade



	def __createHeader(self):

		headerSizer = wx.BoxSizer(wx.HORIZONTAL)

		descText = "SignalHound Spectrum Monitoring tool"

		headerDescriptionLabel = wx.StaticText(self, -1, descText)
		headerDescriptionLabel.SetFont(wx.Font(12, wx.DEFAULT, wx.NORMAL, wx.NORMAL, 0, "MS Shell Dlg 2"))

		peakSenseSlider = wx.Slider(self, -1, minValue=10, maxValue=80, value=55)
		self.Bind(wx.EVT_SCROLL, self.changePeakFindSense, peakSenseSlider)

		headerSizer.Add(headerDescriptionLabel)
		headerSizer.Add((10,10))
		headerSizer.Add(peakSenseSlider, flag=wx.EXPAND, proportion=1)

		return headerSizer


	def __do_layout(self):


		self.mainWindowSizer = wx.BoxSizer(wx.VERTICAL)


		self.mainWindowSizer.Add(self.__createHeader(), 0, flag=wx.ALL | wx.EXPAND, border=5)

		self.visPanel = vizFrame.GraphPanel(self, -1)


		self.mainWindowSizer.Add(self.visPanel, flag=wx.EXPAND, proportion=1)


		self.ClearBackground()
		self.SetSizer(self.mainWindowSizer)

		self.Layout()

		#print "Starting Up..."

	def changePeakFindSense(self, event):
		self.visPanel.changePeakSense(event.GetPosition()/10.0)


	def updateGUI(self, dummy_event): # wxGlade: MainW.<event_handler>		Main Polling Loop
		data = queVars.getData()
		if data != None:
			self.visPanel.setDataArray(data)
			print("Updating graph?")

	def quitApp(self, dummy_event): # wxGlade: MainFrame.<event_handler>
		print "Exiting"
		queVars.run = False
		time.sleep(.1)

		if queVars.sokThread:
			queVars.sokThread.join(.25)

		print "GUI Exiting"
		wx.Exit()




# end of class ThermFrame


class MyApp(wx.App):

	def OnInit(self):
		wx.InitAllImageHandlers()
		mainFrame = SpectrumFrame(None, -1, "")
		self.SetTopWindow(mainFrame)

		#Set up the filter timer, and stop it.
		#It can then be restarted by simply calling filterTimer.Start()



		mainFrame.tbUpdate.Start((1000/30), 0)
		mainFrame.Show()
		return 1

