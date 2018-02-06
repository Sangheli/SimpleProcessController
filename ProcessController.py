#!/usr/bin/env python3
# by Sangheli a.savel.vic@gmail.com

import wx, wx.html
from src import ProcessHandler as PE, ExtractData as extract_data

combolist,combonames = extract_data.process()
pe = PE.ProcessHandle(combolist[0].command_list.commands)

class Frame(wx.Frame):
    def __init__(self, title):
        wx.Frame.__init__(self, None, title=title, pos=(150, 150), size=(800, 200))
        self.Bind(wx.EVT_CLOSE, self.OnClose)

        icon = wx.Icon("data/proccontrl.ico")
        self.SetIcon(icon)

        menuBar = wx.MenuBar()
        menu = wx.Menu()
        m_exit = menu.Append(wx.ID_EXIT, "E&xit\tAlt-X", "Close window and exit program.")
        self.Bind(wx.EVT_MENU, self.OnClose, m_exit)
        menuBar.Append(menu, "&File")
        self.SetMenuBar(menuBar)

        self.statusbar = self.CreateStatusBar()

        panel = wx.Panel(self)
        box = wx.BoxSizer(wx.VERTICAL)

        m_close = wx.Button(panel, wx.ID_CLOSE, "Execute")
        m_close.Bind(wx.EVT_BUTTON, self.OnExecute)
        box.Add(m_close, 0, wx.ALL, 10)

        m_shut = wx.Button(panel, wx.ID_CLOSE, "Shutdown")
        m_shut.Bind(wx.EVT_BUTTON, self.OnPeShutdown)
        box.Add(m_shut, 0, wx.ALL, 10)

        self.MultiLine = wx.TextCtrl(parent=panel,
                                     id=-1,
                                     pos=(300, 0),
                                     size=(200, 200),
                                     style=wx.TE_MULTILINE | wx.TE_READONLY | wx.TE_AUTO_URL)

        self.updateCommandList(0)

        self.lst = wx.ListBox(panel, pos=(100, 0), size = (200,200), choices = combonames, style = wx.LB_SINGLE)
        self.Bind(wx.EVT_LISTBOX, self.changeCommandList, self.lst)
        self.lst.Select(0)

        panel.SetSizer(box)
        panel.Layout()

    def changeCommandList(self,event):
        id = event.GetEventObject().GetSelection()
        self.updateCommandList(id)
        pe.updateCommands(combolist[id].command_list.commands)

    def updateCommandList(self,id):
        self.MultiLine.Clear()
        for name in combolist[id].command_list.names:
            self.MultiLine.AppendText(name+"\n")

    def OnExecute(self,event):
        pe.execute()

    def OnPeShutdown(self,event):
        pe.shutdown()

    def OnClose(self, event):
        dlg = wx.MessageDialog(self,
                               "Do you really want to close this application?",
                               "Confirm Exit", wx.OK | wx.CANCEL | wx.ICON_QUESTION)
        result = dlg.ShowModal()
        dlg.Destroy()
        if result == wx.ID_OK:
            self.Destroy()

app = wx.App(redirect=True)  # Error messages go to popup window
top = Frame("Process Controller")
top.Show()
app.MainLoop()