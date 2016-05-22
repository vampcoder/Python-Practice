import wx

class app(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        self.parent = parent
        self.initialize()

    def initialize(self):
        sizer = wx.GridBagSizer()

        self.entry = wx.TextCtrl(self, -1, value=u'Enter Text Here')
        sizer.Add(self.entry, (0,0), (1, 1), wx.EXPAND)

        button = wx.Button(self, -1, label="Submit")
        sizer.Add(button, (0, 1))

        self.box = wx.ComboBox(self, style = wx.CB_READONLY)
        self.box.SetString(0, "Amol")
        self.box.SetString(1, "Bhaskar")
        self.box.SetString(2, "Bitto")
        sizer.Add(self.box, (2, 0), (2, 2), wx.EXPAND)

        self.label = wx.StaticText(self, -1, label= u'hello !')
        sizer.Add(self.label, (1,0), (1, 2), wx.EXPAND)

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1, self.GetSize().y, -1, self.GetSize().y)
        self.Show(True)

if __name__ == "__main__":
    app1 = wx.App()
    frame = app(None, -1, '')
    app1.MainLoop()