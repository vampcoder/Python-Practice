import wx, sys, requests, json, threading, time, unicodedata

proxies = {
	'http':'http://172.16.21.104:808',
	'https':'http://172.16.21.104:808',
}

class box(wx.Frame):
    def __init__(self, parent, id, title):
        wx.Frame.__init__(self, parent, id, title)
        l = self.available_matches()
        #print l

        sizer = wx.GridBagSizer()
        self.data
        self.thread = None
        self.id1= None
        #To get list of available matches
        self.btn = wx.Button(self, id = 1, label=u'Refresh')
        self.Bind(wx.EVT_BUTTON, self.update_matches, id = 1)
        sizer.Add(self.btn, (0, 0), (1, 1), wx.EXPAND)

        #To select the match
        self.box = wx.ComboBox(self, id= 2, choices = l ,style=wx.CB_READONLY)
        self.Bind(wx.EVT_COMBOBOX, self.get_scores, id = 2)
        sizer.Add(self.box, (0, 1), (1, 3), wx.EXPAND)

        #Display Scores
        self.label = wx.TextCtrl(self, id=3, style=wx.TE_MULTILINE)
        sizer.Add(self.label, (1, 0), (10, 20), wx.EXPAND)

        #on exit
        #self.Bind(wx.EVT_CLOSE, handler=self.onExit, id=wx.ID_EXIT)

        sizer.AddGrowableCol(0)
        self.SetSizerAndFit(sizer)
        self.SetSizeHints(-1, self.GetSize().y, -1, self.GetSize().y)
        self.Show(True)

    def onExit(self, event):
        print "hello"
       # self.thread._stopvent.set()
       # threading.Thread.join(self.thread, None)

    def show_scores(self):
        while True:
            res = requests.get('http://cricscore-api.appspot.com/csa?id=%d' % (self.id1), proxies=proxies)
            res.raise_for_status()
            if res.status_code == 304:
                time.sleep(1)
            else:
                data = res.text
                data = json.loads(data)
                str = data[0]["de"] + "\n" + data[0]["si"]
                print str

                self.label.SetValue(str)
                time.sleep(5)

    def get_scores(self, event):
        sel = event.GetSelection()
        self.id1 = self.data[sel]["id"]
        if self.thread == None:
            self.thread = threading.Thread(target = self.show_scores)
            self.thread.start()

    def available_matches(self):
        res = requests.get('http://cricscore-api.appspot.com/csa', proxies=proxies)
        if res.status_code == 200:
            res.raise_for_status()
            data = res.text
            data = json.loads(data)
            self.data = data
            l= len(data)
            li = []
            for i in range(l):
                str = data[i]["t1"]+ ' VS '+ data[i]["t2"]
                str = unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
                li.append(str)
                #print `i + 1` + ') ', data[i]["t1"], 'VS', data[i]["t2"], "\n"
            return li

    def update_matches(self, event):
        res = requests.get('http://cricscore-api.appspot.com/csa', proxies=proxies)
        if res.status_code == 200:
            res.raise_for_status()
            data = res.text
            data = json.loads(data)
            self.data = data
            l = len(data)
            li = []
            for i in range(l):
                str = data[i]["t1"] + ' VS ' + data[i]["t2"]
                str = unicodedata.normalize('NFKD', str).encode('ascii', 'ignore')
                li.append(str)
                #print `i + 1` + ') ', data[i]["t1"], 'VS', data[i]["t2"], "\n"
            self.box.Clear()
            for i in li:
                self.box.Append(i)

    def show_score(self):
        pass


app1 = wx.App()
bx = box(None, -1, 'Live Scores')
app1.MainLoop()
