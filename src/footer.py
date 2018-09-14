#!/usr/bin/python

###########################################################################
# footer
###########################################################################




debug=True

#---------------------------------------------------------------
#----------------------- class myvars  --------------------
#---------------------------------------------------------------

class myvars:
    widget_value={}

    #---------------------------------------------------------------
    @staticmethod
    def clear_dic():
        myvars.widget_value={}

    #---------------------------------------------------------------
    @staticmethod
    def print_dic():
        print("myvars.widget_value={}".format(myvars.widget_value))
        
    #---------------------------------------------------------------
    @staticmethod
    def widget_STO(widget,field_value):
        if(debug):mydebug(inspect.currentframe())

        myvars.widget_value[widget]=clean_value(field_value)
        #print("STORING {} {}".format(widget.objectName(),field_value))
        
    #---------------------------------------------------------------
    @staticmethod
    def widget_RCL(widget,field_value):
        if(debug):mydebug(inspect.currentframe())

        return_value=False

        old_val=myvars.widget_value.get(widget,'CANT_RETR_OLD_VAL')
        if(old_val=='CANT_RETR_OLD_VAL'):
            if(field_value ==''):
                return_value=True
            else:
                return_value=False
        elif(old_val==field_value):
            return_value=True

        #print("RCL {} old={} new={} rtr_keep={}".format(widget.objectName(),old_val,field_value,return_value))

        return  return_value
        
#---------------------------------------------------------------
#----------------------- class myClickableLabel --------------------------
#---------------------------------------------------------------

class myClickableLabel(QtWidgets.QLabel):
    clicked=QtCore.pyqtSignal()

    def __init__(self, parent=None):
        QtWidgets.QLabel.__init__(self, parent)

    def mousePressEvent(self, ev):
        self.clicked.emit()

    def leaveEvent(self, ev):
        self.clicked.emit()
        
#---------------------------------------------------------------
#----------------------- class MyQMainWindow -------------------
#---------------------------------------------------------------

class myQMainWindow(QtWidgets.QMainWindow):
    def __init__(self,tag):
        super(myQMainWindow, self).__init__()
        self.settings = QSettings( 'ovs-toolbox', tag)     
        self.tag=tag
        self.mypref={
            'iconSize':24,
            'fontSize':24,
            'stylesheet':'01.qss',
            'mgmt': None,
        }
        
    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def restoreSettings(self):
        size=self.settings.value("size", QSize(270, 225))
        position=self.settings.value("pos", QPoint(50, 50))
        self.mypref=self.settings.value("mypref", self.mypref)
        self.resize(size)
        self.move(position)
        print("Restoring size {} and position {} and mypref {} for {}".format(size,position,self.mypref,self.tag))

    def saveSettings(self):
        size=self.size()
        position=self.pos()
        self.settings.setValue("size", size)
        self.settings.setValue("pos", position)
        self.settings.setValue("mypref", self.mypref)
        print("Saving size {} and position {} and mypref {} for {}".format(size,position,self.mypref,self.tag))


#---------------------------------------------------------------
#----------------------- class MyDialog --------------------------
#---------------------------------------------------------------

class myDialog(QtWidgets.QDialog):
    def __init__(self,tag):
        super(myDialog, self).__init__()
        self.settings = QSettings( 'ovs-toolbox', tag)     
        self.tag=tag

    def closeEvent(self, e):
        self.saveSettings()
        e.accept()

    def restoreSettings(self):
        size=self.settings.value("size", QSize(270, 225))
        position=self.settings.value("pos", QPoint(50, 50))
        self.resize(size)
        self.move(position)
        print("Restoring size {} and position {} for {}".format(size,position,self.tag))

    def saveSettings(self):
        size=self.size()
        position=self.pos()
        self.settings.setValue("size", size)
        self.settings.setValue("pos", position)
        print("Saving size {} and position {} for {}".format(size,position,self.tag))

#---------------------------------------------------------------
#----------------------- class MyDockDialog --------------------------
#---------------------------------------------------------------

#subclassing in order to catch closeevent

class MyDockDialog(myDialog):
    def __init__(self, tag):
        super(MyDockDialog, self).__init__(tag)

    def closeEvent(self, evnt):
        # comeback of frame from dialog to mainwindow
        print("CloseEvent for:",self)
        pdock_ui.verticalLayout_for_dock.removeWidget(pdock_Dialog.frame_dockable)
        ui.verticalLayout_dockable.addWidget(pdock_Dialog.frame_dockable)
        print("Calling superCloseEvent for:",self)
        super(MyDockDialog, self).closeEvent(evnt)

#--------------------------------------------------------------------------------------------
#--------------------------------------        MAIN        ----------------------------------
#--------------------------------------------------------------------------------------------
        
app = QtWidgets.QApplication(sys.argv)
MainWindow = myQMainWindow('MainWindow')
pdock_Dialog=MyDockDialog('pdock_Dialog')
if_Dialog = myDialog('if_Dialog')
pt_Dialog = myDialog('pt_Dialog')
vd_Dialog = myDialog('vd_Dialog')
vn_Dialog = myDialog('vn_Dialog')
misc_Dialog = myDialog('misc_Dialog')
pg_Dialog = myDialog('pg_Dialog')
qqueue_Dialog = myDialog('qqueue_Dialog')
qqos_Dialog = myDialog('qqos_Dialog')
qlink_Dialog=myDialog('qlink_Dialog')
of_Dialog=myDialog('of_Dialog')
of_delete_Dialog=myDialog('of_delete_Dialog')
oftrace_Dialog=myDialog('oftrace_Dialog')
output_Dialog=myDialog('output_Dialog')
ofgroup_Dialog=myDialog('ofgroup_Dialog')
mgmt_Dialog=myDialog('mgmt_Dialog')
dockernet_Dialog=myDialog('dockernet_Dialog')
dockerif_Dialog=myDialog('dockerif_Dialog')
iterate_Dialog=myDialog('iterate_Dialog')
iso_Dialog=myDialog('iso_Dialog')
stats_Dialog=myDialog('stats_Dialog')
about_Dialog=myDialog('about_Dialog')
splash_Dialog=myDialog('splash_Dialog')

error_dialog = QtWidgets.QMessageBox()
error_dialog.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding))
confirm_dialog = QtWidgets.QMessageBox()
confirm_dialog.setSizePolicy(QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding,QtWidgets.QSizePolicy.Expanding))

dialog_list=[
    about_Dialog,

    dockerif_Dialog,
    dockernet_Dialog,

    if_Dialog,
    iso_Dialog,
    iterate_Dialog,
    mgmt_Dialog,
    misc_Dialog,
    of_Dialog,
    of_delete_Dialog,
    ofgroup_Dialog,
    oftrace_Dialog,
    output_Dialog,
    pdock_Dialog,
    pg_Dialog,
    pt_Dialog,
    qlink_Dialog,
    qqos_Dialog,
    qqueue_Dialog,
    splash_Dialog,
    stats_Dialog,
    vd_Dialog,
    vn_Dialog,
]

extended_dialog_list=dialog_list.copy()
extended_dialog_list.extend([error_dialog,confirm_dialog])


ui = Ui_MainWindow()
if_ui = Ui_IF_Dialog()
pt_ui = Ui_PT_Dialog()
vn_ui= Ui_vn_Dialog()
vd_ui = Ui_vd_Dialog()
misc_ui = Ui_misc_Dialog()
pg_ui = Ui_pg_Dialog()
qqueue_ui = Ui_qqueue_Dialog()
qqos_ui = Ui_qqos_Dialog()
qlink_ui = Ui_qos_queue_link_Dialog()
pdock_ui = Ui_port_dock_Dialog()
of_ui = Ui_of_Dialog()
ofdel_ui = Ui_of_delete_Dialog()
oftrace_ui = Ui_oftrace_Dialog()
output_ui = Ui_output_Dialog()
ofgroup_ui = Ui_ofgroup_Dialog()
mgmt_ui = Ui_mgmt_Dialog()
dockernet_ui = Ui_dockernet_Dialog()
dockerif_ui = Ui_dockerif_Dialog()
iterate_ui = Ui_iterate_Dialog()
iso_ui = Ui_iso_Dialog()
stats_ui = Ui_stats_Dialog()
about_ui = Ui_about_Dialog()
splash_ui = Ui_splash_Dialog()

font11 = QtGui.QFont()
font11.setPointSize(11)

font16 = QtGui.QFont()
font16.setPointSize(16)

font21 = QtGui.QFont()
font21.setPointSize(21)

ui.setupUi(MainWindow)
if_ui.setupUi(if_Dialog)
pt_ui.setupUi(pt_Dialog)
vd_ui.setupUi(vd_Dialog)
vn_ui.setupUi(vn_Dialog)
misc_ui.setupUi(misc_Dialog)
pg_ui.setupUi(pg_Dialog)
qqueue_ui.setupUi(qqueue_Dialog)
qqos_ui.setupUi(qqos_Dialog)
qlink_ui.setupUi(qlink_Dialog)
pdock_ui.setupUi(pdock_Dialog)
of_ui.setupUi(of_Dialog)
ofdel_ui.setupUi(of_delete_Dialog)
oftrace_ui.setupUi(oftrace_Dialog)
output_ui.setupUi(output_Dialog)
ofgroup_ui.setupUi(ofgroup_Dialog)
mgmt_ui.setupUi(mgmt_Dialog)
dockernet_ui.setupUi(dockernet_Dialog)
dockerif_ui.setupUi(dockerif_Dialog)
iterate_ui.setupUi(iterate_Dialog)
iso_ui.setupUi(iso_Dialog)
stats_ui.setupUi(stats_Dialog)
about_ui.setupUi(about_Dialog)
splash_ui.setupUi(splash_Dialog)
        
#---------------------------------------------------------------
#-----------------------    MyDir     --------------------------
#---------------------------------------------------------------

class MyDir:

    projectdir="{}/.ovs-toolbox".format(expanduser("~"))
    
    #--------------------
    def __init__(self,**options):

        #if first time, create MyDir.projectdir

        mydir=Path(MyDir.projectdir)
        if(not mydir.is_dir()):
            try:
                print("mkdir:",MyDir.projectdir)
                os.makedirs(MyDir.projectdir)
            except OSError as e:
                mywarning("Error {} while trying to create project directory {}".format(e,MyDir.projectdir))

        #create subdirectory

        if(options['absoluteDir']==True):
            self.dir="{}".format(options['dir'])
        else:
            if(options['inProjectDir']==True):
                self.dir="{}/{}".format(MyDir.projectdir,options['dir'])
            else:
                self.dir="{}/{}".format(expanduser("~"),options['dir'])

            if(options['createDir']==True):

                mydir=Path(self.dir)
                if(not mydir.is_dir()):
                    try:
                        print("mkdir:",self.dir)
                        os.makedirs(self.dir)
                    except OSError as e:
                        mywarning("Error {} while trying to create directory {}".format(e,self.dir))
        self.filename=self.dir

        for demo in options.get('demos',[]):
            self.write_demo(demo)
        
    #--------------------
    
    def browse(self,text,**options):
        parent_ui=options.get('parent_ui',ui.centralwidget)
        filename,filter=QFileDialog.getOpenFileName(parent_ui,text,self.dir)
        if(filename):
            self.dir=os.path.dirname(filename)
            self.filename=filename
            return filename
        else:
            return ''
    #--------------------
    
    def save(self,text,**options):
        parent_ui=options.get('parent_ui',ui.centralwidget)
        filename,filter=QFileDialog.getSaveFileName(parent_ui,text,self.dir)
        if(filename):
            self.dir=os.path.dirname(filename)
            self.filename=filename
            return filename
        else:
            return ''
    #--------------------
    
    def file(self,name):
        return "{}/{}".format(self.dir,name)   

    #--------------------
    
    def last_filename(self):
        return self.filename   

    #--------------------
    
    def write_demo(self,demo):
        #reading file from QT ressources
        stream = QtCore.QFile(":democfg/{}".format(demo))
        stream.open(QtCore.QIODevice.ReadOnly)
        text=QtCore.QTextStream(stream).readAll()
        stream.close()

        #writting file to disk
        filename="{}/{}".format(self.dir,demo)
        if(Path(filename).exists()):
            #file already exists
            return
            
        filename_handler = open(filename,'w')
        if(filename_handler):
            print("writing filename: "+filename)
            filename_handler.write(text)
            filename_handler.close()
        else:
            mywarning("Cannot open "+filename+" in write mode !!!")

#---------------------------------------------------------------
#-----------------  class MAIN   -----------
#---------------------------------------------------------------

def start_pdb():
  pyqtRemoveInputHook()
  set_trace()

#-------------------------------------------------------------------------------

def debug_object(ob):

    pprint(vars(ob))
    
#------------------------------------------------------------------------------

def mydebug(frame):
    if(output_ui.checkBox_debug.isChecked()):
        args, _, _, values = inspect.getargvalues(frame)
        print("function name {}".format(inspect.getframeinfo(frame)[2]))
        for i in args:
            print("---> {} = {}".format(i, values[i]))
        print("\n")

#---------------------------------------------------------------
def mywarning(text,**options):

    header_message=options.get('header_msg','Warning: ')
    error_dialog.setText(header_message+text)
    error_dialog.adjustSize()
    error_dialog.exec_()
    print("Warning:",text)
    
#---------------------------------------------------------------
    
batchDir = MyDir(dir='batch',inProjectDir=True,absoluteDir=False,createDir=True)
customDir = MyDir(dir='custom',inProjectDir=True,absoluteDir=False,createDir=True)
diskDir = MyDir(dir='kvm_disks',inProjectDir=True,absoluteDir=False,createDir=True)
dockerParamsDir = MyDir(dir='dockerparams',inProjectDir=True,absoluteDir=False,createDir=True,demos=['_DEMO_docker_run_params_01.txt'])
dockerfileDir = MyDir(dir='dockerfile',inProjectDir=True,absoluteDir=False,createDir=True,demos=['_DEMO_dockerfile_alpine01.txt','_DEMO_dockerfile_fedora_01.txt'])
dockernetDir = MyDir(dir='dockernet',inProjectDir=True,absoluteDir=False,createDir=True,demos=['_DEMO_net_eth0_10.0.0.0.txt','_DEMO_eth0_ipv4_and_eth1_ipv6.txt'])
kvmNetDir = MyDir(dir='kvm_networks',inProjectDir=True,absoluteDir=False,createDir=True)
kvmParamsDir = MyDir(dir='kvm_params',inProjectDir=True,absoluteDir=False,createDir=True,demos=['_DEMO_asa_01.txt'])
mgmtDir = MyDir(dir='mgmt',inProjectDir=True,absoluteDir=False,createDir=True)
ofDir = MyDir(dir='openflow',inProjectDir=True,absoluteDir=False,createDir=True)
ofGroupDir = MyDir(dir='openflow_groups',inProjectDir=True,absoluteDir=False,createDir=True)
ofTraceDir = MyDir(dir='openflow_traces',inProjectDir=True,absoluteDir=False,createDir=True)
outputDir = MyDir(dir='output',inProjectDir=True,absoluteDir=False,createDir=True)
packetDir = MyDir(dir='packets',inProjectDir=True,absoluteDir=False,createDir=True)
#prefDir = MyDir(dir='preferences',inProjectDir=True,absoluteDir=False,createDir=True)
plotnetcfgDir = MyDir(dir='plotnetcfg',inProjectDir=True,absoluteDir=False,createDir=True)
sshDir=MyDir(dir='.ssh',inProjectDir=False,absoluteDir=False,createDir=False)
stylesheetDir = MyDir(dir='stylesheets',inProjectDir=True,absoluteDir=False,createDir=True)
tmpDir = MyDir(dir='tmp',inProjectDir=True,absoluteDir=False,createDir=True)
keyDir = MyDir(dir='keys',inProjectDir=True,absoluteDir=False,createDir=True)

#---------------------------------------------------------------
#-----------------  class myJsonExport (decorator)   -----------
#---------------------------------------------------------------
class myJsonExport(object):

    def __init__(self, dir_cat, dir_message,parent_ui):
        self.dir_cat = dir_cat
        self.dir_message = dir_message
        self.parent_ui = parent_ui
        
    def __call__(self, f):
        #def wrapped_f(*args):
        def wrapped_f():
            filename=self.dir_cat.save(self.dir_message,parent_ui=self.parent_ui)
            if(filename):
                filename_handler = open(filename,'w')
                if(filename_handler):
                    #liste=f(*args)
                    liste=f()
                    json_txt = json.dumps(liste, sort_keys=True, indent=4)
                    print("writing filename:"+filename)
                    filename_handler.write(json_txt+"\n")
                    filename_handler.close()
                    return(filename)
                else:
                    mywarning("Cannot open "+filename+" !!!")
                    return None
            else:
                print("No filename given !")
                return None
                
        return wrapped_f

#---------------------------------------------------------------
#-----------------  class myJsonImport (decorator)   -----------
#---------------------------------------------------------------
class myJsonImport(object):

    def __init__(self, dir_cat, dir_message,parent_ui):
        self.dir_cat = dir_cat
        self.dir_message = dir_message
        self.parent_ui = parent_ui

    def __call__(self, f):
        def wrapped_f(**opts):
            if('filename' in opts):
                filename=opts['filename']
                print('Autoloading:',filename)
            else:
                filename=self.dir_cat.browse(self.dir_message,parent_ui=self.parent_ui)
                print('Loading:',filename)
            if(filename):
                with open(filename) as fh:
                    l=fh.read()
                    try:
                        opts['json']=json.loads(l)
                    except json.decoder.JSONDecodeError as e:
                        mywarning("json format error in:{}\n\nError:{}".format(filename,e))
                        
                    f(**opts)
                    return(filename)
        return wrapped_f

#---------------------------------------------------------------
def myconfirm(dialog_type,text):
    if(debug):mydebug(inspect.currentframe())
    
    confirm_dialog.setText("Warning: "+text)

    if(dialog_type=='YesNo'):
        confirm_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.No)
    else:
        confirm_dialog.setStandardButtons(QtWidgets.QMessageBox.Ok | QtWidgets.QMessageBox.Cancel)

    retval=confirm_dialog.exec_()

    if(retval==1024 or retval==16384):
        return True
    else:
        return False

#---------------------------------------------------------------

def cursor(shape):
    if(debug):mydebug(inspect.currentframe())

    if(shape):
        if(shape=='WAIT'):
            shape=QtCore.Qt.WaitCursor
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(shape))
    else:
        QtWidgets.QApplication.restoreOverrideCursor()
        
#---------------------------------------------------------------

def action_code_split(text):
    if(debug):mydebug(inspect.currentframe())

    stack=[]

    read_chars=''
    liste=[]
    
    for c in text:
        if(c in ['{','[','(']):
            stack.append(c)
        elif(c in ['}',']',')']):
            stack.pop()
            
        if(not stack):
            if(c==','):
                liste.append(read_chars)
                read_chars=''
            else:
                read_chars=read_chars+c
        else:
            read_chars=read_chars+c

    if(read_chars):
        liste.append(read_chars)
            
    return liste
#---------------------------------------------------------------
def load_filename_to_widget(widget,text,dirobj):
    if(debug):mydebug(inspect.currentframe())

    filename=dirobj.browse(text)
    if(filename):
        widget.setText(filename)
        widget.setCursorPosition(0)
        
#---------------------------------------------------------------
def load_file_content_to_widget(widget,text,dirobj):
    if(debug):mydebug(inspect.currentframe())

    filename=dirobj.browse(text)
    if(filename):
        with open(filename,'r') as fh:
            content=fh.read()
            widget.setText(content)

        widget.setCursorPosition(0)
#---------------------------------------------------------------
def save_preferences(model):
    if(debug):mydebug(inspect.currentframe())

    for w in dialog_list:
        w.saveSettings()
        
    MainWindow.saveSettings()

    
#---------------------------------------------------------------
def define_stylesheet(model):
    if(debug):mydebug(inspect.currentframe())

    MainWindow.mypref['stylesheet']=model
    if(model =='custom'):
        stylesheetDir.browse('Select your stylesheet',parent_ui=ui.menu_stylesheet1)
        
    load_stylesheet(model)

#---------------------------------------------------------------
def action_export_stylesheet(model):
    if(debug):mydebug(inspect.currentframe())

    filename=stylesheetDir.save('Save running stylesheet to file',parent_ui=ui.menu_stylesheet1)
    if(filename):
        filename_handler = open(filename,'w')
        print("Saving filename:",filename)
        if(filename_handler):
            filename_handler.write(MainWindow.styleSheet())
    
#---------------------------------------------------------------
def load_stylesheet(model):
    if(debug):mydebug(inspect.currentframe())

    if(model =='nostylesheet'):
        stylesheet=''
    elif(model=='custom'):
        filename=stylesheetDir.last_filename()
        with open(filename) as fh:
            stylesheet=fh.read()
    else:
        #embedded stylesheets
        stream = QtCore.QFile(":stylesheets/{}".format(model))
        stream.open(QtCore.QIODevice.ReadOnly)
        stylesheet=QtCore.QTextStream(stream).readAll()
        stream.close()
        
    #dynamic stylesheet
    #double braces to avoid format keyerror
    icon_size=int(MainWindow.mypref['iconSize'])
    #icon_size=int(MainWindow.mypref['iconSize']*3/5)
    font_size=MainWindow.mypref['fontSize']

    stylesheet=stylesheet+"""

/* ##########  Dynamically generated stylesheet  ############# */

* {{font: {}px;}}

QPushButton {{
qproperty-iconSize: {}px;
}}

""".format(font_size,icon_size)

    stylesheet=stylesheet+"""
QRadioButton::indicator {{
width: {}px;
height: {}px;
}}

QRadioButton {{
font: {}px;
}}
""".format(icon_size,icon_size,font_size)
    
    stylesheet=stylesheet+"""
QCheckBox::indicator {{
width: {}px;
height: {}px;
}}

QCheckBox {{
font: {}px
 }}
""".format(icon_size,icon_size,font_size)

    stylesheet=stylesheet+"""
QScrollBar:vertical {{
width: {}px;
margin: {}px 0 {}px 0;
}}
""".format(icon_size,icon_size+2,icon_size+2)
    
    stylesheet=stylesheet+"""
QScrollBar::add-line:vertical {{
height: {}px;
}}
""".format(icon_size)

    stylesheet=stylesheet+"""
QScrollBar::sub-line:vertical {{
height: {}px;
}}
""".format(icon_size)

    stylesheet=stylesheet+"""
QScrollBar:horizontal {{
height: {}px;
margin: 0 {}px 0 {}px;
}}
""".format(icon_size,icon_size+2,icon_size+2)
    
    stylesheet=stylesheet+"""
QScrollBar::add-line:horizontal {{
width: {}px;
}}
""".format(icon_size)
    
    stylesheet=stylesheet+"""
QScrollBar::sub-line:horizontal {{
width: {}px;
}}
""".format(icon_size)
    
    stylesheet=stylesheet+"""
QMenu::indicator:non-exclusive:checked {{
image: url(':/images/chevron-right.png');
width: {}px;
height: {}px;
}}
""".format(font_size,font_size)

    stylesheet=stylesheet+"""
QTreeView::branch{{
width: {}px;
height: {}px;
qproperty-iconSize: {}px;
}}

QTreeView::branch:has-children:!has-siblings:closed,
QTreeView::branch:closed:has-children:has-siblings {{
border-image: none;
image: url(':/images/chevron-right.png');
}}

QTreeView::branch:open:has-children:!has-siblings,
QTreeView::branch:open:has-children:has-siblings{{
border-image: none;
image: url(':/images/chevron-down.png');
}}
""".format(font_size*2,font_size*2,font_size*2)

    
    MainWindow.setStyleSheet(stylesheet)        

    
    for w in extended_dialog_list:
        w.setStyleSheet(stylesheet)

    #qos_table.resize()
    queue_table.resize()
    docker_if_table.resize()
    docker_net_table.resize()

    
#---------------------------------------------------------------
def validate(ovs_comm,section_name,table_name):
    if(debug):mydebug(inspect.currentframe())

    mycommand=validate_prepare(ovs_comm,section_name,table_name)
    
    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        mycommand2=array_replace(mycommand,'_VARIABLE_',portname)
        #print("mycommand2=",mycommand2)
        exec_and_display(mycommand2)

#---------------------------------------------------------------
def validate_prepare(ovs_comm,section_name,table_name):
    if(debug):mydebug(inspect.currentframe())

    mycommand=[]
    mycommand.extend(widgets_to_ovs(section_name,table_name,'_VARIABLE_'))

    if(mycommand):
        if(mycommand[0]=='--'):
            mycommand=[ovs_comm] + mycommand
        else:
            mycommand=[ovs_comm,'set',table_name,'_VARIABLE_'] + mycommand

        return mycommand
    else:    
        return []
    
#---------------------------------------------------------------
def widgets_to_ovs(section_name,table_name,record_name):
    if(debug):mydebug(inspect.currentframe())

    mycommand=[]
    mycommand_remove=[]
    
    for w_k,w in listcom2widget_mapping[section_name].items():
        #print("widgets_to_ovs processing {} {}".format(w_k,w))
        if('readonly' in w):
            if(w['readonly']):continue

        #if(not w.get('never_skip',False)):
        #    fmt=w.get('fmt',False)        
        #    if(not (fmt=='options' or fmt=='other_config')):        
        #        if(not field_known_to_exist_in_table(section_name,w_k)):
        #            print("Skipping field {} from section {}".format(w_k,section_name))
        #            continue
                
        if('widgets_from' in w):
            widget=w['widgets_from'][0]
        elif('widgets' in w):
            widget=w['widgets'][0]
        else:
            print("Error!!, no 'widgets' key in:{} for {}".format(w,w_k))
            print("Error!!:",section_name,table_name,record_name)
            continue

        w_enable,w_val=widget_read(widget)
        if(myvars.widget_RCL(widget,w_val)):
            #nothing to do because widget value is same as old
            continue
            
        if('fmt' in w): 
            fmt=w['fmt']
        else:
            fmt=''

        f=w.get('preprocess_func',None)
        if(f):
            w_val=f(w_val)
            
        if(w_enable):
            if(w_val):
                mycommand.extend(["{}={}".format(w_k,w_val)])
            else:
                mycommand_remove.extend(gen_remove_config(table_name,record_name,fmt,w_k))
        else:
            mycommand_remove.extend(gen_remove_config(table_name,record_name,fmt,w_k))

    mycommand.extend(mycommand_remove)
    return mycommand
    
#---------------------------------------------------------------
def clean_value(text):
    text=pattern_brackets.sub('',text)
    text=pattern_surrounding_quotes.sub('',text)
    return text
    
#---------------------------------------------------------------
def fill_widget_from_field(list_type,field_name,field_value):
    if(debug):mydebug(inspect.currentframe())

    #sometimes fieldname in otherconfig is quoted, sometimes not.
    field_name=pattern_surrounding_quotes.sub('',field_name)

    if(field_name in listcom2widget_mapping[list_type].keys()):

        field_dic=listcom2widget_mapping[list_type][field_name]

        
        if('widgets' in field_dic):
            widget_list=field_dic['widgets']
        else:
            widget_list=None

        if('action' in field_dic):
            action=field_dic['action']
        else:
            action=''

        if('values' in field_dic):
            widget_values=field_dic['values']
        else:
            widget_values=[]

        if('col' in field_dic):
            col=field_dic['col']
        else:
            col=0

        #print("field name:{} action:{}".format(field_name,action))

        if('bracket_chop' in field_dic):
            if(field_dic['bracket_chop']):
                field_value=pattern_brackets.sub('',field_value)
        
        if('quote_chop' in field_dic):
            if(field_dic['quote_chop']):
                field_value=pattern_surrounding_quotes.sub('',field_value)

        #non default processing
        if(action=='process_dict_config'):
            process_dict_config(field_name,field_value,list_type)
            return
        elif(action=='color_led'):
            color_led(field_name,field_value,widget_list,list_type)
            return

        if(action=='convert_uuid2ports'):
            field_value=convert_uuid2ports(field_name,field_value,widget_list,list_type)

        #ovs_tables_dict[list_type][field_name]=clean_value(field_value) # remember field value
        #print("REMEMBER {}:{}={}".format(list_type,field_name,field_value))


        if(isinstance(widget_list[0], QtWidgets.QLineEdit)):
            widget_list[0].setText(field_value)
            myvars.widget_STO(widget_list[0],field_value)
            
        elif(isinstance(widget_list[0], QtWidgets.QCheckBox)):
            if(widget_values.index(field_value)==0):
                widget_list[0].setChecked(True)
            else:
                widget_list[0].setChecked(False)
            myvars.widget_STO(widget_list[0],field_value)

        elif(isinstance(widget_list[0], QtWidgets.QRadioButton)):
            widget_list[widget_values.index(field_value)].setChecked(True)
            myvars.widget_STO(widget_list[widget_values.index(field_value)],field_value)
            
        elif(isinstance(widget_list[0], QtWidgets.QLabel)):
            widget_list[0].setText(field_value)

        elif(isinstance(widget_list[0], QtWidgets.QComboBox)):
            comboBox_Write(widget_list[0],field_value)
            myvars.widget_STO(widget_list[0],field_value)
            
        elif(isinstance(widget_list[0], Mytable)):
            table_fill(widget_list[0],col,field_name,field_value)

        elif(isinstance(widget_list[0], myTree)):
            qos_tree_fill(widget_list[0],field_name,field_value)

#---------------------------------------------------------------

def clear_widgets(wtype):
    if(debug):mydebug(inspect.currentframe())

    for w,default_value in cleanable_widget_list[wtype]:
        if(isinstance(w, QtWidgets.QLineEdit)):
            w.setText(default_value)
        elif(isinstance(w, QtWidgets.QCheckBox)):
            w.setChecked(default_value)
        elif(isinstance(w, QtWidgets.QRadioButton)):
            w.setChecked(default_value)
        elif(isinstance(w, QtWidgets.QLabel)):
            w.setText(default_value)
        elif(isinstance(w, QtWidgets.QComboBox)):
            w.setCurrentIndex(default_value)


                
#---------------------------------------------------------------
def refresh_destination():
    if(debug):mydebug(inspect.currentframe())

#---------------------------------------------------------------

def main_tab_changed():
    if(debug):mydebug(inspect.currentframe())

    if(ui.tabs_main.currentIndex() >0):
        profile_test()
        
    #if(ui.tabs_main.currentIndex()==2):
    #    #action_port_filter()
    #    #if(old_selected_port_row>=0):
    #    #    portlist.select(old_selected_port_row)
    #    #action_vlan_refresh()
    #elif(ui.tabs_main.currentIndex()==3):
    #    #action_MCAST_refresh()
    #elif(ui.tabs_main.currentIndex()==4):
    #    #action_STP_refresh()
    #    #action_RSTP_refresh()
    #elif(ui.tabs_main.currentIndex()==5):
    #    #action_netflow_list(output=False)
    #    #action_sflow_list()
    #    #action_IPFIX_list(output=False)
    #elif(ui.tabs_main.currentIndex()==6):
    #    #action_qos_queue_refresh(False)
    #    #action_qos_porttree_refresh(False)
    #    pass
    #elif(ui.tabs_main.currentIndex()==7):
    #    #action_docker_image_filter()
    #    pass
    #elif(ui.tabs_main.currentIndex()==8):
    #    #action_kvm_net_list()

#---------------------------------------------------------------

def tabs_port_changed():
    if(debug):mydebug(inspect.currentframe())

    setEnableWidgetList(ports_widget_list,False)
    #setEnableWidgetList([ui.tabs_ports],False)
    #

    for portline in port_tree.get_selected():
        portname=portline[0]

        #setEnableWidgetList([ui.tabs_ports],True)
        setEnableWidgetList(ports_widget_list,True)
        
        if(ui.tabs_ports.currentIndex()==0):
            action_vlan_refresh()
        elif(ui.tabs_ports.currentIndex()==1):
            action_interface_refresh()
        elif(ui.tabs_ports.currentIndex()==2):
            action_interface_type_refresh()
        elif(ui.tabs_ports.currentIndex()==3):
            action_ingress_refresh()
        elif(ui.tabs_ports.currentIndex()==4):
            action_port_STP_refresh()
        elif(ui.tabs_ports.currentIndex()==5):
            action_port_RSTP_refresh()
        elif(ui.tabs_ports.currentIndex()==6):
            action_port_MCAST_refresh()
        elif(ui.tabs_ports.currentIndex()==7):
            action_mirror_refresh()
        elif(ui.tabs_ports.currentIndex()==8):
            action_bond_refresh()

        #stop after first port
        break
    else:
        #no port was selected
        ui.tabs_ports.setCurrentIndex(8)   

#---------------------------------------------------------------
def action_output_save():
    if(debug):mydebug(inspect.currentframe())

    filename=outputDir.save('Save output text to file',parent_ui=output_ui.pushButton_outputsave)
    if(filename):
        filename_handler = open(filename,'w')
        print("Saving filename:",filename)
        if(filename_handler):
            filename_handler.write(output_ui.Output.toPlainText())

#---------------------------------------------------------------
def action_output_clear():
    if(debug):mydebug(inspect.currentframe())
    
    output_ui.Output.clear()
#---------------------------------------------------------------

def plaintext_print(widget,text):
    if(debug):mydebug(inspect.currentframe())

    msg=decode_from_byte(text)
    widget.moveCursor(QtGui.QTextCursor.End)
    widget.textCursor().insertText('{}\n'.format(msg))
    gui_refresh()
    
#---------------------------------------------------------------

def gui_refresh():
    if(debug):mydebug(inspect.currentframe())

    QtWidgets.QApplication.processEvents()

#---------------------------------------------------------------

def output_display(msg):
    if(debug):mydebug(inspect.currentframe())

    output_button_color('my_notice')

    plaintext_print(output_ui.Output,msg)
    
#---------------------------------------------------------------
def output_display_command(msg):
    if(debug):mydebug(inspect.currentframe())

    msg=decode_from_byte(msg)
    msg=html_escape(msg)
    output_ui.Output.moveCursor(QtGui.QTextCursor.End)
    output_ui.Output.textCursor().insertHtml("<b>{}</b><br><br>".format(msg))
    gui_refresh()
    
#---------------------------------------------------------------
def decode_from_byte(text):
    if(debug):mydebug(inspect.currentframe())

    if(type(text) != type(str())):
        text=text.decode('utf8')
    return text
    
#---------------------------------------------------------------
def output_display_error(msg):
    if(debug):mydebug(inspect.currentframe())

    msg=decode_from_byte(msg)
    msg=html_escape(msg)
    output_ui.Output.moveCursor(QtGui.QTextCursor.End)
    output_ui.Output.textCursor().insertHtml("<p style=\"color:red\">[{}]#   {}</p><br><br>".format(time.strftime("%Y-%m-%d %H:%M:%S"),msg))
    gui_refresh()
    
#---------------------------------------------------------------
def output_dialog_show():
    if(debug):mydebug(inspect.currentframe())

    output_Dialog.close()
    output_button_color('')
    output_Dialog.show()

#---------------------------------------------------------------

def output_command_exec():
    if(debug):mydebug(inspect.currentframe())

    nickname=ui.lineEdit_ovs_profile.text()
    if(not nickname):
        clear_profile_bar()
        mywarning('Please select a profile in Management tab !')
        return

    profile=Mymgmt.get_profile_for_nickname(nickname)
    if(not profile):
        clear_profile_bar()
        mywarning('Please select a profile in Management tab !')
        return

    switch=ui.lineEdit_ovs_name.text() # needed for replacement of _SWITCHNAME_

    command=output_ui.lineEdit_output_command.text()
    if(command):
        command=switch_pattern_replace(command,switch)
        command_list=pattern_space.split(command)
        exec_and_display(command_list,force_output=True)
                        
#---------------------------------------------------------------
def output_select_batch():
    if(debug):mydebug(inspect.currentframe())

    filename=batchDir.browse("Select batch file to execute on host",parent_ui=output_ui.pushButton_output_select_batch_file)
    if(filename):
        output_ui.lineEdit_output_batch.setText(filename)
    
#---------------------------------------------------------------
def output_batch_exec():
    if(debug):mydebug(inspect.currentframe())

    nickname=ui.lineEdit_ovs_profile.text()
    if(not nickname):
        clear_profile_bar()
        mywarning('Please select a profile in Management tab !')
        return

    profile=Mymgmt.get_profile_for_nickname(nickname)
    if(not profile):
        clear_profile_bar()
        mywarning('Please select a profile in Management tab !')
        return

    switch=ui.lineEdit_ovs_name.text() # needed for replacement of _SWITCHNAME_

    filename=output_ui.lineEdit_output_batch.text()
    if(filename):
        with open(filename) as fh:
            for l in fh.readlines():
                command=[]
                if(pattern_begin_by_letter.match(l)): # exclusion of empty or comment lines in file
                    l=switch_pattern_replace(l,switch)
                    for w in pattern_space.split(l.rstrip()):
                        command.append(w)

                    exec_and_display(command,force_output=True)
                        
#---------------------------------------------------------------
def switch_pattern_replace(line,switch):
    if(debug):mydebug(inspect.currentframe())

    if(switch):
        #replacing SWITCHNAME by real switch name 
        l=pattern_SWITCHNAME.sub(switch,line)
        return l
    else:
        return line
    
#---------------------------------------------------------------

def html_escape(text):
    if(debug):mydebug(inspect.currentframe())
    return "".join(html_replace.get(c,c) for c in text)


#---------------------------------------------------------------

def widget_modify_property(widget,wproperty,wpropertyval):
    if(debug):mydebug(inspect.currentframe())

    widget.setProperty(wproperty,wpropertyval)
    ui.pushButton_output.setStyleSheet('')

#---------------------------------------------------------------

def profile_test(**options):

    nickname=options.get('nickname',ui.lineEdit_ovs_profile.text())
    
    if(nickname):
        profile=Mymgmt.get_profile_for_nickname(nickname)
        if(not profile):
            clear_profile_bar()
            mywarning('Please first select a profile in Communication tab !')
            ui.tabs_main.setCurrentIndex(0)
            return
    else:
            clear_profile_bar()
            mywarning('Please first select a profile in Commmunication tab !')
            ui.tabs_main.setCurrentIndex(0)
            return

    
#---------------------------------------------------------------
    
def clear_profile_bar(**opts):
    ui.lineEdit_ovs_name.setText('')
    if('profile' in opts):
        if(opts['profile']==True):
            ui.lineEdit_ovs_profile.setText('')
 
#---------------------------------------------------------------

def exec_and_display(mycommand,**opts):
    if(debug):mydebug(inspect.currentframe())

    if(not mycommand):
        return
    
    hide_output=opts.get('hide_output',False)
    input_text=opts.get('input',None)
    force_output=opts.get('force_output',False)
    lang_c=opts.get('lang_c',False)
    decode=opts.get('decode',True)
    force_mgmt_nickname=opts.get('force_mgmt_nickname',False)
    ssh_auto_keycheck=opts.get('ssh_auto_keycheck',False)
    
    if(force_mgmt_nickname):
        nickname=force_mgmt_nickname
    else:
        nickname=ui.lineEdit_ovs_profile.text()

    if(nickname):
        profile=Mymgmt.get_profile_for_nickname(nickname)
        if(not profile):
            clear_profile_bar()
            mywarning('Please select a profile in Management tab !')
            return
    else:
            clear_profile_bar()
            mywarning('Please select a profile in Management tab !')
            return

    if(profile.custom_enable):
        if(profile.custom_script):
            mycommand=[profile.custom_script]+ pattern_space_comma.split(profile.custom_script_args) + mycommand
        else:
            mywarning("No custom script defined !")
            return ''
            
    if(profile.comm=='ssh' or profile.comm=='paramiko_key' or profile.comm=='paramiko_password'):
        mycommand=array_inside_replace(mycommand,'_mySPECIALQUOTE_','"')
        if(not profile.hostname):
            mywarning("Remote communication needs a hostname !")
            return ''

        username=profile.ssh_username
        if(not username):
            username='root'
    else:
        mycommand=array_inside_replace(mycommand,'_mySPECIALQUOTE_','')
            
    if(profile.sudo_enable):
        #sudo in mode non interactive
        mycommand=["sudo","-n"] + mycommand
        
    if(profile.comm=='paramiko_key' or profile.comm=='paramiko_password'):
        
        try:
            client = paramiko.SSHClient()
            #client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            ########################### PARAMIKO ##################################
            if(profile.comm=='paramiko_key'):
                try:
                    if(profile.ssh_key_type=='dss'):
                        k = paramiko.DSSKey.from_private_key_file(profile.ssh_key)
                    elif(profile.ssh_key_type=='ecdsa'):
                        k = paramiko.ECDSAKey.from_private_key_file(profile.ssh_key)
                    elif(profile.ssh_key_type=='ed25519'):
                        k = paramiko.Ed25519Key.from_private_key_file(profile.ssh_key)
                    else:
                        k = paramiko.RSAKey.from_private_key_file(profile.ssh_key)

                except paramiko.ssh_exception.SSHException:
                    output_error("ERROR: Wrong key type ?!?!!")
                    client.close()
                    return ''
                except FileNotFoundError:
                    output_error("ERROR: File not found ! Verify key path !")
                    client.close()
                    return ''
                except:
                    output_error("Unknown ERROR in processing key!")
                    client.close()
                    return ''

                password=''
                paramiko_mode='[PARAMIKO+KEY] '

            elif(profile.comm=='paramiko_password'):
                k=None
                password=profile.ssh_password
                paramiko_mode='[PARAMIKO+PASSWD] '

            if(lang_c):
                mycommand=['LANG=C']+mycommand
            
            #display command
            if(output_ui.checkBox_outputcommand.isChecked() or force_output):
                if(not hide_output):
                    output_display_command(paramiko_mode + " ".join(mycommand))

            cursor('WAIT')        
            client.connect(profile.hostname,
                           username=username,
                           password=password,
                           pkey=k,
                           timeout=int(profile.ssh_connect_timeout),
                           banner_timeout=int(profile.ssh_connect_timeout),
                           auth_timeout=int(profile.ssh_connect_timeout))


            stdin, stdout, stderr = client.exec_command(" ".join(mycommand))
            if(input_text):
                #https://stackoverflow.com/questions/8138241/after-executing-a-command-by-python-paramiko-how-could-i-save-result
                stdin.channel.send(input_text)
                stdin.channel.shutdown_write()
            result=stdout.read()
            errors=stderr.read()
            if(errors):
                cursor('')        
                output_error(errors)
        except socket.timeout:
            cursor('')        
            output_error("Timeout while trying to establish ssh connection with paramiko !")
            result=''
        except paramiko.ssh_exception.SSHException:
            cursor('')        
            output_error("No authentication methods available !")
            result=''
        except paramiko.ssh_exception.AuthenticationException:
            cursor('')        
            output_error("Authentication failed !")
            result=''
        except paramiko.ssh_exception.BadHostKeyException:
            cursor('')        
            output_error("Bad host key exception !")
            result=''
        #except:
        #    output_error("Unknown error in executing paramiko connect !!!")
        #    result=''
        finally:
            client.close()
            cursor('')        
            
    else:
        ########################### SSH ##################################
        if(profile.comm=='ssh'):

            
            if(lang_c):
               mycommand=['LANG=C']+mycommand

            tmpcommand=['ssh',
                       '-i',
                       profile.ssh_key]

            if(ssh_auto_keycheck):
                tmpcommand.extend(['-o','StrictHostKeyChecking=no'])
                            
            tmpcommand.extend(['-o',
                       "ConnectTimeout={}".format(profile.ssh_connect_timeout),
                       "{}@{}".format(username,profile.hostname)])

            mycommand=tmpcommand + mycommand
        
        ########################### SUBPROCESS (COMMON) ##################################
        try:
            
            if(output_ui.checkBox_outputcommand.isChecked() or force_output):
                if(not hide_output):
                    output_display_command(" ".join(mycommand))

            new_env = dict( os.environ ) 
            new_env['LC_ALL'] = 'C' 

            cursor('WAIT')
            
            r=subprocess.run(mycommand, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=int(profile.command_timeout),universal_newlines=True,input=input_text,env=new_env)
            result=r.stdout

        except subprocess.CalledProcessError as e:
            text=e.stderr
            print("SUBPROCESS ERROR text",text)
            cursor('')
            output_error(text)
            return ''
            
        except subprocess.TimeoutExpired:
            cursor('')
            output_error("Command timeout triggered ! \n(Command was aborted because it ran longer than current defined timeout of {} seconds. If you need, you can change this timeout in the management tab.)".format(profile.command_timeout))
            return ''

    cursor('')
    if(decode):
        result=decode_from_byte(result)

        #Strangely if using sudo, result can be quoted
        result=remove_enclosing_quotes(result)

        # Displaying result in output window    
        if(output_ui.checkBox_outputresult.isChecked() or force_output):
            if(not hide_output):
                output_display(result)
                if force_output: output_dialog_show()
            
    return(result)

#---------------------------------------------------------------
def remove_enclosing_quotes(text):
    if(debug):mydebug(inspect.currentframe())
    
    pattern_enclosing_quote=re.compile(r'^\'(.*)\'$')

    text=pattern_enclosing_quote.sub(r'\1',text)
    return text

#---------------------------------------------------------------
def output_button_color(text):
    if(debug):mydebug(inspect.currentframe())

    if(text=='my_alarm'):
        widget_modify_property(ui.pushButton_output,'my_alarm',True)
        widget_modify_property(ui.pushButton_output,'my_notice',False)
    elif(text=='my_notice'):
        widget_modify_property(ui.pushButton_output,'my_alarm',False)
        widget_modify_property(ui.pushButton_output,'my_notice',True)
    else:
        widget_modify_property(ui.pushButton_output,'my_alarm',False)
        widget_modify_property(ui.pushButton_output,'my_notice',False)
        
#---------------------------------------------------------------
def output_error(text):
    if(debug):mydebug(inspect.currentframe())

    output_button_color('my_alarm')

    if(output_ui.checkBox_outputerror.isChecked()):
        output_display_error(text)
        MainWindow.repaint()
    

#---------------------------------------------------------------
def comboBox_Write(w,text):
    row=w.findText(text)
    w.setCurrentIndex(row)

#---------------------------------------------------------------

def comboBox_Clear(w):
    w.setCurrentIndex(-1)


#---------------------------------------------------------------

def LineEdit_Read(qtle):
    return qtle.text()

#---------------------------------------------------------------

def LineEdit_Write(qtle,sometext):
    qtle.setText(sometext)

#---------------------------------------------------------------

def LineEdit_Clear(qtle):
    return qtle.clear()

#---------------------------------------------------------------

def set_default_other_config(page_type,item):
    if(debug):mydebug(inspect.currentframe())

    for portline in port_tree.get_selected():
        portname=portline[0]

        mycommand=['ovs-vsctl']
        mycommand.extend(gen_remove_config('Port',portname,'other_config',item))

        exec_and_display(mycommand)

    if(page_type=='PORT-RSTP'):
        action_port_RSTP_refresh()
    elif(page_type=='PORT-STP'):
        action_port_STP_refresh()

#---------------------------------------------------------------

def gen_remove_config(table,record,fmt,key):
    if(debug):mydebug(inspect.currentframe())

    pc=pattern_colon2.match(key)
    if(pc):
        column=pc.group(1)
        k=pc.group(2)

        
    if(fmt):
        if(fmt == 'clear'):
            mycommand=['--','clear',table,record,key]
        elif(fmt=='setclear'):
            mycommand=['--','set',table,record,"{}=[\"\"]".format(key)]
        elif(fmt=='setclear2'):
            mycommand=['--','set',table,record,"{}=[]".format(key)]
        elif(fmt=='zero'):
            mycommand=['--','set',table,record,"{}=0".format(key)]
        else:
            mycommand=['--','remove',table,record,column,k]
    else:
        mycommand=["{}=''".format(key)]
        
    #print("REMOVE COMMAND:",mycommand)
    
    return mycommand

#---------------------------------------------------------------

def process_dict_config(field_name,field_value,list_type):
    if(debug):mydebug(inspect.currentframe())

    tmpdict=string_to_dict(field_value)

    for f,v in tmpdict.items():
        fill_widget_from_field(list_type,"{}:{}".format(field_name,f),v)

#---------------------------------------------------------------

def field_known_to_exist_in_table(list_type,field_name):
    if(debug):mydebug(inspect.currentframe())
    
    #print("??? EXIST QUERY {}:{}".format(list_type,field_name))
    ovs_tables_dict=Mymgmt.get_current_profile_attr('tables')
    if(ovs_tables_dict==None):
        return False
        
    if(ovs_tables_dict.get(list_type,None)):
        if(ovs_tables_dict[list_type].get(field_name,False)):
            #print("EXISTS {}:{}".format(list_type,field_name))
            return True

    return False

        
#---------------------------------------------------------------

def process_fields(list_type,text_to_process,**opts):
    if(debug):mydebug(inspect.currentframe())

    if(not ('keep_dic' in opts)):
        myvars.clear_dic()
    
    for line in text_to_process.splitlines():
        pline=pattern_field.match(line)
        if(pline):
            field_name=pline.group(1)
            field_value=pline.group(2)
            fill_widget_from_field(list_type,field_name,field_value)

    #myvars.print_dic()    

#---------------------------------------------------------------

def string_to_dict(text):
    if(debug):mydebug(inspect.currentframe())
    
    text=pattern_brackets.sub('',text)
    tmplist=pattern_other_config.split(text)
    
    return dict(zip(tmplist[::2], tmplist[1::2]))

#---------------------------------------------------------------
#------------------------ MGMT ---------------------------------
#---------------------------------------------------------------

def action_testssh():
    if(debug):mydebug(inspect.currentframe())

    result=exec_and_display(['cat','/proc/version'],force_output=True,ssh_auto_keycheck=True)

#---------------------------------------------------------------

def action_mgmt_custom_enable_fields():
    if(debug):mydebug(inspect.currentframe())

    setEnableWidgetDic('MGMT_CUSTOM','ALL',False)
    comm=mgmt_ui.comboBox_mgmt_custom.currentText()
    if(comm=='enable'):
        setEnableWidgetDic('MGMT_CUSTOM','ALL',True)


#---------------------------------------------------------------

def action_mgmt_access_enable_fields():
    if(debug):mydebug(inspect.currentframe())

    setEnableWidgetDic('MGMT','ALL',False)
    comm=mgmt_ui.comboBox_mgmt_comm.currentText()
    if(comm=='local'):
        setEnableWidgetDic('MGMT','local',True)
    elif(comm=='ssh'):
        setEnableWidgetDic('MGMT','ssh',True)
    elif(comm=='paramiko_key'):
        setEnableWidgetDic('MGMT','paramiko_key',True)
    elif(comm=='paramiko_password'):
        setEnableWidgetDic('MGMT','paramiko_password',True)

    
#---------------------------------------------------------------
def action_mgmt_select_customscript():
    if(debug):mydebug(inspect.currentframe())

    filename=customDir.browse('Select your launcher custom script',parent_ui=mgmt_ui.pushButton_mgmt_select_customscript)
    LineEdit_Write(mgmt_ui.lineEdit_mgmt_custom_script,filename)
    
#---------------------------------------------------------------
def action_mgmt_add():
    if(debug):mydebug(inspect.currentframe())

    setEnableWidgetDic('MGMT','ALL',False)
    action_mgmt_access_enable_fields()
    action_mgmt_custom_enable_fields()
    if(mgmt_Dialog.exec()):
        action_mgmt_process_dialog(True)
        
#---------------------------------------------------------------

def action_mgmt_select():
    if(debug):mydebug(inspect.currentframe())

    nickname=mgmt_table.getcurrenttext(0)
    if(nickname):
        if(nickname=='_dot_mgmt'):
            return
        profile=Mymgmt.get_profile_for_nickname(nickname)
        profile.set_current()
        ui.lineEdit_ovs_profile.setText(nickname)
        ui.lineEdit_ovs_name.setText(profile.switch)
        ui.lineEdit_ovs_hostname.setText(profile.hostname)
        output_ui.label_output_host.setText(profile.hostname)
#---------------------------------------------------------------
def param_abbrev(rowpos,comm,sudo_enable,custom_enable):
    if(debug):mydebug(inspect.currentframe())

    param_list=[]
    if(comm=='local'):
        param_list.append('LOC')
    elif(comm=='ssh'):
        param_list.append('SSH')
    elif(comm=='paramiko_key'):
        param_list.append('PA_K')
    elif(comm=='paramiko_password'):
        param_list.append('PA_P')


    if(sudo_enable):
        param_list.append('SUDO')

    if(custom_enable):
        param_list.append('CUS')        

    params=','.join(param_list)
    return params    
    
#---------------------------------------------------------------
def action_mgmt_process_dialog(newmgmt):
    if(debug):mydebug(inspect.currentframe())

    nname=mgmt_ui.lineEdit_mgmt_nickname.text()
    host=mgmt_ui.lineEdit_mgmt_host.text()
    ssh_password=mgmt_ui.lineEdit_mgmt_ssh_password.text()
    ssh_user=mgmt_ui.lineEdit_mgmt_ssh_username.text()
    ssh_key=mgmt_ui.lineEdit_mgmt_ssh_id.text()
    ssh_connect_timeout=mgmt_ui.lineEdit_mgmt_ssh_connect_timeout.text()
    command_timeout=mgmt_ui.lineEdit_mgmt_command_timeout.text()
    custom_script=mgmt_ui.lineEdit_mgmt_custom_script.text()
    custom_script_args=mgmt_ui.lineEdit_mgmt_custom_script_args.text()
    switch=mgmt_ui.lineEdit_mgmt_switch.text()

    force_of=mgmt_ui.comboBox_mgmt_openflow_protocol.currentText()
    of_nostats=mgmt_ui.comboBox_mgmt_of_no_stats.currentText()
    comm=mgmt_ui.comboBox_mgmt_comm.currentText()
    docker_release=mgmt_ui.comboBox_mgmt_openflow_docker_release.currentText()
    
    if(nname=='_dot_mgmt'):
        mywarning("Cannot edit '_dot_mgmt' management profile. It is reserved for plotnet dot command.")
        return
    
    if(mgmt_ui.radioButton_mgmt_ssh_keytype_dss.isChecked()):
        ssh_key_type='dss'
    elif(mgmt_ui.radioButton_mgmt_ssh_keytype_ecdsa.isChecked()):
        ssh_key_type='ecdsa'
    elif(mgmt_ui.radioButton_mgmt_ssh_keytype_ed25519.isChecked()):
        ssh_key_type='ed25519'
    else:
        ssh_key_type='rsa'
        
    if(mgmt_ui.radioButton_mgmt_sudo_enable.isChecked()):
        sudo_enable=True
    else:
        sudo_enable=False

    if(mgmt_ui.comboBox_mgmt_custom.currentText()=='enable'):
        custom_enable=True
    else:
        custom_enable=False
        
    if(not nname):
        mywarning("Please enter a nickname for this management profile")
        return

    if(newmgmt):
        Mymgmt(nickname=nname,
               hostname=host,
               ssh_username=ssh_user,
               ssh_key=ssh_key,
               ssh_key_type=ssh_key_type,
               ssh_password=ssh_password,
               ssh_connect_timeout=ssh_connect_timeout,
               custom_script=custom_script,
               custom_script_args=custom_script_args,
               comm=comm,
               sudo_enable=sudo_enable,
               custom_enable=custom_enable,
               command_timeout=command_timeout,
               switch=switch,
               force_of=force_of,
               docker_release=docker_release,
               of_nostats=of_nostats,
        )
    else:
        mgmt=Mymgmt.get_profile_for_nickname(nname)
        if(mgmt):
            mgmt.modify(nickname=nname,
                        hostname=host,
                        ssh_username=ssh_user,
                        ssh_key=ssh_key,
                        ssh_key_type=ssh_key_type,
                        ssh_password=ssh_password,
                        ssh_connect_timeout=ssh_connect_timeout,
                        custom_script=custom_script,
                        custom_script_args=custom_script_args,
                        comm=comm,
                        command_timeout=command_timeout,
                        sudo_enable=sudo_enable,
                        custom_enable=custom_enable,
                        switch=switch,
                        force_of=force_of,
                        docker_release=docker_release,
                        of_nostats=of_nostats,
                    )
        else:
            retval=myconfirm('YesNo',"Cannot modify non existing profile! Do you want me to create it ?")
            if(retval):
                Mymgmt(nickname=nname,
                       hostname=host,
                       ssh_username=ssh_user,
                       ssh_key=ssh_key,
                       ssh_key_type=ssh_key_type,
                       ssh_password=ssh_password,
                       ssh_connect_timeout=ssh_connect_timeout,
                       custom_script=custom_script,
                       custom_script_args=custom_script_args,
                       comm=comm,
                       command_timeout=command_timeout,
                       sudo_enable=sudo_enable,
                       custom_enable=custom_enable,
                       switch=switch,
                       force_of=force_of,
                       docker_release=docker_release,
                       of_nostats=of_nostats,
                )
                    
    action_mgmt_refresh(profile=nname)
    
#---------------------------------------------------------------

def action_mgmt_edit():
    if(debug):mydebug(inspect.currentframe())

    nickname=mgmt_table.getcurrenttext(0)
    row_mem=mgmt_table.getcurrent_rownumber()

    if(nickname):

        if(nickname=='_dot_mgmt'):
            mywarning("Cannot edit '_dot_mgmt' management profile. It is reserved for plotnet dot command.")
            return

        mgmt=Mymgmt.get_profile_for_nickname(nickname)
        mgmt_ui.lineEdit_mgmt_nickname.setText(mgmt.nickname)
        mgmt_ui.lineEdit_mgmt_host.setText(mgmt.hostname)
        mgmt_ui.lineEdit_mgmt_switch.setText(mgmt.switch)
        mgmt_ui.lineEdit_mgmt_ssh_id.setText(mgmt.ssh_key)
        mgmt_ui.lineEdit_mgmt_custom_script.setText(mgmt.custom_script)
        mgmt_ui.lineEdit_mgmt_custom_script_args.setText(mgmt.custom_script_args)
        mgmt_ui.lineEdit_mgmt_ssh_username.setText(mgmt.ssh_username)
        mgmt_ui.lineEdit_mgmt_ssh_connect_timeout.setText(mgmt.ssh_connect_timeout)
        mgmt_ui.lineEdit_mgmt_command_timeout.setText(mgmt.command_timeout)
        mgmt_ui.lineEdit_mgmt_ssh_password.setText(mgmt.ssh_password)
        comboBox_Write(mgmt_ui.comboBox_mgmt_comm,mgmt.comm)
        comboBox_Write(mgmt_ui.comboBox_mgmt_openflow_protocol,mgmt.force_of)
        comboBox_Write(mgmt_ui.comboBox_mgmt_of_no_stats,mgmt.of_nostats)
        comboBox_Write(mgmt_ui.comboBox_mgmt_openflow_docker_release,mgmt.docker_release)
        if(mgmt.ssh_key_type=='dss'):
            mgmt_ui.radioButton_mgmt_ssh_keytype_dss.setChecked(True)
        elif(mgmt.ssh_key_type=='ecdsa'):
            mgmt_ui.radioButton_mgmt_ssh_keytype_ecdsa.setChecked(True)
        elif(mgmt.ssh_key_type=='ed25519'):
            mgmt_ui.radioButton_mgmt_ssh_keytype_ed25519.setChecked(True)
        else:
            mgmt_ui.radioButton_mgmt_ssh_keytype_rsa.setChecked(True)
               
        if(mgmt.custom_enable):
            comboBox_Write(mgmt_ui.comboBox_mgmt_custom,'enable')
        else:
            comboBox_Write(mgmt_ui.comboBox_mgmt_custom,'disable')
        action_mgmt_custom_enable_fields()
            
        if(mgmt.sudo_enable):
           mgmt_ui.radioButton_mgmt_sudo_enable.setChecked(True) 
        else:
           mgmt_ui.radioButton_mgmt_sudo_disable.setChecked(True) 

        
    action_mgmt_access_enable_fields()
    action_mgmt_custom_enable_fields()
    if(mgmt_Dialog.exec()):
        action_mgmt_process_dialog(False)
        mgmt_table.select(row_mem,0)
        
#---------------------------------------------------------------

def action_mgmt_del_all():
    if(debug):mydebug(inspect.currentframe())

    Mymgmt.removeAll()
    Mymgmt.create_system_mgmt()
    action_mgmt_refresh()
    
#---------------------------------------------------------------

def action_mgmt_del():
    if(debug):mydebug(inspect.currentframe())

    nickname=mgmt_table.getcurrenttext(0)
    if(nickname):
        if(nickname=='_dot_mgmt'):
            mywarning("Cannot edit '_dot_mgmt' management profile. It is reserved for plotnet dot command.")
            return
        Mymgmt.remove(nickname)
        action_mgmt_refresh()

#---------------------------------------------------------------
def action_mgmt_export():
  if(debug):mydebug(inspect.currentframe())

  filename=action_mgmt_export_real()
  Mymgmt.remember_last_file_name(filename)

#---------------------------------------------------------------
@myJsonExport(mgmtDir,'Save management profiles to file',ui.pushButton_mgmt_export)
def action_mgmt_export_real():
    if(debug):mydebug(inspect.currentframe())
    
    liste=[]
    #ssh password will NOT be exported to file. This is a choice !
    for t in Mymgmt.getall(): 
        if(t.nickname=='_dot_mgmt'):
            continue

        d={'nickname': t.nickname,
           'switch' : t.switch,
           'ssh_key' : t.ssh_key,
           'ssh_key_type' : t.ssh_key_type,
           'ssh_username' : t.ssh_username,
           'command_timeout' : t.command_timeout,
           'ssh_connect_timeout' : t.ssh_connect_timeout,
           'comm' : t.comm,
           'sudo_enable' : t.sudo_enable,
           'hostname' : t.hostname,
           'custom_enable' : t.custom_enable,
           'custom_script' : t.custom_script,
           'custom_script_args' : t.custom_script_args,
           'force_of' : t.force_of,
           'of_nostats' : t.of_nostats,
           'docker_release' : t.docker_release,
       }
        liste.append(d)
      
    return liste

#---------------------------------------------------------------
@myJsonImport(mgmtDir,'Load management profiles from file',ui.pushButton_mgmt_import)
def action_mgmt_import(**opts):
    if(debug):mydebug(inspect.currentframe())

    Mymgmt.removeAll()

    
    json_txt=opts['json']
    
    for profile_dict in json_txt:
        nname=profile_dict.get('nickname')
        switch=profile_dict.get('switch',None)
        ssh_key=profile_dict.get('ssh_key',None)
        ssh_key_type=profile_dict.get('ssh_key_type','rsa')
        ssh_username=profile_dict.get('ssh_username',None)
        command_timeout=profile_dict.get('command_timeout','30')
        ssh_connect_timeout=profile_dict.get('ssh_connect_timeout','10')
        comm=profile_dict.get('comm','local')
        sudo_enable=profile_dict.get('sudo_enable',False)
        custom_enable=profile_dict.get('custom_enable',False)
        host=profile_dict.get('hostname',None)
        custom_script=profile_dict.get('custom_script',None)
        custom_script_args=profile_dict.get('custom_script_args',None)
        force_of=profile_dict.get('force_of','')
        of_nostats=profile_dict.get('of_nostats','original')
        docker_release=profile_dict.get('docker_release','>=1.13')

        if(nname=='_dot_mgmt'):
            continue

        Mymgmt(nickname=nname,
               hostname=host,
               ssh_username=ssh_username,
               ssh_key=ssh_key,
               ssh_key_type=ssh_key_type,
               command_timeout=command_timeout,
               ssh_connect_timeout=ssh_connect_timeout,
               custom_script=custom_script,
               custom_script_args=custom_script_args,
               switch=switch,
               sudo_enable=sudo_enable,
               custom_enable=custom_enable,
               comm=comm,
               force_of=force_of,
               docker_release=docker_release,
               of_nostats=of_nostats,
           )

    Mymgmt.create_system_mgmt()
    action_mgmt_refresh()
#---------------------------------------------------------------
        
def action_mgmt_refresh(**opts):
    if(debug):mydebug(inspect.currentframe())

    row_to_select=-1
    mgmt_table.delete_all_rows()
    clear_profile_bar(profile=True)
    for t in Mymgmt.getall():
        if(t.nickname=='_dot_mgmt'):
            continue
        rowpos=mgmt_table.new_row()
        mgmt_table.settext(rowpos,0,t.nickname)
        mgmt_table.settext(rowpos,1,t.switch)
        mgmt_table.settext(rowpos,2,t.hostname)
        mgmt_table.settext(rowpos,3,param_abbrev(rowpos,t.comm,t.sudo_enable,t.custom_enable))
        mgmt_table.settext(rowpos,4,t.force_of)
        if(opts.get('profile',None)==t.nickname):
            row_to_select=rowpos

    if(row_to_select>=0):
        mgmt_table.select(row_to_select,0)
        action_mgmt_select()
        
#---------------------------------------------------------------
def action_mgmt_interactive_import():
    if(debug):mydebug(inspect.currentframe())

    filename=action_mgmt_import()
    Mymgmt.remember_last_file_name(filename)

#---------------------------------------------------------------
def action_mgmt_auto_import():
    if(debug):mydebug(inspect.currentframe())

    filename=MainWindow.mypref.get('mgmt',None)
    if(filename):
        action_mgmt_import(filename=filename)

#---------------------------------------------------------------
#------------------------ PLOTNET ---------------------------------
#---------------------------------------------------------------


def plotnet_filter(text_array,filter_list):
    if(debug):mydebug(inspect.currentframe())

    result=[]
    for l in text_array:
        examine_this=[]

        pdl=pattern_dot_label.search(l)
        if(pdl):
            examine_this.extend(pdl.groups())

        pda=pattern_dot_arrow.search(l)
        if(pda):
            examine_this.extend(pda.groups())

        if(plotnet_search(examine_this,filter_list)):
            result.append(l)
        
    return result

#---------------------------------------------------------------
@myJsonImport(plotnetcfgDir,'Load filter keywords from file',ui.pushButton_plotnet_import)
def action_plotnet_import(**opts):
    if(debug):mydebug(inspect.currentframe())

    ui.lineEdit_plotnet_label_filter.setText('')
    json_txt=opts['json']

#    for bloc in json_txt:
#        filter=bloc.get('filter_keywords','')
#        ui.lineEdit_plotnet_label_filter.setText(filter)
#        break

    filter=json_txt.get('filter_keywords','')
    ui.lineEdit_plotnet_label_filter.setText(filter)
        
    action_plotnet_refresh()
        
#---------------------------------------------------------------
@myJsonExport(plotnetcfgDir,'Export filter keywords  to file',ui.pushButton_plotnet_export)
def action_plotnet_export():
    if(debug):mydebug(inspect.currentframe())

    #liste=[]
    d={'filter_keywords':ui.lineEdit_plotnet_label_filter.text()}
    #liste.append(d)

    return d

#---------------------------------------------------------------

def plotnet_search(text,filter_list):
    if(debug):mydebug(inspect.currentframe())
    
    for t in text:
        for f in filter_list:
            if(re.search(f,t)):
                return False
        
    return True

#---------------------------------------------------------------

def action_plotnet_refresh():
    if(debug):mydebug(inspect.currentframe())

    filename=tmpDir.file('plotnetcfg.png')
    filter=ui.lineEdit_plotnet_label_filter.text()
    plotnet_fontsize=ui.lineEdit_plotnet_font_size.text()
    plotnet_ranksep=ui.lineEdit_plotnet_rank_sep.text()
    plotnet_nodesep=ui.lineEdit_plotnet_node_sep.text()
    
    if(filter):
        filter_list=pattern_space_comma.split(filter)
    else:
        filter_list=[]

    result=exec_and_display(['plotnetcfg'])
    input_text=[]

    subgraph=False

    plotnet_options=''
    if(plotnet_fontsize):
        fontsize=",fontsize={}]\nfontsize={}\nedge [fontsize={}]\n".format(plotnet_fontsize,plotnet_fontsize,plotnet_fontsize)
    else:
        fontsize="]\n"

    if(plotnet_ranksep):
        plotnet_options="ranksep={}\n".format(plotnet_ranksep)
    if(plotnet_nodesep):
        plotnet_options=plotnet_options+"nodesep={}\n".format(plotnet_nodesep)
    
    for l in result.splitlines():
        pdsb=pattern_dot_subgraph_begin.match(l)
        l=pattern_dot_node.sub(r'\1'+"{}\n{}".format(fontsize,plotnet_options),l)

        if(pdsb):            #beginning of subgraph
            subgraph=True
            text_subgraph_header=l
            text_subgraph=[]
            label_found=False
            blacklist_subgraph=False
            continue
            
        if(subgraph==True):
            if(not label_found):
                pdsl=pattern_dot_subgraph_label.match(l)
                if(pdsl):
                    #print("SUBGRAPH LABEL:{}:".format(pdsl.group(1)))
                    if(not plotnet_search([pdsl.group(1)],filter_list)):
                        blacklist_subgraph=True
                label_found=True
                
            pdse=pattern_dot_subgraph_end.match(l)            
            if(pdse): #end of subgraph
                if(not blacklist_subgraph): 
                    #we process subgraph inside content
                    input_text.append(text_subgraph_header)
                    input_text.extend(plotnet_filter(text_subgraph,filter_list))
                    input_text.append(l)
                subgraph=False
            else:
                text_subgraph.append(l)
            
        else:
            # we process normal line
            if(plotnet_filter([l],filter_list)):
                input_text.append(l)

                

    input="\n".join(input_text)
    #print("\nINPUT=\n\n",input)
    exec_and_display(['dot','-Tpng',"-o{}".format(filename)],force_mgmt_nickname='_dot_mgmt',input=input)

    ui.plotnet_img.setText('image saved: {}'.format(filename))
    
    pixmap = QPixmap(filename)

    ui.label_plotnet.setScaledContents(False)
    ui.label_plotnet.setPixmap(pixmap)
    ui.label_plotnet.resize(pixmap.width(),pixmap.height())
    ui.label_plotnet.adjustSize()
    
#---------------------------------------------------------------
#------------------------ CONTROLLER ---------------------------------
#---------------------------------------------------------------
def action_controller_update():
    if(debug):mydebug(inspect.currentframe())

    # ovs-vsctl set-controller mybr tcp:192.168.0.155:1234
    ovs=ui.lineEdit_ovs_name.text()
    controller=ui.lineEdit_controller_target.text()
    if(not ovs):
        mywarning("Please select a bridge")
        return

    if(controller):
        exec_and_display(['ovs-vsctl','set-controller',ovs,controller])
    else:
        exec_and_display(['ovs-vsctl','del-controller',ovs])

    action_controller_refresh()
#---------------------------------------------------------------

def action_controller_conn_update():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    controller=ui.lineEdit_controller_target.text()
    if(not ovs):
        mywarning("Please select a bridge")
        return

    if(controller):
        mycommand=validate_prepare('ovs-vsctl','CONTROLLER_CONN','Controller')
        mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
        exec_and_display(mycommand2)

    action_controller_refresh()

#---------------------------------------------------------------

def action_controller_params_update():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    controller=ui.lineEdit_controller_target.text()
    if(not ovs):
        mywarning("Please select a bridge")
        return

    if(controller):
        mycommand=validate_prepare('ovs-vsctl','CONTROLLER_PARAMS','Controller')
        mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
        exec_and_display(mycommand2)

    action_controller_refresh()



#---------------------------------------------------------------

def action_controller_refresh():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        clear_widgets('CONTROLLER')
        result=exec_and_display(['ovs-vsctl','list','controller',switch])
        process_fields('CONTROLLER',result)
        process_fields('CONTROLLER_STATS',result,keep_dic=True)
        process_fields('CONTROLLER_CONN',result,keep_dic=True)
        process_fields('CONTROLLER_PARAMS',result,keep_dic=True)
        
#---------------------------------------------------------------
def action_controller_show():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(['ovs-vsctl','list','controller',switch],force_output=True)

#---------------------------------------------------------------
#------------------------ OPEN_VSWITCH ---------------------------------
#---------------------------------------------------------------
def action_open_vswitch_validate():
    if(debug):mydebug(inspect.currentframe())

    mycommand=validate_prepare('ovs-vsctl','OPEN_VSWITCH','open_vswitch')
    mycommand2=array_replace(mycommand,'_VARIABLE_','.')
    exec_and_display(mycommand2)
    action_open_vswitch_refresh()

#---------------------------------------------------------------
    
def action_open_vswitch_stats_validate():
    if(debug):mydebug(inspect.currentframe())

    mycommand=validate_prepare('ovs-vsctl','OPEN_VSWITCH_STATS','open_vswitch')
    mycommand2=array_replace(mycommand,'_VARIABLE_','.')
    exec_and_display(mycommand2)
    action_open_vswitch_refresh()

#---------------------------------------------------------------

def action_open_vswitch_refresh():
    if(debug):mydebug(inspect.currentframe())

    result=exec_and_display(['ovs-vsctl','list','open_vswitch'])
    clear_widgets('OPEN_VSWITCH')
    process_fields('OPEN_VSWITCH',result)
    process_fields('OPEN_VSWITCH_STATS',result,keep_dic=True)
        
#---------------------------------------------------------------
def action_open_vswitch_show():
    if(debug):mydebug(inspect.currentframe())

    exec_and_display(['ovs-vsctl','list','open_vswitch'],force_output=True)

#---------------------------------------------------------------
#------------------------ MANAGER ---------------------------------
#---------------------------------------------------------------
def action_manager_update():
    if(debug):mydebug(inspect.currentframe())

    validate('ovs-vsctl','MANAGER','manager')
    action_manager_refresh()

#---------------------------------------------------------------

def action_manager_refresh():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        result=exec_and_display(['ovs-vsctl','list','manager',switch])
        clear_widgets('MANAGER')
        process_fields('MANAGER',result)
        
#---------------------------------------------------------------
def action_manager_show():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(['ovs-vsctl','list','manager',switch],force_output=True)

#---------------------------------------------------------------
#------------------------ SSL ---------------------------------
#---------------------------------------------------------------

def action_ssl_update():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    privatekey=ui.lineEdit_ssl_private_key.text()
    cert=ui.lineEdit_ssl_cert.text()
    cacert=ui.lineEdit_ssl_ca_cert.text()
    bootstrap=ui.comboBox_ssl_bootstrap_cacert.currentText()
    if(ovs):
        if(bootstrap=='true'):
            command=['ovs-vsctl','--','--bootstrap']
        else:
            command=['ovs-vsctl']

        if(privatekey and cacert and cert):
            command.extend(['set-ssl',privatekey,cert,cacert])
        else:
            command.extend(['del-ssl'])
            
        exec_and_display(command)
        action_ssl_refresh()

#---------------------------------------------------------------
        
def action_ssl_refresh():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        result=exec_and_display(['ovs-vsctl','list','ssl'])
        clear_widgets('SSL')
        process_fields('SSL',result)
        
#---------------------------------------------------------------
def action_ssl_show():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(['ovs-vsctl','list','ssl'],force_output=True)
        

#---------------------------------------------------------------
#------------------------ BRIDGE ---------------------------------
#---------------------------------------------------------------

def action_bridge_update():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        mycommand=validate_prepare('ovs-vsctl','BRIDGE','Bridge')
        mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
        exec_and_display(mycommand2)
        action_bridge_refresh()

#---------------------------------------------------------------
        
def action_bridge_refresh():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        result=exec_and_display(['ovs-vsctl','list','bridge',switch])
        clear_widgets('BRIDGE')
        process_fields('BRIDGE',result)
#---------------------------------------------------------------
        
def action_bridge_mactable_show():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(['ovs-appctl','fdb/show',switch],force_output=True)

#---------------------------------------------------------------
        
def action_bridge_mactable_flush():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(['ovs-appctl','fdb/flush',switch])

#---------------------------------------------------------------        

def action_bridge_del_bridge():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        answer=myconfirm('YesCancel',"Are you sure you want to delete bridge:  {}  ???".format(switch))
        if(answer):
            exec_and_display(['ovs-vsctl','del-br',switch])
            ui.lineEdit_ovs_name.setText('')

#---------------------------------------------------------------
def action_bridge_add_bridge():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()

    if(switch):
        exec_and_display(['ovs-vsctl','add-br',switch,'--','set-fail-mode',switch,'standalone'])

#---------------------------------------------------------------
def action_ovs_route_show():
    if(debug):mydebug(inspect.currentframe())

    exec_and_display(['ovs-appctl','ovs/route/show'],force_output=True)
        
#---------------------------------------------------------------
def action_bridge_list_bridge():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(["ovs-vsctl",'--column=_uuid,name,status',"list","bridge",switch])
        
                    
#---------------------------------------------------------------
#------------------------ OPENFLOW GROUPS    -------------------
#---------------------------------------------------------------
def action_ofgroup_param_add():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_params_table.new_row()
#---------------------------------------------------------------
def action_ofgroup_param_del():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_params_table.delete_row()
#---------------------------------------------------------------
def action_ofgroup_param_up():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_params_table.up_row()
#---------------------------------------------------------------
def action_ofgroup_param_down():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_params_table.down_row()
#---------------------------------------------------------------
def action_ofgroup_param_del_all():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_params_table.delete_all_rows()


#---------------------------------------------------------------
def action_ofgroup_bucket_add():
    if(debug):mydebug(inspect.currentframe())

    params=[]
    actions=[]
    
    rowpos=ofgroup_buckets_table.new_row()
    for i in range(ofgroup_params_table.rowcount()):
        p=ofgroup_params_table.gettext(i,0)
        if(p):
            params.append(p)

    for i in range(ofaction_table.rowcount()):
        p=ofaction_table.gettext(i,0)
        if(p):
            actions.append(p)

    ofgroup_buckets_table.settext(rowpos,0,','.join(params))
    ofgroup_buckets_table.settext(rowpos,1,','.join(actions))
    ofgroup_buckets_table.select(rowpos,0)
    
#---------------------------------------------------------------
def action_ofgroup_bucket_del():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_buckets_table.delete_row()
    action_ofgroup_params_refresh()
    
#---------------------------------------------------------------
def action_ofgroup_bucket_up():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_buckets_table.up_row()
#---------------------------------------------------------------
def action_ofgroup_bucket_down():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_buckets_table.down_row()
#---------------------------------------------------------------
def action_ofgroup_bucket_del_all():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_buckets_table.delete_all_rows()
    
#---------------------------------------------------------------
def action_ofgroup_add(**opts):
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):

        groupid=ofgroup_ui.lineEdit_ofgroup_id.text()
        grouptype=ofgroup_ui.comboBox_ofgroup_type.currentText()

        ofproto=Mymgmt.get_current_profile_attr('force_of')
            
        if(groupid):
            buckets=[]
            for r in range(ofgroup_buckets_table.rowcount()):
                params=ofgroup_buckets_table.gettext(r,0)
                actions=ofgroup_buckets_table.gettext(r,1)

                #print("PARAMS=",params)
                #print("ACTIONS=",actions)
                if(actions):
                    if(params):
                       buckets.append("bucket={},actions={}".format(params,actions))
                    else:
                       #no params in this bucket
                       buckets.append("actions={}".format(actions))
                else:
                    mywarning("Bucket without action ! Aborting add-group")
                    return()
                       
            if(buckets):
                if(opts['newgroup']):
                    exec_and_display(['ovs-ofctl','add-group','-O',ofproto,switch,"group_id={},type={},{}".format(groupid,grouptype,",".join(buckets))])                    
                else:
                    exec_and_display(['ovs-ofctl','mod-group','-O',ofproto,switch,"group_id={},type={},{}".format(groupid,grouptype,",".join(buckets))])
                action_ofgroup_refresh()
            else:
                mywarning("You need at least one bucket in your group")
        else:
            mywarning("Please specify a Group ID !")
    else:
        mywarning("Please select a switch !")
        
    
#---------------------------------------------------------------
def action_ofgroup_refresh():
    if(debug):mydebug(inspect.currentframe())

    ofgroup_table.delete_all_rows()
    
    nickname=ui.lineEdit_ovs_profile.text()
    if(nickname):
        profile=Mymgmt.get_profile_for_nickname(nickname)
        ofproto=profile.force_of
    else:
        mywarning('A management profile is needed')
        return
    
    mybr=ui.lineEdit_ovs_name.text()
    if(mybr):
        group_filter=ui.lineEdit_ofgroup_filter.text()

        #ofgroup_table.w.setSortingEnabled(False)
        filter=[]
        if(group_filter):
            filter.append("group_id={}".format(group_filter))
        if(filter):
            result=exec_and_display(['ovs-ofctl','-O',ofproto,'dump-groups',mybr,"_mySPECIALQUOTE_{}_mySPECIALQUOTE_".format(",".join(filter))])
        else:
            result=exec_and_display(['ovs-ofctl','-O',ofproto,'dump-groups',mybr])
            
        for f in result.splitlines():
            #table='0'
            #cond=''
            
            pfg=pattern_flow_group.match(f)
            if(pfg):
                groupid=pfg.group(1)
                typeg=pfg.group(2)
                buckets=pfg.group(3)
                
                rowpos=ofgroup_table.new_row()
                ofgroup_table.settext(rowpos,0,groupid)
                ofgroup_table.settext(rowpos,1,typeg)
                ofgroup_table.settext(rowpos,2,buckets)

        ofgroup_table.resize()
            
    else:
        mywarning("Please select a bridge !")
        
    #ofgroup_table.w.setSortingEnabled(True)
    ofgroup_table.resize()

#---------------------------------------------------------------
    
def action_ofgroup_import():

    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        nickname=ui.lineEdit_ovs_profile.text()
        if(nickname):
            profile=Mymgmt.get_profile_for_nickname(nickname)
            ofproto=profile.force_of
        else:
            mywarning('A management profile is needed')
            return
            
        filename=ofGroupDir.browse("Select OFGROUP file to import",parent_ui=ui.pushButton_ofgroup_import)
        if(filename):
            # we copy in tmp fil only valid group lines from input file
            with tempfile.NamedTemporaryFile(prefix='ovs',delete=False) as ftmp:
                with open(filename) as finput:
                    for l in finput.readlines():
                        pfg=pattern_flow_group.match(l)
                        if(pfg):
                            ftmp.write(bytes(l, 'utf-8'))
                    ftmp.close()
                exec_and_display(['ovs-ofctl','add-groups','-O',ofproto,switch,ftmp.name])                    
                os.unlink(ftmp.name)
                action_ofgroup_refresh()
    else:
        mywarning("Please select a switch !")
        
#---------------------------------------------------------------

def action_ofgroup_export():
    
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        nickname=ui.lineEdit_ovs_profile.text()
        if(nickname):
            profile=Mymgmt.get_profile_for_nickname(nickname)
            ofproto=profile.force_of
        else:
            mywarning('A management profile is needed')
            return

        filename=ofGroupDir.save("Select OFGROUP file for export",parent_ui=ui.pushButton_ofgroup_export)
        if(filename):
            with open(filename,'w') as fh:
                result=exec_and_display(['ovs-ofctl','dump-groups','-O',ofproto,switch])
                fh.write(result)
                fh.close()


#---------------------------------------------------------------

def action_ofgroup_delete_all():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        nickname=ui.lineEdit_ovs_profile.text()
        if(nickname):
            profile=Mymgmt.get_profile_for_nickname(nickname)
            ofproto=profile.force_of
        else:
            mywarning('A management profile is needed')
            return

        exec_and_display(['ovs-ofctl','del-groups','-O',ofproto,switch])    

        action_ofgroup_refresh()

#---------------------------------------------------------------

def action_ofgroup_delete():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        rowpos=ofgroup_table.getcurrent_rownumber()
        if(rowpos>=0):
            nickname=ui.lineEdit_ovs_profile.text()
            if(nickname):
                profile=Mymgmt.get_profile_for_nickname(nickname)
                ofproto=profile.force_of
            else:
                mywarning('A management profile is needed')
                return

            group_id=ofgroup_table.gettext(rowpos,0)
            exec_and_display(['ovs-ofctl','del-groups','-O',ofproto,switch,"group_id={}".format(group_id)])    

            action_ofgroup_refresh()

#---------------------------------------------------------------
            
def action_ofgroup_bucket_refresh():
    if(debug):mydebug(inspect.currentframe())

    if(ofgroup_Dialog.isVisible()):
        rowpos=ofgroup_table.getcurrent_rownumber()
        #rowToSelect=0
        if(rowpos>=0):
            nickname=ui.lineEdit_ovs_profile.text()
            if(nickname):
                #profile=Mymgmt.get_profile_for_nickname(nickname)
                #ofproto=profile.force_of
                pass
            else:
                mywarning('A management profile is needed')
                return

            group_id=ofgroup_table.gettext(rowpos,0)
            group_type=ofgroup_table.gettext(rowpos,1)
            group_buckets=ofgroup_table.gettext(rowpos,2)

            comboBox_Write(ofgroup_ui.comboBox_ofgroup_type,group_type)
            ofgroup_ui.lineEdit_ofgroup_id.setText(group_id)
            ofgroup_buckets_table.delete_all_rows()
            ofgroup_params_table.delete_all_rows()
            for bucket in pattern_bucket.split(group_buckets):
                if(bucket):
                    rowpos=ofgroup_buckets_table.new_row()
                    pbpa=pattern_bucket_params_actions.match(bucket)
                    if(pbpa):
                        params=pbpa.group(1)
                        actions=pbpa.group(2)
                        params=params.rstrip(',')
                        actions=actions.rstrip(',')
                        ofgroup_buckets_table.settext(rowpos,0,params)
                        ofgroup_buckets_table.settext(rowpos,1,actions)
        
#---------------------------------------------------------------
            
def action_ofgroup_editor():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        ofgroup_Dialog.show()
        action_ofgroup_bucket_refresh()
        of_Dialog.show()

#---------------------------------------------------------------
            
def action_ofgroup_params_refresh():
    if(debug):mydebug(inspect.currentframe())

    rowpos=ofgroup_buckets_table.getcurrent_rownumber()
    if(rowpos>=0):
        ofgroup_params_table.delete_all_rows()
        ofaction_table.delete_all_rows()
        ofgroup_params_table.delete_all_rows()
        
        params=ofgroup_buckets_table.gettext(rowpos,0)
        actions=ofgroup_buckets_table.gettext(rowpos,1)

        for p in pattern_comma.split(params):
            if(p):
                rowpos=ofgroup_params_table.new_row()
                ofgroup_params_table.settext(rowpos,0,p)

        action_code_split_loop(actions)

        

#---------------------------------------------------------------
#------------------------ OPENFLOW ---------------------------------
#---------------------------------------------------------------


#---------------------------------------------------------------
def action_bridge_ofctl_show():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        exec_and_display(['ovs-ofctl','-O',ofproto,'show',switch],force_output=True)

#---------------------------------------------------------------
def action_trace_packet_show():
    if(debug):mydebug(inspect.currentframe())

    oftrace_Dialog.show()
    of_Dialog.show()

#---------------------------------------------------------------
def action_trace_packet_load():
    if(debug):mydebug(inspect.currentframe())

    filename=packetDir.browse('Select your packet file',parent_ui=oftrace_ui.pushButton_of_trace_packet_load)

    if(filename):
        if(oftrace_ui.radioButton_of_trace_pcap.isChecked()):
            result=exec_and_display(['ovs-pcap',filename])
            if(result):
                oftrace_ui.lineEdit_of_trace_packet.setText(result)
        else:
            with open(filename,'r') as fh:
                packet_raw=fh.read()
                oftrace_ui.lineEdit_of_trace_packet.setText(packet_raw)

        oftrace_ui.lineEdit_of_trace_packet.setCursorPosition(0)

#---------------------------------------------------------------
def action_trace_run():
    if(debug):mydebug(inspect.currentframe())

    name=oftrace_table.getcurrenttext(0)

    switch=ui.lineEdit_ovs_name.text()
    condl=[]
    actionl=[]
    if(switch):
        if(name):
            t=Mytrace.get(name)
            
            for c in t.condlist:
                condl.append(c)

            for a in t.actionlist:
                actionl.append(a)

            cmdline=['ovs-appctl']

            flags=[]
            for flag in ('trk','new','est','rel','rpl','inv','dnat','snat'):
                if(flag in t.ctlist):
                    flags.append(flag)

            if('packetout' in t.optlist):
                cmdline.append('ofproto/trace-packet-out')
                if('consistent' in t.optlist):
                    cmdline.append('-consistent')
                    
                cmdline.extend([switch,"_mySPECIALQUOTE_{}_mySPECIALQUOTE_".format(','.join(condl)),"_mySPECIALQUOTE_{}_mySPECIALQUOTE_".format(','.join(actionl))])

            else:
                cmdline.append('ofproto/trace')
                cmdline.extend([switch,"_mySPECIALQUOTE_{}_mySPECIALQUOTE_".format(','.join(condl))])
                if(flags):
                    cmdline.append("--ct-next '{}'".format(','.join(flags)))
                
            if(t.packet):
                cmdline.append(t.packet)
            elif('generate' in t.optlist):
                cmdline.append('-generate')

            exec_and_display(cmdline,force_output=True)
        else:
            mywarning("Please select a trace first !")
    else:
        mywarning("Please select a switch !")
        
#---------------------------------------------------------------
    
def action_select_oftrace():
    if(debug):mydebug(inspect.currentframe())

    name=oftrace_table.getcurrenttext(0)
    t=Mytrace.get(name)

    clear_widgets('OFTRACE')
    oftrace_ui.lineEdit_of_trace_name.setText(t.name)

    if(t.packet):oftrace_ui.lineEdit_of_trace_packet.setText(t.packet)
    
    if('packetout' in t.optlist):
        oftrace_ui.checkBox_of_trace_packetout.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_packetout.setChecked(False)
        
    if('generate' in t.optlist):
        oftrace_ui.checkBox_of_trace_generate.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_generate.setChecked(False)
        
    if('consistent' in t.optlist):
        oftrace_ui.checkBox_of_trace_consistent.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_consistent.setChecked(False)


    if('trk' in t.ctlist):
        oftrace_ui.checkBox_of_trace_trk.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_trk.setChecked(False)
    if('new' in t.ctlist):
        oftrace_ui.checkBox_of_trace_new.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_new.setChecked(False)
    if('est' in t.ctlist):
        oftrace_ui.checkBox_of_trace_est.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_est.setChecked(False)
    if('rel' in t.ctlist):
        oftrace_ui.checkBox_of_trace_rel.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_rel.setChecked(False)
    if('rpl' in t.ctlist):
        oftrace_ui.checkBox_of_trace_rpl.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_rpl.setChecked(False)
    if('inv' in t.ctlist):
        oftrace_ui.checkBox_of_trace_inv.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_inv.setChecked(False)
    if('dnat' in t.ctlist):
        oftrace_ui.checkBox_of_trace_dnat.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_dnat.setChecked(False)
    if('snat' in t.ctlist):
        oftrace_ui.checkBox_of_trace_snat.setChecked(True)
    else:
        oftrace_ui.checkBox_of_trace_snat.setChecked(False)

    ofcond_table.delete_all_rows()
    ofaction_table.delete_all_rows()
    
    for c in t.condlist:
        r=ofcond_table.new_row()
        ofcond_table.settext(r,0,c)

    for a in t.actionlist:
        r=ofaction_table.new_row()
        ofaction_table.settext(r,0,a)

    oftrace_ui.lineEdit_of_trace_packet.setCursorPosition(0)
    
#---------------------------------------------------------------
def action_trace_add():
    if(debug):mydebug(inspect.currentframe())

    trace_name=oftrace_ui.lineEdit_of_trace_name.text()
    trace_packet=oftrace_ui.lineEdit_of_trace_packet.text()
    ct_list=[]
    opt_list=[]
    if(trace_name):

        (conditions,actions)=of_gen_flow(array_output=True)
        print("conditions=",conditions)
        print("actions=",actions)

        
        if(oftrace_ui.checkBox_of_trace_packetout.isChecked()):
            opt_list.append('packetout')
        if(oftrace_ui.checkBox_of_trace_generate.isChecked()):
            opt_list.append('generate')
        if(oftrace_ui.checkBox_of_trace_consistent.isChecked()):
            opt_list.append('consistent')


        if(oftrace_ui.checkBox_of_trace_trk.isChecked()):
            ct_list.append('trk')
        if(oftrace_ui.checkBox_of_trace_new.isChecked()):
            ct_list.append('new')
        if(oftrace_ui.checkBox_of_trace_est.isChecked()):
            ct_list.append('est')
        if(oftrace_ui.checkBox_of_trace_rel.isChecked()):
            ct_list.append('rel')
        if(oftrace_ui.checkBox_of_trace_rpl.isChecked()):
            ct_list.append('rpl')
        if(oftrace_ui.checkBox_of_trace_inv.isChecked()):
            ct_list.append('inv')
        if(oftrace_ui.checkBox_of_trace_dnat.isChecked()):
            ct_list.append('dnat')
        if(oftrace_ui.checkBox_of_trace_snat.isChecked()):
            ct_list.append('snat')
            
        Mytrace(trace_name,
                condlist=conditions,
                actionlist=actions,
                packet=trace_packet,
                ctlist=ct_list,
                optlist=opt_list)
        
        action_trace_refresh()

    else:
        mywarning("Name is mandatory. Please provide a name for this trace.")

#---------------------------------------------------------------
def action_trace_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('OFTRACE')
    oftrace_table.delete_all_rows()

    for t in Mytrace.getall():
        r=oftrace_table.new_row()
        oftrace_table.settext(r,0,t.name)

    
#---------------------------------------------------------------
def action_trace_del():
    if(debug):mydebug(inspect.currentframe())

    if(oftrace_table.getcurrent_rownumber()>=0):
        tname=oftrace_table.getcurrenttext(0)
        Mytrace.remove(tname)
        action_trace_refresh()
    else:
        mywarning("Please select a trace !")
        
#---------------------------------------------------------------
@myJsonExport(ofTraceDir,'Save traces config to file',oftrace_ui.pushButton_of_trace_export)
def action_trace_export():
    if(debug):mydebug(inspect.currentframe())

    liste=[]
    for t in Mytrace.getall():
        d={'name': t.name,
           'packet' : t.packet,
           'optlist' : t.optlist,
           'ctlist' : t.ctlist,
           'condlist' : t.condlist,
           'actionlist' : t.actionlist}
        liste.append(d)

    return liste

#---------------------------------------------------------------

def action_trace_import():
    if(debug):mydebug(inspect.currentframe())

    filename=ofTraceDir.browse('Select trace config file to import',parent_ui=oftrace_ui.pushButton_of_trace_import)
    if(filename):
        with open(filename) as fh:
            l=fh.read()
            liste_dict=json.loads(l)
            for oftrace_dic in liste_dict:
                actionl=oftrace_dic.get('actionlist',[])
                Mytrace(oftrace_dic['name'],
                        condlist=oftrace_dic['condlist'],
                        packet=oftrace_dic['packet'],
                        ctlist=oftrace_dic['ctlist'],
                        optlist=oftrace_dic['optlist'],
                        actionlist=actionl
                )

            action_trace_refresh()

#---------------------------------------------------------------
def action_trace_del_all():
    if(debug):mydebug(inspect.currentframe())

    Mytrace.removeAll()
            
    action_trace_refresh()
    
#---------------------------------------------------------------

def action_of_dialog_cond_del_all():
    if(debug):mydebug(inspect.currentframe())

    if(not ofcond_table.isreadOnly()):
        ofcond_table.delete_all_rows()
    
#---------------------------------------------------------------

def action_of_dialog_action_del_all():
    
    if(debug):mydebug(inspect.currentframe())
    ofaction_table.delete_all_rows()
    
#---------------------------------------------------------------

def action_of_dialog_cond_add():
    
    if(debug):mydebug(inspect.currentframe())

    if(not ofcond_table.isreadOnly()):
        row=ofcond_table.new_row()

#---------------------------------------------------------------

def action_of_dialog_cond_del():
    
    if(debug):mydebug(inspect.currentframe())

    if(not ofcond_table.isreadOnly()):
        ofcond_table.delete_row()
        #ofcond_table.resize()
    
#---------------------------------------------------------------

def action_of_dialog_action_add():
    
    if(debug):mydebug(inspect.currentframe())

    ofaction_table.new_row()
    #ofaction_table.resize()
    
#---------------------------------------------------------------
    
def action_of_dialog_action_del():
    
    if(debug):mydebug(inspect.currentframe())

    ofaction_table.delete_row()
    
    
#---------------------------------------------------------------

def action_of_dialog_action_up():
    
    if(debug):mydebug(inspect.currentframe())

    ofaction_table.up_row()
    
#---------------------------------------------------------------

def action_of_dialog_action_down():
    
    if(debug):mydebug(inspect.currentframe())

    ofaction_table.down_row()
#---------------------------------------------------------------

def action_of_import():
    
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        filename=ofDir.browse("Select OF file to import",parent_ui=oftrace_ui.pushButton_of_trace_import)
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        if(filename):
            with open(filename) as fh:
                text=fh.read()
                exec_and_display(['ovs-ofctl','-O',ofproto,'add-flow',switch,'-'],input=text)
            action_of_refresh()
    else:
        mywarning("Please select a switch !")
        
#---------------------------------------------------------------

def of_no_stats(of_nostats,flow):
    if(debug):mydebug(inspect.currentframe())

    if(of_nostats=='python'):
        return pattern_of_stats.sub('',flow)
    else:
        return flow

#---------------------------------------------------------------

def dump_flows(switch,**options):
    if(debug):mydebug(inspect.currentframe())
            
    of_nostats=Mymgmt.get_current_profile_attr('of_nostats')
    ofproto=Mymgmt.get_current_profile_attr('force_of')

    filter=options.get('filter',None)
    
    if(of_nostats=='original'):
        command=['ovs-ofctl','-O',ofproto,'dump-flows','--no-stats',switch]
    else:
        command=['ovs-ofctl','-O',ofproto,'dump-flows',switch]
        
    if(filter):
        command.append(filter)

    result=exec_and_display(command)
    return of_no_stats(of_nostats,result)
            

#---------------------------------------------------------------

def action_of_export():
    
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        filename=ofDir.save("Select OF file for export",parent_ui=ui.pushButton_of_export)

        if(filename):
            with open(filename,'w') as fh:
                result=dump_flows(switch)
                fh.write(result)
                fh.close()
#---------------------------------------------------------------

def action_of_delete_all():
    
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        table_filter=ui.lineEdit_of_filter_table.text()
        cookie_filter=ui.lineEdit_of_filter_cookie.text()
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        
        if(of_delete_Dialog.exec()):
            if(ofdel_ui.radioButton_of_delete_cookie.isChecked()):
                if(cookie_filter):
                    if(pattern_slash.search(cookie_filter)):
                        filter="_mySPECIALQUOTE_cookie={}_mySPECIALQUOTE_".format(cookie_filter)
                    else:
                        filter="_mySPECIALQUOTE_cookie={}/-1_mySPECIALQUOTE_".format(cookie_filter)
                    exec_and_display(['ovs-ofctl','-O',ofproto,'del-flows',switch,filter])
                else:
                    mywarning("There is no cookie filter")
            elif(ofdel_ui.radioButton_of_delete_table.isChecked()):
                if(table_filter):
                    filter="_mySPECIALQUOTE_table={}_mySPECIALQUOTE_".format(table_filter)
                    
                    exec_and_display(['ovs-ofctl','-O',ofproto,'del-flows',switch,filter])
                else:
                    mywarning("There is no table filter")

            elif(ofdel_ui.radioButton_of_delete_table_and_cookie.isChecked()):
                if(table_filter):
                    filter="table={}".format(table_filter)
                    
                else:
                    mywarning("There is no table filter")

                if(cookie_filter):
                    if(pattern_slash.search(cookie_filter)):
                        filter=filter+",cookie={}".format(cookie_filter)
                    else:
                        filter=filter+",cookie={}/-1".format(cookie_filter)

                    exec_and_display(['ovs-ofctl','-O',ofproto,'del-flows',switch,"_mySPECIALQUOTE_{}_mySPECIALQUOTE_".format(filter)])
                else:
                    mywarning("There is no cookie filter")

            elif(ofdel_ui.radioButton_of_delete_all.isChecked()):
                exec_and_display(['ovs-ofctl','-O',ofproto,'del-flows',switch])
                
            
            action_of_refresh()
#---------------------------------------------------------------

def action_of_delete():
    
    if(debug):mydebug(inspect.currentframe())
    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        rowpos=of_table.getcurrent_rownumber()
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        if(rowpos>=0):
            table=of_table.gettext(rowpos,0)
            conds=of_table.gettext(rowpos,1)
            if(not conds):
                conds='ip_src=7.7.7.7'
            flow="_mySPECIALQUOTE_table={},{}_mySPECIALQUOTE_".format(table,conds)

            exec_and_display(['ovs-ofctl','-O',ofproto,'--strict','del-flows',switch,flow])
            action_of_refresh()
#---------------------------------------------------------------

def action_of_floweditor():
    
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        of_Dialog.show()
        sync_selected_of()
   
    else:
        mywarning("Please select a switch !")

#---------------------------------------------------------------
def sync_selected_of():
    if(debug):mydebug(inspect.currentframe())

    rowpos_flow=of_table.getcurrent_rownumber()             
    if(rowpos_flow>=0):                                     
        ofcond_table.delete_all_rows()                          
        ofaction_table.delete_all_rows()                        

        table_read=of_table.gettext(rowpos_flow,0)                                                                               
        if(table_read!='0'):
            rowpos_cond=ofcond_table.new_row()              
            ofcond_table.settext(rowpos_cond,0,"table={}".format(table_read))      

        cond_read=of_table.gettext(rowpos_flow,1)                       
        if(cond_read):                                          
            for cond_l in cond_read.split(','):             
                rowpos_cond=ofcond_table.new_row()              
                ofcond_table.settext(rowpos_cond,0,cond_l)      
                                                                
        action_read=of_table.gettext(rowpos_flow,2)
        action_code_split_loop(action_read)

#---------------------------------------------------------------

def action_code_split_loop(actions):
    if(debug):mydebug(inspect.currentframe())
    
    for action_l in action_code_split(actions):         
        rowpos_action=ofaction_table.new_row()              
        ofaction_table.settext(rowpos_action,0,action_l)    


    
#---------------------------------------------------------------

def action_of_add():
    
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        (conditions,actions)=of_gen_flow(array_output=False)
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        if(conditions):
            exec_and_display(['ovs-ofctl','-O',ofproto,'add-flow', switch, "_mySPECIALQUOTE_{},actions={}_mySPECIALQUOTE_".format(conditions,actions)])
        else:
            exec_and_display(['ovs-ofctl','-O',ofproto,'add-flow', switch, "_mySPECIALQUOTE_actions={}_mySPECIALQUOTE_".format(actions)])
        
        action_of_refresh()
            
    else:
        mywarning("Please select a switch !")

#---------------------------------------------------------------

def action_of_edit():
    
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        (conditions,actions)=of_gen_flow(array_output=False)
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        
        if(conditions):
            exec_and_display(['ovs-ofctl','-O',ofproto,'--strict','mod-flows', switch, "_mySPECIALQUOTE_{},actions={}_mySPECIALQUOTE_".format(conditions,actions)])
        else:
            exec_and_display(['ovs-ofctl','-O',ofproto,'--strict','mod-flows', switch, "_mySPECIALQUOTE_actions={}_mySPECIALQUOTE_".format(actions)])
                
        action_of_refresh()

    else:
        mywarning("Please select a switch !")

#---------------------------------------------------------------

def of_gen_flow(**opts):
    if(debug):mydebug(inspect.currentframe())

    cond_list=[]
    action_list=[]
            
    for rc in range(ofcond_table.rowCount()):
        cond=ofcond_table.gettext(rc,0)
        cond_list.append("{}".format(cond))


                
    for ra in range(ofaction_table.rowCount()):
        action=ofaction_table.gettext(ra,0)
        action_list.append("{}".format(action))

    if(opts['array_output']):
        conditions=cond_list
        actions=action_list
    else:
        conditions=",".join(cond_list)
        actions=",".join(action_list)

    return (conditions,actions)

#---------------------------------------------------------------

def action_of_dpctl_dumpflows():
    mybr=ui.lineEdit_ovs_name.text()
    if(mybr):
        exec_and_display(['ovs-dpctl','dump-flows'],force_output=True)

#---------------------------------------------------------------

def action_of_dumpflows():
    mybr=ui.lineEdit_ovs_name.text()
    if(mybr):
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        exec_and_display(['ovs-ofctl','-O',ofproto,'dump-flows',mybr],force_output=True)
        
#---------------------------------------------------------------

def action_of_refresh():
    
    if(debug):mydebug(inspect.currentframe())

    of_table.delete_all_rows()

    mybr=ui.lineEdit_ovs_name.text()
    if(mybr):
        table_filter=ui.lineEdit_of_filter_table.text()
        cookie_filter=ui.lineEdit_of_filter_cookie.text()
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        
        filter=[]
        if(table_filter):
            filter.append("table={}".format(table_filter))
        if(cookie_filter):
            if(pattern_slash.search(cookie_filter)):
                filter.append("cookie={}".format(cookie_filter))
            else:
                filter.append("cookie={}/-1".format(cookie_filter))
                
        if(filter):
            result=dump_flows(mybr,filter="_mySPECIALQUOTE_{}_mySPECIALQUOTE_".format(",".join(filter)))
        else:
            result=dump_flows(mybr)
            
        for f in result.splitlines():
            table='0'
            cond=''
            
            pft=pattern_flow_table.match(f)
            if(pft):
                table=pft.group(1)
                length=len(pft.group(0))
                #remove table field
                f=f[length:]

            pfc=pattern_flow_cond.match(f)
            if(pfc):
                cond=pfc.group(1)
                length=len(pfc.group(0))
                #remove cond field
                f=f[length:]

            pfa=pattern_flow_actions.match(f)
            if(pfa):
                actions=pfa.group(1)
                rowpos=of_table.new_row()
                of_table.settext(rowpos,0,table)
                of_table.settext(rowpos,1,cond)
                of_table.settext(rowpos,2,actions)

        of_table.resize()
            
    else:
        mywarning("Please select a bridge !")


#---------------------------------------------------------------
#------------------------ QOS ---------------------------------
#---------------------------------------------------------------

def action_qos_addflow():
    
    if(debug):mydebug(inspect.currentframe())

    for mapline in qos_get_queue_mapid():
        qos=mapline[0]
        map_id=mapline[1]
        break
    else:
        mywarning("Please select a linked queue in qos table !")
        return
    
    mybr=ui.lineEdit_ovs_name.text()
    ofproto=Mymgmt.get_current_profile_attr('force_of')

    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        
        of_port_result=exec_and_display(['ovs-vsctl','get','Interface', interfacename,'ofport'])
        pp=pattern_portname.match(of_port_result)
        if(pp):
            ofport=pp.group(1)
            if(int(ofport)>0):
                exec_and_display(['ovs-ofctl','-O',ofproto,'add-flow',mybr,'in_port={},actions=set_queue:{},normal'.format(ofport,map_id)])
            else:
                mywarning("Port {} doesnt have any openflow number.".format(portname))
        else:
            print("unexpected result:{} len:{}".format(of_port_result,len(of_port_result)))

        break
    else:
        mywarning("Please select a portname")    
    
#---------------------------------------------------------------

def action_qos_remove_queue():
    
    if(debug):mydebug(inspect.currentframe())

    queue_table_row=queue_table.getcurrent_rownumber()

    if(queue_table_row <0):
        mywarning("Please select a queue in queue table !")
        return

    queue=queue_table.gettext(queue_table_row,0)
    exec_and_display(['ovs-vsctl','destroy','queue', queue])
    action_qos_queue_refresh(False)
    action_qos_porttree_refresh(False)
    
#---------------------------------------------------------------


def action_qos_remove_qos():
    
    if(debug):mydebug(inspect.currentframe())

    for treeline in qos_tree.get_selected():
        qos=treeline[0]
        exec_and_display(['ovs-vsctl','destroy','qos', qos])

    action_qos_porttree_refresh(False)
    
#---------------------------------------------------------------
def qos_get_queue_mapid():

    if(debug):mydebug(inspect.currentframe())

    result=[]
    for treeline in qos_tree.get_selected():
        qos=treeline[0]

        if(len(treeline)==3):
            queuelong=treeline[2]
            pqm=pattern_queue_map.match(queuelong)
            if(pqm):
                result.append([qos,pqm.group(1)])
    
    if(not result):
        mywarning("Please select a linked queue in qos table !")

    return result

#---------------------------------------------------------------
def action_qos_unlink_queue():
    if(debug):mydebug(inspect.currentframe())

    for mapline in qos_get_queue_mapid():
        qos=mapline[0]
        map_id=mapline[1]
        exec_and_display(['ovs-vsctl','remove','qos',qos,'queues', map_id])

    action_qos_porttree_refresh(False)

    
#---------------------------------------------------------------
def action_qos_link_queue():
    if(debug):mydebug(inspect.currentframe())

    queue_table_row=queue_table.getcurrent_rownumber()

    if(queue_table_row <0):
        mywarning("Please select a queue in queue table !")
        return

    for treeline in qos_tree.get_selected():
        qos=treeline[0]
        queue=queue_table.gettext(queue_table_row,0)

        qlink_ui.lineEdit_dialog_qos_queue.setText(queue)
        qlink_ui.lineEdit_dialog_qos_qos.setText(qos)
        if(qlink_Dialog.exec()):
            map_id=qlink_ui.lineEdit_dialog_queue_mapid.text()
            if(map_id):
                exec_and_display(['ovs-vsctl','add','qos',qos,'queues', "{}={}".format(map_id,queue)])
            else:
                mywarning("You didn't provide a map id. Operation cancelled for qos:{}".format(qos))

    action_qos_porttree_refresh(False)    

#---------------------------------------------------------------

def action_qos_port_set():
    if(debug):mydebug(inspect.currentframe())

    qos=None
    for treeline in qos_tree.get_selected():
        qos=treeline[0]
        break
    
    for portline in port_tree.get_selected():
        portname=portline[0]

        if(qos):
            exec_and_display(['ovs-vsctl','set','port',portname,"qos={}".format(qos)])
        else:
            mywarning("Please select a qos !")
    else:
        return
    
    mywarning("Please select a port !")
    
#---------------------------------------------------------------

def action_qos_port_unset():
    if(debug):mydebug(inspect.currentframe())

    #portname=ui.lineEdit_qos_port.text()
    for portline in port_tree.get_selected():
        portname=portline[0]
        exec_and_display(['ovs-vsctl','clear','port',portname,"qos"])
    else:
        return
    
    mywarning("Please select a port !")

#---------------------------------------------------------------

def action_qos_queue_refresh(output):
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        queue_table.delete_all_rows()

        if(output):
            result=exec_and_display(['ovs-vsctl','--columns=_uuid,dscp,other_config','list','queue'],force_output=True)
        else:
            result=exec_and_display(['ovs-vsctl','--columns=_uuid,dscp,other_config','list','queue'])
            
        process_fields('QUEUE',result)

        queue_table.resize()


#---------------------------------------------------------------

def action_qos_qos_show():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        for portline in port_tree.get_selected():
            portname,interfacename=port_and_interface(portline)
            exec_and_display(['ovs-appctl','qos/show',portname],force_output=True)
#---------------------------------------------------------------

def action_qos_show_stats():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        exec_and_display(['ovs-ofctl','-O',ofproto,'queue-stats',switch],force_output=True)
                             
#---------------------------------------------------------------

def action_qos_qos_show_types():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        for portline in port_tree.get_selected():
            portname,interfacename=port_and_interface(portline)
            exec_and_display(['ovs-appctl','qos/show-types',portname],force_output=True)
    
#---------------------------------------------------------------

def action_qos_porttree_refresh(output):
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        qos_tree.delete_all_rows()

        if(output):
            result=exec_and_display(['ovs-vsctl','--columns=_uuid,queues,type,other_config','list','qos'],force_output=True)
        else:
            result=exec_and_display(['ovs-vsctl','--columns=_uuid,queues,type,other_config','list','qos'])
        process_fields('QOS',result)
#---------------------------------------------------------------

def action_qos_find_ports():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    qos=None
    if(switch):
        for treeline in qos_tree.get_selected():
            qos=treeline[0]
            exec_and_display(['ovs-vsctl','--columns=name','find','port',"qos={}".format(qos)],force_output=True)
            break

    
#---------------------------------------------------------------

def action_qos_qos_refresh(output):
    if(debug):mydebug(inspect.currentframe())

    action_qos_porttree_refresh(output)
    
    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        #qos_table.delete_all_rows()
        if(output):
            result=exec_and_display(['ovs-vsctl','--columns=_uuid,queues,type,other_config','list','qos'],force_output=True)
        else:
            result=exec_and_display(['ovs-vsctl','--columns=_uuid,queues,type,other_config','list','qos'])
        process_fields('QOS',result)

#---------------------------------------------------------------

def qos_tree_fill(widget_mytable,field_name,field_value):
    if(debug):mydebug(inspect.currentframe())

    field_value=pattern_brackets.sub('',field_value)
    field_value=pattern_surrounding_quotes.sub('',field_value)
    
    if(field_name == '_uuid'):
        tree_item=qos_tree.insert(None,field_value)
        qos_tree.last_queue_item=qos_tree.insert(tree_item,'queues')
    else:
        tree_item=qos_tree.getlast_rootitem()
        if(field_name=='queues'):
            queue_dict=string_to_dict(field_value)
            for item,itemvalue in queue_dict.items():
                qos_tree.insert(qos_tree.last_queue_item,"{}={}".format(item,itemvalue))
        else:
            field_name=field_name.replace('other_config:','')
            qos_tree.insert(tree_item,"{}={}".format(field_name,field_value))
            
#---------------------------------------------------------------

def table_fill(widget_mytable,col,field_name,field_value):
    if(debug):mydebug(inspect.currentframe())

    field_value=pattern_brackets.sub('',field_value)
    field_value=pattern_surrounding_quotes.sub('',field_value)
    
    if(field_name == '_uuid'):
        rowpos=widget_mytable.new_row()
    else:
        rowpos=widget_mytable.getlast_rownumber()

    widget_mytable.settext(rowpos,col,field_value)

    widget_mytable.w.update()
    widget_mytable.resize()

#---------------------------------------------------------------

def action_dialog_qos_qos(newqos):
    if(debug):mydebug(inspect.currentframe())

    qos_uuid=None
    setEnableWidgetList(qos_dialog_all,False)
    if(not newqos):
        toplevel_item=qos_tree.get_top_level_parent_of_selected()
        if(toplevel_item):
            clear_widgets('QOS')
            qos_uuid=toplevel_item.text()
            for c in myTree.get_childs(toplevel_item):
                p=pattern_qos_param.match(c)
                if(p):
                    param=p.group(1)
                    param_val=p.group(2)
                    if(param=='type'):
                        comboBox_Write(qqos_ui.comboBox_dialog_qos_qos_type,param_val)
                    elif(param=='perturb'):
                        qqos_ui.lineEdit_dialog_qos_qos_perturb.setText(param_val)
                    elif(param=='quantum'):
                        qqos_ui.lineEdit_dialog_qos_qos_quantum.setText(param_val)
                    elif(param=='max-rate'):
                        qqos_ui.lineEdit_dialog_qos_qos_maxrate.setText(param_val)
                    elif(param=='cir'):
                        qqos_ui.lineEdit_dialog_qos_qos_cir.setText(param_val)
                    elif(param=='cbs'):
                        qqos_ui.lineEdit_dialog_qos_qos_cbs.setText(param_val)
            action_qos_dialog_enable_fields()
        else:
            return

    if(qqos_Dialog.exec()):
        #workaround because ovs-vsctl -- --id=@q1 create queue dscp=[] -- set queue @q1 dscp=10 DOESNT WORK
        if(not qos_uuid):
            result=exec_and_display(['ovs-vsctl','create','qos','type=dummy'])
            for l in result.splitlines():
                pw=pattern_word.match(l)
                if(pw):
                    qos_uuid=pw.group(1)
                    break

        if(qos_uuid):
            mycommand=validate_prepare('ovs-vsctl','QOS','qos')
            mycommand2=array_replace(mycommand,'_VARIABLE_',qos_uuid)

            exec_and_display(mycommand2)
            action_qos_porttree_refresh(False)            


#---------------------------------------------------------------
def action_dialog_qos_edit_queue():
    if(debug):mydebug(inspect.currentframe())

    queue_table_row=queue_table.getcurrent_rownumber()

    if(queue_table_row <0):
        mywarning("Please select a queue in queue table !")
        return

    uuid=queue_table.gettext(queue_table_row,0)

    for n,w in enumerate([qqueue_ui.lineEdit_dialog_qos_queue_minrate,
                qqueue_ui.lineEdit_dialog_qos_queue_maxrate,
                qqueue_ui.lineEdit_dialog_qos_queue_burst,
                qqueue_ui.lineEdit_dialog_qos_queue_priority,
                qqueue_ui.lineEdit_dialog_qos_queue_dscp]):

        w.setText(queue_table.gettext(queue_table_row,n+1))
    
    if(qqueue_Dialog.exec()):
        mycommand=validate_prepare('ovs-vsctl','QUEUE','queue')
        mycommand2=array_replace(mycommand,'_VARIABLE_',uuid)

        exec_and_display(mycommand2)
        action_qos_queue_refresh(False)
    
#---------------------------------------------------------------

def action_dialog_qos_queue():
    if(debug):mydebug(inspect.currentframe())

    if(qqueue_Dialog.exec()):
        result=exec_and_display(['ovs-vsctl','create','queue','dscp=[]'])
        for l in result.splitlines():
            pw=pattern_word.match(l)
            if(pw):
                uuid=pw.group(1)
                mycommand=validate_prepare('ovs-vsctl','QUEUE','queue')
                mycommand2=array_replace(mycommand,'_VARIABLE_',uuid)

                exec_and_display(mycommand2)
                action_qos_queue_refresh(False)
                break
        

#---------------------------------------------------------------        
def action_qos_dialog_enable_fields():
    if(debug):mydebug(inspect.currentframe())

    mode=qqos_ui.comboBox_dialog_qos_qos_type.currentText()
    
    setEnableWidgetList(qos_dialog_all,False)
    
    if(mode=='linux-htb'):
        setEnableWidgetList(qos_dialog_linux_htb,True)
    elif(mode=='linux-hfsc'):
        setEnableWidgetList(qos_dialog_linux_hfsc,True)
    elif(mode=='linux-sfq'):
        setEnableWidgetList(qos_dialog_linux_sfq,True)
    elif(mode=='linux-codel'):
        setEnableWidgetList(qos_dialog_linux_codel,True)
    elif(mode=='linux-fq_codel'):
        setEnableWidgetList(qos_dialog_linux_fq_codel,True)
    elif(mode=='linux-noop'):
        setEnableWidgetList(qos_dialog_linux_noop,True)
    elif(mode=='egress-policer'):
        setEnableWidgetList(qos_dialog_egress_policer,True)

#---------------------------------------------------------------        
#---------------------------------------------------------------
#------------------------ MCAST ---------------------------------
#---------------------------------------------------------------

def action_port_MCAST_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('MCAST_PORT')
    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        if(portname=='_HOST'):
            continue

        result=exec_and_display(['ovs-vsctl','--column=other_config','list','port',portname])
        process_fields('MCAST_PORT',result)

        #stop after first port
        break

#---------------------------------------------------------------

def action_MCAST_port_update():
    if(debug):mydebug(inspect.currentframe())

    validate('ovs-vsctl','MCAST_PORT','Port')
    action_port_MCAST_refresh()

#---------------------------------------------------------------

def action_MCAST_toggle():
    if(debug):mydebug(inspect.currentframe())

    if(ui.comboBox_MCAST_enable.currentText()=='true'):
        setEnableWidgetList([ui.frame_mcast],True)
    else:
        setEnableWidgetList([ui.frame_mcast],False)
#---------------------------------------------------------------
        
def action_MAST_table_show():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(['ovs-appctl','mdb/show',switch],force_output=True)

#---------------------------------------------------------------
        
def action_MCAST_table_flush():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(['ovs-appctl','mdb/flush',switch])

    
#---------------------------------------------------------------

def action_MCAST_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('MCAST')
    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        result=exec_and_display(['ovs-vsctl','list','Bridge',ovs])
        process_fields('MCAST',result)
        action_MCAST_toggle()

#---------------------------------------------------------------

def action_MCAST_validate():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        mycommand=validate_prepare('ovs-vsctl','MCAST','Bridge')
        mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
        exec_and_display(mycommand2)
        action_MCAST_refresh()


#---------------------------------------------------------------
#------------------------ RSTP ---------------------------------
#---------------------------------------------------------------

def action_RSTP_show():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(not ovs): return

    exec_and_display(['ovs-apptctl','rstp/show',ovs],force_output=True)
                            
#---------------------------------------------------------------

def action_port_RSTP_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('PORT-RSTP')
    
    ovs=ui.lineEdit_ovs_name.text()
    if(not ovs): return

    for portline in port_tree.get_selected():
        portname=portline[0]
        if(portname=='_HOST'):
            continue

        
        if(pattern_portname.match(portname)):
            result=exec_and_display(['ovs-vsctl','list','port',portname])
            process_fields('PORT-RSTP',result)


#---------------------------------------------------------------

def action_RSTP_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('RSTP')
    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        result=exec_and_display(['ovs-vsctl','list','Bridge',ovs])
        process_fields('RSTP',result)

        action_RSTP_toggle()
#---------------------------------------------------------------

def action_RSTP_toggle():
    if(debug):mydebug(inspect.currentframe())
    
    if(ui.comboBox_RSTP_enable.currentText()=='true'):
        setEnableWidgetList([ui.frame_RSTP_main,ui.frame_RSTP_status],True)
    else:
        setEnableWidgetList([ui.frame_RSTP_main,ui.frame_RSTP_status],False)

#---------------------------------------------------------------

def action_RSTP_validate():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):

        mycommand=validate_prepare('ovs-vsctl','RSTP','Bridge')
        mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)            
        exec_and_display(mycommand2)
        action_RSTP_refresh()

        
#---------------------------------------------------------------

def action_port_RSTP_validate():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(not ovs):return

    validate('ovs-vsctl','PORT-RSTP','Port')
    action_port_RSTP_refresh()
        
#---------------------------------------------------------------
#------------------------ STP ---------------------------------
#---------------------------------------------------------------

def action_STP_show():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(not ovs): return

    exec_and_display(['ovs-apptctl','stp/show',ovs],force_output=True)

#---------------------------------------------------------------


def action_STP_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('STP')
    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        result=exec_and_display(['ovs-vsctl','list','Bridge',ovs])
        process_fields('STP',result)

        action_STP_toggle()
        
#---------------------------------------------------------------

def action_STP_toggle():
    if(debug):mydebug(inspect.currentframe())

    if(ui.comboBox_STP_enable.currentText()=='true'):
        setEnableWidgetList([ui.frame_STP_main,ui.frame_STP_status],True)
    else:
        setEnableWidgetList([ui.frame_STP_main,ui.frame_STP_status],False)

        
#---------------------------------------------------------------

def action_STP_validate():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):

        mycommand=validate_prepare('ovs-vsctl','STP','Bridge')
        mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)            
        exec_and_display(mycommand2)
        action_STP_refresh()

#---------------------------------------------------------------

def action_port_STP_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('PORT-STP')
    
    ovs=ui.lineEdit_ovs_name.text()
    if(not ovs): return

    for portline in port_tree.get_selected():
        portname=portline[0]
        if(portname=='_HOST'):
            continue

        if(pattern_portname.match(portname)):
            result=exec_and_display(['ovs-vsctl','list','port',portname])
            process_fields('PORT-STP',result)

#---------------------------------------------------------------

def action_port_STP_validate():
    if(debug):mydebug(inspect.currentframe())

    validate('ovs-vsctl','PORT-STP','Port')
    action_port_STP_refresh()

    
                
#---------------------------------------------------------------
#------------------------ NETFLOW ---------------------------------
#---------------------------------------------------------------

def action_netflow_create():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    targets=preprocess_targets(ui.lineEdit_netflow_targets.text())
    
    if(ovs):
        if(targets):
                exec_and_display(['ovs-vsctl','--','set','Bridge',ovs,'netflow=@nf','--','--id=@nf','create','netflow',"targets={}".format(targets)])

                mycommand=validate_prepare('ovs-vsctl','netflow','netflow')
                mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
                exec_and_display(mycommand2)
                
                action_netflow_list(output=False)

        else:
            mywarning("Please specify target !")
    else:
        mywarning("Please select an OvS bridge first !")

#---------------------------------------------------------------

def action_netflow_clear():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        exec_and_display(['ovs-vsctl','clear','Bridge',ovs,'netflow'])
        action_netflow_list(output=False)
    else:
        mywarning("Please select an OvS bridge first !")

#---------------------------------------------------------------

def action_netflow_update():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        mycommand=validate_prepare('ovs-vsctl','netflow','netflow')
        mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
        exec_and_display(mycommand2)
        action_netflow_list(output=False)
    else:
        mywarning("Please select an OvS bridge first !")
    
#---------------------------------------------------------------

def action_netflow_list(**opts):
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        clear_widgets('netflow')
        result0=exec_and_display(['ovs-vsctl','get','Bridge',ovs,'netflow'])
        if(pattern_word.match(result0)):
            if('output' in opts):
                if(opts['output']==True):
                    result=exec_and_display(['ovs-vsctl','list','netflow',ovs],force_output=True)
                else:
                    result=exec_and_display(['ovs-vsctl','list','netflow',ovs])
                
                process_fields('netflow',result)
            
#---------------------------------------------------------------
#------------------------ IPFIX ---------------------------------
#---------------------------------------------------------------

def action_IPFIX_list(**opts):
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        clear_widgets('IPFIX')
        result0=exec_and_display(['ovs-vsctl','get','Bridge',ovs,'ipfix'])
        if(pattern_word.match(result0)):
            if('output' in opts):
                if(opts['output']==True):
                    result=exec_and_display(['ovs-vsctl','list','ipfix',ovs],force_output=True)
                else:
                    result=exec_and_display(['ovs-vsctl','list','ipfix',ovs])

                process_fields('IPFIX',result)

#---------------------------------------------------------------

def action_IPFIX_create():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    
    targets=preprocess_targets(ui.lineEdit_IPFIX_targets.text())
    
    if(ovs):
        if(targets):

            exec_and_display(['ovs-vsctl','--','set','Bridge',ovs,'ipfix=@i','--','--id=@i','create','IPFIX',"targets={}".format(targets)])
            mycommand=validate_prepare('ovs-vsctl','IPFIX','ipfix')
            mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
            exec_and_display(mycommand2)
            
            action_IPFIX_list(output=False)
    else:
        mywarning("Please select an OvS bridge first !")

#---------------------------------------------------------------

def action_IPFIX_update():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()

    if(ovs):
            mycommand=validate_prepare('ovs-vsctl','IPFIX','ipfix')
            mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
            exec_and_display(mycommand2)

            action_IPFIX_list(output=False)
    else:
        mywarning("Please select an OvS bridge first !")

#---------------------------------------------------------------

def action_IPFIX_clear():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        exec_and_display(['ovs-vsctl','clear','Bridge',ovs,'ipfix'])
        action_IPFIX_list(output=False)
    else:
        mywarning("Please select an OvS bridge first !")


#---------------------------------------------------------------
#------------------------ SFLOW ---------------------------------
#---------------------------------------------------------------

def preprocess_targets(text):
    if(text):
        return '_mySPECIALQUOTE_'+text.replace(':','\:')+'_mySPECIALQUOTE_'
    else:
        return ''
#---------------------------------------------------------------

def preprocess_liste(text):
    if(text):
        return pattern_space_comma.sub(',',text)
    else:
        return ''

#---------------------------------------------------------------

def action_sflow_list(**opts):
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        clear_widgets('sflow')
        result0=exec_and_display(['ovs-vsctl','get','Bridge',ovs,'sflow'])
        if(pattern_word.match(result0)):
            if('output' in opts):
                if(opts['output']==True):
                    result=exec_and_display(['ovs-vsctl','list','sflow',ovs],force_output=True)
                else:
                    result=exec_and_display(['ovs-vsctl','list','sflow',ovs])

                process_fields('sflow',result)

#---------------------------------------------------------------

def action_sflow_create():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    targets=preprocess_targets(ui.lineEdit_sflow_targets.text())
    
    if(ovs):
        if(targets):

            exec_and_display(['ovs-vsctl','--','--id=@s','create','sflow',"target={}".format(targets),'--','set','Bridge',ovs,'sflow=@s'])            

            mycommand=validate_prepare('ovs-vsctl','sflow','sflow')
            mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
            exec_and_display(mycommand2)

            action_sflow_list(output=False)
        else:
            mywarning("Please fill targets !")
    else:
        mywarning("Please select an OvS bridge first !")

#---------------------------------------------------------------

def action_sflow_update():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()

    if(ovs):
            mycommand=validate_prepare('ovs-vsctl','sflow','sflow')
            mycommand2=array_replace(mycommand,'_VARIABLE_',ovs)
            exec_and_display(mycommand2)
    else:
        mywarning("Please select an OvS bridge first !")

#---------------------------------------------------------------

def action_sflow_clear():
    if(debug):mydebug(inspect.currentframe())

    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        exec_and_display(['ovs-vsctl','clear','Bridge',ovs,'sFlow'])
        action_sflow_list(output=False)
    else:
        mywarning("Please select an OvS bridge first !")

#---------------------------------------------------------------
#------------------------ KVM ---------------------------------
#---------------------------------------------------------------


def action_kvm_virt_net_fill():
    if(debug):mydebug(inspect.currentframe())

    mode=vn_ui.comboBox_dialog_kvm_virt_device.currentText()
    setEnableWidgetList(vn_all_list,False)

    #clear all
    LineEdit_Write(vn_ui.lineEdit_dialog_kvm_virt_bridge,'')
    LineEdit_Write(vn_ui.lineEdit_dialog_kvm_virt_network,'')
    LineEdit_Write(vn_ui.lineEdit_dialog_kvm_virt_target,'')
    comboBox_Clear(vn_ui.comboBox_dialog_kvm_virt_model)
    comboBox_Clear(vn_ui.comboBox_dialog_kvm_virt_virtualport)

    if(mode == 'openvswitch bridge'):
        LineEdit_Write(vn_ui.lineEdit_dialog_kvm_virt_bridge,LineEdit_Read(ui.lineEdit_ovs_name))
        comboBox_Write(vn_ui.comboBox_dialog_kvm_virt_model,'virtio')
        comboBox_Write(vn_ui.comboBox_dialog_kvm_virt_virtualport,'openvswitch')
        setEnableWidgetList(vn_ovs_list,True)
    elif(mode == 'kvm network with portgroups'):
        setEnableWidgetList(vn_kvm_portgroup_list,True)
    elif(mode == 'linux bridge'):
        setEnableWidgetList(vn_kvm_linux_bridge_list,True)

#---------------------------------------------------------------
        
def kvm_virt_disk_create(filename,fmt,size):
    if(debug):mydebug(inspect.currentframe())

    if(not filename):
        mywarning(' Missing filename for disk !!! ')
        return False

    result=exec_and_display(['ls','-d',filename])
    for line in result.splitlines():
        mywarning('File disk already exists !')
        return False
        
    if(not size):
        mywarning('A disk file is needed !')
        return False
            
    if(not fmt):
        mywarning('A disk format is needed !  ( qcow2, vdi, etc.. ) ')
        return False
    mywarning("I am going to create a new disk {} size {}\n\n Press OK and wait until you see the next popup message".format(filename,size))

    exec_and_display(['qemu-img','create','-f',fmt,filename,size])

    result=exec_and_display(['ls','-d',filename])
    for line in result.splitlines():
        mywarning(' Operation completed !')
        break
    else:
        mywarning(' Could not find created disk ! Verify your disk path !')
        return False

#---------------------------------------------------------------

def action_dialog_kvm_virt_disk():
    if(debug):mydebug(inspect.currentframe())

    mgmt=ui.lineEdit_ovs_profile.text()
    if(not mgmt):
        mywarning("First select a management profile in order to tell on which host is kvm running and with what credentials you can access it")
        return

    if(vd_Dialog.exec()):
        if(vd_ui.comboBox_dialog_kvm_virt_disk_device.currentText()=='Select device'):
            mywarning('Please select device type !')
            return

        if(not vd_ui.lineEdit_dialog_kvm_virt_disk_path):
            mywarning('Please enter a device path !')
            return
        
        filename=vd_ui.lineEdit_dialog_kvm_virt_disk_path.text()
        fmt=vd_ui.comboBox_dialog_kvm_virt_disk_format.currentText()
        size=vd_ui.lineEdit_dialog_kvm_virt_disk_size.text()
        
        if(vd_ui.checkBox_dialog_kvm_virt_disk_new.isChecked()):
            print("Disk creation is asked")
            if(kvm_virt_disk_create(filename,fmt,size)==False): return
        else:
            print("Disk creation isnt asked")
        
        rowpos=kvm_virt_disk_table.new_row()
        for index,text in enumerate([
                filename,
                fmt,
                vd_ui.comboBox_dialog_kvm_virt_disk_device.currentText(),
                vd_ui.comboBox_dialog_kvm_virt_disk_bus.currentText(),
                vd_ui.comboBox_dialog_kvm_virt_disk_cache.currentText(),
                vd_ui.comboBox_dialog_kvm_virt_disk_io.currentText()
        ]):
            kvm_virt_disk_table.settext(rowpos,index,text)
            
#---------------------------------------------------------------

def action_dialog_kvm_virt_net():
    if(debug):mydebug(inspect.currentframe())

    if(vn_Dialog.exec()):
        if(vn_ui.comboBox_dialog_kvm_virt_device.currentText()=='Select mode'):
            return
        rowpos=kvm_virt_net_table.new_row()
        for index,text in enumerate([
                vn_ui.lineEdit_dialog_kvm_virt_bridge.text(),
                vn_ui.lineEdit_dialog_kvm_virt_network.text(),
                vn_ui.comboBox_dialog_kvm_virt_model.currentText(),
                vn_ui.comboBox_dialog_kvm_virt_virtualport.currentText(),
                vn_ui.lineEdit_dialog_kvm_virt_target.text()
        ]):
            kvm_virt_net_table.settext(rowpos,index,text)

#---------------------------------------------------------------

def action_kvm_virt_run():
    if(debug):mydebug(inspect.currentframe())

    
    mgmt=ui.lineEdit_ovs_profile.text()
    if(not mgmt):
        mywarning("First select a management profile in order to tell on which host is kvm running and with what credentials you can access it")
        return

    run_cmd=['virt-install']

    #lineedit section
    for option in ('--name','--ram','--vcpu'):
        option_val=LineEdit_Read(kvm_virt_mapping[option])
        mw=pattern_word.match(option_val)
        if(mw):
            run_cmd.extend([option,mw.group(1)])
        else:
            mywarning("Cant find value for "+option)
            return

    for l in kvm_virt_disk_table.get_tabletext():
        run_cmd.extend(['--disk', ','.join(l)])

    for l in kvm_virt_net_table.get_tabletext():
        run_cmd.extend(['--network', ','.join(l)])
        

    #misc_section
    for r in range(0,kvm_virt_misc_table.w.rowCount()):
        row=kvm_virt_misc_table.get_rowtext(r)
        if(row[1]):
            run_cmd.extend(["--"+row[0],row[1]])
        else:
            run_cmd.extend(["--"+row[0]])

    run_cmd.extend(["--noautoconsole"])
    print(run_cmd)
    exec_and_display(run_cmd)


#---------------------------------------------------------------

def action_save_kvm_xml_file():
    if(debug):mydebug(inspect.currentframe())

    net=kvm_net_list.get()

    if(net):
        filename=kvmNetDir.save('Save kvm network to xml file',parent_ui=ui.pushButton_kvm_net_save)
        if(filename):
            result=exec_and_display(['virsh','net-dumpxml',net],lang_c=True)
            filename_handler = open(filename,'w')
            print("Saving filename:",filename)
            if(filename_handler):
                for line in result.splitlines():
                    #stripping uuid section from xml
                    if(pattern_net_uuid.match(line)):
                        pass
                    else:
                        filename_handler.write(line+"\n")

                filename_handler.close()

            else:
                mywarning("Cannot write "+filename+" !!!")

#---------------------------------------------------------------

def action_kvm_iso_gen():
    if(debug):mydebug(inspect.currentframe())

    if(iso_Dialog.exec()):
        srcdir=iso_ui.lineEdit_dialog_kvm_iso_srcdir.text()
        dstfile=iso_ui.lineEdit_dialog_kvm_iso_dstfile.text()

        if(not srcdir):
            mywarning('Please provide a source directory !')
            return
        if(not dstfile):
            mywarning('Please provide a filename for the new iso file !')
            return
            
        exec_and_display(['mkisofs','-r','-o',dstfile,srcdir])

#---------------------------------------------------------------

def action_select_kvm_xml_file():
    if(debug):mydebug(inspect.currentframe())

    filename=kvmNetDir.browse('Select xml file for new kvm network',parent_ui=ui.pushButton_kvm_net_load)
    if(filename):

        retval=myconfirm('YesNo',"Do you want this network to be persistent ?")
        if(retval):
            exec_and_display(['virsh','net-define',filename],lang_c=True)
        else:
            exec_and_display(['virsh','net-create',filename],lang_c=True)
        action_kvm_net_list()

#---------------------------------------------------------------

@myJsonImport(kvmParamsDir,'Load KVM virt-install params from file',ui.pushButton_kvm_virt_import)
def action_kvm_virt_import(**opts):
    if(debug):mydebug(inspect.currentframe())

    json_txt=opts['json']
    
    action_kvm_virt_clear()
    
    for kvmbloc in json_txt:
        ui.lineEdit_kvm_virt_ram.setText(kvmbloc.get('ram',''))
        ui.lineEdit_kvm_virt_vcpu.setText(kvmbloc.get('vcpu',''))

        for d in kvmbloc['disk']:
            rowpos=kvm_virt_disk_table.new_row()
            for col,text in enumerate(d):
                kvm_virt_disk_table.settext(rowpos,col,text)

        for n in kvmbloc['net']:
            rowpos=kvm_virt_net_table.new_row()
            for col,text in enumerate(n):
                kvm_virt_net_table.settext(rowpos,col,text)
            
        for m in kvmbloc['misc']:
            rowpos=kvm_virt_misc_table.new_row()
            for col,text in enumerate(m):
                kvm_virt_misc_table.settext(rowpos,col,text)
                
        break
        
#---------------------------------------------------------------
@myJsonExport(kvmParamsDir,'Save KVM virt-install params to file',ui.pushButton_kvm_virt_export)
def action_kvm_virt_export():
    if(debug):mydebug(inspect.currentframe())

    d={'ram':ui.lineEdit_kvm_virt_ram.text(),
       'vcpu':ui.lineEdit_kvm_virt_vcpu.text(),
    }

    #disk
    d['disk']=kvm_virt_disk_table.get_allrowtext()
        
    #network
    d['net']=kvm_virt_net_table.get_allrowtext()
        
    #misc
    d['misc']=kvm_virt_misc_table.get_allrowtext()
        
    liste=[d]
      
    return liste
#---------------------------------------------------------------
def action_kvm_virt_clear():
    if(debug):mydebug(inspect.currentframe())

    ui.lineEdit_kvm_virt_ram.setText('')
    ui.lineEdit_kvm_virt_vcpu.setText(''),


    #disk
    kvm_virt_disk_table.delete_all_rows()
        
    #network
    kvm_virt_net_table.delete_all_rows()
        
    #misc
    kvm_virt_misc_table.delete_all_rows()

#---------------------------------------------------------------
#------------------------ HOST ---------------------------------
#---------------------------------------------------------------

def action_selectssh():
    if(debug):mydebug(inspect.currentframe())

    filename=sshDir.browse('Select your ssh public key',parent_ui=mgmt_ui.pushButton_selectssh)
    LineEdit_Write(mgmt_ui.lineEdit_mgmt_ssh_id,filename)

#---------------------------------------------------------------

def action_findovs(lineedit_widget):
    if(debug):mydebug(inspect.currentframe())

    result=exec_and_display(['ovs-vsctl','--column=name','list','br'])
    items=[]
    #print ("result=",result)
    if(not result):
        clear_profile_bar()
        return
        
    for line in result.splitlines():
        m=pattern_name.match(line)
        if(m):
            items.append(m.group(1))

    if(items):
        item, ok = QInputDialog.getItem(ui.pushButton_findovs,"OvS selector","Select OvS:", items, 0, False)
        if ok and item:
            LineEdit_Write(lineedit_widget,item)
            action_port_filter()
    else:
        clear_profile_bar()
            
#---------------------------------------------------------------

def action_port_filter():

    if(debug):mydebug(inspect.currentframe())

    ui.lineEdit_port.setText('')
    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        l=[]
        #portlist.clear()
        #port_table.delete_all_rows()
        port_tree.delete_all_rows()
        
        port_clear_fields()

        ui.lineEdit_port_filter.clearFocus()

        pattern_filter=re.compile(LineEdit_Read(ui.lineEdit_port_filter))
        result=exec_and_display(['ovs-vsctl','list-ports',LineEdit_Read(ui.lineEdit_ovs_name)],hide_output=True)
        for line in result.splitlines():
            m=pattern_filter.search(line)
            if(m):
                l.append(line.rstrip("\n"))
                #portlist.addlist([line])

        myInterface.refresh()
        myPort.refresh(l)

        for port in l:
            item=port_tree.insert(None,port)
            interfaces=myPort.get(port).interfaces

            for i in interfaces:
                port_tree.insert(item,myInterface.getname(i))

        setEnableWidgetList(ports_widget_list,False)

        if(ui.checkBox_host_interface.isChecked()):
            pattern_filter_host=re.compile(ui.lineEdit_host_inf_filter.text())
            result=exec_and_display(['ip','-br','link'],hide_output=True)
            item_host=port_tree.insert(None,'_HOST')
            for line in result.splitlines():
                mifh=pattern_filter_host.search(line)
                if(mifh):
                    pipl=pattern_iplink.search(line)
                    if(pipl):
                        port_tree.insert(item_host,pipl.group(1))
        
#---------------------------------------------------------------

def action_port_add():
    if(debug):mydebug(inspect.currentframe())

    portname=LineEdit_Read(ui.lineEdit_port)
    if(pattern_portname.match(portname)):
        mycommand=['ovs-vsctl','add-port',ui.lineEdit_ovs_name.text(),portname]
        of_request=ui.lineEdit_of_request.text()
        
        if(pattern_number.match(of_request)):
            mycommand.extend(['--','set','Interface',portname,"ofport_request={}".format(of_request)])
        exec_and_display(mycommand)

        action_port_filter()

#---------------------------------------------------------------
def port_clear_fields():
    if(debug):mydebug(inspect.currentframe())

    for w in (ui.lineEdit_vlan_access,
              ui.lineEdit_vlan_trunk,
              ui.lineEdit_ingress_rate,
              ui.lineEdit_ingress_burst):
        LineEdit_Clear(w)

    for w in (ui.comboBox_vlan_mode,
              ui.comboBox_type):
        w.setCurrentIndex(0)

#---------------------------------------------------------------
def setEnableWidgetDic(categ,subcateg,state):
    if(debug):mydebug(inspect.currentframe())

    if(subcateg=='ALL'):
        l=wenable_dic[categ]['ALL'].values()
    else:
        l=[wenable_dic[categ]['ALL'][x] for x in wenable_dic[categ][subcateg]]

    setEnableWidgetList(l,state)
        
#---------------------------------------------------------------
def setEnableWidgetList(l,state,**opts):
    if(debug):mydebug(inspect.currentframe())

    if('testcheckbox' in opts):
        if(not opts['testcheckbox'].isChecked()):
            state = not state
            
    for w in l:
        w.setEnabled(state)

    refresh_stylesheet(l)

#---------------------------------------------------------------
def list_port_select():
    #global old_selected_port_row

    if(debug):mydebug(inspect.currentframe())

    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        setEnableWidgetList(ports_widget_list,True)
        tabs_port_changed()
        ui.lineEdit_port.setText(interfacename)
        break
#---------------------------------------------------------------

def action_port_del():
    global old_selected_port_row

    if(debug):mydebug(inspect.currentframe())

    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)

        if(portname == '_HOST'):
                exec_and_display(['ip','link','delete',interfacename])
        else:
            if(pattern_portname.match(portname)):
                exec_and_display(['ovs-vsctl','del-port',LineEdit_Read(ui.lineEdit_ovs_name),portname])
                old_selected_port_row=-1
                #action_port_filter()
                
                
    action_port_filter()
    port_clear_fields()
#---------------------------------------------------------------

def if_close():

    if(debug):mydebug(inspect.currentframe())

    action_timer_define(timer_interfacelist,0)
    if_ui.comboBox_if_ar.setCurrentIndex(0)
    if_Dialog.setVisible(False)

#---------------------------------------------------------------

def pt_close():

    if(debug):mydebug(inspect.currentframe())

    action_timer_define(timer_portlist,0)
    pt_ui.comboBox_pt_ar.setCurrentIndex(0)
    pt_Dialog.setVisible(False)

#---------------------------------------------------------------

def action_about(text_type,**opts):
    if(debug):mydebug(inspect.currentframe())

    about_ui.plainTextEdit_about.clear()
    if(text_type in legal):
        plaintext_print(about_ui.plainTextEdit_about,legal[text_type])
    else:
        plaintext_print(about_ui.plainTextEdit_about,opts['text'])

    about_Dialog.exec_()


    
#---------------------------------------------------------------

def about_versions():
    if(debug):mydebug(inspect.currentframe())
    
    text="Python version: {}\n\nQt version:  {}\nSIP version:  {}\nPyQt version:  {}\n\n".format(platform.python_version(),QT_VERSION_STR,SIP_VERSION_STR,PYQT_VERSION_STR)

    result=exec_and_display(['pip3','show','lxml','paramiko'],force_mgmt_nickname='_dot_mgmt')

    text=text+result    

    action_about('other',text=text)
    

#---------------------------------------------------------------

def ovs_close():

    if(debug):mydebug(inspect.currentframe())

    if_close()
    pt_close()

    for w in extended_dialog_list:
        print("Calling close on:",w)
        w.close()
        
    MainWindow.close()
    
#---------------------------------------------------------------
#------------------------- KVM ---------------------------------
#---------------------------------------------------------------


def kvm_pg_gen_xml(pgname):
    if(debug):mydebug(inspect.currentframe())

    vlan=LineEdit_Read(pg_ui.lineEdit_kvm_pg_tags)

    if(pg_ui.checkBox_kvm_pg.isChecked()):
        vlan_code="<portgroup name='{}' default='yes'>".format(pgname)
    else:
        vlan_code="<portgroup name='{}'>".format(pgname)

    vlanmode=pg_ui.comboBox_dialog_kvm_pg_mode.currentText()

    if(vlanmode=='none'):
        pass
    elif(vlanmode=='vlan'):
        pvlan=pattern_vlan.match(vlan)
        if(pvlan):
            if(pvlan.group(2)=='u'):
                vlan_code+="<vlan><tag id='{}' nativeMode='untagged'/></vlan>".format(vlan)
            elif(pvlan.group(2)=='t'):
                vlan_code+="<vlan><tag id='{}' nativeMode='tagged'/></vlan>".format(vlan)
            else:
                vlan_code+="<vlan><tag id='{}'/></vlan>".format(vlan)
        else:
            mywarning("Invalid tag")
            return None
    elif(vlanmode=='trunk'):
        vlan_code+="<vlan trunk='yes'>"
        for v in vlan.split(','):

            pvlan=pattern_vlan.match(v)
            if(pvlan):
                if(pvlan.group(2)=='u'):
                    vlan_code+="<tag id='{}' nativeMode='untagged'/>".format(pvlan.group(1))
                elif(pvlan.group(2)=='t'):
                    vlan_code+="<tag id='{}' nativeMode='tagged'/>".format(pvlan.group(1))
                else:
                    vlan_code+="<tag id='{}'/>".format(pvlan.group(1))

        vlan_code+='</vlan>'

    vlan_code+="</portgroup>"

    vlan_code='_mySPECIALQUOTE_'+vlan_code+'_mySPECIALQUOTE_'

    print("VLAN_CODE=",vlan_code)

    return(vlan_code)

#---------------------------------------------------------------

def action_kvm_pg_create():
    if(debug):mydebug(inspect.currentframe())

    clear_kvm_pg_widgets()
    if(pg_Dialog.exec()):
        net=kvm_net_list.get()
        pd=LineEdit_Read(pg_ui.lineEdit_dialog_kvm_pg_name)

        pgm=pattern_pgname.match(pd)
        if(net):
            if(pgm):
                vlan_code=kvm_pg_gen_xml(pgm.group(1))

                if(vlan_code):
                    (net_active,net_persistent)=action_kvm_net_getinfo(net)
                    if(net_active=='no'):
                        exec_and_display(['virsh','net-update','--network', net,'add-last','portgroup','--xml',vlan_code,"--config"])
                    else:
                        exec_and_display(['virsh','net-update','--network', net,'add-last','portgroup','--xml',vlan_code,"--live"])
                        
                    refresh_kvm_pg_list(net)

#---------------------------------------------------------------

def clear_kvm_pg_widgets():
    if(debug):mydebug(inspect.currentframe())



    pg_ui.lineEdit_dialog_kvm_pg_name.setText('')
    pg_ui.lineEdit_kvm_pg_tags.setText('')
    pg_ui.checkBox_kvm_pg.setChecked(False)
    pg_ui.comboBox_dialog_kvm_pg_mode.setCurrentIndex(0)

#---------------------------------------------------------------

def action_kvm_pg_edit():
    if(debug):mydebug(inspect.currentframe())

    net=kvm_net_list.get()
    if(net):
        portgroup_name=kvm_pg_table.getcurrenttext(0)
        pg_ui.lineEdit_dialog_kvm_pg_name.setText(portgroup_name)
        pg_ui.lineEdit_kvm_pg_tags.setText(kvm_pg_table.getcurrenttext(3))

        if(kvm_pg_table.getcurrenttext(1)=='yes'):
            pg_ui.checkBox_kvm_pg.setChecked(True)
        else:
            pg_ui.checkBox_kvm_pg.setChecked(False)

        if(kvm_pg_table.getcurrenttext(2)=='trunk'):
            comboBox_Write(pg_ui.comboBox_dialog_kvm_pg_mode,'trunk')
        else:
            comboBox_Write(pg_ui.comboBox_dialog_kvm_pg_mode,'vlan')

        if(pg_Dialog.exec()):
            vlan_code=kvm_pg_gen_xml(portgroup_name)
            (net_active,net_persistent)=action_kvm_net_getinfo(net)
            if(net_active=='no'):
                exec_and_display(['virsh','net-update','--network', net,'modify','portgroup','--xml',vlan_code,"--config"])
            else:
                exec_and_display(['virsh','net-update','--network', net,'modify','portgroup','--xml',vlan_code,"--live"])
                        
            refresh_kvm_pg_list(net)

#---------------------------------------------------------------

def action_kvm_pg_delete():
    if(debug):mydebug(inspect.currentframe())

    net=kvm_net_list.get()
    pg=kvm_pg_table.getcurrenttext(0)
    if(net):
        if(pg):
            exec_and_display(['virsh','net-update','--network', net,'delete','portgroup','--xml',"_mySPECIALQUOTE_<portgroup name=\'{}\'></portgroup>_mySPECIALQUOTE_".format(pg)],lang_c=True)

        refresh_kvm_pg_list(net)

#---------------------------------------------------------------

#def action_kvm_pg_select():
#    if(debug):mydebug(inspect.currentframe())
#
#    mywarning("Cette fonction est elle lue ? kvm_pg_list n existe pas !!")
#
#    net=kvm_net_list.get()
#    pg=kvm_pg_list.get()
#
#    listetag=[]
#
#    xmlresult=exec_and_display(['virsh','net-dumpxml',net],lang_c=True)
#    #http://apprendre-python.com/page-xml-python-xpath
#
#    root=etree.XML(xmlresult)
#    for pgval in root.xpath("/network/portgroup[@name='{}']/vlan/tag".format(pg)):
#        tag_id=pgval.get('id')
#        tag_native=pgval.get('nativeMode')
#        if(tag_native == 'tagged'):
#            listetag.append(pgval.get('id') + 't')
#        elif(tag_native == 'untagged'):
#            listetag.append(pgval.get('id') + 'u')
#        else:
#            listetag.append(pgval.get('id'))
#
#    LineEdit_Write(ui.lineEdit_kvm_pg_tags,','.join(listetag))
#---------------------------------------------------------------

def action_kvm_net_start():

    if(debug):mydebug(inspect.currentframe())

    net=kvm_net_list.get()
    if(net):
        exec_and_display(['virsh','net-start',net],lang_c=True)
        action_kvm_net_list()
#---------------------------------------------------------------

def action_kvm_net_destroy():

    if(debug):mydebug(inspect.currentframe())

    net=kvm_net_list.get()
    if(net):
        (net_active,net_persistent)=action_kvm_net_getinfo(net)
        if(net_persistent=='yes'):
            exec_and_display(['virsh','net-destroy',net],lang_c=True)
            action_kvm_net_list()
        else:
            retval=myconfirm('YesCancel',"Stopping a non-persistent network will destroy it ! Proceed anyway ? ")
            if(retval):
                exec_and_display(['virsh','net-destroy',net],lang_c=True)
                action_kvm_net_list()


#---------------------------------------------------------------

def action_kvm_net_undefine():

    if(debug):mydebug(inspect.currentframe())

    net=kvm_net_list.get()
    if(net):
        (net_active,net_persistent)=action_kvm_net_getinfo(net)
        if(net_persistent=='yes'):
            exec_and_display(['virsh','net-undefine',net],lang_c=True)
            action_kvm_net_list()
        else:
            mywarning("Cannot undefine non-persistent network ! Use stop instead !")

#---------------------------------------------------------------

def action_kvm_net_dumpxml():

    if(debug):mydebug(inspect.currentframe())

    net=kvm_net_list.get()
    if(net):
        exec_and_display(['virsh','net-dumpxml',net],lang_c=True,force_output=True)

#---------------------------------------------------------------

def action_kvm_net_select():

    if(debug):mydebug(inspect.currentframe())

    net=kvm_net_list.get()
    action_kvm_net_getinfo(net)
    refresh_kvm_pg_list(net)

#---------------------------------------------------------------

def action_kvm_net_getinfo(net):

    if(debug):mydebug(inspect.currentframe())

    result=exec_and_display(['virsh','net-info',net],lang_c=True)
    for line in result.splitlines():
        pline=pattern_if_field.match(line)
        if(pline):
            field_name,field_value=pline.group(1),pline.group(2)
            if(field_name == 'Name'):
                LineEdit_Write(ui.lineEdit_kvm_net,field_value)

            else:
                try:
                    name2label_mapping[field_name].setText(field_value)
                except:
                    print("unknown field:",field_name)
                    
                if(field_name=='Active'):
                    net_active=field_value
                elif(field_name=='Persistent'):
                    net_persistent=field_value
    return(net_active,net_persistent)

#---------------------------------------------------------------

def refresh_kvm_pg_list(net):

    if(debug):mydebug(inspect.currentframe())

    kvm_pg_table.delete_all_rows()
    clear_kvm_pg_widgets()

    xmlresult=exec_and_display(['virsh','net-dumpxml',net],lang_c=True)
    switch_type='none'
    root=etree.XML(xmlresult)
    for vp in root.xpath("/network/virtualport"):
        switch_type=vp.get('type')

    if(switch_type == 'openvswitch'):
        for pg in root.xpath("/network/portgroup"):
            row=kvm_pg_table.new_row()
            portgroup_name=pg.get('name')
            kvm_pg_table.settext(row,0,portgroup_name)
            portgroup_default=pg.get('default')
            if(portgroup_default):
                kvm_pg_table.settext(row,1,'yes')
            else:
                kvm_pg_table.settext(row,1,'no')

            listetag=[]
            print("portgroup_name=",portgroup_name)
            for vlan_item in root.xpath("/network/portgroup[@name='{}']/vlan".format(portgroup_name)):
                vlantype=vlan_item.get('trunk')
                print("vlan type=",vlantype)
                for child in vlan_item:
                    tag_id=child.get('id')
                    tag_native=child.get('nativeMode')
                    if(tag_native == 'tagged'):
                        listetag.append(tag_id + 't')
                    elif(tag_native == 'untagged'):
                        listetag.append(tag_id + 'u')
                    else:
                        listetag.append(tag_id)

                if(vlantype=='yes'):
                    kvm_pg_table.settext(row,2,'trunk')
                else:
                    kvm_pg_table.settext(row,2,'')

                kvm_pg_table.settext(row,3,','.join(listetag))


        #degriser tous les boutons net et pg
        setEnableWidgetList(kvmwidgetlist,True)
    else:
        setEnableWidgetList(kvmwidgetlist,False)
        #griser tous les boutons net et pg

    ui.label_kvm_net_virtualport.setText(switch_type)


#---------------------------------------------------------------

def action_kvm_net_list():

    if(debug):mydebug(inspect.currentframe())
    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        kvm_net_list.clear()

        setEnableWidgetList(kvmwidgetlist,False)

        result=exec_and_display(['virsh','net-list','--name','--all'])
        for line in result.splitlines():
            pn=pattern_net.match(line)
            if(pn):
                kvm_net_list.addlist([pn.group(1)])

#---------------------------------------------------------------


def action_kvm_net_create(persistent):

    if(debug):mydebug(inspect.currentframe())

    name=LineEdit_Read(ui.lineEdit_kvm_net)
    pn=pattern_net.match(name)
    if(pn):
        with tempfile.NamedTemporaryFile(prefix='ovs',delete=False) as fp:
            ovs=LineEdit_Read(ui.lineEdit_ovs_name)
            if(ovs):
                xml="<network><name>{}</name><forward mode=\'bridge\'/><bridge name=\'{}\'/><virtualport type=\'openvswitch\'></virtualport></network>\n".format(name,ovs)
                fp.write(xml.encode())
                fp.close()
                if(persistent):
                    result=exec_and_display(['virsh','net-define',fp.name])
                else:
                    result=exec_and_display(['virsh','net-create',fp.name])
                os.unlink(fp.name)
                action_kvm_net_list()
            else:
                mywarning("What is current ovs ?")
    else:
        mywarning("Please specify a kvm network name !")

#---------------------------------------------------------------

def action_port_list():

    if(debug):mydebug(inspect.currentframe())

    firsttime=True

    pt_Dialog.close()
    for portline in port_tree.get_selected():

        portname=portline[0]
        pt_Dialog.setWindowTitle("Port: {}".format(portname))

        if(pattern_portname.match(portname)):
            result=exec_and_display(['ovs-vsctl','list','port',portname])
            for line in result.splitlines():
                if(firsttime):pt_Dialog.show()
                firsttime=False

                mpt_field=pattern_if_field.match(line)
                if(mpt_field):
                    pt_field=mpt_field.group(1)
                    pt_value=mpt_field.group(2)
                    try:
                        le=getattr(pt_ui, "lineEdit_pt_{}".format(pt_field))
                    except AttributeError:
                        mywarning("Cant find attr {}".format(pt_field))
                    else:
                        LineEdit_Write(le,pt_value)
                        
        # only want the first one if multiselection
        break
#---------------------------------------------------------------

def action_timer_define(timer_name,delay):
    if(debug):mydebug(inspect.currentframe())



    if(delay>0):
        print("Setting timer {} to {}".format(timer_name,delay))
        timer_name.start(delay)
    else:
        print("Stopping timer {}".format(timer_name))
        timer_name.stop()

#---------------------------------------------------------------
#-------------------------- MOD PORT ----------------------------
#---------------------------------------------------------------


#---------------------------------------------------------------

def action_mod_port(action):
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        ofproto=Mymgmt.get_current_profile_attr('force_of')
        for portline in port_tree.get_selected():
            portname,interfacename=port_and_interface(portline)
            exec_and_display(['ovs-ofctl','-O',ofproto,'mod-port',switch,interfacename,action])

        action_interface_refresh()
            
#---------------------------------------------------------------
#-------------------------- MIRRORS ----------------------------
#---------------------------------------------------------------

def uuid2port_gen():

    port_dict={}
    
    result_ports=exec_and_display(['ovs-vsctl','--column=_uuid,name','list','port'])
    for line in result_ports.splitlines():
        pf=pattern_field.match(line)
        if(pf):
            field=pf.group(1)
            field_val=pf.group(2).rstrip("\n")
            if(field=='_uuid'):
                uuid=field_val
            elif(field=='name'):
                port_dict[uuid]=field_val.replace('"','')

    return port_dict

#---------------------------------------------------------------

def convert_uuid2ports(field_name,field_value,widget_list,list_type):
    if(debug):mydebug(inspect.currentframe())

    port_list=[]
    field_value=field_value.rstrip("\n")

    uuid2port=uuid2port_gen()

    uuid_list=pattern_space_comma.split(field_value)
    for uuid in uuid_list:
        if(uuid in uuid2port):
            port_list.append(uuid2port[uuid])
    
    return ",".join(port_list)

#---------------------------------------------------------------

def action_mirror_select():
    if(debug):mydebug(inspect.currentframe())

    name=mirror_table.getcurrenttext(0)
    clear_widgets('MIRROR')
    
    result=exec_and_display(['ovs-vsctl','--column=name,output_port,output_vlan,select_all,select_dst_port,select_src_port,select_vlan,snaplen','find','mirror',"name={}".format(name)])
    process_fields('MIRROR',result)

    if(ui.lineEdit_mirror_output_vlan.text()):
        ui.radioButton_mirror_output_vlan.setChecked(True)
    else:
        ui.radioButton_mirror_output_port.setChecked(True)
    
#---------------------------------------------------------------

def action_mirror_add():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    mirrorname=ui.lineEdit_mirror_name.text()
    output_port=ui.lineEdit_mirror_output_port.text()
    output_vlan=ui.lineEdit_mirror_output_vlan.text()
    select_src=preprocess_liste(ui.lineEdit_mirror_select_src.text())
    select_dst=preprocess_liste(ui.lineEdit_mirror_select_dst.text())
    select_vlan=preprocess_liste(ui.lineEdit_mirror_select_vlans.text())
    snaplen=ui.lineEdit_mirror_snaplen.text()

    select_src_port_list=[]
    select_dst_port_list=[]
    output_port_list=[]
    port_list=[]
        
    if(switch):
        #'set mirrors=uuid' will replace mirror list by new mirror whereas 'add mirror uuid' will append to the mirror list
        mycommand=['ovs-vsctl','add','Bridge',switch,'mirrors','@m']
        if(mirrorname):
            for outputport in pattern_space_comma.split(output_port):
                if(pattern_portname.match(output_port)):

                    output_port_list.append("@{}".format(outputport))
                    port_list.append(outputport)
                    
            if(not ui.checkBox_mirror_select_all.isChecked()):

                for srcport in pattern_space_comma.split(select_src):
                    if(pattern_portname.match(srcport)):

                        select_src_port_list.append("@{}".format(srcport))
                        port_list.append(srcport)
                        
                for dstport in pattern_space_comma.split(select_dst):
                    if(pattern_portname.match(dstport)):

                        select_dst_port_list.append("@{}".format(dstport))
                        port_list.append(dstport)

            #duplicates are not tolerated, we remove them with "set"
            for port in list(set(port_list)):
                mycommand.extend(['--',"--id=@{}".format(port),'get','Port', port])


            if(ui.checkBox_mirror_select_all.isChecked()):
                mycommand.extend(['--','--id=@m','create','Mirror',"name={}".format(mirrorname),'select_all=true'])
            else:
                mycommand.extend(['--','--id=@m','create','Mirror',"name={}".format(mirrorname),'select_all=false'])

                if(select_dst_port_list):
                    mycommand.extend(["select-dst-port={}".format(",".join(select_dst_port_list))])
                if(select_src_port_list):
                    mycommand.extend(["select-src-port={}".format(",".join(select_src_port_list))])

            if(select_vlan):
                mycommand.extend(["select_vlan={}".format(select_vlan)])

            if(snaplen):
                mycommand.extend(["snaplen={}".format(snaplen)])
                    
            if(ui.radioButton_mirror_output_port.isChecked()):
                    mycommand.extend(["output-port={}".format(",".join(output_port_list))])
            else:
                mycommand.extend(["output-vlan={}".format(output_vlan)])

            exec_and_display(mycommand)
            action_mirror_refresh()
            
        else:
            mywarning("Please enter a mirror name !")
                
    else:
        mywarning("Please enter a switchname !")

#---------------------------------------------------------------

def action_mirror_refresh():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        result1=exec_and_display(['ovs-vsctl','get','Bridge',switch,'mirrors'])
        bridge_mirror_list= pattern_space_comma.split(result1.lstrip('[').rstrip(']\n'))
        mirror_table.delete_all_rows()

        result2=exec_and_display(['ovs-vsctl','--columns=_uuid,name','list','mirror'])
        for line in result2.splitlines():
            pf=pattern_field.match(line)
            if(pf):
                if(pf.group(1)=='_uuid'):
                    uuid=pf.group(2)
                elif(pf.group(1)=='name'):
                    rowpos=mirror_table.new_row()
                    name=pf.group(2)
                    name=name.replace('"',"")
                    name=name.replace("'",'')
                    if(uuid in bridge_mirror_list): #only list mirrors of current bridge
                        mirror_table.settext(rowpos,0,name)
                        mirror_table.settext(rowpos,1,uuid)
        
#---------------------------------------------------------------

def action_mirror_del():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        rowpos=mirror_table.getcurrent_rownumber()
        if(rowpos>=0):
            uuid=mirror_table.gettext(rowpos,1)
            exec_and_display(['ovs-vsctl','remove','Bridge',switch,'mirrors',uuid])
            action_mirror_refresh()
            
#---------------------------------------------------------------

def action_mirror_select_port(widget,**opts):
    if(debug):mydebug(inspect.currentframe())

    port_list=get_selected_ports()
    if(opts['single']==True):
        widget.setText(port_list.pop(0))
    else:
        widget.setText(",".join(port_list))

#---------------------------------------------------------------

def action_mirror_list():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        exec_and_display(['ovs-vsctl','list','mirror'],force_output=True)

#---------------------------------------------------------------
#-------------------------- BONDING ----------------------------
#---------------------------------------------------------------

def action_bond_hash():
    if(debug):mydebug(inspect.currentframe())

    mac=ui.lineEdit_bond_try_mac.text()
    if(mac):
        result=exec_and_display(['ovs-appctl','bond/hash',mac])
        ui.lineEdit_bond_calculated_hash.setText(result)
    else:
        ui.lineEdit_bond_calculated_hash.setText('')

#---------------------------------------------------------------

def action_bond_slave_enable():
    if(debug):mydebug(inspect.currentframe())

    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        exec_and_display(['ovs-appctl','bond/enable-slave',portname,interfacename])
                
#---------------------------------------------------------------

def action_bond_slave_disable():
    if(debug):mydebug(inspect.currentframe())

    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        exec_and_display(['ovs-appctl','bond/disable-slave',portname,interfacename])
    
#---------------------------------------------------------------

def action_bond_slave_active():
    if(debug):mydebug(inspect.currentframe())

    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        exec_and_display(['ovs-appctl','bond/set-active-slave',portname,interfacename])
        break

#---------------------------------------------------------------

def action_bond_list():
    if(debug):mydebug(inspect.currentframe())

    exec_and_display(['ovs-appctl','bond/list'],force_output=True)

#---------------------------------------------------------------

def action_bond_lacp_show():
    if(debug):mydebug(inspect.currentframe())

    exec_and_display(['ovs-appctl','lacp/show'],force_output=True)

#---------------------------------------------------------------

def action_bond_params_update():
    if(debug):mydebug(inspect.currentframe())

    newbond=False
    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        bondname=ui.lineEdit_bond_name.text()
        bonds=get_bond_list()
        portline_list=port_tree.get_selected()

        if(not bondname in bonds):
            action_bond_add()
            #in case of creation, replace existing portline_list
            portline_list=[[bondname]]
            newbond=True

        mycommand=validate_prepare('ovs-vsctl','BOND','Port')
            
        bonds=get_bond_list()
            
        for portline in portline_list:
            bondname,interfacename=port_and_interface(portline)

            if(bondname in bonds):
                mycommand2=array_replace(mycommand,'_VARIABLE_',bondname)
                exec_and_display(mycommand2)

        action_bond_refresh()
        if(newbond):
            action_port_filter()
            
#---------------------------------------------------------------

def array_replace(myarray,src,dst):
    if(debug):mydebug(inspect.currentframe())

    if(myarray):
        return [ dst if x==src else x for x in myarray]
    else:
        return []
        
#---------------------------------------------------------------

def array_inside_replace(myarray,src,dst):
    if(debug):mydebug(inspect.currentframe())

    return [ x.replace(src,dst) for x in myarray]
        
#---------------------------------------------------------------

def action_bond_add():
    if(debug):mydebug(inspect.currentframe())

    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        bondname=ui.lineEdit_bond_name.text()

        ofrequest_list=[]
        ofrequest=ui.lineEdit_of_request.text()
        if(ofrequest):
            ofrequest_list=pattern_space_comma.split(ofrequest)
        
        if(bondname):        
            mycommand=['ovs-vsctl','add-bond',switch,bondname]
            for portline in port_tree.get_selected():
                portname,interfacename=port_and_interface(portline)
                mycommand.append(interfacename)
                
            for portline,of in zip(port_tree.get_selected(),ofrequest_list):
                portname,interfacename=port_and_interface(portline)
                mycommand.extend(['--','set','Interface',interfacename,"ofport_request={}".format(of)])
                
            exec_and_display(mycommand)
            #action_port_filter()
        else:
            mywarning("Please enter a name for your new bond")
#---------------------------------------------------------------

def get_bond_list():
    if(debug):mydebug(inspect.currentframe())

    result=exec_and_display(['ovs-appctl','bond/list'])
    bonds=[]

    for line in result.splitlines():
        pb=pattern_bond.search(line)
        if(pb):
            bonds.append(pb.group(1))

    bonds.pop(0) # remove header

    return bonds
    
#---------------------------------------------------------------

def action_bond_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('BOND')
    bonds=get_bond_list()
    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        if(portname in bonds):
            result=exec_and_display(['ovs-vsctl','--column=name,bond_active_slave,bond_downdelay,bond_fake_iface,bond_mode,bond_updelay,lacp,other_config','list','port',portname])
            process_fields('BOND',result)
            
        #stop after first port
        break

#---------------------------------------------------------------

def action_show_bond():
    if(debug):mydebug(inspect.currentframe())

    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)

        exec_and_display(['ovs-appctl','bond/show',portname],force_output=True)


#---------------------------------------------------------------
#-------------------------- PORT ----------------------------------
#---------------------------------------------------------------

def action_port_dock():
    if(debug):mydebug(inspect.currentframe())

    me=ui.frame_dockable
    pdock_Dialog.frame_dockable=me
    
    if(me.parent().layout().objectName()=='verticalLayout_dockable'):
        ui.verticalLayout_dockable.removeWidget(me)
        pdock_ui.verticalLayout_for_dock.addWidget(me)
        pdock_Dialog.show()
    else:
        #PROBLEM !!! AttributeError: 'MyQDialog' object has no attribute 'frame_dockable'
        pdock_ui.verticalLayout_for_dock.removeWidget(me)
        ui.verticalLayout_dockable.addWidget(me)
        pdock_Dialog.close()
    
#---------------------------------------------------------------
def action_port_list_refresh():
    if(debug):mydebug(inspect.currentframe())

    delay=int(pt_ui.comboBox_pt_ar.currentText())
    action_timer_define(timer_portlist,delay*1000)

#---------------------------------------------------------------
def action_vlan_refresh():

    if(debug):mydebug(inspect.currentframe())

    clear_widgets('PORT')
    #port_clear_fields()
    
    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        if(portname=='_HOST'):
            continue

        
        #result=exec_and_display(['ovs-vsctl','list','port',portname])
        result=exec_and_display(['ovs-vsctl','list','port',portname])
        process_fields('PORT',result)

        #stop after first port
        break

#---------------------------------------------------------------

def action_vlan_modify():
    if(debug):mydebug(inspect.currentframe())

    validate('ovs-vsctl','PORT','Port')
    action_vlan_refresh()
    
#---------------------------------------------------------------

def get_selected_ports():

    if(debug):mydebug(inspect.currentframe())

    return([ port_and_interface(portline)[0] for portline in port_tree.get_selected() ])
    

#---------------------------------------------------------------
#----------------------- IP -----------------------------
#---------------------------------------------------------------

def action_create_dummy_interface():
    if(debug):mydebug(inspect.currentframe())

    portname=ui.lineEdit_ip_dummy.text()
    if(portname):
        exec_and_display(['ip','link','add',portname,'type','dummy'])
        exec_and_display(['ip','link','set','dev',portname,'up'])
        action_port_filter()
#---------------------------------------------------------------

def action_create_tap_interface():
    if(debug):mydebug(inspect.currentframe())

    portname=ui.lineEdit_ip_tap.text()
    if(portname):
        exec_and_display(['ip','tuntap','add','name',portname,'mode','tap'])
        exec_and_display(['ip','link','set','dev',portname,'up'])
        action_port_filter()
#---------------------------------------------------------------

def action_create_tun_interface():
    if(debug):mydebug(inspect.currentframe())

    portname=ui.lineEdit_ip_tun.text()
    if(portname):
        exec_and_display(['ip','tuntap','add','name',portname,'mode','tun'])
        exec_and_display(['ip','link','set','dev',portname,'up'])
        action_port_filter()
#---------------------------------------------------------------

def action_ip_link():
    if(debug):mydebug(inspect.currentframe())

    exec_and_display(['ip','link'],force_output=True)

#---------------------------------------------------------------

def action_ip_addr():
    if(debug):mydebug(inspect.currentframe())

    exec_and_display(['ip','addr'],force_output=True)

#---------------------------------------------------------------

def action_ip_address_add():
    if(debug):mydebug(inspect.currentframe())

    ip_a=ui.lineEdit_ip_address.text()
    if(ip_a):
        for portline in port_tree.get_selected():
            portname,interfacename=port_and_interface(portline)

            exec_and_display(['ip','addr','add',ip_a,'dev',interfacename])
            break
    else:
        mywarning('You need to enter an ip address first !')
            
#---------------------------------------------------------------

def action_ip_address_flush():
    if(debug):mydebug(inspect.currentframe())

    for portline in port_tree.get_selected():
            portname,interfacename=port_and_interface(portline)

            exec_and_display(['ip','addr','flush','dev',interfacename])

#---------------------------------------------------------------

def action_ip_set_mtu():
    if(debug):mydebug(inspect.currentframe())

    mtu=ui.lineEdit_ip_mtu.text()
    if(mtu):
        for portline in port_tree.get_selected():
            portname,interfacename=port_and_interface(portline)

            exec_and_display(['ip','link','set','dev',interfacename,'mtu',mtu])
    else:
        mywarning('You need to enter a MTU first !')


    
#---------------------------------------------------------------

def action_create_veth_pair():
    if(debug):mydebug(inspect.currentframe())

    portname1=ui.lineEdit_ip_veth1.text()
    portname2=ui.lineEdit_ip_veth2.text()
    if(portname1 and portname2):
        exec_and_display(['ip','link','add','dev',portname1,'type','veth','peer','name', portname2])
        exec_and_display(['ip','link','set','dev',portname1,'up'])
        exec_and_display(['ip','link','set','dev',portname2,'up'])
        action_port_filter()

#---------------------------------------------------------------
#----------------------- BRIDGE -----------------------------
#---------------------------------------------------------------

def bridge_list(columns):
    if(debug):mydebug(inspect.currentframe())
    ovs=ui.lineEdit_ovs_name.text()
    if(ovs):
        if(columns):
            exec_and_display(['ovs-vsctl',"--column={}".format(columns),'list','Bridge',ovs],force_output=True)
        else:
            exec_and_display(['ovs-vsctl','list','Bridge',ovs],force_output=True)
        
#---------------------------------------------------------------
#----------------------- INTERFACE -----------------------------
#---------------------------------------------------------------

# read http://docs.openvswitch.org/en/latest/howto/userspace-tunneling/


def action_interface_list_refresh():
    if(debug):mydebug(inspect.currentframe())

    delay=int(if_ui.comboBox_if_ar.currentText())
    action_timer_define(timer_interfacelist,delay*1000)

#---------------------------------------------------------------
    
def action_interface_list():
    if(debug):mydebug(inspect.currentframe())


    firsttime=True
    if_Dialog.close()
    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
            
        if_Dialog.setWindowTitle("Interface: {}".format(interfacename))

        if(pattern_portname.match(portname)):
            result=exec_and_display(['ovs-vsctl','list','interface',interfacename])
            for line in result.splitlines():
                if(firsttime):if_Dialog.show()
                firsttime=False

                #print("LINE=[{}]".format(line))
                mif_field=pattern_if_field.match(line)
                if(mif_field):
                    if_field=mif_field.group(1)
                    if_value=mif_field.group(2)
                    #print("field {} value {}\n".format(if_field,if_value))
                    try:
                        le=getattr(if_ui, "lineEdit_{}".format(if_field))
                    except AttributeError:
                        mywarning("Cant find attr {}".format(if_field))
                    else:
                        LineEdit_Write(le,if_value)

        #only want first interface if multiselection
        break

#---------------------------------------------------------------

def port_and_interface(portline):
    if(debug):mydebug(inspect.currentframe())
    
    if(len(portline)>1):
        return (portline[0],portline[1])
    else:
        #if no interface selected, fallback to port
        return (portline[0],portline[0])
#---------------------------------------------------------------

def get_selected_interfaces():
    if(debug):mydebug(inspect.currentframe())

    return([ port_and_interface(portline)[1] for portline in port_tree.get_selected() ])

#---------------------------------------------------------------

def action_stats_dialog_show():
    if(debug):mydebug(inspect.currentframe())

    MyStats.clear()

    
    nickname=ui.lineEdit_ovs_profile.text()
    if(not nickname):
        clear_profile_bar()
        mywarning('Please select a profile in Management tab !')
        return

    if_list=get_selected_interfaces()
    if(not if_list):
        mywarning('Please select some interfaces')
        return
        
    MyStats.set_selected_interfaces(nickname=nickname,if_list=if_list)
    action_interface_statistics_refresh()
    stats_Dialog.show()
    
#---------------------------------------------------------------

def action_set_delta_origin():
    if(debug):mydebug(inspect.currentframe())

    MyStats.set_delta_origin_all_interfaces()
    action_interface_statistics_refresh()
    
#---------------------------------------------------------------
def action_interface_statistics_refresh():
    if(debug):mydebug(inspect.currentframe())

    nickname=ui.lineEdit_ovs_profile.text()
    if(nickname != MyStats.mgmt_nickname): #mgmt change force recalculation
        mywarning("Cannot refresh because of Management profile change. Closing Dialog !")
        stats_Dialog.close()
        return

    stats_table.enableSorting(False)
    stats_table.delete_all_rows()

    if(stats_ui.radioButton_stats_K.isChecked()):
        coeff=1024
    elif(stats_ui.radioButton_stats_M.isChecked()):
        coeff=1048576
    elif(stats_ui.radioButton_stats_G.isChecked()):
        coeff=1073741824
    elif(stats_ui.radioButton_stats_T.isChecked()):
        coeff=1099511627776
    elif(stats_ui.radioButton_stats_P.isChecked()):
        coeff=1125899906842624
    else:
        coeff=1

    if(stats_ui.radioButton_stats_delta.isChecked()):
        delta_mode=1
    elif(stats_ui.radioButton_stats_deltasec.isChecked()):
        delta_mode=2
    else:
        delta_mode=0
    
    result=exec_and_display(['ovs-vsctl','--column=name,statistics','find','interface'],hide_output=False)
    for line in result.splitlines():
        pf=pattern_field.match(line)
        if(pf):
            fieldname=pf.group(1)
            if(fieldname == 'name'):
                name=pf.group(2).rstrip('"').lstrip('"')
            elif(fieldname == 'statistics'):
                if(name in MyStats.if_list):

                    statistics=pf.group(2).rstrip('}').lstrip('{')
                    s=MyStats.add_or_modify(name=name,stats=statistics)

                    item_list=[name]

                    for idx,col in enumerate(('collisions','rx_bytes','rx_crc_err','rx_dropped','rx_errors','rx_frame_err','rx_over_err','rx_packets','tx_bytes','tx_dropped','tx_errors','tx_packets')):
                        if(delta_mode==0):
                            sval=s.stats[col]
                        elif(delta_mode==1):
                            sval=s.delta()[col]
                        elif(delta_mode==2):
                            sval=s.deltasec()[col]
                            
                        if(col in ('rx_bytes','tx_bytes') and coeff !=1):
                            val="{:.1f}".format(float(sval)/coeff)
                        else:
                            val="{:.0f}".format(float(sval))
                                
                        item_list.append(val)
                    stats_table.new_row(item_list)
                        
    stats_table.enableSorting(True)
                    
#---------------------------------------------------------------
                        
def action_interface_stats_refresh(switch):
    if(debug):mydebug(inspect.currentframe())

    ui.plainTextEdit_port_stats.clear()
    interface_list=get_selected_interfaces()
    ofproto=Mymgmt.get_current_profile_attr('force_of')
    result=exec_and_display(['ovs-ofctl','-O',ofproto,'dump-ports-desc',switch],hide_output=False)
    display_flag=False
    for line in result.splitlines():
        pld=pattern_interface_desc.search(line)
        if(pld):
            if(pld.group(1) in interface_list):
                display_flag=True
            else:
                display_flag=False
        if(display_flag):
            plaintext_print(ui.plainTextEdit_port_stats,line)

    #display stats
    result=exec_and_display(['ovs-ofctl','-O',ofproto,'dump-ports',switch],hide_output=False)
    display_flag=False
    for line in result.splitlines():
        pld=pattern_interface_nodesc.search(line)
        if(pld):
            if(pld.group(1) in interface_list):
                display_flag=True
            else:
                display_flag=False
        if(display_flag):
            plaintext_print(ui.plainTextEdit_port_stats,line)
#---------------------------------------------------------------

def action_interface_type_refresh():

    if(debug):mydebug(inspect.currentframe())

    clear_widgets('INTERFACE_TYPE')    
    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        for portline in port_tree.get_selected():
            #get interface name ( not portname )
            portname,interfacename=port_and_interface(portline)
            if(portname=='_HOST'):
                continue

            result=exec_and_display(['ovs-vsctl','list','interface',interfacename],hide_output=False)
            process_fields('INTERFACE_TYPE',result)
            break
            
        action_interface_type_enable_fields()                    

#---------------------------------------------------------------

def action_interface_refresh():

    if(debug):mydebug(inspect.currentframe())

    clear_widgets('INTERFACE')
    switch=ui.lineEdit_ovs_name.text()
    if(switch):
        for portline in port_tree.get_selected():
            #get interface name ( not portname )
            portname,interfacename=port_and_interface(portline)
            if(portname=='_HOST'):
                continue
            
            #cannot use column because some fields do not exist in old OF version
            #result=exec_and_display(['ovs-vsctl','--column=admin_state,link_state,external_ids,mtu,mtu_request,error,link_speed,duplex,statistics','list','interface',interfacename],hide_output=False)
            result=exec_and_display(['ovs-vsctl','list','interface',interfacename],hide_output=False)
            process_fields('INTERFACE',result)

            #stop after first port            
            break
            
        action_interface_stats_refresh(switch)
        
#---------------------------------------------------------------        
def action_interface_type_enable_fields():
    if(debug):mydebug(inspect.currentframe())

    mode=ui.comboBox_type.currentText()

    setEnableWidgetDic('INTERFACE','ALL',False)    
    
    if(mode=='gre'):
        setEnableWidgetDic('INTERFACE','gre',True)
    elif(mode=='patch'):
        setEnableWidgetDic('INTERFACE','patch',True)
    elif(mode=='vxlan'):
        setEnableWidgetDic('INTERFACE','vxlan',True)
    elif(mode=='stt'):
        setEnableWidgetDic('INTERFACE','stt',True)
    elif(mode=='geneve'):
        setEnableWidgetDic('INTERFACE','geneve',True)
    elif(mode=='lisp'):
        setEnableWidgetDic('INTERFACE','lisp',True)

#---------------------------------------------------------------

def action_interface_update():
    if(debug):mydebug(inspect.currentframe())

    validate('ovs-vsctl','INTERFACE','Interface')
    action_interface_refresh()
    
#---------------------------------------------------------------

def action_interface_type_update():
    if(debug):mydebug(inspect.currentframe())

    validate('ovs-vsctl','INTERFACE_TYPE','Interface')
    action_interface_type_refresh()
    
#---------------------------------------------------------------
def widget_read(widget):
    if(debug):mydebug(inspect.currentframe())

    if(widget.isEnabled()):
        if(isinstance(widget, QtWidgets.QLineEdit)):
            widget_val=widget.text()
            if(widget_val):
                return(True,widget_val)

        elif(isinstance(widget, QtWidgets.QCheckBox)):
            if(widget.isChecked()):
                return(True,'true')
            else:
                return(True,'false')

        elif(isinstance(widget, QtWidgets.QComboBox)):
            widget_val=widget.currentText()
            if(widget_val):
                return(True,widget_val)

        elif(isinstance(widget, QtWidgets.QRadioButton)):
            if(widget.isChecked()):
                return(True,'true')
            else:
                return(True,'false')

            
    return (False,'')
    

#---------------------------------------------------------------

def color_led(field_name,field_value,widget_list,list_type):
    if(debug):mydebug(inspect.currentframe())

    w=widget_list[0]

    if(field_value=='up'):
        w.setProperty('ledstate',True)
    else:
        w.setProperty('ledstate',False)

    w.setStyleSheet('')
    
#---------------------------------------------------------------
#------------------------ ingress policy   ---------------------
#---------------------------------------------------------------

def action_ingress_refresh():
    if(debug):mydebug(inspect.currentframe())

    clear_widgets('PORT_INGRESS')    
    for portline in port_tree.get_selected():
        portname,interfacename=port_and_interface(portline)
        if(portname=='_HOST'):
            continue

        result=exec_and_display(['ovs-vsctl','--column=ingress_policing_burst,ingress_policing_rate','find','interface',"name={}".format(interfacename)],hide_output=True)
        process_fields('PORT_INGRESS',result)
        #stop after first port
        break
        
#---------------------------------------------------------------

def action_ingress_modify():
    if(debug):mydebug(inspect.currentframe())

    validate('ovs-vsctl','PORT_INGRESS','Interface')
    action_ingress_refresh()


#---------------------------------------------------------------
def replace_suffixe(text,n,**opts):

    if(opts.get('ip_mode',False)):
        if(pattern_XX_ipv6.search(text)):
            suffix=":{}/".format(n)
            textre=pattern_XX_ipv6.sub(suffix,text)
        else:
            suffix=".{}/".format(n)
            textre=pattern_XX_ipv4.sub(suffix,text)
    else:
        suffix="{:02d}".format(n)
        textre=pattern_XX.sub(suffix,text)
    return(textre)
        
#---------------------------------------------------------------
def replace_double_dollar(text,n):
    return(text.replace('$$',"{:02d}".format(n)))


#---------------------------------------------------------------
#-------------------------- DOCKNET -----------------------------
#---------------------------------------------------------------            

def action_dockernet_enable_fields():
    if(debug):mydebug(inspect.currentframe())

    setEnableWidgetDic('DOCKERNET','ALL',False)
    combo=dockernet_ui.comboBox_dockernet.currentText()
    if(combo=='addr'):
        setEnableWidgetDic('DOCKERNET','ip',True)
    elif(combo=='route'):
        setEnableWidgetDic('DOCKERNET','net',True)
    elif(combo=='default route'):
        setEnableWidgetDic('DOCKERNET','net',True)
        dockernet_ui.lineEdit_dialog_dockernet_net.setText('default')

#---------------------------------------------------------------
def action_dockernet_refresh():
    if(debug):mydebug(inspect.currentframe())

    docker_net_table.delete_all_rows()
    interface=docker_if_table.getcurrenttext(0)
    if(interface):
        MyDockerNet.populate_table(interface)

#---------------------------------------------------------------
def action_dockernet_del():
    if(debug):mydebug(inspect.currentframe())

    interface_uid=docker_if_table.getcurrenttext(0)
    if(interface_uid):
      net_uid=docker_net_table.getcurrenttext(0)
      if(net_uid):
        MyDockerNet.delete(net_uid)
        docker_net_table.delete_row()
        MyDockerNet.mem_order(interface_uid)
      else:
        mywarning('Please select a net !')
    else:
      mywarning('Please select interface before selecting net !')

#---------------------------------------------------------------
def action_dockernet_up():
    if(debug):mydebug(inspect.currentframe())

    interface_uid=docker_if_table.getcurrenttext(0)
    if(interface_uid):
      net_uid=docker_net_table.getcurrenttext(0)
      if(net_uid):
        docker_net_table.up_row()
        MyDockerNet.mem_order(interface_uid)
      else:
        mywarning('Please select a net !')
    else:
      mywarning('Please select interface before selecting net !')

#---------------------------------------------------------------
def action_dockernet_down():
    if(debug):mydebug(inspect.currentframe())

    interface_uid=docker_if_table.getcurrenttext(0)
    if(interface_uid):
      net_uid=docker_net_table.getcurrenttext(0)
      if(net_uid):
        docker_net_table.down_row()
        MyDockerNet.mem_order(interface_uid)
      else:
        mywarning('Please select a net !')
    else:
      mywarning('Please select interface before selecting net !')
    
#---------------------------------------------------------------
def action_dockernet_add(newnet):
    if(debug):mydebug(inspect.currentframe())

    if(not newnet):
        net_uid=docker_net_table.getcurrenttext(0)
        docknet=MyDockerNet.dic[net_uid]
        net_type=docknet.net_type
        if(net_type=='ad'):
            net_type='addr'

        ip=getattr(docknet,'ip',None)
        if(ip):
            dockernet_ui.lineEdit_dialog_dockernet_ip.setText(ip)

        net=getattr(docknet,'net',None)
        if(net):
            if(net=='default'):
                net_type='default route'
            else:
                net_type='route'

            dockernet_ui.lineEdit_dialog_dockernet_net.setText(net)


        gw=getattr(docknet,'gw',None)
        if(gw):    
            dockernet_ui.lineEdit_dialog_dockernet_gw.setText(gw)
            
        comboBox_Write(dockernet_ui.comboBox_dockernet,net_type)    

    action_dockernet_enable_fields()
    if(dockernet_Dialog.exec()):

        net_type=dockernet_ui.comboBox_dockernet.currentText()
        ip=dockernet_ui.lineEdit_dialog_dockernet_ip.text()
        net=dockernet_ui.lineEdit_dialog_dockernet_net.text()
        gw=dockernet_ui.lineEdit_dialog_dockernet_gw.text()

       
        if(net_type):
            interface_uid=docker_if_table.getcurrenttext(0)
            if(interface_uid):
                if(newnet):
                    docknet=MyDockerNet(interface_uid,net_type,ip,net,gw)
                    docknet.populate_line()
                    MyDockerNet.mem_order(interface_uid)
                else:
                    docknet.modify(net_type,ip,net,gw)
                    docknet.populate_line(row=docker_net_table.w.currentRow())
            else:
                mywarning("Don't know which interface, this net is for!  You first have to select an interface !")

#---------------------------------------------------------------
def action_dockerif_del():
    if(debug):mydebug(inspect.currentframe())

    interface_uid=docker_if_table.getcurrenttext(0)
    docker_if_table.delete_row()
    docker_net_table.delete_all_rows()
    for net_uid in MyDockerIf.dic[interface_uid].net:
        MyDockerNet.clear_net_by_uid(net_uid)

    MyDockerIf.clear_if_by_uid(interface_uid)


#---------------------------------------------------------------
def action_dockerif_up():
    if(debug):mydebug(inspect.currentframe())

    docker_if_table.up_row()
    
#---------------------------------------------------------------
def action_dockerif_down():
    if(debug):mydebug(inspect.currentframe())

    docker_if_table.down_row()

#---------------------------------------------------------------
def action_dockerif_add(newintf):
    if(debug):mydebug(inspect.currentframe())

    if(not newintf):
            interface_uid=docker_if_table.getcurrenttext(0)
            dockif=MyDockerIf.dic[interface_uid]
            dockerif_ui.lineEdit_dialog_dockerif_ext.setText(dockif.ifext)
            dockerif_ui.lineEdit_dialog_dockerif_int.setText(dockif.ifint)
            dockerif_ui.lineEdit_dialog_dockerif_vlan.setText(dockif.vlan)
            dockerif_ui.lineEdit_dialog_dockerif_mac.setText(dockif.mac)
            dockerif_ui.lineEdit_dialog_dockerif_of.setText(dockif.of)

    
    if(dockerif_Dialog.exec()):
        if(newintf):
            fields=[dockerif_ui.lineEdit_dialog_dockerif_ext.text(),
                    dockerif_ui.lineEdit_dialog_dockerif_int.text(),
                    dockerif_ui.lineEdit_dialog_dockerif_vlan.text(),
                    dockerif_ui.lineEdit_dialog_dockerif_mac.text(),
                    dockerif_ui.lineEdit_dialog_dockerif_of.text()]

            dockif=MyDockerIf(fields[0],fields[1],fields[2],fields[3],fields[4])
            dockif.populate_line()
            docker_net_table.delete_all_rows()
        else:
            dockif.ifext=dockerif_ui.lineEdit_dialog_dockerif_ext.text()
            dockif.ifint=dockerif_ui.lineEdit_dialog_dockerif_int.text()
            dockif.vlan=dockerif_ui.lineEdit_dialog_dockerif_vlan.text()
            dockif.mac=dockerif_ui.lineEdit_dialog_dockerif_mac.text()
            dockif.of=dockerif_ui.lineEdit_dialog_dockerif_of.text()

            dockif.populate_line(row=docker_if_table.w.currentRow())
#---------------------------------------------------------------
@myJsonExport(dockernetDir,"Choose a filename to save your docker network",ui.pushButton_dockernet_export)
def action_dockernet_export():
    if(debug):mydebug(inspect.currentframe())

    liste=[]
    for intf_uid in docker_if_table.get_coltext(0):
        intf=MyDockerIf.dic[intf_uid]
        liste.append({'type':'intf',
                      'ifext':intf.ifext,
                      'ifint':intf.ifint,
                      'vlan':intf.vlan,
                      'mac':intf.mac,
                      'of':intf.of}
                 )
        for net_uid in intf.net:
            dnet=MyDockerNet.dic[net_uid]
            if(dnet.net_type=='ad'):
                liste.append({'type':'net',
                              'net_type':dnet.net_type,
                              'ip':dnet.ip})
            else:
                liste.append({'type':'net',
                              'net_type':dnet.net_type,
                              'net':dnet.net,
                              'gw':dnet.gw})
    return liste
#---------------------------------------------------------------

@myJsonImport(dockernetDir,"Load your docker network from file",ui.pushButton_dockernet_import)
def action_dockernet_import(**opts):
    if(debug):mydebug(inspect.currentframe())

    json_txt=opts['json']
    
    MyDockerNet.clear()
    MyDockerIf.clear()

    last_interface_uid=None
    
    for dockbloc in json_txt:
        #print("DOCBLOCK:",dockbloc)
        if(dockbloc.get('type',None)=='intf'):

            if(last_interface_uid):
                MyDockerNet.mem_order(last_interface_uid)
                docker_net_table.delete_all_rows()
                last_interface_uid=None
                
            dockif=MyDockerIf(dockbloc.get('ifext',''),
                              dockbloc.get('ifint',''),
                              dockbloc.get('vlan',''),
                              dockbloc.get('mac',''),
                              dockbloc.get('of',''),
                          )
            dockif.populate_line()
            last_interface_uid=dockif.uid
        elif(dockbloc.get('type',None)=='net'):
            if(dockbloc.get('net_type',None)=='ad'):
                docknet=MyDockerNet(last_interface_uid,'ad',dockbloc.get('ip',''),'','')
            else:
                docknet=MyDockerNet(last_interface_uid,'rt','',dockbloc.get('net',''),dockbloc.get('gw',''))
            docknet.populate_line()

    if(last_interface_uid):
        MyDockerNet.mem_order(last_interface_uid)
        docker_net_table.delete_all_rows()


#---------------------------------------------------------------
#-------------------------- DOCKER -----------------------------
#---------------------------------------------------------------            
        
def action_docker_remove_image():
    if(debug):mydebug(inspect.currentframe())

    image=dockerimage_table.getcurrenttext(2)
    if(image):
        docker_release=Mymgmt.get_current_profile_attr('docker_release')
        if(docker_release=='<1.13'):
            exec_and_display(['docker','rmi',image])
        else:
            exec_and_display(['docker','image','rm',image])
        action_docker_image_filter()
#---------------------------------------------------------------            
    
def action_dockerfile_add_line():
    if(debug):mydebug(inspect.currentframe())

    dockerfile_table.new_row()
#---------------------------------------------------------------            
def action_dockerfile_del_line():
    if(debug):mydebug(inspect.currentframe())

    dockerfile_table.delete_row()
#---------------------------------------------------------------            
def action_dockerfile_up_line():
    if(debug):mydebug(inspect.currentframe())

    dockerfile_table.up_row()
#---------------------------------------------------------------            
def action_dockerfile_down_line():
    if(debug):mydebug(inspect.currentframe())

    dockerfile_table.down_row()

#---------------------------------------------------------------            
def action_dockerfile_clear():
    if(debug):mydebug(inspect.currentframe())

    dockerfile_table.delete_all_rows()
#---------------------------------------------------------------            
def action_dockerfile_build():
    if(debug):mydebug(inspect.currentframe())

    text=[]
    tag=ui.lineEdit_dockerfile_tag.text()
    if(tag):
        for r in dockerfile_table.get_allrowtext():
            if(r[0]):
                text.append(r[0].rstrip(' ')+' '+r[1]+"\n")
            else:
                text.append("\t"+r[1]+"\n")

        hostname=ui.lineEdit_ovs_hostname.text()
        docker_release=Mymgmt.get_current_profile_attr('docker_release')

        pseudo_random_dir="/tmp/docker_build_{}_{:010d}".format(tag,random.randint(0,1000000000))
        dockerfile="{}/Dockerfile".format(pseudo_random_dir)
        dockerbuild="{}/Build".format(pseudo_random_dir)
        dockerlog="{}/build.log".format(pseudo_random_dir)

        t=myTar()
        t.add(dockerfile,0o400,''.join(text))


        if(docker_release=='<1.13'):
            t.add(dockerbuild,0o700,"#!/bin/sh\n\ncd {}\nnohup docker build -t {} -f {} . > {} 2>&1 &\n".format(pseudo_random_dir,tag,dockerfile,dockerlog))

            #exec_and_display(['docker','build','-t',tag,'-'],input="".join(text),force_output=True)
        else:
            t.add(dockerbuild,0o700,"#!/bin/sh\n\ncd {}\nnohup docker image build -t {} -f {} . > {} 2>&1 &\n".format(pseudo_random_dir,tag,dockerfile,dockerlog))

            #exec_and_display(['docker','image','build','-t',tag,'-'],input="".join(text),force_output=True)


        t.close()
        archive_data=t.get_archive_rawdata()
        t.close_stream()
        exec_and_display(['tar','xPf','-'],input=archive_data,force_output=True)
        exec_and_display([dockerbuild],force_output=True)
        
        mywarning("Docker image build can take a long to complete. Please manually refresh image list periodically to check. In case of doubt you can watch remote log file {}:{}".format(hostname,dockerlog))
        action_docker_image_filter()
        
#---------------------------------------------------------------            
def action_dockerfile_import():
    if(debug):mydebug(inspect.currentframe())

    filename=dockerfileDir.browse('Select dockerfile to import',parent_ui=ui.pushButton_dockerfile_import)
    if(filename):
        dockerfile_table.delete_all_rows()

        with open(filename) as fh:
            for l in fh.readlines():
                pd=pattern_dockerfile.match(l) or pattern_comment.match(l)
                if(pd):
                    rowpos=dockerfile_table.new_row()
                    dockerfile_table.settext(rowpos,0,pd.group(1))
                    dockerfile_table.settext(rowpos,1,pd.group(2))


#---------------------------------------------------------------            
def action_dockerfile_export():
    if(debug):mydebug(inspect.currentframe())
    
    filename=dockerfileDir.save('Save dockerfile to file',parent_ui=ui.pushButton_dockerfile_export)
    if(filename):
        filename_handler = open(filename,'w')
        if(filename_handler):
            print("writing filename:"+filename)
            for r in dockerfile_table.get_allrowtext():
                if(r[0]):
                    filename_handler.write(r[0].rstrip(' ')+' '+r[1]+"\n")
                else:
                    #filling first row with tab if empty
                    filename_handler.write("\t"+r[1]+"\n")
            filename_handler.close()

        else:
            mywarning("Cannot write "+filename+" !!!")
    else:
        print("No filename given !")

#---------------------------------------------------------------

def docker_inspect():
    if(debug):mydebug(inspect.currentframe())

    name=dockerps_table.getcurrenttext(6)
    if(name):
        docker_release=Mymgmt.get_current_profile_attr('docker_release')
        if(docker_release=='<1.13'):
            exec_and_display(['docker','inspect', name],force_output=True)
        else:
            exec_and_display(['docker','container','inspect', name],force_output=True)

#---------------------------------------------------------------

def docker_pid(container):
    if(debug):mydebug(inspect.currentframe())

    docker_release=Mymgmt.get_current_profile_attr('docker_release')
    if(docker_release=='<1.13'):
        result=exec_and_display(['docker','inspect','--format','\'{{ .State.Pid }}\'', container])
    else:
        result=exec_and_display(['docker','container','inspect','--format','\'{{ .State.Pid }}\'', container])

    mnum=pattern_number.match(result)
    if(mnum):
        return mnum.group(1)
    else:
        return '0'

#---------------------------------------------------------------            
def action_docker_stopremove():
    if(debug):mydebug(inspect.currentframe())

    liste=[]
    for row in dockerps_table.get_selected_rows():
        liste.append(dockerps_table.gettext(row,6))

    if(liste):
        docker_release=Mymgmt.get_current_profile_attr('docker_release')
        if(docker_release=='<1.13'):
            liste2=['docker','stop']
            liste3=['docker','rm']
        else:
            liste2=['docker','container','stop']
            liste3=['docker','container','rm']
        
        liste2.extend(liste)
        liste3.extend(liste)
        exec_and_display(liste2)
        exec_and_display(liste3)

    action_docker_ps()
    
#---------------------------------------------------------------            
def action_docker_stop():
    if(debug):mydebug(inspect.currentframe())

    liste=[]
    for row in dockerps_table.get_selected_rows():
        liste.append(dockerps_table.gettext(row,6))

    if(liste):
        docker_release=Mymgmt.get_current_profile_attr('docker_release')
        if(docker_release=='<1.13'):
            liste2=['docker','stop']
        else:
            liste2=['docker','container','stop']
        
        liste2.extend(liste)
        exec_and_display(liste2)
            
    action_docker_ps()
#---------------------------------------------------------------            
def action_docker_start():
    if(debug):mydebug(inspect.currentframe())

    liste=[]
    for row in dockerps_table.get_selected_rows():
        liste.append(dockerps_table.gettext(row,6))

    if(liste):
        docker_release=Mymgmt.get_current_profile_attr('docker_release')
        if(docker_release=='<1.13'):
            liste2=['docker','start']
        else:
            liste2=['docker','container','start']
        
        liste2.extend(liste)
        exec_and_display(liste2)
            
    action_docker_ps()
#---------------------------------------------------------------            
def action_docker_remove():
    if(debug):mydebug(inspect.currentframe())

    liste=[]
    for row in dockerps_table.get_selected_rows():
        liste.append(dockerps_table.gettext(row,6))

    if(liste):
        docker_release=Mymgmt.get_current_profile_attr('docker_release')
        if(docker_release=='<1.13'):
            liste2=['docker','rm']
        else:
            liste2=['docker','container','rm']

        liste2.extend(liste)
        exec_and_display(liste2)
    
    action_docker_ps()

#---------------------------------------------------------------            
def dockerimage_select():
    if(debug):mydebug(inspect.currentframe())

    ui.lineEdit_docker_image_repo.setText(dockerimage_table.getcurrenttext(0))
    ui.lineEdit_docker_image_tag.setText(dockerimage_table.getcurrenttext(1))
    ui.lineEdit_docker_image_id.setText(dockerimage_table.getcurrenttext(2))
    

#---------------------------------------------------------------
def action_docker_link(iter_mode,n,container_name,ovs_name):
    if(debug):mydebug(inspect.currentframe())

    if(iter_mode=='$$'):
        container_name=replace_double_dollar(container_name,n)
    elif(iter_mode=='XX'):
        container_name=replace_suffixe(container_name,n)                

        
    pid=docker_pid(container_name)
    if(pid=='0'):
        mywarning("Cant find pid of docker container !!!!")
        return

    for intf_uid in docker_if_table.get_coltext(0):
        intf=MyDockerIf.dic[intf_uid]
        action_docker_create_if(iter_mode,n,intf_uid,ovs_name,pid)
#---------------------------------------------------------------
def iterate_string(iter_mode,n,text,**opts):
    if(text):
        if(iter_mode=='$$'):
            text=replace_double_dollar(text,n)
        elif(iter_mode=='XX'):
            text=replace_suffixe(text,n,**opts)

    return text

#---------------------------------------------------------------
def iterate_array(iter_mode,n,ltext,**opts):
    liste=[]

    if(iter_mode=='iteration_disabled'):
        return ltext
    
    if(opts.get('deny_XX_mode',False) and iter_mode=='XX'):
        return ltext
        
    for text in ltext:
        liste.append(iterate_string(iter_mode,n,text,**opts))

    return liste
        
#---------------------------------------------------------------
def action_docker_create_if(iter_mode,n,interface_uid,ovs_name,pid):
    if(debug):mydebug(inspect.currentframe())


    interface=MyDockerIf.dic[interface_uid]
    ext_veth=interface.ifext
    int_veth=interface.ifint
    int_veth_tmp=ext_veth+'_tmp'
    vlan=interface.vlan
    mac=interface.mac
    of_port=interface.of

    (mac,of_port,ext_veth,int_veth_tmp)=iterate_array(iter_mode,n,
                                                      [mac,of_port,ext_veth,int_veth_tmp])
    
    line=[]
    #Create a pair of veth
    #exec_and_display(['ip','link','add', int_veth,'type','veth','peer','name', ext_veth])
    line.append(['ip','link','add', int_veth_tmp,'type','veth','peer','name', ext_veth])
        
    #Change mac of internal veth
    if(mac):
        #exec_and_display(['ip','link','set', int_veth,'address', mac])
        line.append(['ip','link','set', int_veth_tmp,'address', mac])

    #Enable outside veth
    line.append(['ip','link','set',ext_veth,'up'])
        
    #add veth to bridge
    subline=['ovs-vsctl','add-port', ovs_name, ext_veth]
    if(of_port):
        subline.extend(['--','set','interface', ext_veth,"ofport_request={}".format(of_port)])
        #set vlan
    if(vlan):
        subline.extend(['--','set','port', ext_veth,"tag={}".format(vlan)])

    line.append(subline)
                
    #Move one of the veth in docker container namespace
    line.append(['ip','link','set','netns',pid,'dev', int_veth_tmp])

    nsline=[]
    #Rename docker veth to something like eth0
    nsline.append("ip link set dev {} name {}".format(int_veth_tmp, int_veth))
    nsline.append("ip link set {} up".format(int_veth))
    
    for n_uid in interface.net:
        net=MyDockerNet.dic[n_uid]
        
        if(net.net_type=='ad'):
            ip=net.ip
            (ip,)=iterate_array(iter_mode,n,[ip],ip_mode=True)
            ip=pattern_ip_zeroprefix.sub(r'\.\1',ip)
            #set ip on inside veth
            nsline.append("ip addr add {} dev {}".format(ip, int_veth))
        else:
            network=net.net
            gateway=net.gw
            (network,gateway)=iterate_array(iter_mode,n,[network,gateway],deny_XX_mode=True)
            #add route on inside veth
            nsline.append("ip route add {} via {} dev {}".format(network,gateway,int_veth))

    line.append(['nsenter','-t', pid, '-n','bash','-c',
                 '_mySPECIALQUOTE_'+';'.join(nsline)+'_mySPECIALQUOTE_',
             ])

    for l in line:
        exec_and_display(l)
            
#---------------------------------------------------------------
@myJsonImport(dockerParamsDir,'Load docker run params from file',ui.pushButton_docker_import)
def action_docker_import(**opts):
    if(debug):mydebug(inspect.currentframe())

    json_txt=opts['json']
    
    for dockbloc in json_txt:
        ui.lineEdit_docker_run_options.setText(dockbloc.get('run_options',''))
        ui.lineEdit_docker_run_cmd.setText(dockbloc.get('run_command',''))
        break
        
#---------------------------------------------------------------
@myJsonExport(dockerParamsDir,'Save docker run params to file',ui.pushButton_docker_export)
def action_docker_export():
    if(debug):mydebug(inspect.currentframe())

    liste=[{'run_options': ui.lineEdit_docker_run_options.text(),
            'run_command' : ui.lineEdit_docker_run_cmd.text(),
       }]
      
    return liste

#---------------------------------------------------------------

def action_docker_ps():
    if(debug):mydebug(inspect.currentframe())

    dockerps_table.delete_all_rows()
    ui.lineEdit_docker_ps_filter.clearFocus()

    filter=LineEdit_Read(ui.lineEdit_docker_ps_filter)
    
    pattern_filter=re.compile(filter)

    docker_release=Mymgmt.get_current_profile_attr('docker_release')
    if(docker_release=='<1.13'):
        result=exec_and_display(['docker','ps','-a',"--format=\'{{.ID}}%%{{.Image}}%%{{.Command}}%%{{.CreatedAt}}%%{{.Status}}%%{{.Ports}}%%{{.Names}}\'"])
    else:
        result=exec_and_display(['docker','container','ls','-a',"--format=\'{{.ID}}%%{{.Image}}%%{{.Command}}%%{{.CreatedAt}}%%{{.Status}}%%{{.Ports}}%%{{.Names}}\'"])


    for line in result.splitlines():
        m=pattern_filter.search(line)
        if(not filter or m):
            #removing quote and double quote
            line=line.replace("'","")
            line=line.replace('"',"")

            rowpos=dockerps_table.new_row()
            col=0
            for field in line.split('%%'):
                dockerps_table.settext(rowpos,col,field)
                col +=1

#---------------------------------------------------------------

def action_docker_iterate_check():
    if(debug):mydebug(inspect.currentframe())

    iterate_mode=iterate_ui.comboBox_docker_iterate.currentText()
    iterate_from=iterate_ui.lineEdit_dialog_docker_iterate_from.text()
    iterate_to=iterate_ui.lineEdit_dialog_docker_iterate_to.text()
    if(not iterate_from):
        mywarning("Please fill both 'From' field !")
        return('err',0,0)
    if(not iterate_to):
        mywarning("Please fill 'To' field !")
        return('err',0,0)
    iterate_from=int(iterate_from)
    iterate_to=int(iterate_to)    
    if(iterate_from<1 or iterate_from>99):
        mywarning("'From' must be a number between 1 and 99 !")
        return('err',0,0)
    if(iterate_to<1 or iterate_to>99):
        mywarning("'To' must be a number between 1 and 99 !")
        return('err',0,0)

    if((iterate_to-iterate_from)<0):
        mywarning("'To' must be greater than 'From' !")
        return('err',0,0)

    if(iterate_mode=='last 2 digits'):
        iterate_mode='XX'
    else:
        iterate_mode='$$'
        
    return(iterate_mode,iterate_from,iterate_to)
        
#---------------------------------------------------------------

def action_docker_run_iterate(iter_enabled):
    if(debug):mydebug(inspect.currentframe())


    
    image_full_name=ui.lineEdit_docker_image_id.text()
    container_name=LineEdit_Read(ui.lineEdit_docker_name)

    if(not image_full_name):
        mywarning('Please provide an image name')
        return
    if(not container_name):
        mywarning('Please provide a container name')
        return
    
    if(iter_enabled):
        iterate_ui.label_dialog_docker_iterate.setText('Iterate container creation')
        if(iterate_Dialog.exec()):
            (iter_mode,iter_to,iter_from)=action_docker_iterate_check()
            if(iter_mode=='err'):
                return
            for n in range(iter_to,iter_from+1):
                action_docker_run(iter_mode,n,image_full_name,container_name)

    else:
        action_docker_run('iteration_disabled','',image_full_name,container_name)
        
    action_docker_ps()
            
#---------------------------------------------------------------

def action_docker_link_iterate(iter_enabled):
    if(debug):mydebug(inspect.currentframe())

    container_name=LineEdit_Read(ui.lineEdit_docker_name)
    if(container_name):
        ovs_name=LineEdit_Read(ui.lineEdit_ovs_name)
    else:
        mywarning("Please select a docker container !!!!")
        return

    if(not ovs_name):
        mywarning("Please select an OvS switch  first !")
        return

    if(iter_enabled):
        iterate_ui.label_dialog_docker_iterate.setText('Iterate container network setup')
        if(iterate_Dialog.exec()):
            (iter_mode,iter_to,iter_from)=action_docker_iterate_check()
            if(iter_mode=='err'):
                return
            for n in range(iter_to,iter_from+1):
                action_docker_link(iter_mode,n,container_name,ovs_name)

    else:
        action_docker_link('iteration_disabled','',container_name,ovs_name)
        
#---------------------------------------------------------------

def action_docker_run(iter_mode,n,image_full_name,container_name):
    if(debug):mydebug(inspect.currentframe())

    run_options=LineEdit_Read(ui.lineEdit_docker_run_options)
    run_command=LineEdit_Read(ui.lineEdit_docker_run_cmd)

    (container_name,)=iterate_array(iter_mode,n,[container_name])
    (run_options,run_command)=iterate_array(iter_mode,n,[run_options,run_command],deny_XX_mode=True)

    docker_release=Mymgmt.get_current_profile_attr('docker_release')
    if(docker_release=='<1.13'):
        cmd=['docker','run']
    else:
        cmd=['docker','container','run']

    cmd.extend(run_options.split())
    cmd.extend(['-h',container_name,'--name',container_name,image_full_name,run_command])

    exec_and_display(cmd)
    
#---------------------------------------------------------------

def action_docker_image_filter():
    if(debug):mydebug(inspect.currentframe())


    dockerimage_table.delete_all_rows()
    ui.lineEdit_docker_images_filter.clearFocus()

    filter=LineEdit_Read(ui.lineEdit_docker_images_filter)
    
    pattern_filter=re.compile(filter)
    docker_release=Mymgmt.get_current_profile_attr('docker_release')
    if(docker_release=='<1.13'):
        result=exec_and_display(['docker','images','--format="{{.Repository}}%%{{.Tag}}%%{{.ID}}%%{{.CreatedAt}}%%{{.Size}}"'])
    else:
        result=exec_and_display(['docker','image','ls','--format="{{.Repository}}%%{{.Tag}}%%{{.ID}}%%{{.CreatedAt}}%%{{.Size}}"'])

    for line in result.splitlines():
        m=pattern_filter.search(line)
        if(not filter or m):
            #removing quote and double quote
            line=line.replace("'","")
            line=line.replace('"',"")
    
            rowpos=dockerimage_table.new_row()
            col=0
            for field in line.split('%%'):
                dockerimage_table.settext(rowpos,col,field)
                col +=1
                
#---------------------------------------------------------------
#---------------------------------------------------------------
#---------------------------------------------------------------

def begin_pref():
    if(debug):mydebug(inspect.currentframe())

    for w in dialog_list:
        w.restoreSettings()
        
    MainWindow.restoreSettings()

    define_stylesheet(MainWindow.mypref['stylesheet'])
    fontsize=MainWindow.mypref['fontSize']
    iconsize=MainWindow.mypref['iconSize']
    change_font_size(fontsize)
    change_icon_size(iconsize)
#---------------------------------------------------------------

def bind_actions():
    if(debug):mydebug(inspect.currentframe())

    #buttons
    for bname,actionlist in buttons_mapping.items():
        (w,action)=actionlist
        b=getattr(w, bname)
        b.clicked.connect(action)

    #lineedits
    for lname,actionlist in lineedit_mapping.items():
        (w,action)=actionlist
        l=getattr(w, lname)
        l.returnPressed.connect(action)

    #comboboxs
    for cname,actionlist in combobox_mapping.items():
        (w,action)=actionlist
        l=getattr(w, cname)
        l.activated.connect(action)

    #menus
    for mname,actionlist in menu_mapping.items():
        (w,action)=actionlist
        l=getattr(w, mname)
        l.triggered.connect(action)

    ##list
    for lname,actionlist in list_mapping.items():
        (w,action)=actionlist
        l=getattr(w, lname)
        l.itemClicked.connect(action)

    #radiobutton
    for rname,actionlist in radiobutton_mapping.items():
        (w,action)=actionlist
        l=getattr(w, rname)
        l.toggled.connect(action)

    #checkbutton
    for rname,actionlist in checkbutton_mapping.items():
        (w,action)=actionlist
        l=getattr(w, rname)
        l.toggled.connect(action)

        
    #tablewidget
    for tname,actionlist in tablewidget_mapping.items():
        (w,actions)=actionlist
        #(w,action,signal)=actionlist
        l=getattr(w, tname)
        for ac in actions:
            (action,signal)=ac
            if(signal=='cellChanged'):
                l.cellChanged.connect(action)
            elif(signal=='cellDoubleClicked'):
                l.cellDoubleClicked.connect(action)
            else:
                l.cellClicked.connect(action)


            
#---------------------------------------------------------------

def refresh_stylesheet(widgets):
    if(debug):mydebug(inspect.currentframe())

    for w in widgets:
        w.setStyleSheet("")

#---------------------------------------------------------------

def change_icon_size(size):
    if(debug):mydebug(inspect.currentframe())

    MainWindow.mypref['iconSize']=size
    load_stylesheet(MainWindow.mypref['stylesheet'])
    for pt in range(12,68,4):
        if(pt == size):
            getattr(ui,"actionIconSize{}".format(pt)).setChecked(True)
            continue
        getattr(ui,"actionIconSize{}".format(pt)).setChecked(False)
        
#---------------------------------------------------------------

def change_font_size(fontsize):
    if(debug):mydebug(inspect.currentframe())
    
    MainWindow.mypref['fontSize']=fontsize
    load_stylesheet(MainWindow.mypref['stylesheet'])
    for pt in range(12,68,4):
        if(pt == fontsize):
            getattr(ui,"actionFontSize{}".format(pt)).setChecked(True)
            continue
        getattr(ui,"actionFontSize{}".format(pt)).setChecked(False)

#---------------------------------------------------------------
#----------------------- myTree --------------------------
#---------------------------------------------------------------

class myTar:

    #--------------------
    def __init__(self):
        if(debug):mydebug(inspect.currentframe())

        self.archive_data = io.BytesIO()
        self.archive = tarfile.open(fileobj=self.archive_data,mode='w')

    #--------------------
    def add(self,filename,mode,text):
        if(debug):mydebug(inspect.currentframe())
        
        data=text.encode('utf-8')
        s = io.BytesIO(data)
        s.seek(0)
        tarinfo = tarfile.TarInfo(name=filename)
        tarinfo.size = len(text)
        tarinfo.mode = mode
        self.archive.addfile(tarinfo=tarinfo, fileobj=s)
        s.close()
        
    #--------------------
    def close(self):
        if(debug):mydebug(inspect.currentframe())

        self.archive.close()

    #--------------------
    def get_archive_rawdata(self):
        if(debug):mydebug(inspect.currentframe())

        self.archive_data.seek(0)
        return self.archive_data.getvalue().decode("utf-8")

    #--------------------
    def close_stream(self):
        if(debug):mydebug(inspect.currentframe())

        self.archive_data.close()


        
#---------------------------------------------------------------
#----------------------- myTree --------------------------
#---------------------------------------------------------------

class myTree:

    
    #--------------------
    def __init__(self,w,**optionDict):
        if(debug):mydebug(inspect.currentframe())

        self.w = w
        self.model = QStandardItemModel()
        self.w.setModel(self.model)
        self.last_root=None


        if 'ReadOnly' in optionDict['Opts']:
            self.w.setreadOnly()

        if 'HeaderHidden' in optionDict['Opts']:
            self.w.setHeaderHidden(True)
        else:
            self.w.setHeaderHidden(False)
            
        if 'SingleSelection' in optionDict['Opts']:
            self.w.setSelectionMode(QAbstractItemView.SingleSelection)

        if 'MultiSelection' in optionDict['Opts']:
            self.w.setSelectionMode(QAbstractItemView.MultiSelection)

        if 'ExtendedSelection' in optionDict['Opts']:
            self.w.setSelectionMode(QAbstractItemView.ExtendedSelection)

        if 'DragAndDrop' in optionDict['Opts']:
            self.w.setDragDropMode(QAbstractItemView.InternalMove)
        
    #--------------------
    def get_selected(self):
        if(debug):mydebug(inspect.currentframe())

        result=[]
        
        for index in self.w.selectedIndexes():
            crawler = index.model().itemFromIndex(index)
            result.append(myTree.construct_chain(crawler,[]))

        return result

    #--------------------
    @staticmethod
    def construct_chain(crawler,a):
        if(debug):mydebug(inspect.currentframe())

        if(crawler.parent()):
            a.insert(0,crawler.text())
            a=myTree.construct_chain(crawler.parent(),a)
        else:
            a.insert(0,crawler.text())

        return a
    
    #--------------------
    def insert(self,parent,text):
        if(debug):mydebug(inspect.currentframe())

        if(parent):
            parentItem=parent
            item = QStandardItem(text)
        else:
            parentItem = self.model.invisibleRootItem()
            item = QStandardItem(text)
            self.last_root=item

        parentItem.appendRow(item)

        return item

    #--------------------
    def getlast_rootitem(self):
        if(debug):mydebug(inspect.currentframe())

        return self.last_root
    
    #--------------------
    def delete_all_rows(self):
        if(debug):mydebug(inspect.currentframe())

        for c in range(self.model.rowCount()-1,-1,-1):
            self.model.removeRow(c)

    #--------------------
    @staticmethod
    def get_top_level_parent(crawler):
        if(debug):mydebug(inspect.currentframe())
        
        parent=crawler.parent()
        if(parent):
            return(myTree.get_top_level_parent(parent))
        else:
            return crawler


    #--------------------
    def get_top_level_parent_of_selected(self):
        if(debug):mydebug(inspect.currentframe())

        for index in self.w.selectedIndexes():
            crawler = index.model().itemFromIndex(index)
            return(myTree.get_top_level_parent(crawler))
        else:
            return None


    #--------------------
    @staticmethod
    def get_childs(crawler):
        if(debug):mydebug(inspect.currentframe())

        child_list=[]            
        for r in range(crawler.rowCount()):
            child_list.append(crawler.child(r).text())
        return child_list
            
#---------------------------------------------------------------
#----------------------- class myPort ---------------------
#---------------------------------------------------------------

class myPort:

    port_dict={}

    #---------------------------------------------------------------
    
    def __init__(self,uuid,name,interfaces):
        self.uuid = uuid
        self.name = name
        interfaces=interfaces.lstrip('[')
        interfaces=interfaces.rstrip(']')
        self.interfaces = pattern_comma.split(interfaces)
        myPort.port_dict[name]=self
        
    #---------------------------------------------------------------
    @staticmethod
    def clear():
        myPort.port_dict={}

    #---------------------------------------------------------------
    @staticmethod
    def get(name):
        if(debug):mydebug(inspect.currentframe())

        return myPort.port_dict[name]

    #---------------------------------------------------------------
    @staticmethod
    def refresh(bridge_port_list):
        if(debug):mydebug(inspect.currentframe())

        myPort.clear()

        switch=ui.lineEdit_ovs_name.text()
        uuid=None
        
        if(switch):

            result=exec_and_display(['ovs-vsctl','--column=_uuid,name,interfaces','list','port'],hide_output=True)
            for line in result.splitlines():
                mpt_field=pattern_if_field.match(line)
                if(mpt_field):
                    pt_field=mpt_field.group(1)
                    pt_value=mpt_field.group(2)

                    if(pt_field == '_uuid'):
                        if(uuid):
                            #add port only if belongs to cuurent bridge
                            if(name in bridge_port_list):
                                p=myPort(uuid,name,interfaces)                                             
                                #debug_object(p)
                        uuid=pt_value
                        name=''
                    elif(pt_field == 'name'):
                        name=pt_value.replace('"',"")
                        name=name.replace("'","")
                    elif(pt_field == 'interfaces'):
                        interfaces=pt_value
            else:
                #add last port
                if(len(result)>0):
                    if(name in bridge_port_list):
                        myPort(uuid,name,interfaces)                                             

#---------------------------------------------------------------
#----------------------- class myInterface ---------------------
#---------------------------------------------------------------

class myInterface:

    interface_dict={}

    #---------------------------------------------------------------
    
    def __init__(self,uuid,name):
        self.uuid = uuid
        self.name = name
        myInterface.interface_dict[uuid]=name
        
    #---------------------------------------------------------------
    @staticmethod
    def clear():
        myInterface.interface_dict={}
    #---------------------------------------------------------------
    @staticmethod
    def getname(uuid):
        if(debug):mydebug(inspect.currentframe())

        return myInterface.interface_dict[uuid]
    #---------------------------------------------------------------
    @staticmethod
    def refresh():
        if(debug):mydebug(inspect.currentframe())

        myInterface.clear()

        switch=ui.lineEdit_ovs_name.text()
        uuid=None
        
        if(switch):
            result=exec_and_display(['ovs-vsctl','--column=_uuid,name','list','interface'],hide_output=True)
            for line in result.splitlines():
                mif_field=pattern_if_field.match(line)
                if(mif_field):
                    if_field=mif_field.group(1)
                    if_value=mif_field.group(2)

                    if(if_field == '_uuid'):
                        if(uuid): # creating last read interface. Yes name variable will exist ! 
                            i=myInterface(uuid,name) # this is not a bug !
                        uuid=if_value
                        name=''
                    elif(if_field == 'name'):
                        name=if_value.replace('"','')
                        name=name.replace("'","")

        
            #add last interface
            if(uuid):
                myInterface(uuid,name)                                             
                
        
            #print("\nDICT=",myInterface.interface_dict)

        
#---------------------------------------------------------------
#----------------------- class myCompleter ---------------------
#---------------------------------------------------------------

class myCompleter():
    
    def __init__(self,compListKey):
        self.completer = QCompleter()
        self.completer.setFilterMode(QtCore.Qt.MatchContains)
        self.model = QStringListModel()
        self.model.setStringList(autocomplete[compListKey])            
        self.completer.setModel(self.model)

    def linkTo(self,widget):
        widget.setCompleter(self.completer)

#---------------------------------------------------------------
#----------------------- class ItemDelegate ---------------------
#---------------------------------------------------------------


class ItemDelegate(QItemDelegate):
    
    def __init__(self, parent,myCompleter):
        if(debug):mydebug(inspect.currentframe())

        self.myCompleter=myCompleter
        super(ItemDelegate, self).__init__(parent)

    #----------------------------------------
    
    def createEditor(self, parent, option, index):
        if(debug):mydebug(inspect.currentframe())

        edit = QtWidgets.QLineEdit(parent)

        if(self.myCompleter):
            self.myCompleter.linkTo(edit)
            
        return edit
    
#---------------------------------------------------------------
#----------------------- class Mytrace --------------------------
#---------------------------------------------------------------

class Mytrace:

    tracedict={}

    #--------------------
    def __init__(self,name,**optionsdict):
        if(debug):mydebug(inspect.currentframe())

        self.name=name
        Mytrace.tracedict[name]=self
        
        self.condlist=optionsdict['condlist']
        self.actionlist=optionsdict['actionlist']
        self.packet=optionsdict.get('packet',None)
        self.ctlist=optionsdict['ctlist']
        self.optlist=optionsdict['optlist']

    #--------------------
    @staticmethod
    def remove(name):
        if(debug):mydebug(inspect.currentframe())

        Mytrace.tracedict[name]
        del(Mytrace.tracedict[name])

    #--------------------
    @staticmethod
    def removeAll():
        if(debug):mydebug(inspect.currentframe())

        Mytrace.tracedict={}


    #--------------------
    @staticmethod
    def getall():
        if(debug):mydebug(inspect.currentframe())

        return Mytrace.tracedict.values()

    #--------------------
    @staticmethod
    def get(name):
        if(debug):mydebug(inspect.currentframe())
        
        return Mytrace.tracedict[name]

#---------------------------------------------------------------
#----------------------- class numberSortModel -----------------
#---------------------------------------------------------------
class MySortModel(QSortFilterProxyModel):

    def lessThan(self, left, right):

        if(self.sortColumn()==0): #different algo for column 0
            lvalue = str(left.data())
            rvalue = str(right.data())
        else:
            lvalue = float(left.data())
            rvalue = float(right.data())

        return lvalue < rvalue

        
#---------------------------------------------------------------
#----------------------- class MytableV --------------------------
#---------------------------------------------------------------

class MytableV:

    def __init__(self,widget,**optionDict):
        if(debug):mydebug(inspect.currentframe())

        self.w=widget
        self.readOnly=False
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(optionDict['Header_name'])
        self.w.setModel(self.model)
        self.w.setEditTriggers(QAbstractItemView.NoEditTriggers)

        hheader = self.w.horizontalHeader()
        hheader.setSectionResizeMode(QHeaderView.Stretch);

        self.w.verticalHeader().hide()

        self.proxy = MySortModel()
        self.proxy.setSourceModel(self.model)

        self.w.setModel(self.proxy)
        self.w.setSortingEnabled(True)

        if 'Header' in optionDict:
            for h_index,h_value in optionDict['Header'].items():
                if(h_value=='ResizeToContents'):
                    hheader.setSectionResizeMode(h_index,QHeaderView.ResizeToContents)
                elif(h_value=='Stretch'):
                    hheader.setSectionResizeMode(h_index,QHeaderView.Stretch)
                elif(h_value=='Hidden'):
                    print("Hiding colum {} of widget {}".format(h_index,self.w))
                    self.w.setColumnHidden(h_index,True)
                    
        if 'AdjustToContents' in optionDict['Opts']:
            self.w.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)

    #--------------------
    def show(self):
        self.w.view.show()
            
    #--------------------
    def new_row(self,item_list):

        row=[]
        for item in item_list:
            row.append(QStandardItem(str(item)))
        self.model.appendRow(row)

    #--------------------
    def enableSorting(self,flag):
        self.w.setSortingEnabled(flag)
            
    #--------------------
    def rowcount(self):
        return self.model.rowCount()
        
    #--------------------
    def delete_all_rows(self):
        for rownumber in range(self.rowCount(),0,-1):
            self.delete_row(rownumber-1)
            
    #--------------------

    def delete_row(self,pos):
        self.model.removeRow(pos) 
    

    #--------------------
    def rowCount(self):
        return self.model.rowCount()

    #--------------------
    def resize(self):
        if(debug):mydebug(inspect.currentframe())
        
        self.w.resizeColumnsToContents()
        self.w.resizeRowsToContents()

    #---------------------------------------------------------------

    def hide_table_column(self,**options):
        if(debug):mydebug(inspect.currentframe())

        col=options.get('col')
        
        if('checkbox' in options):
            widget_checkbox=options.get('checkbox')
            if(widget_checkbox.isChecked()):
                self.w.setColumnHidden(col,False)
            else:
                self.w.setColumnHidden(col,True)
        elif('hide' in options):
            self.w.setColumnHidden(col,options['hide'])

        
#---------------------------------------------------------------
#----------------------- class Mytable --------------------------
#---------------------------------------------------------------

class Mytable:
    
    last_row_entered=None
    
    #--------------------
    def __init__(self,widget,**optionDict):
        if(debug):mydebug(inspect.currentframe())

        self.w=widget
        self.subtable={}
        self.subtables_list=[]
        self.father_row=-1
        self.readOnly=False
        self.tag=None
        
        hheader = self.w.horizontalHeader()
        hheader.setSectionResizeMode(QHeaderView.Stretch);

        if 'ReadOnly' in optionDict['Opts']:
            self.setreadOnly() 
            #self.w.setreadOnly() 'QTableWidget' object has no attribute 'setreadOnly'

        if 'SelectRows' in optionDict['Opts']:
            self.w.setSelectionBehavior(QAbstractItemView.SelectRows)
            
        if 'SingleSelection' in optionDict['Opts']:
            self.w.setSelectionMode(QAbstractItemView.SingleSelection)

        if 'MultiSelection' in optionDict['Opts']:
            self.w.setSelectionMode(QAbstractItemView.MultiSelection)

        if 'ExtendedSelection' in optionDict['Opts']:
            self.w.setSelectionMode(QAbstractItemView.ExtendedSelection)
            
            
        if 'Header' in optionDict:
            for h_index,h_value in optionDict['Header'].items():
                if(h_value=='ResizeToContents'):
                    hheader.setSectionResizeMode(h_index,QHeaderView.ResizeToContents)
                elif(h_value=='Stretch'):
                    hheader.setSectionResizeMode(h_index,QHeaderView.Stretch)
                elif(h_value=='Hidden'):
                    print("Hiding colum {} of widget {}".format(h_index,self.w))
                    self.w.setColumnHidden(h_index,True)
                    
        if 'AdjustToContents' in optionDict['Opts']:
            self.w.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)


    #--------------------
    def setTag(self,**options):
        self.tag=[]

        if('row' in options):
            row=options['row']
        else:
            row=self.w.currentRow()
            
        if(row>=0):
            for c in options['cols']:
                self.tag.append(self.getcurrenttext(c))

    #--------------------
    def isRowTagged(self,**options):

        if(self.w.currentRow()>=0):
            if(self.tag):
                listetags=[self.getcurrenttext(c) for c in options['cols']]
                if(listetags == self.tag):
                    return True

        return False
            
    #--------------------
    def deselect(self):

        self.w.clearSelection()

    #--------------------
    def select(self,row,col):

        self.w.setCurrentCell(row,col)

    #--------------------
    def isreadOnly(self):

        return self.readOnly


        
    #--------------------
    def setreadOnly(self):
        self.readOnly=True
        self.w.setEditTriggers(QAbstractItemView.NoEditTriggers);

    #--------------------
    def setreadWrite(self):
        self.readOnly=False
        self.w.setEditTriggers(QAbstractItemView.AllEditTriggers);

    #--------------------
    def rowcount(self):
        return self.w.rowCount()
        
    #--------------------
    def new_row(self,*pos):

        if(pos):
            rowpos=pos[0]
        else:
            # no row selected
            if(self.w.currentRow()<0):
                #choose last one
                rowpos=self.w.rowCount()
            else:
                rowpos = self.w.currentRow()+1

        self.w.insertRow(rowpos)
        self.subtable[rowpos]={}
        
        return(rowpos)

    #--------------------

    def get_colnames(self):
        return [ self.w.horizontalHeaderItem(c).text() for c in range(0,self.w.columnCount())]

    #--------------------

    def get_rowtext(self,r):
        return [ self.gettext(r,c) for c in range(0,self.w.columnCount())]

    #--------------------

    def get_coltext(self,c):
        return [ self.gettext(r,c) for r in range(0,self.w.rowCount())]
        
    #--------------------

    def get_allrowtext(self):
        liste=[]
        for r in range(0,self.w.rowCount()):
            liste.append([ self.gettext(r,c) for c in range(0,self.w.columnCount())])

        return liste
    
    #--------------------

    def get_tabletext(self):
        headers=self.get_colnames()
        return [ list(filter(lambda x:x!=None,
                             map(lambda h,r:"{}={}".format(h,r) if(r) else None,
                                 headers,self.get_rowtext(rownumber)))) for rownumber in range(0,self.w.rowCount())]

    #--------------------
    def delete_all_rows(self):
        for rownumber in range(self.w.rowCount(),0,-1):

            #removing of subtable inside tables
            if rownumber in self.subtable.keys():
                for colnumber in self.subtable[rownumber]:
                    if(isinstance(self.subtable[rownumber][colnumber],QtWidgets.QTableWidget)):
                        self.removeCellWidget(rownumber,colnumber)
                        self.subtable[rownumber][colnumber]=None
                        
            self.delete_row(rownumber-1)
            
        self.subtable={}
        self.subtables_list=[]

    #--------------------

    def delete_row(self,*pos):
        if(pos):
            r=pos[0]
        else:
            r=self.w.currentRow()

        if(r>=0):
            self.w.removeRow(r)
            if(r>=1):
                self.w.setCurrentCell(r-1,0)


    #--------------------

    def up_row(self):

        r=self.w.currentRow()
        if(r>=1):
            self.new_row(r-1)
            self.copyrow(r+1,r-1)
            self.delete_row(r+1)
            self.w.setCurrentCell(r-1,0)

    #--------------------

    def down_row(self):

        r=self.w.currentRow()
        if(r>=0):
            if(r<(self.w.rowCount()-1)):
                self.new_row(r+2)
                self.copyrow(r,r+2)
                self.delete_row(r)
                self.w.setCurrentCell(r+1,0)
                
    #--------------------
    def get_selected_rows(self):
        if(debug):mydebug(inspect.currentframe())
        
        return [index.row() for index in self.w.selectionModel().selectedRows()]

    #--------------------
    def get_all_but_current_rownumber(self):
        if(debug):mydebug(inspect.currentframe())
        
        row_current=self.w.currentRow()

        l=[r for r in range(0,self.w.rowCount()) if r != row_current]

        return l
            
    #--------------------
    def get_all_but_current_subtable(self,widget,colpos):
        if(debug):mydebug(inspect.currentframe())

        l1=[]
        l2=[]
        
        for c in range(0,self.w.rowCount()):
            st=self.get_subtable(c,colpos)
            if(st!=None):
                if(st!= widget):
                    l1.append([c,st])
                else:
                    l2.append([c,st])

        return [l1,l2]
            
    
    #--------------------
    def getcurrent_rownumber(self):

        row=self.w.currentRow()
        return row

    #--------------------
    def getlast_rownumber(self):

        return self.w.rowCount()-1

    #--------------------
    def rowCount(self):
    
        return self.w.rowCount()

    #--------------------
    def getcurrenttext(self,*c):

        row=self.w.currentRow()
        if(row<0):
            return ''
        
        if(c):
            col=c[0]
        else:
            col=self.w.currentColumn()

        return self.gettext(row,col)

    #--------------------

    def gettext(self,r,c):

        if(self.w.item(r,c)):
            return self.w.item(r,c).text()
        else:
            return ''

    #--------------------

    def settext(self,r,c,text):
        if(debug):mydebug(inspect.currentframe())

        if(self.w.item(r,c)):
            self.w.item(r,c).setText(text)
        else:
            self.w.setItem(r,c, QtWidgets.QTableWidgetItem(text))

    #--------------------

    def copyrow(self,r1,r2):

        #self.showtype()
        for c in range(0,self.w.columnCount()):
            self.settext(r2,c,self.gettext(r1,c))

    #--------------------

    def showtype(self):

        for r in range(0,self.w.columnCount()):
            for c in range(0,self.w.columnCount()):
                print("SHOW R1={} col={}  ITEM={}".format(r,c,self.w.item(r,c)))

    #--------------------
    def resize(self):
        if(debug):mydebug(inspect.currentframe())
        
        self.w.resizeColumnsToContents()
        self.w.resizeRowsToContents()

    #--------------------
        
    def get_cellwidget(self,rowpos,colpos):
        if(debug):mydebug(inspect.currentframe())

        return self.w.cellWidget(rowpos,colpos)
    
    #--------------------
    def get_subtable(self,rowpos,colpos):
        if(debug):mydebug(inspect.currentframe())

        return self.subtable[rowpos][colpos]

    #--------------------
    def delegate_col(self,col,compl):
        if(debug):mydebug(inspect.currentframe())
        self.w.setItemDelegateForColumn(col,ItemDelegate(self.w,compl))
            
    #--------------------

    def clear(self):
        if(debug):mydebug(inspect.currentframe())
        self.w.clear()

    #---------------------------------------------------------------

    def hide_table_column(self,**options):
        if(debug):mydebug(inspect.currentframe())

        col=options.get('col')
        
        if('checkbox' in options):
            widget_checkbox=options.get('checkbox')
            if(widget_checkbox.isChecked()):
                self.w.setColumnHidden(col,False)
            else:
                self.w.setColumnHidden(col,True)
        elif('hide' in options):
            self.w.setColumnHidden(col,options['hide'])

#---------------------------------------------------------------
#----------------------- class Mymgmt --------------------------
#---------------------------------------------------------------

class Mymgmt:
    
    mgmtdict={}

    mgmtcurrent=None
    lastfile=None
    
    #--------------------

    def __init__(self,**options):
        if(debug):mydebug(inspect.currentframe())

        self.nickname=options.get('nickname',None)

        if(not self.nickname):
            return
            
        self.comm=options.get('comm','local')
        self.command_timeout=options.get('command_timeout','30')
        self.custom_script=options.get('custom_script',None)
        self.custom_script_args=options.get('custom_script_args','')
        self.hostname=options.get('hostname',None)
        self.ssh_connect_timeout=options.get('ssh_connect_timeout','10')
        self.ssh_key=options.get('ssh_key',None)
        self.ssh_key_type=options.get('ssh_key_type','rsa')
        self.ssh_username=options.get('ssh_username',None)
        self.ssh_password=options.get('ssh_password',None)
        self.ssh_connect_timeout=options.get('self.ssh_connect_timeout','10')
        self.sudo_enable=options.get('sudo_enable',False)
        self.custom_enable=options.get('custom_enable',False)
        self.switch=options.get('switch',None)
        self.force_of=options.get('force_of','openflow14')
        self.of_nostats=options.get('of_nostats','original')
        self.docker_release=options.get('docker_release','>=1.13')
        self.tables={}
        
        self.setdefault()
        
        Mymgmt.mgmtdict[self.nickname]=self
        if(self.nickname!='_dot_mgmt'):
            self.set_current()

    #--------------------
    @staticmethod
    def get_current_nickname():
        if(debug):mydebug(inspect.currentframe())

        return Mymgmt.mgmtcurrent

    #--------------------
    @staticmethod
    def create_system_mgmt():
        if(debug):mydebug(inspect.currentframe())

        Mymgmt(nickname='_dot_mgmt',comm='local')

    #--------------------
    @staticmethod
    def get_current_profile_attr(attr):
        if(debug):mydebug(inspect.currentframe())

        nickname=Mymgmt.get_current_nickname()
        if(nickname):
            profile=Mymgmt.get_profile_for_nickname(nickname)
            return getattr(profile,attr)
        else:
            return None

    #--------------------
    def setdefault(self):
        if(debug):mydebug(inspect.currentframe())

        if(not self.ssh_connect_timeout): self.ssh_connect_timeout='10'
        if(not self.command_timeout): self.command_timeout='30'
        if(not self.comm): self.comm='local'
        if(not self.ssh_key_type): self.ssh_key_type='rsa'
    
    #--------------------
    def modify(self,**options):
        if(debug):mydebug(inspect.currentframe())

        self.nickname=options.get('nickname',None)
        self.comm=options.get('comm','local')
        self.command_timeout=options.get('command_timeout','30')
        self.custom_script=options.get('custom_script',None)
        self.custom_script_args=options.get('custom_script_args','')
        self.hostname=options.get('hostname',None)
        self.ssh_connect_timeout=options.get('ssh_connect_timeout','10')
        self.ssh_key=options.get('ssh_key',None)
        self.ssh_key_type=options.get('ssh_key_type','rsa')
        self.ssh_username=options.get('ssh_username',None)
        self.ssh_password=options.get('ssh_password',None)
        self.sudo_enable=options.get('sudo_enable',False)
        self.custom_enable=options.get('custom_enable',False)
        self.switch=options.get('switch',None)
        self.force_of=options.get('force_of','openflow14')
        self.of_nostats=options.get('of_nostats','original')
        self.docker_release=options.get('docker_release','>=1.13')
        self.setdefault()

    #--------------------
    def set_current(self):
        if(debug):mydebug(inspect.currentframe())
        
        Mymgmt.mgmtcurrent=self.nickname
        ui.lineEdit_ovs_profile.setText(self.nickname)
        
    #--------------------
    @staticmethod
    def get_profile_for_nickname(name):
        if(debug):mydebug(inspect.currentframe())
        
        if(name in Mymgmt.mgmtdict):
            return Mymgmt.mgmtdict[name]
        else:
            return None

    #--------------------
    @staticmethod
    def getall():
        if(debug):mydebug(inspect.currentframe())

        return Mymgmt.mgmtdict.values()
    
    #--------------------
    @staticmethod
    def get_current_profile():
        if(debug):mydebug(inspect.currentframe())
        
        return Mymgmt.mgmtdict[Mymgmt.mgmtcurrent]


    #--------------------
    @staticmethod
    def remove(name):
        if(debug):mydebug(inspect.currentframe())

        Mymgmt.mgmtdict[name]
        del(Mymgmt.mgmtdict[name])

    #--------------------
    @staticmethod
    def removeAll():
        if(debug):mydebug(inspect.currentframe())

        Mymgmt.mgmtdict={}

    #--------------------
    @staticmethod
    def remember_last_file_name(filename):
        if(debug):mydebug(inspect.currentframe())

        Mymgmt.lastfile=filename
        MainWindow.mypref['mgmt']=filename

#---------------------------------------------------------------
#----------------------- class MyDockerNet --------------------------
#---------------------------------------------------------------

class MyDockerNet:

    dic={}
    uid=1
    
    #--------------------

    def __init__(self,interface,net_type,ip,network,gateway):
        if(debug):mydebug(inspect.currentframe())
        
        self.interface=interface

        self.modify(net_type,ip,network,gateway)
        
        self.uid=str(MyDockerNet.uid)
        MyDockerNet.uid=MyDockerNet.uid+1
        MyDockerNet.dic[self.uid]=self

    #---------------------------------------------------------------
    def modify(self,net_type,ip,network,gateway):

        if(net_type=='addr' or net_type=='ad'):
            self.ip=ip
            self.net_type='ad'
        else:
            self.net=network
            self.gw=gateway
            self.net_type='rt'

    
    #---------------------------------------------------------------
    @staticmethod
    def clear_net_by_uid(uid):
        MyDockerNet.dic[uid]=None

    #---------------------------------------------------------------
    @staticmethod
    def clear():
        MyDockerNet.dic={}
        MyDockerNet.uid=1
        docker_net_table.delete_all_rows()

    #---------------------------------------------------------------
    @staticmethod
    def delete(uid):
      MyDockerNet.dic[uid]=None
  
    #---------------------------------------------------------------
    @staticmethod
    def mem_order(interface_uid):
      if(debug):mydebug(inspect.currentframe())

      MyDockerIf.dic[interface_uid].net=docker_net_table.get_coltext(0)

    #---------------------------------------------------------------
    @staticmethod
    def populate_table(interface):
        if(debug):mydebug(inspect.currentframe())

        for net_uid in MyDockerIf.dic[interface].net:
            net=MyDockerNet.dic[net_uid]
            net.populate_line()

    #---------------------------------------------------------------
    def populate_line(self,**options):
        if(debug):mydebug(inspect.currentframe())        

        rowpos=options.get('row',-1)
        if(rowpos < 0):
            rowpos=docker_net_table.new_row()
            
        docker_net_table.settext(rowpos,0,self.uid)
        if(self.net_type=='ad'):
            docker_net_table.settext(rowpos,1,'ad')
            docker_net_table.settext(rowpos,2,self.ip)
        else:
            docker_net_table.settext(rowpos,1,'rt')
            docker_net_table.settext(rowpos,3,self.net)
            docker_net_table.settext(rowpos,4,self.gw)
#---------------------------------------------------------------
#----------------------- MyStats --------------------------
#---------------------------------------------------------------

class MyStats:

    stats_dict={}
    if_list=[]
    mgmt_nickname=''
    
    #--------------------
    def __init__(self,**options):

        self.name=options.get('name')
        self.stats=string_to_dict(options.get('stats'))
        self.set_delta_origin()
        MyStats.stats_dict[self.name]=self

        
    #--------------------
    def remember(self,**options):
        self.memstats=string_to_dict(options.get('stats'))

    #--------------------
    @staticmethod
    def add_or_modify(**options):
        name=options.get('name')
        stats=options.get('stats')
        if(name in MyStats.stats_dict):
            s=MyStats.stats_dict[name]
            s.stats=string_to_dict(stats)
        else:
            s=MyStats(name=name,stats=stats)

        s.time=time.time()

        #for some interfaces(tunnel) some fields are missing. We populate them with 0
        for field in ('collisions','rx_bytes','rx_crc_err','rx_dropped','rx_errors','rx_frame_err','rx_over_err','rx_packets','tx_bytes','tx_dropped','tx_errors','tx_packets'):
            if(not field in s.stats):
                s.stats[field]=0
                    
        return s

    #--------------------
    @staticmethod
    def set_delta_origin_all_interfaces():
        for i in MyStats.stats_dict:
            MyStats.stats_dict[i].set_delta_origin()
            
    #--------------------
    def set_delta_origin(self):
        self.memstats=self.stats
        self.delta_time=time.time()

    #--------------------
    @staticmethod
    def set_selected_interfaces(**options):
        MyStats.if_list=options.get('if_list')
        MyStats.mgmt_nickname=options.get('nickname')
        
    #--------------------
    def delta(self):
        delta={}
        for k in self.stats:
            delta[k]=str(int(self.stats[k])-int(self.memstats[k]))

        return delta
    #--------------------
    def deltasec(self):
        
        delta={}
        timediff=self.time-self.delta_time
        if(timediff<=0):
            for k in self.stats:
                delta[k]='-1'
        else:
            for k in self.stats:
                delta[k]=str((int(self.stats[k])-int(self.memstats[k]))/timediff)

        return delta
            
    #---------------------------------------------------------------
    @staticmethod
    def clear():
        MyStats.stats_dict={}
        MyStats.if_list=[]
        MyStats.mgmt_nickname=''
        
        
#---------------------------------------------------------------
#----------------------- class MyDockerIf --------------------------
#---------------------------------------------------------------

class MyDockerIf:

    dic={}
    uid=1
    
    #--------------------
    def __init__(self,ifext,ifint,vlan,mac,of):
        if(debug):mydebug(inspect.currentframe())
        self.ifext=ifext
        self.ifint=ifint
        self.vlan=vlan
        self.mac=mac
        self.of=of
        self.net=[]
        self.uid=str(MyDockerIf.uid)
        MyDockerIf.uid=MyDockerIf.uid+1
        MyDockerIf.dic[self.uid]=self

    #---------------------------------------------------------------
    @staticmethod
    def clear_if_by_uid(uid):
        MyDockerIf.dic[uid]=None

    #--------------------
    @staticmethod
    def clear():

        MyDockerIf.dic={}
        MyDockerIf.uid=1
        docker_if_table.delete_all_rows()
        
    #--------------------
    def populate_line(self,**options):

        rowpos=options.get('row',-1)
        if(rowpos < 0):
            rowpos=docker_if_table.new_row()
            
        for idx,f in enumerate(['uid','ifext','ifint','vlan','mac','of']):
            docker_if_table.settext(rowpos,idx,getattr(self,f,''))
        
#---------------------------------------------------------------
#----------------------- class Mylist --------------------------
#---------------------------------------------------------------

class Mylist:

    #--------------------

    def __init__(self,widgetlist):
        self.w=widgetlist

    #--------------------

    def addlist(self,newitemlist):
        for newitem in newitemlist:
            item = QtWidgets.QListWidgetItem(newitem)
            self.w.addItem(item)

    #--------------------

    def delete(self):
        r=self.w.currentRow()
        if(r>=0):
            print ("row=",r," val=",self.get())
            item=self.w.takeItem(r)
            item=None

    #--------------------

    def get(self):
        if(self.w.currentItem()):
            return self.w.currentItem().text()
        else:
            return None

    #--------------------

    def getrow(self):
        if(self.w.currentItem()):
            return self.w.currentRow()
        else:
            return None

    #--------------------

    def select(self,row):
        self.w.setCurrentRow(row)


    #--------------------

    def clear(self):
        self.w.clear()
        

#######################################################################################
################                     MAIN                   ###########################
#######################################################################################

if __name__ == "__main__":
    
    autocomplete={
        'kvm_misc':[
            'connect',
            'name',
            'memory',
            'vcpus',
            'cpu',
            'metadata',
            'cdrom',
            'location',
            'pxe',
            'import',
            'livecd',
            'extra-args',
            'initrd-inject',
            'os-variant',
            'boot',
            'idmap',
            'disk',
            'network',
            'graphics',
            'controller',
            'input',
            'serial',
            'parallel',
            'channel',
            'console',
            'hostdev',
            'filesystem',
            'sound',
            'watchdog',
            'video',
            'smartcard',
            'redirdev',
            'memballoon',
            'tpm',
            'rng',
            'panic',
            'memdev',
            'security',
            'numatune',
            'memtune',
            'blkiotune',
            'memorybacking',
            'features',
            'clock',
            'pm',
            'events',
            'resource',
            'sysinfo',
            'qemu-commandline',
            'hvm',
            'paravirt',
            'container',
            'virt-type',
            'arch',
            'machine',
            'autostart',
            'transient',
            'wait',
            'noautoconsole',
            'noreboot',
            'print-xml',
            'dry-run',
            'check',
            'quiet',
            'debug',
            ],
        'dockerfile':[
            'escape ',
            'FROM ',
            'RUN ',
            'ARG ',
            'CMD ',
            'LABEL ',
            'EXPOSE ',
            'ENV ',
            'ADD ',
            'COPY ',
            'ENTRYPOINT ',
            'VOLUME ',
            'USER ',
            'WORKDIR ',
            'ONBUILD ',
            'STOPSIGNAL ',
            'HEALTCHECK ',
            'SHELL ',
        ],
        'ofgroup_params':[
            'watch_port:',
            'watch_group:',
            'weight:',
        ],
        'actions_val':[
            'NXM_NX_CT_IPV6_DST',
            'NXM_NX_CT_IPV6_SRC',
            'NXM_NX_CT_LABEL',
            'NXM_NX_CT_MARK',
            'NXM_NX_CT_NW_DST',
            'NXM_NX_CT_NW_PROTO',
            'NXM_NX_CT_NW_SRC',
            'NXM_NX_CT_STATE',
            'NXM_NX_CT_TP_DST',
            'NXM_NX_CT_TP_SRC',
            'NXM_NX_CT_ZONE',
            'NXM_NX_PKT_MARK',
            'NXM_NX_REG0',
            'NXM_NX_REG0..to..15',
            'NXM_NX_TUN_FLAGS',
            'NXM_NX_TUN_GBP_FLAGS',
            'NXM_NX_TUN_GBP_ID',
            'NXM_NX_TUN_ID',
            'NXM_NX_TUN_IPV4_DST',
            'NXM_NX_TUN_IPV4_SRC',
            'NXM_NX_TUN_IPV6_DST',
            'NXM_NX_TUN_IPV6_SRC',
            'NXM_NX_TUN_METADATA0',
            'NXM_NX_XXREG0',
            'NXM_NX_XXREG0..to..3',
            'NXM_OF_ETH_DST',
            'NXM_OF_ETH_SRC',
            'NXM_OF_ETH_TYPE',
            'NXM_OF_IN_PORT',
            'NXM_OF_VLAN_TCI',
        ],
        'of_cond': [
            'actset_output=',
            'arp',
            'arp_op=',
            'arp_sha=',
            'arp_spa=',
            'arp_tha=',
            'arp_tpa=',
            'conj_id=',
            'cookie=',
            'ct_ipv6_dst=',
            'ct_ipv6_src=',
            'ct_mark=',
            'ct_nw_dst=',
            'ct_nw_proto=',
            'ct_nw_src=',
            'ct_state=',
            'ct_tp_dst=',
            'ct_tp_src=',
            'ct_zone=',
            'dl_dst=',
            'dl_src=',
            'dl_type=',
            'dl_vlan=',
            'dl_vlan_pcp=',
            'eth',
            'eth_dst=',
            'eth_src=',
            'eth_type=',
            'eth_type=',
            'hard_timeout=',
            'icmp',
            'icmp6',
            'icmp_code=',
            'icmp_type=',
            'icmpv6_code=',
            'icmpv6_type=',
            'idle_timeout=',
            'importance=',
            'in_port=',
            'in_port_oxm=',
            'ip',
            'ip_dscp=',
            'ip_dst=',
            'ip_ecn=',
            'ip_frag=',
            'ip_proto=',
            'ip_src=',
            'ipv6',
            'ipv6_dst=',
            'ipv6_label=',
            'ipv6_src=',
            'metadata=',
            'mpls',
            'mpls_bos=',
            'mpls_label=',
            'mpls_tc=',
            'mpls_ttl=',
            'mplsm',
            'nd_sll=',
            'nd_target=',
            'nd_tll=',
            'nsh_c1=',
            'nsh_c2=',
            'nsh_c3=',
            'nsh_c4=',
            'nsh_flags=',
            'nsh_mdtype=',
            'nsh_np=',
            'nsh_si=',
            'nsh_spi=',
            'nshc1=',
            'nshc2=',
            'nshc3=',
            'nshc4=',
            'nsi=',
            'nsp=',
            'nw_dst=',
            'nw_ecn=',
            'nw_proto=',
            'nw_src=',
            'nw_tos=',
            'nw_ttl=',
            'packet_type=',
            'pkt_mark=',
            'priority=',
            'rarp',
            'reg0=',
            'reg1=',
            'reg2=',
            'reg3=',
            'reg4=',
            'reg5..to..reg15=',
            'sctp',
            'sctp6',
            'sctp_dst=',
            'sctp_src=',
            'skb_priority=',
            'table=',
            'tcp',
            'tcp6',
            'tcp_dst=',
            'tcp_flags=',
            'tcp_src=',
            'tp_dst=',
            'tp_src=',
            'tun_dst=',
            'tun_flags=',
            'tun_gbp_flags=',
            'tun_gbp_id    =',
            'tun_id=',
            'tunnel_id=',
            'tun_ipv6_dst=',
            'tun_ipv6_src=',
            'tun_metadata0=',
            'tun_metadata1=',
            'tun_metadata10..to..63=',
            'tun_metadata2=',
            'tun_metadata3=',
            'tun_metadata4=',
            'tun_metadata5=',
            'tun_metadata6=',
            'tun_metadata7=',
            'tun_metadata8=',
            'tun_metadata9=',
            'tun_src=',
            'tunnel_id=',
            'udp',
            'udp6',
            'udp_dst=',
            'udp_src=',
            'vlan_pcp=',
            'vlan_tci=',
            'vlan_vid=',
            'xreg0=',
            'xreg1=',
            'xreg2=',
            'xreg3=',
            'xreg4=',
            'xreg5=',
            'xreg6=',
            'xreg7=',
            'xxreg0=',
            'xxreg1=',
            'xxreg2=',
            'xxreg3=',
        ],
        'of_action':[
            'all',
            'bundle(',
            'bundle_load(',
            'clear_actions',
            'clone(',
            'conjunction',
            'conjunction(',
            'controller',
            'controller(',
            'controller:',
            'ct',
            'ct(',
            'ct_clear',
            'dec_mpls_ttl',
            'dec_ttl',
            'dec_ttl(',
            'decap(',
            'drop',
            'encap(',
            'enqueue:',
            'exit',
            'fin_timeout(',
            'flood',
            'goto_table:',
            'group:',
            'in_port',
            'learn(',
            'load:',
            'local',
            'meter:',
            'mod_dl_dst:',
            'mod_dl_src:',
            'mod_nw_dst:',
            'mod_nw_ecn:',
            'mod_nw_src:',
            'mod_nw_tos:',
            'mod_nw_ttl:',
            'mod_tp_dst:',
            'mod_tp_src:',
            'mod_vlan_pcp:',
            'mod_vlan_vid:',
            'move:',
            'multipath(',
            'normal',
            'note:',
            'output(',
            'output:',
            'pop:',
            'pop_mpls',
            'pop_queue',
            'push:',
            'push_mpls:',
            'push_vlan:',
            'resubmit(',
            'resubmit:',
            'sample(',
            'set_field:',
            'set_mpls_label:',
            'set_mpls_tc:',
            'set_mpls_ttl:',
            'set_queue:',
            'set_tunnel64:',
            'set_tunnel:',
            'strip_vlan',
            'write_actions',
            'write_metadata:',
        ],
    }

    
    

    old_selected_port_row=-1

    #print("opening preferences:",prefDir.file('default'))
    
    compl_cond=myCompleter('of_cond')
    compl_action=myCompleter('of_action')
    compl_of_groups_params=myCompleter('ofgroup_params')
    compl_dockerfile=myCompleter('dockerfile')
    compl_misc_kvm=myCompleter('kvm_misc')
    
    kvm_virt_disk_table=Mytable(ui.tableWidget_kvm_virt_disk,Opts=['SelectRows','SingleSelection'],Header={1:'ResizeToContents',2:'ResizeToContents',3:'ResizeToContents',4:'ResizeToContents',5:'ResizeToContents'})
    kvm_virt_misc_table=Mytable(ui.tableWidget_kvm_virt_misc,Opts=['SelectRows','SingleSelection'],Header={0:'Stretch',1:'Stretch'})
    kvm_virt_net_table=Mytable(ui.tableWidget_kvm_virt_network,Opts=['SelectRows','SingleSelection'],Header={2:'ResizeToContents',3:'ResizeToContents'})
    kvm_pg_table=Mytable(ui.tableWidget_kvm_pg,Opts=['SelectRows','SingleSelection'],Header={0:'ResizeToContents',1:'ResizeToContents',2:'ResizeToContents'})
    queue_table=Mytable(ui.tableWidget_qos_queue,Opts=['SelectRows','SingleSelection'],Header={1:'ResizeToContents',2:'ResizeToContents',3:'ResizeToContents',4:'ResizeToContents',5:'ResizeToContents'})
    of_table=Mytable(ui.tableWidget_of,Opts=['SelectRows','SingleSelection'],Header={0:'ResizeToContents'})
    ofgroups_table=Mytable(ui.tableWidget_ofgroups,Opts=['SelectRows','SingleSelection'],Header={0:'ResizeToContents'})
    ofcond_table=Mytable(of_ui.tableWidget_of_cond,Opts=['SingleSelection'],Header={})
    ofaction_table=Mytable(of_ui.tableWidget_of_actions,Opts=['SingleSelection'],Header={})
    oftrace_table=Mytable(oftrace_ui.tableWidget_of_trace,Opts=['SingleSelection'],Header={})
    ofgroup_table=Mytable(ui.tableWidget_ofgroups,Opts=['SingleSelection'],Header={0:'ResizeToContents',1:'ResizeToContents'})
    ofgroup_buckets_table=Mytable(ofgroup_ui.tableWidget_ofgroup_buckets,Opts=['SelectRows','SingleSelection','ReadOnly'],Header={0:'ResizeToContents'})
    ofgroup_params_table=Mytable(ofgroup_ui.tableWidget_ofgroup_params,Opts=['SelectRows','SingleSelection'],Header={})
    mgmt_table=Mytable(ui.tableWidget_mgmt,Opts=['SelectRows','SingleSelection','ReadOnly'],Header={0:'ResizeToContents',1:'ResizeToContents',3:'ResizeToContents',4:'ResizeToContents'})
    dockerimage_table=Mytable(ui.tableWidget_dockerimage,Opts=['SelectRows','SingleSelection','ReadOnly'],Header={1:'ResizeToContents',2:'ResizeToContents',3:'ResizeToContents',4:'ResizeToContents'})
    dockerps_table=Mytable(ui.tableWidget_dockerps,Opts=['SelectRows','ExtendedSelection','ReadOnly'],Header={2:'ResizeToContents',3:'ResizeToContents',4:'ResizeToContents',5:'ResizeToContents',6:'ResizeToContents'})
    dockerfile_table=Mytable(ui.tableWidget_dockerfile,Opts=['SingleSelection'],Header={0:'ResizeToContents'})
    mirror_table=Mytable(ui.tableWidget_mirrors,Opts=['SelectRows','SingleSelection'],Header={0:'ResizeToContents'})
    
    docker_if_table=Mytable(ui.tableWidget_docker_if,Opts=['SelectRows','SingleSelection'],Header={0:'Hidden',1:'ResizeToContents',2:'ResizeToContents',3:'ResizeToContents',4:'Stretch',5:'ResizeToContents'})
    docker_net_table=Mytable(ui.tableWidget_docker_net,Opts=['SelectRows','SingleSelection'],Header={0:'Hidden',1:'ResizeToContents',2:'Stretch',3:'Stretch',4:'Stretch'})
    stats_table=MytableV(stats_ui.tableView_stats,Opts=['SelectRows','SingleSelection'],Header={0:'Stretch',1:'ResizeToContents',2:'ResizeToContents',3:'ResizeToContents',4:'ResizeToContents',5:'ResizeToContents',6:'ResizeToContents',7:'ResizeToContents',8:'ResizeToContents',9:'ResizeToContents',10:'ResizeToContents',11:'ResizeToContents',12:'ResizeToContents'},Header_name=['interface','collis','rx_byt','rx_crc_err','rx_drop','rx_err','rx_frame_err','rx_over_err','rx_pack','tx_byt','tx_drop','tx_err','tx_pack'])

    port_tree=myTree(ui.port_treeView,Opts=['ExtendedSelection','HeaderHidden'])
    qos_tree=myTree(ui.treeView_qos,Opts=['ExtendedSelection','HeaderHidden'])

    ofcond_table.delegate_col(0,compl_cond)
    ofaction_table.delegate_col(0,compl_action)
    ofgroup_params_table.delegate_col(0,compl_of_groups_params)
    dockerfile_table.delegate_col(0,compl_dockerfile)
    kvm_virt_misc_table.delegate_col(0,compl_misc_kvm)

    listcom2widget_mapping={
        'netflow' : {
            '_uuid' :{
                'readonly':True,
                'widgets':[ui.label_netflow_uuid]},
            'engine_id':{
                'bracket_chop':True,
                'widgets':[ui.lineEdit_netflow_engine_id],
                'fmt':'clear'},
            'engine_type':{
                'bracket_chop':True,
                'widgets':[ui.lineEdit_netflow_engine_type],
                'fmt':'clear'},
            'active_timeout' :{
                'widgets':[ui.lineEdit_netflow_active_timeout],
                'fmt':'zero'},
            'add_id_to_interface' :{
                'widgets':[ui.comboBox_netflow_add_ofid],
                'quote_chop':True,
                'fmt':'clear'},
            'targets' :{
                'widgets':[ui.lineEdit_netflow_targets],
                'preprocess_func':preprocess_targets,
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'clear'},
        },
        'sflow' : {
            '_uuid' :{
                'readonly':True,
                'widgets':[ui.label_sflow_uuid]},
            'agent' :{
                'widgets':[ui.lineEdit_sflow_agent],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'clear'},
            'polling' :{
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'clear',
                'widgets':[ui.lineEdit_sflow_polling]},
            'header' :{
                'quote_chop':True,
                'bracket_chop':True,
                'widgets':[ui.lineEdit_sflow_header],
                'fmt':'clear'},
            'sampling' :{
                'quote_chop':True,
                'bracket_chop':True,
                'widgets':[ui.lineEdit_sflow_sampling],
                'fmt':'clear'},
            'targets' :{
                'widgets':[ui.lineEdit_sflow_targets],
                'quote_chop':True,
                'preprocess_func':preprocess_targets,
                'bracket_chop':True},
            }
        ,
        'IPFIX' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            '_uuid' :{
                'readonly':True,
                'widgets':[ui.label_IPFIX_uuid]},
            'targets' :{
                'widgets':[ui.lineEdit_IPFIX_targets],
                'quote_chop':True,
                'preprocess_func':preprocess_targets,
                'bracket_chop':True},
            'obs_domain_id' :{
                'quote_chop':True,
                'bracket_chop':True,
                'widgets':[ui.lineEdit_IPFIX_obs_domain_id],
                'fmt':'clear'},
            'other_config:virtual_obs_id' :{
                'quote_chop':True,
                'bracket_chop':True,
                'widgets':[ui.lineEdit_IPFIX_virtual_obs_domain_id],
                'fmt':'other_config'},
            'obs_point_id' :{
                'quote_chop':True,
                'bracket_chop':True,
                'widgets':[ui.lineEdit_IPFIX_obs_point_id],
                'fmt':'clear'},
            'cache_active_timeout' :{
                'quote_chop':True,
                'bracket_chop':True,
                'widgets':[ui.lineEdit_IPFIX_cache_active_timeout],
                'fmt':'clear'},
            'cache_max_flows' :{
                'quote_chop':True,
                'bracket_chop':True,
                'widgets':[ui.lineEdit_IPFIX_max_flow_cache_size],
                'fmt':'clear'},
            'sampling' :{
                'widgets':[ui.lineEdit_IPFIX_sampling],
                'bracket_chop':True,
                'fmt':'clear'},
            'other_config:enable-input-sampling' :{
                'bracket_chop':True,
                'quote_chop':True,
                'widgets':[ui.comboBox_IPFIX_input_sampling],
                'fmt':'other_config'},
            'other_config:enable-output-sampling' :{
                'bracket_chop':True,
                'quote_chop':True,
                'widgets':[ui.comboBox_IPFIX_output_sampling],
                'fmt':'other_config'},
            'other_config:enable-tunnel-sampling':{
                'bracket_chop':True,
                'quote_chop':True,
                'widgets':[ui.comboBox_IPFIX_tunnel_sampling],
                'fmt':'other_config'},
        },
        'STP' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'status' :{
                'readonly':True,
                'action':'process_dict_config'},
            'stp_enable' :{
                'widgets':[ui.comboBox_STP_enable],
                'never_skip':True,
                'quote_chop':True,
            },
            'other_config:stp-forward-delay' :{
                'widgets':[ui.lineEdit_STP_forward_delay],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:stp-hello-time' :{
                'widgets':[ui.lineEdit_STP_hello_time],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:stp-max-age' :{
                'widgets':[ui.lineEdit_STP_max_age],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:stp-priority' :{
                'widgets':[ui.lineEdit_STP_bridge_priority],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:stp-system-id' :{
                'widgets':[ui.lineEdit_STP_bridge_system_id],
                'quote_chop':True,
                'fmt':'other_config'},
            'status:stp_bridge_id' :{
                'widgets':[ui.label_STP_bridge_id],
                'quote_chop':True,
                'readonly':True,
                'fmt':'other_config'},
            'status:stp_designated_root' :{
                'widgets':[ui.label_STP_designated_root],
                'quote_chop':True,
                'readonly':True,
                'fmt':'status'},
            'status:stp_root_path_cost' :{
                'widgets':[ui.label_STP_root_path_cost],
                'quote_chop':True,
                'readonly':True,
                'fmt':'status'},
        },
        'RSTP' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'rstp_status' :{
                'readonly':True,
                'action':'process_dict_config'},            
            'rstp_enable' :{
                'widgets':[ui.comboBox_RSTP_enable],
                'quote_chop':True,
                'never_skip':True,
            },
            'other_config:rstp-priority' :{
                'widgets':[ui.lineEdit_RSTP_bridge_priority],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-address' :{
                'widgets':[ui.lineEdit_RSTP_bridge_address],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-ageing-time' :{
                'widgets':[ui.lineEdit_RSTP_bridge_ageing_time],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-force-protocol-version' :{
                'widgets':[ui.comboBox_RSTP_force_protocol],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-forward-delay' :{
                'widgets':[ui.lineEdit_RSTP_forward_delay],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-max-age' :{
                'widgets':[ui.lineEdit_RSTP_max_age],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-transmit-hold-count' :{
                'widgets':[ui.lineEdit_RSTP_bridge_transmit_hold_count],
                'quote_chop':True,
                'fmt':'other_config'},
            'rstp_status:rstp_bridge_id' :{
                'widgets':[ui.label_RSTP_bridge_id],
                'quote_chop':True,
                'readonly':True,
                'fmt':'rstp_status'},
            'rstp_status:rstp_bridge_port_id' :{
                'widgets':[ui.label_RSTP_bridge_port_id],
                'quote_chop':True,
                'readonly':True,
                'fmt':'rstp_status'},
            'rstp_status:rstp_designated_id' :{
                'widgets':[ui.label_RSTP_designated_id],
                'quote_chop':True,
                'readonly':True,
                'fmt':'rstp_status'},
            'rstp_status:rstp_designated_port_id' :{
                'widgets':[ui.label_RSTP_designated_port_id],
                'quote_chop':True,
                'readonly':True,
                'fmt':'rstp_status'},
            'rstp_status:rstp_root_id' :{
                'widgets':[ui.label_RSTP_root_id],
                'quote_chop':True,
                'readonly':True,
                'fmt':'rstp_status'},
            'rstp_status:rstp_root_path_cost' :{
                'widgets':[ui.label_RSTP_root_path_cost],
                'quote_chop':True,
                'readonly':True,
                'fmt':'rstp_status'},
        },
        "MCAST" : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'mcast_snooping_enable' :{
                'widgets':[ui.comboBox_MCAST_enable],
                'quote_chop':True,
                'never_skip':True,
                },
            'other_config:mcast-snooping-aging-time' :{
                'widgets':[ui.lineEdit_MCAST_snooping_ageing],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:mcast-snooping-table-size' :{
                'widgets':[ui.lineEdit_MCAST_table_size],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:mcast-snooping-disable-flood-unregistered' :{
                'widgets':[ui.comboBox_MCAST_unregistred_flood_enable],
                'quote_chop':True,
                'fmt':'other_config'},
        },
        'MCAST_PORT' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'other_config:mcast-snooping-flood' :{
                'widgets':[ui.comboBox_mcast_port_flood],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:mcast-snooping-flood-reports' :{
                'widgets':[ui.comboBox_mcast_port_flood_reports],
                'quote_chop':True,
                'fmt':'other_config'},
        },
        'MANAGER' : {
            'sampling' :{
                'widgets':[ui.lineEdit_IPFIX_sampling],
                'bracket_chop':True,
                'fmt':'clear'},
        },
        'CONTROLLER' : {
            'target' :{
                'widgets':[ui.lineEdit_controller_target],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
        },
        'CONTROLLER_CONN' : {
            'connection_mode' :{
                'widgets':[ui.comboBox_controller_connection_mode],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
            'local_ip' :{
                'widgets':[ui.lineEdit_controller_local_ip],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
            'local_netmask' :{
                'widgets':[ui.lineEdit_controller_local_netmask],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
            'local_gateway' :{
                'widgets':[ui.lineEdit_controller_local_gateway],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
        },
        'CONTROLLER_PARAMS' : {
            'max_backoff' :{
                'widgets':[ui.lineEdit_controller_max_backoff],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
            'enable_async_messages' :{
                'widgets':[ui.comboBox_controller_enable_async],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
            'controller_rate_limit' :{
                'widgets':[ui.lineEdit_controller_rate_limit],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
            'inactivity_probe' :{
                'widgets':[ui.lineEdit_controller_inactivity_probe],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
            'controller_burst_limit' :{
                'widgets':[ui.lineEdit_controller_burst_limit],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'clear'},
        },
        'CONTROLLER_STATS' : {
            'status' :{
                'readonly':True,
                'action':'process_dict_config'},
            'is_connected' :{
                'widgets':[ui.label_controller_is_connected],
                'bracket_chop':True,
                'readonly':True,
                },
            '_uuid' :{
                'widgets':[ui.label_controller_uuid],
                'bracket_chop':True,
                'readonly':True,
                },
            'role' :{
                'widgets':[ui.label_controller_role],
                'bracket_chop':True,
                'readonly':True,
                },
            'status:last_error' :{
                'widgets':[ui.label_controller_last_error],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,
                },
            'status:sec_since_disconnect' :{
                'widgets':[ui.label_controller_sec_since_disconnect],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,
                },
            'status:state' :{
                'widgets':[ui.label_controller_state],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,
                },
        },
        'OPEN_VSWITCH' : {
            'external_ids' :{            
                'readonly':True,
                'action':'process_dict_config'},
            'external_ids:ovn-remote' :{
                'widgets':[ui.lineEdit_open_vswitch_ovn_remote],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'other_config'},
            'external_ids:ovn-nb' :{
                'widgets':[ui.lineEdit_open_vswitch_ovn_nb],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'other_config'},
            'external_ids:ovn-encap-ip' :{
                'widgets':[ui.lineEdit_open_vswitch_ovn_ncap_ip],
                'bracket_chop':True,
                'quote_chop':True,
                'fmt':'other_config'},
            'external_ids:ovn-encap-type' :{
                'widgets':[ui.comboBox_open_vswitch_ovn_tunnel],
                'bracket_chop':True,
                'fmt':'other_config'},
        },
        'OPEN_VSWITCH_STATS' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'other_config:enable-statistics' :{
                'widgets':[ui.comboBox_open_vswitch_stats],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'other_config'},
            'statistics' :{
                'readonly':True,
                'action':'process_dict_config'},
            'statistics:cpu' :{
                'widgets':[ui.label_open_vswitch_cpu],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,},
            'statistics:process_ovsdb-server' :{
                'widgets':[ui.label_open_vswitch_ovsdb_server],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,},
            'statistics:process_ovs-vswitchd' :{
                'widgets':[ui.label_open_vswitch_ovs_vswitchd],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,},
            'statistics:load_average' :{
                'widgets':[ui.label_open_vswitch_load],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,},
            'statistics:memory' :{
                'widgets':[ui.label_open_vswitch_mem],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,},
            'ovs_version' :{
                'widgets':[ui.label_open_vswitch_ovsvers],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,},
            'db_version' :{
                'widgets':[ui.label_open_vswitch_dbvers],
                'bracket_chop':True,
                'quote_chop':True,
                'readonly':True,},
            'iface_types' :{
                'widgets':[ui.label_open_vswitch_iface_types],
                'bracket_chop':True,
                'readonly':True,},
            'other_config:stats-update-interval' :{
                'widgets':[ui.lineEdit_open_vswitch_update_interval],
                'quote_chop':True,
                'fmt':'other_config'},
        },

        "PORT-STP" : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'other_config:stp-path-cost' :{
                'widgets':[ui.lineEdit_STP_port_path_cost],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:stp-port-priority' :{
                'widgets':[ui.lineEdit_STP_port_priority],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:stp-port-num' :{
                'widgets':[ui.lineEdit_STP_port_num],
                'quote_chop':True,
                'fmt':'other_config'},
            'status' :{
                'readonly':True,
                'widgets':[ui.plainTextEdit_stp_status]},
        },
        "PORT-RSTP" : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'other_config:rstp-port-priority' :{
                'widgets':[ui.lineEdit_RSTP_port_priority],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-port-num' :{
                'widgets':[ui.lineEdit_RSTP_port_num],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-port-path-cost' :{
                'widgets':[ui.lineEdit_RSTP_port_path_cost],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-enable' :{
                'widgets':[ui.comboBox_port_RSTP_enable],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-port-admin-edge' :{
                'widgets':[ui.comboBox_port_RSTP_admin_edge_enable],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-port-auto-edge' :{
                'widgets':[ui.comboBox_port_RSTP_auto_edge_enable],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:rstp-port-mcheck' :{
                'widgets':[ui.comboBox_port_RSTP_mcheck_enable],
                'quote_chop':True,
                'fmt':'other_config'},
            'rstp_status' :{
                'readonly':True,
                'widgets':[ui.plainTextEdit_rstp_status]},
            'rstp_statistics' :{
                'readonly':True,
                'widgets':[ui.plainTextEdit_rstp_statistics],},
        },
        'QUEUE' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'dscp' :{
                'fmt':'setclear2',
                'widgets':[queue_table],
                'widgets_from':[qqueue_ui.lineEdit_dialog_qos_queue_dscp],
                'col':5},
            '_uuid' :{
                'readonly':True,
                'widgets':[queue_table],
                'col':0},
            'other_config:min-rate' :{
                'widgets':[queue_table],
                'widgets_from':[qqueue_ui.lineEdit_dialog_qos_queue_minrate],
                'col':1,
                'fmt':'other_config'},
            'other_config:max-rate' :{
                'widgets':[queue_table],
                'widgets_from':[qqueue_ui.lineEdit_dialog_qos_queue_maxrate],
                'col':2,
                'fmt':'other_config'},
            'other_config:burst' :{
                'widgets':[queue_table],
                'widgets_from':[qqueue_ui.lineEdit_dialog_qos_queue_burst],
                'col':3,
                'fmt':'other_config'},
            'other_config:priority' :{
                'widgets':[queue_table],
                'widgets_from':[qqueue_ui.lineEdit_dialog_qos_queue_priority],
                'col':4,
                'fmt':'other_config'},
        },
        'QOS' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            '_uuid' :{
                'readonly':True,
                'widgets':[qos_tree],
                },
            'type' :{
                'widgets_from':[qqos_ui.comboBox_dialog_qos_qos_type],
                'widgets':[qos_tree],
                'never_skip':True,
                },
            'queues' :{
                'readonly':True,
                'widgets':[qos_tree],
                },
            'other_config:max-rate' :{
                'widgets_from':[qqos_ui.lineEdit_dialog_qos_qos_maxrate],
                'widgets':[qos_tree],
                'fmt':'other_config'},
            'other_config:cir' :{
                'widgets_from':[qqos_ui.lineEdit_dialog_qos_qos_cir],
                'widgets':[qos_tree],
                'fmt':'other_config'},
            'other_config:cbs' :{
                'widgets_from':[qqos_ui.lineEdit_dialog_qos_qos_cbs],
                'widgets':[qos_tree],
                'fmt':'other_config'},
            'other_config:perturb' :{
                'widgets_from':[qqos_ui.lineEdit_dialog_qos_qos_perturb],
                'widgets':[qos_tree],
                'fmt':'other_config'},
            'other_config:quantum' :{
                'widgets_from':[qqos_ui.lineEdit_dialog_qos_qos_quantum],
                'widgets':[qos_tree],
                'fmt':'other_config'},
        },
        'BOND' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'name' :{
                'readonly':True,
                'widgets':[ui.lineEdit_bond_name],
                'quote_chop':True},
            'bond_mode':{
                'widgets':[ui.comboBox_bond_mode],
                'fmt':'clear',
                'quote_chop':True},
            'bond_updelay' :{
                'widgets':[ui.lineEdit_bond_updelay],
                'quote_chop':True,
                'fmt':'zero'},
            'bond_downdelay' :{
                'widgets':[ui.lineEdit_bond_downdelay],
                'quote_chop':True,
                'fmt':'zero'},
            'bond_fake_iface' :{
                'widgets':[ui.comboBox_bond_fake_iface],
                'quote_chop':True,
            },
            'lacp':{
                'widgets':[ui.comboBox_lacp],
                'fmt':'clear',
                'quote_chop':True},
            'other_config:bond-detect-mode':{
                'widgets':[ui.comboBox_bond_detect_mode],
                'fmt':'other_config'},
            'other_config:bond-hash-basis' :{
                'widgets':[ui.lineEdit_bond_hash_basis],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:bond-miimon-interval' :{
                'widgets':[ui.lineEdit_bond_miimon_interval],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:bond-rebalance-interval' :{
                'widgets':[ui.lineEdit_bond_rebalance_interval],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:lacp-fallback-ab' :{
                'widgets':[ui.comboBox_lacp_fallback_ab],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:lacp-system-id' :{
                'widgets':[ui.lineEdit_lacp_system_id],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:lacp-system-priority' :{
                'widgets':[ui.lineEdit_lacp_system_priority],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:lacp-time':{
                'widgets':[ui.comboBox_lacp_time],
                'quote_chop':True,
                'fmt':'other_config'},
            'other_config:lacp-aggregation-key':{
                'widgets':[ui.lineEdit_lacp_aggr_key],
                'quote_chop':True,
                'fmt':'other_config'},
        },
        "MIRROR" : {
            'name':{
                'readonly':True,
                'widgets':[ui.lineEdit_mirror_name],
                'quote_chop':True},
            'select_src_port':{
                'widgets':[ui.lineEdit_mirror_select_src],
                'quote_chop':True,
                'bracket_chop':True,
                'action':'convert_uuid2ports'},
            'select_dst_port':{
                'widgets':[ui.lineEdit_mirror_select_dst],
                'quote_chop':True,
                'bracket_chop':True,
                'action':'convert_uuid2ports'},
            'select_vlan':{
                'widgets':[ui.lineEdit_mirror_select_vlans],
                'quote_chop':True,
                'bracket_chop':True},
            'snaplen':{
                'widgets':[ui.lineEdit_mirror_snaplen],
                'quote_chop':True,
                'bracket_chop':True},
            'output_port':{
                'widgets':[ui.lineEdit_mirror_output_port],
                'quote_chop':True,
                'bracket_chop':True,
                'action':'convert_uuid2ports'},
            'output_vlan':{
                'widgets':[ui.lineEdit_mirror_output_vlan],
                'quote_chop':True,
                'bracket_chop':True
                },
            'select_all':{
                'widgets':[ui.checkBox_mirror_select_all],
                'values':['true','false']},
        },
        'INTERFACE' : {
            'external_ids':{
                'readonly':True,
                'action':'process_dict_config'},
            'admin_state':{
                'readonly':True,
                'widgets':[ui.pushButton_interface_admin_state],
                'action':'color_led'},
            'link_state':{
                'readonly':True,
                'widgets':[ui.pushButton_interface_link_state],
                'action':'color_led'},
            'mtu':{
                'readonly':True,
                'widgets':[ui.label_interface_mtu],
                'quote_chop':True,
                'bracket_chop':True,
                'readonly':True,
                },
            'mtu_request':{
                'widgets':[ui.lineEdit_interface_mtu_request],
                'quote_chop':True,
                'bracket_chop':True,
            },
            'error':{
                'readonly':True,
                'widgets':[ui.label_interface_iface_error],
                'quote_chop':True,
                'bracket_chop':True,
                'readonly':True,
                },
            'duplex':{
                'widgets':[ui.label_interface_duplex],
                'quote_chop':True,
                'bracket_chop':True,
                'readonly':True,},
            'link_speed':{
                'widgets':[ui.label_interface_link_speed],
                'quote_chop':True,
                'bracket_chop':True,
                'readonly':True,
                },
            'external_ids:iface-id':{
                'widgets':[ui.label_interface_iface_id],
                'quote_chop':True,
                'bracket_chop':True,
                'readonly':True,},
            'external_ids:attached-mac':{
                'widgets':[ui.label_interface_attached_mac],
                'quote_chop':True,
                'bracket_chop':True,
                'readonly':True,},
            'external_ids:iface-status':{
                'widgets':[ui.label_interface_iface_status],
                'quote_chop':True,
                'bracket_chop':True,
                'readonly':True,},
            'external_ids:vm-id':{
                'widgets':[ui.label_interface_vm_id],
                'quote_chop':True,
                'bracket_chop':True,
                'readonly':True,},

        },
        'INTERFACE_TYPE' : {
            'options' :{
                'readonly':True,
                'action':'process_dict_config'},
            'lldp':{
                'readonly':True,
                'action':'process_dict_config'},
            'type':{
                'widgets':[ui.comboBox_type],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'setclear'},
            'options:peer':{
                'widgets':[ui.lineEdit_interface_peer],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:remote_ip':{
                'widgets':[ui.lineEdit_interface_remote_ip],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:local_ip':{
                'widgets':[ui.lineEdit_interface_local_ip],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:in_key':{
                'widgets':[ui.lineEdit_interface_in_key],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:out_key':{
                'widgets':[ui.lineEdit_interface_out_key],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:key':{
                'widgets':[ui.lineEdit_interface_key],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:dst_port':{
                'widgets':[ui.lineEdit_interface_dst_port],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:egress_pkt_mark':{
                'widgets':[ui.lineEdit_interface_egress_pkt_mark],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:packet_type':{
                'widgets':[ui.comboBox_interface_packettype],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:ttl':{
                'widgets':[ui.lineEdit_interface_ttl],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:exts':{
                'widgets':[ui.comboBox_interface_exts],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:tos':{
                'widgets':[ui.lineEdit_interface_tos],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'options'},
            'options:df_default':{
                'widgets':[ui.comboBox_interface_df],
                'quote_chop':True,
                'fmt':'options'},
            'options:csum':{
                'widgets':[ui.comboBox_interface_csum],
                'quote_chop':True,
                'fmt':'options'},
            'lldp:enable':{
                'widgets':[ui.comboBox_interface_lldp],
                'quote_chop':True,
                'fmt':'lldp'},
        },
        "PORT" : {
            'tag':{
                'widgets':[ui.lineEdit_vlan_access],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'clear'
                },
            'trunks':{
                'widgets':[ui.lineEdit_vlan_trunk],
                'quote_chop':True,
                'bracket_chop':True,
                'preprocess_func':preprocess_liste,
                'fmt':'clear'
                },
            'cvlans':{
                'widgets':[ui.lineEdit_vlan_cvlans],
                'quote_chop':True,
                'bracket_chop':True,
                'preprocess_func':preprocess_liste,
                'fmt':'clear'
                },
            'vlan_mode':{
                'widgets':[ui.comboBox_vlan_mode],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'clear'                
                },
        },
        "PORT_INGRESS" : {
            'ingress_policing_rate':{
                'widgets':[ui.lineEdit_ingress_rate],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'zero'                
            },
            'ingress_policing_burst':{
                'widgets':[ui.lineEdit_ingress_burst],
                'quote_chop':True,
                'bracket_chop':True,
                'fmt':'zero'                
            },
        },
        'SSL' : {
            '_uuid':{
                'widgets':[ui.label_ssl_uuid],
                'quote_chop':True,
                'readonly':True,
                'bracket_chop':True,
            },
            'private_key':{
                'widgets':[ui.lineEdit_ssl_private_key],
                'quote_chop':True,
                'bracket_chop':True,
            },
            'certificate':{
                'widgets':[ui.lineEdit_ssl_cert],
                'quote_chop':True,
                'bracket_chop':True,
            },
            'ca_cert':{
                'widgets':[ui.lineEdit_ssl_ca_cert],
                'quote_chop':True,
                'bracket_chop':True,
            },
            'bootstrap_ca_cert':{
                'widgets':[ui.comboBox_ssl_bootstrap_cacert],
                'quote_chop':True,
                'bracket_chop':True,
            },

        },
        'BRIDGE' : {
            'other_config' :{
                'readonly':True,
                'action':'process_dict_config'},
            'controller':{
                'widgets':[ui.label_bridge_controller],
                'quote_chop':True,
                'readonly':True,
                'bracket_chop':True,
            },
            'fail_mode':{
                'widgets':[ui.comboBox_bridge_failmode],
                'quote_chop':True,
                'bracket_chop':True,
            },
            'flood_vlans':{
                'widgets':[ui.lineEdit_bridge_flood_vlans],
                'quote_chop':True,
                'preprocess_func':preprocess_liste,
                'bracket_chop':True,
            },
        },
    }


    #widget,value
    cleanable_widget_list={
        'OFTRACE' : [
            [oftrace_ui.lineEdit_of_trace_name,''],
            [oftrace_ui.lineEdit_of_trace_packet,''],
            [oftrace_ui.checkBox_of_trace_packetout,False],
            [oftrace_ui.checkBox_of_trace_generate,False],
            [oftrace_ui.checkBox_of_trace_consistent,False],
            [oftrace_ui.checkBox_of_trace_trk,False],
            [oftrace_ui.checkBox_of_trace_new,False],
            [oftrace_ui.checkBox_of_trace_est,False],
            [oftrace_ui.checkBox_of_trace_rel,False],
            [oftrace_ui.checkBox_of_trace_rpl,False],
            [oftrace_ui.checkBox_of_trace_inv,False],
            [oftrace_ui.checkBox_of_trace_dnat,False],
            [oftrace_ui.checkBox_of_trace_snat,False],
            [oftrace_ui.radioButton_of_trace_pcap,True],
            ],
        'netflow' : [
            [ui.lineEdit_netflow_targets,''],
            [ui.lineEdit_netflow_active_timeout,''],
            [ui.comboBox_netflow_add_ofid,0],
            [ui.label_netflow_uuid,''],
            ],
        'sflow' : [
            [ui.lineEdit_sflow_targets,''],
            [ui.lineEdit_sflow_agent,''],
            [ui.lineEdit_sflow_header,''],
            [ui.lineEdit_sflow_sampling,''],
            [ui.lineEdit_sflow_polling,''],
            [ui.label_sflow_uuid,''],
            ],
        'IPFIX' : [
            [ui.lineEdit_IPFIX_targets,''],
            [ui.lineEdit_IPFIX_obs_domain_id,''],
            [ui.lineEdit_IPFIX_obs_point_id,''],
            [ui.lineEdit_IPFIX_cache_active_timeout,''],
            [ui.lineEdit_IPFIX_max_flow_cache_size,''],
            [ui.lineEdit_IPFIX_virtual_obs_domain_id,''],
            [ui.comboBox_IPFIX_tunnel_sampling,0],
            [ui.comboBox_IPFIX_input_sampling,0],
            [ui.comboBox_IPFIX_output_sampling,0],
            [ui.label_IPFIX_uuid,''],
            [ui.lineEdit_IPFIX_sampling,''],
        ],
        'STP' : [
            [ui.comboBox_STP_enable,0],
            [ui.lineEdit_STP_bridge_priority,''],
            [ui.lineEdit_STP_bridge_system_id,''],
            [ui.lineEdit_STP_hello_time,''],
            [ui.lineEdit_STP_max_age,''],
            [ui.lineEdit_STP_forward_delay,''],
            [ui.lineEdit_STP_bridge_priority,''],
            [ui.lineEdit_STP_bridge_system_id,''],
            [ui.label_STP_bridge_id,''],
            [ui.label_STP_designated_root,''],
            [ui.label_STP_root_path_cost,''],
            ],
        'RSTP' : [
            [ui.comboBox_RSTP_enable,0],
            [ui.lineEdit_RSTP_bridge_priority,''],
            [ui.lineEdit_RSTP_bridge_address,''],
            [ui.lineEdit_RSTP_bridge_ageing_time,''],
            [ui.lineEdit_RSTP_max_age,''],
            [ui.lineEdit_RSTP_forward_delay,''],
            [ui.lineEdit_RSTP_bridge_transmit_hold_count,''],
            [ui.label_RSTP_bridge_id,''],
            [ui.label_RSTP_bridge_port_id,''],
            [ui.label_RSTP_designated_id,''],
            [ui.label_RSTP_designated_port_id,''],
            [ui.label_RSTP_root_id,''],
            [ui.label_RSTP_root_path_cost,''],
            [ui.comboBox_RSTP_force_protocol,0],
        ],
        'MCAST' : [
            [ui.lineEdit_MCAST_snooping_ageing,''],
            [ui.lineEdit_MCAST_table_size,''],
            [ui.comboBox_MCAST_enable,0],
            [ui.comboBox_MCAST_unregistred_flood_enable,0],
        ],
        'MCAST_PORT' : [
            [ui.comboBox_mcast_port_flood,0],
            [ui.comboBox_mcast_port_flood_reports,0],
        ],
        'CONTROLLER' : [
            [ui.lineEdit_controller_target,''],
            [ui.label_controller_uuid,'?'],
            [ui.comboBox_controller_connection_mode,0],
            [ui.lineEdit_controller_local_ip,''],
            [ui.lineEdit_controller_local_netmask,''],
            [ui.lineEdit_controller_local_gateway,''],
            [ui.lineEdit_controller_max_backoff,''],
            [ui.lineEdit_controller_inactivity_probe,''],
            [ui.comboBox_controller_enable_async,0],
            [ui.lineEdit_controller_rate_limit,''],
            [ui.lineEdit_controller_burst_limit,''],
            [ui.label_controller_is_connected,'?'],
            [ui.label_controller_role,'?'],
            [ui.label_controller_state,'?'],
            [ui.label_controller_last_error,'?'],
            [ui.label_controller_sec_since_disconnect,'?'],
            [ui.label_controller_packetin_bypassed,'?'],
            [ui.label_controller_packetin_dropped,'?'],
            [ui.label_controller_packetin_queued,'?'],
            [ui.label_controller_packetin_backlog,'?'],
        ],
        'MANAGER' : [
            [ui.lineEdit_manager_target,''],
            [ui.comboBox_manager_connection_mode,0],
            [ui.lineEdit_manager_max_backoff,''],
            [ui.lineEdit_manager_inactivity_probe,''],
            [ui.lineEdit_manager_dscp,''],
            [ui.label_manager_uuid,'?'],
            [ui.label_manager_is_connected,'?'],
            [ui.label_manager_state,'?'],
            [ui.label_manager_sec_since_connect,'?'],
            [ui.label_manager_sec_since_disconnect,'?'],
            [ui.label_manager_last_error,'?'],
            [ui.label_manager_bound_port,'?'],
        ],
        'OPEN_VSWITCH' : [
            [ui.lineEdit_open_vswitch_ovn_remote,''],
            [ui.lineEdit_open_vswitch_ovn_nb,''],
            [ui.lineEdit_open_vswitch_ovn_ncap_ip,''],
            [ui.comboBox_open_vswitch_ovn_tunnel,0],
            [ui.comboBox_open_vswitch_stats,0],
            [ui.label_open_vswitch_cpu,'?'],
            [ui.label_open_vswitch_load,'?'],
            [ui.label_open_vswitch_mem,'?'],
            [ui.label_open_vswitch_ovsvers,'?'],
            [ui.label_open_vswitch_dbvers,'?'],
            [ui.label_open_vswitch_iface_types,'?'],
            [ui.label_open_vswitch_ovs_vswitchd,'?'],
            [ui.label_open_vswitch_ovsdb_server,'?'],
        ],
        
        'PORT-STP' : [
            [ui.lineEdit_STP_port_priority,''],
            [ui.lineEdit_STP_port_path_cost,''],
            [ui.lineEdit_STP_port_num,''],
        ],
        'PORT-RSTP' : [
            [ui.lineEdit_RSTP_port_priority,''],
            [ui.lineEdit_RSTP_port_path_cost,''],
            [ui.lineEdit_RSTP_port_num,''],
            [ui.comboBox_port_RSTP_enable,0],
            [ui.comboBox_port_RSTP_admin_edge_enable,0],
            [ui.comboBox_port_RSTP_auto_edge_enable,0],
            [ui.comboBox_port_RSTP_mcheck_enable,0],
        ],
        'BOND' : [
            [ui.lineEdit_bond_name,''],
            [ui.comboBox_bond_fake_iface,0],
            [ui.comboBox_lacp_fallback_ab,0],
            [ui.comboBox_bond_detect_mode,0],
            [ui.comboBox_bond_mode,0],
            [ui.comboBox_lacp,0],
            [ui.comboBox_lacp_time,0],
            [ui.lineEdit_bond_downdelay,''],
            [ui.lineEdit_bond_hash_basis,''],
            [ui.lineEdit_bond_miimon_interval,''],
            [ui.lineEdit_bond_rebalance_interval,''],
            [ui.lineEdit_bond_updelay,''],
            [ui.lineEdit_lacp_system_id,''],
            [ui.lineEdit_lacp_system_priority,''],
        ],
        'MIRROR' : [
            [ui.lineEdit_mirror_name,''],
            [ui.lineEdit_mirror_select_src,''],
            [ui.lineEdit_mirror_select_dst,''],
            [ui.lineEdit_mirror_select_vlans,''],
            [ui.lineEdit_mirror_snaplen,''],
            [ui.lineEdit_mirror_output_port,''],
            [ui.lineEdit_mirror_output_vlan,''],
            [ui.checkBox_mirror_select_all,False],
        ],
        'INTERFACE' : [
            [ui.label_interface_iface_id,''],
            [ui.label_interface_iface_status,''],
            [ui.label_interface_attached_mac,''],
            [ui.label_interface_vm_id,''],
            [ui.label_interface_duplex,'?'],
            [ui.label_interface_link_speed,'?'],
            [ui.label_interface_mtu,'?'],
            [ui.lineEdit_interface_mtu_request,''],
            [ui.label_interface_iface_error,''],
        ],
        'INTERFACE_TYPE' : [
            [ui.comboBox_type,0],
            [ui.lineEdit_interface_peer,''],
            [ui.lineEdit_interface_remote_ip,''],
            [ui.lineEdit_interface_local_ip,''],
            [ui.lineEdit_interface_in_key,''],
            [ui.lineEdit_interface_out_key,''],
            [ui.lineEdit_interface_key,''],
            [ui.lineEdit_interface_dst_port,''],
            [ui.lineEdit_interface_egress_pkt_mark,''],
            [ui.comboBox_interface_packettype,0],
            [ui.lineEdit_interface_ttl,''],
            [ui.comboBox_interface_exts,0],
            [ui.lineEdit_interface_tos,''],
            [ui.comboBox_interface_df,0],
            [ui.comboBox_interface_csum,0],
            [ui.comboBox_interface_lldp,0],
        ],
        'PORT' : [
            [ui.comboBox_vlan_mode,0],
            [ui.lineEdit_vlan_access,''],
            [ui.lineEdit_vlan_trunk,''],
            [ui.lineEdit_vlan_cvlans,''],
            ],
        'PORT_INGRESS' : [
            [ui.lineEdit_ingress_rate,''],
            [ui.lineEdit_ingress_burst,''],
            ],
        'BRIDGE' : [
            [ui.comboBox_bridge_failmode,0],
            [ui.label_bridge_controller,'?'],
            [ui.lineEdit_bridge_flood_vlans,''],
        ],
        'SSL' : [
            [ui.label_ssl_uuid,'?'],
            [ui.lineEdit_ssl_private_key,''],
            [ui.lineEdit_ssl_cert,''],
            [ui.lineEdit_ssl_ca_cert,''],
            [ui.comboBox_ssl_bootstrap_cacert,0],
        ],
        'QOS' : [
            [qqos_ui.lineEdit_dialog_qos_qos_maxrate,''],
            [qqos_ui.lineEdit_dialog_qos_qos_cir,''],
            [qqos_ui.lineEdit_dialog_qos_qos_cbs,''],
            [qqos_ui.lineEdit_dialog_qos_qos_perturb,''],
            [qqos_ui.lineEdit_dialog_qos_qos_quantum,''],
            [qqos_ui.comboBox_dialog_qos_qos_type,0],
        ],
    }

    typewidgetlist=[
        #ui.lineEdit_type_peer,
    ]

    ports_widget_list=[
      ui.tabs_ports,
      #ui.tab_vlan,
      #ui.tab_interface,
      #ui.tab_interface_type,
      #ui.tab_ingress_policy,
      #ui.tab_STP,
      #ui.tab_RSTP,
      #ui.tab_Mcast,
      #ui.tab_Mirror,
      #ui.tab_Bond,
      ui.pushButton_port_list,
      ui.pushButton_interface_list,
      ui.pushButton_port_del,
      ui.pushButton_ip_addr_flush
    ]

    mirror_port_list=[
        ui.lineEdit_mirror_select_src,
        ui.lineEdit_mirror_select_dst
    ]

    wenable_dic={
        'INTERFACE':{
            'ALL':{
                'e00':ui.lineEdit_interface_peer,
                'l00':ui.label_interface_peer,
                'c01':ui.comboBox_interface_csum,
                'c02':ui.comboBox_interface_lldp,
                'c03':ui.comboBox_interface_df,
                'e04':ui.lineEdit_interface_remote_ip,
                'l04':ui.label_interface_remote_ip,
                'e05':ui.lineEdit_interface_local_ip,
                'l05':ui.label_interface_local_ip,
                'e06':ui.lineEdit_interface_in_key,
                'l06':ui.label_interface_in_key,
                'b06':ui.pushButton_interface_load_in_key,
                'e07':ui.lineEdit_interface_out_key,
                'l07':ui.label_interface_out_key,
                'b07':ui.pushButton_interface_load_out_key,
                'e08':ui.lineEdit_interface_key,
                'l08':ui.label_interface_key,
                'b08':ui.pushButton_interface_load_key,
                'e09':ui.lineEdit_interface_dst_port,
                'l09':ui.label_interface_dst_port,
                'e10':ui.lineEdit_interface_tos,
                'l10':ui.label_interface_tos,
                'e11':ui.lineEdit_interface_ttl,
                'l11':ui.label_interface_ttl,
                'e12':ui.lineEdit_interface_egress_pkt_mark,
                'l12':ui.label_interface_egress_pkt_mark,
                'c13':ui.comboBox_interface_packettype,
                'l13':ui.label_interface_packet_type,
                'c14':ui.comboBox_interface_exts,
                'l14':ui.label_interface_exts,
            },
            'patch':[
                'e00','l00',
            ],
            'gre':[
                'e04','l04','e05','l05',
                'e06','l06','b06','e07','l07','b07','e08','l08','b08',
                'e09','l09',
                'l10','l10',
                'e11','l11',
                'e12','l12',
                'c13','l13',
                'c01','c02','c03'
            ],
            'geneve':[
                'e04','l04','e05','l05',
                'e06','l06','b06','e07','l07','b07','e08','l08','b08',
                'e09','l09',
                'l10','l10',
                'e11','l11',
                'e12','l12',
                'c01','c02','c03'
            ],
            'stt':[
                'e04','l04','e05','l05',
                'e06','l06','b06','e07','l07','b07','e08','l08','b08',
                'e09','l09',
                'l10','l10',
                'e11','l11',
                'e12','l12',
                'c02','c03'
            ],
            'vxlan':[
                'e04','l04','e05','l05',
                'e06','l06','b06','e07','l07','b07','e08','l08','b08',
                'e09','l09',
                'l10','l10',
                'e11','l11',
                'e12','l12',
                'c13','l13',
                'c14','l14',
                'c01','c02','c03'
            ],
            'lisp':[
                'e04','l04','e05','l05',
                'e06','l06','b06','e07','l07','b07','e08','l08','b08',
                'e09','l09',
                'l10','l10',
                'e11','l11',
                'e12','l12',
                'c13','l13',
                'c02','c03'
            ],
            'interface_patch_list':[
                'e00','l00',
                'c02'
            ],
        },
        'MGMT':{
            'ALL':{
                'l00':mgmt_ui.label_mgmt_host,
                'e00':mgmt_ui.lineEdit_mgmt_host,

                'l01':mgmt_ui.label_mgmt_ssh_user,
                'e01':mgmt_ui.lineEdit_mgmt_ssh_username,

                'l02':mgmt_ui.label_mgmt_passwd,                
                'e02':mgmt_ui.lineEdit_mgmt_ssh_password,
                
                'l03':mgmt_ui.label_mgmt_sshkey,
                'f03':mgmt_ui.frame_mgmt_sshkey,
                
                'l04':mgmt_ui.label_mgmt_sshkeytype,
                'f04':mgmt_ui.frame_mgmt_sshkeytype,
                
                'l06':mgmt_ui.label_mgmt_ssh_connect_timeout,
                'e06':mgmt_ui.lineEdit_mgmt_ssh_connect_timeout,

                'f07':mgmt_ui.frame_mgmt_sudo,
                'l07':mgmt_ui.label_mgmt_sudo,


            },
            'local':[
                'l07','f07',
            ],
            'ssh':[
                'l00','e00',
                'l01','e01',
                'l03','f03',
                'l06','e06',
                'l07','f07',
            ],
            'paramiko_key':[
                'l00','e00',
                'l01','e01',
                'l03','f03',
                'l04','f04',
                'l06','e06',
                'l07','f07',
            ],
            'paramiko_password':[
                'l00','e00',
                'l01','e01',
                'l02','e02',
                'l06','e06',
                'l07','f07',
            ],
        },
        'MGMT_CUSTOM':{
            'ALL':{
                'l01':mgmt_ui.label_mgmt_script_args,
                'l02':mgmt_ui.lineEdit_mgmt_custom_script,
                'l03':mgmt_ui.lineEdit_mgmt_custom_script_args,
                'b01':mgmt_ui.pushButton_mgmt_select_customscript,
                'l04':mgmt_ui.label_mgmt_script_filename,
            },
            'custom':[
                'l01','b01','l02','l03','l04',
            ],
        },
        'DOCKERNET':{
            'ALL':{
                'l00':dockernet_ui.label_5,
                'e00':dockernet_ui.lineEdit_dialog_dockernet_ip,
                'l01':dockernet_ui.label_6,
                'e01':dockernet_ui.lineEdit_dialog_dockernet_net,
                'l02':dockernet_ui.label_7,
                'e02':dockernet_ui.lineEdit_dialog_dockernet_gw,
            },
            'ip':[
                'l00','e00',
            ],
            'net':[
                'l01','e01',
                'l02','e02',
            ],

        },


    }

    
    
    kvmwidgetlist=[
        ui.tableWidget_kvm_pg,
        ui.pushButton_kvm_pg_add,
        ui.pushButton_kvm_pg_delete,
        ui.pushButton_kvm_pg_edit,
        ui.label_kvm_pglist,
    ]

    vn_all_list= [
        vn_ui.lineEdit_dialog_kvm_virt_bridge,
        vn_ui.lineEdit_dialog_kvm_virt_network,
        vn_ui.comboBox_dialog_kvm_virt_model,
        vn_ui.comboBox_dialog_kvm_virt_virtualport,
        vn_ui.lineEdit_dialog_kvm_virt_target,
    ]

    vn_ovs_list= [
        vn_ui.lineEdit_dialog_kvm_virt_target,
    ]

    vn_kvm_portgroup_list= [
        vn_ui.lineEdit_dialog_kvm_virt_network,
        vn_ui.lineEdit_dialog_kvm_virt_target,
    ]

    vn_kvm_linux_bridge_list= [
        vn_ui.lineEdit_dialog_kvm_virt_bridge,
    ]
    mirror_src_dst_ports= [
        ui.lineEdit_mirror_select_src,
        ui.lineEdit_mirror_select_dst,
        ui.pushButton_mirror_select_src,
        ui.pushButton_mirror_select_dst
    ]

    qos_dialog_all= [
        qqos_ui.lineEdit_dialog_qos_qos_maxrate,
        qqos_ui.lineEdit_dialog_qos_qos_cir,
        qqos_ui.lineEdit_dialog_qos_qos_cbs,
        qqos_ui.lineEdit_dialog_qos_qos_perturb,
        qqos_ui.lineEdit_dialog_qos_qos_quantum,
    ]

    qos_dialog_linux_htb= [
        qqos_ui.lineEdit_dialog_qos_qos_maxrate,
    ]

    qos_dialog_linux_hfsc= [
        qqos_ui.lineEdit_dialog_qos_qos_maxrate,
    ]
        
    qos_dialog_linux_sfq= [
        qqos_ui.lineEdit_dialog_qos_qos_perturb,
        qqos_ui.lineEdit_dialog_qos_qos_quantum,
    ]
        
    qos_dialog_linux_codel= [
    ]

    qos_dialog_linux_fq_codel= [
    ]

    qos_dialog_linux_noop= [
    ]

    qos_dialog_egress_policer= [
        qqos_ui.lineEdit_dialog_qos_qos_cir,
        qqos_ui.lineEdit_dialog_qos_qos_cbs,
    ]

    radiobutton_mapping={
        "radioButton_mirror_output_port" : [ui,lambda:[setEnableWidgetList([ui.lineEdit_mirror_output_vlan],False,testcheckbox=ui.radioButton_mirror_output_port),setEnableWidgetList([ui.lineEdit_mirror_output_port,ui.pushButton_mirror_select_outputport],True,testcheckbox=ui.radioButton_mirror_output_port)]],
        #"radioButton_MCAST_enable" : [ui,action_MCAST_toggle],
        #"radioButton_MCAST_disable" : [ui,action_MCAST_toggle],
        "radioButton_stats_0" : [stats_ui,action_interface_statistics_refresh],
        "radioButton_stats_G" : [stats_ui,action_interface_statistics_refresh],
        "radioButton_stats_K" : [stats_ui,action_interface_statistics_refresh],
        "radioButton_stats_M" : [stats_ui,action_interface_statistics_refresh],
        "radioButton_stats_T" : [stats_ui,action_interface_statistics_refresh],
        "radioButton_stats_abs" : [stats_ui,action_interface_statistics_refresh],
        "radioButton_stats_delta" : [stats_ui,action_interface_statistics_refresh],
        "radioButton_stats_deltasec" : [stats_ui,action_interface_statistics_refresh],
    }

    checkbutton_mapping={
        "checkBox_mirror_select_all" : [ui,lambda:setEnableWidgetList(mirror_src_dst_ports,False,testcheckbox=ui.checkBox_mirror_select_all)],
        "checkBox_dialog_stats_coll" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_coll,col=1)],
        "checkBox_dialog_stats_rx_byt" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_rx_byt,col=2)],
        "checkBox_dialog_stats_rx_crc_err" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_rx_crc_err,col=3)],
        "checkBox_dialog_stats_rx_drop" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_rx_drop,col=4)],
        "checkBox_dialog_stats_rx_err" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_rx_err,col=5)],
        "checkBox_dialog_stats_rx_frame_err" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_rx_frame_err,col=6)],
        "checkBox_dialog_stats_rx_over_err" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_rx_over_err,col=7)],
        "checkBox_dialog_stats_rx_pack" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_rx_pack,col=8)],
        "checkBox_dialog_stats_tx_byt" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_tx_byt,col=9)],
        "checkBox_dialog_stats_tx_drop" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_tx_drop,col=10)],
        "checkBox_dialog_stats_tx_err" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_tx_err,col=11)],
        "checkBox_dialog_stats_tx_pack" : [stats_ui,lambda:stats_table.hide_table_column(checkbox=stats_ui.checkBox_dialog_stats_tx_pack,col=12)],
    }

    tablewidget_mapping={
        #"tableWidget_qos_qos" : [ui,[[action_select_qos,'']]],
        "tableWidget_of_trace" : [oftrace_ui,[[action_select_oftrace,'']]],
        "tableWidget_of"  : [ui,[[sync_selected_of,'']]],
        "tableWidget_ofgroup_buckets"  : [ofgroup_ui,[[action_ofgroup_params_refresh,'']]],
        "tableWidget_ofgroups"  : [ui,[[action_ofgroup_bucket_refresh,'']]],
        "tableWidget_mgmt"  : [ui,[[action_mgmt_select,'']]],
        "tableWidget_dockerimage"  : [ui,[[dockerimage_select,'']]],
        "tableWidget_mirrors"  : [ui,[[action_mirror_select,'']]],
        "tableWidget_docker_if"  : [ui,[[action_dockernet_refresh,'']]],
    }



    
    buttons_mapping={
        "buttonBox_ofeditor" : [of_ui,lambda:of_Dialog.setVisible(False)],
        "pushButton_IPFIX_clear" : [ui,action_IPFIX_clear],
        "pushButton_IPFIX_create" : [ui,action_IPFIX_create],
        "pushButton_IPFIX_list" : [ui,lambda:action_IPFIX_list(output=True)],
        "pushButton_IPFIX_refresh" : [ui,lambda:action_IPFIX_list(output=False)],
        "pushButton_IPFIX_update" : [ui,action_IPFIX_update],
        "pushButton_MCAST_port_refresh" :  [ui,action_port_MCAST_refresh],
        "pushButton_MCAST_port_update" :  [ui,action_MCAST_port_update],
        "pushButton_MCAST_refresh" :  [ui,action_MCAST_refresh],
        "pushButton_MCAST_validate" :  [ui,action_MCAST_validate],
        "pushButton_MCAST_table_show" :  [ui,action_MAST_table_show],
        "pushButton_MCAST_table_flush" :  [ui,action_MCAST_table_flush],
        "pushButton_RSTP_list" : [ui,lambda:bridge_list('name,other_config,rstp_enable,rstp_status,status')],
        "pushButton_RSTP_port_refresh" : [ui,action_port_RSTP_refresh],
        "pushButton_RSTP_port_validate" : [ui,action_port_RSTP_validate],
        "pushButton_RSTP_refresh" : [ui,action_RSTP_refresh],
        "pushButton_RSTP_validate" :  [ui,action_RSTP_validate],
        "pushButton_STP_show" :  [ui,action_STP_show],
        "pushButton_RSTP_show" :  [ui,action_RSTP_show],
        "pushButton_STP_list" : [ui,lambda:bridge_list('name,other_config,stp_enable,status')],
        "pushButton_STP_port_refresh" : [ui,action_port_STP_refresh],
        "pushButton_STP_port_validate" : [ui,action_port_STP_validate],
        "pushButton_STP_refresh" : [ui,action_STP_refresh],
        "pushButton_STP_validate" : [ui,action_STP_validate],
        "pushButton_bond_lacp_show"  : [ui,action_bond_lacp_show],
        "pushButton_bond_list" : [ui,action_bond_list],
        "pushButton_bond_show" : [ui,action_show_bond],
        "pushButton_bond_slave_active" : [ui,action_bond_slave_active],
        "pushButton_bond_slave_disable" : [ui,action_bond_slave_disable],
        "pushButton_bond_slave_enable" : [ui,action_bond_slave_enable],
        "pushButton_bond_update"  : [ui,action_bond_params_update],
        "pushButton_bond_refresh"  : [ui,action_bond_refresh],
        "pushButton_bridge_list" : [ui,lambda:bridge_list('name,other_config,mcast_snooping_enable,status')],
        "pushButton_bridge_list_bridge" : [ui,action_bridge_list_bridge],
        "pushButton_bridge_listall" : [ui,lambda:bridge_list('')],
        "pushButton_bridge_newbridge" : [ui,action_bridge_add_bridge],
        "pushButton_bridge_ofctl_show" : [ui,action_bridge_ofctl_show],
        "pushButton_bridge_refresh" : [ui,action_bridge_refresh],
        "pushButton_bridge_update" : [ui,action_bridge_update],
        "pushButton_bridge_mactable_show" : [ui,action_bridge_mactable_show],
        "pushButton_bridge_mactable_flush" : [ui,action_bridge_mactable_flush],
        "pushButton_controller_conn_validate" : [ui,action_controller_conn_update],
        "pushButton_controller_params_validate" : [ui,action_controller_params_update],
        "pushButton_controller_refresh" : [ui,action_controller_refresh],
        "pushButton_controller_show" : [ui,action_controller_show],
        "pushButton_controller_validate" : [ui, action_controller_update],
        "pushButton_delete_bridge" : [ui,action_bridge_del_bridge],
        "pushButton_docker_export" : [ui,action_docker_export],
        "pushButton_docker_filter" : [ui,action_docker_image_filter],
        "pushButton_docker_import" : [ui,action_docker_import],
        "pushButton_docker_inspect" : [ui,docker_inspect],
        "pushButton_docker_link" : [ui,lambda:action_docker_link_iterate(False)],
        "pushButton_docker_link_iterate" : [ui,lambda:action_docker_link_iterate(True)],
        "pushButton_docker_ps_filter" : [ui,action_docker_ps],
        "pushButton_docker_remove" : [ui,action_docker_remove],
        "pushButton_docker_remove_image" : [ui,action_docker_remove_image],
        "pushButton_docker_run" : [ui,lambda:action_docker_run_iterate(False)],
        "pushButton_docker_run_iterate" : [ui,lambda:action_docker_run_iterate(True)],
        "pushButton_docker_start" : [ui,action_docker_start],
        "pushButton_docker_stop" : [ui,action_docker_stop],
        "pushButton_docker_stopremove" : [ui,action_docker_stopremove],
        "pushButton_dockerfile_add_line" : [ui,action_dockerfile_add_line],
        "pushButton_dockerfile_build" : [ui,action_dockerfile_build],
        "pushButton_dockerfile_clear" : [ui,action_dockerfile_clear],
        "pushButton_dockerfile_del_line" : [ui,action_dockerfile_del_line],
        "pushButton_dockerfile_down_line" : [ui,action_dockerfile_down_line],
        "pushButton_dockerfile_export" : [ui,action_dockerfile_export],
        "pushButton_dockerfile_import" : [ui,action_dockerfile_import],
        "pushButton_dockerfile_up_line" : [ui,action_dockerfile_up_line],
        "pushButton_dockerint_add_line" : [ui,lambda:action_dockerif_add(True)],
        "pushButton_dockerint_del_line" : [ui,action_dockerif_del],
        "pushButton_dockerint_down_line" : [ui,action_dockerif_down],
        "pushButton_dockerint_edit" : [ui,lambda:action_dockerif_add(False)],
        "pushButton_dockerint_up_line" : [ui,action_dockerif_up],
        "pushButton_dockernet_add_line" : [ui,lambda:action_dockernet_add(True)],
        "pushButton_dockernet_del_line" : [ui,action_dockernet_del],
        "pushButton_dockernet_down_line" : [ui,action_dockernet_down],
        "pushButton_dockernet_edit" : [ui,lambda:action_dockernet_add(False)],
        "pushButton_dockernet_export" : [ui,action_dockernet_export],
        "pushButton_dockernet_import" : [ui,action_dockernet_import],
        "pushButton_dockernet_up_line" : [ui,action_dockernet_up],
        "pushButton_findovs" : [ui,lambda:action_findovs(ui.lineEdit_ovs_name)],
        "pushButton_flood_off"  : [ui,lambda:action_mod_port('noflood')],
        "pushButton_flood_on"  : [ui,lambda:action_mod_port('flood')],
        "pushButton_forward_off"  : [ui,lambda:action_mod_port('noforward')],
        "pushButton_forward_on"  : [ui,lambda:action_mod_port('forward')],
        "pushButton_ingress_modify" : [ui,action_ingress_modify],
        "pushButton_ingress_refresh" : [ui,action_ingress_refresh],
        "pushButton_interface_list" : [ui,action_interface_list],
        "pushButton_interface_refresh" : [ui,action_interface_refresh],
        "pushButton_interface_type_refresh" : [ui,action_interface_type_refresh],
        "pushButton_interface_type_update" : [ui,action_interface_type_update],
        "pushButton_interface_update" : [ui,action_interface_update],
        "pushButton_ip_addr" : [ui,action_ip_addr],
        "pushButton_ip_addr_add" : [ui,action_ip_address_add],
        "pushButton_ip_addr_flush" : [ui,action_ip_address_flush],
        "pushButton_ip_link" : [ui,action_ip_link],
        "pushButton_ip_link_dummy_add" : [ui,action_create_dummy_interface],
        "pushButton_ip_link_mtu_set" : [ui,action_ip_set_mtu],
        "pushButton_ip_link_tap_add" : [ui,action_create_tap_interface],
        "pushButton_ip_link_tun_add" : [ui,action_create_tun_interface],
        "pushButton_ip_link_veth_add" : [ui,action_create_veth_pair],
        "pushButton_kvm_net_create" : [ui,lambda:action_kvm_net_create(False)],
        "pushButton_kvm_net_define" : [ui,lambda:action_kvm_net_create(True)],
        "pushButton_kvm_net_destroy" : [ui,action_kvm_net_destroy],
        "pushButton_kvm_net_dumpxml" : [ui,action_kvm_net_dumpxml],
        "pushButton_kvm_net_list" : [ui,action_kvm_net_list],
        "pushButton_kvm_net_load" : [ui,action_select_kvm_xml_file],
        "pushButton_kvm_net_save" : [ui,action_save_kvm_xml_file],
        "pushButton_kvm_net_start" : [ui,action_kvm_net_start],
        "pushButton_kvm_net_undefine" : [ui,action_kvm_net_undefine],
        "pushButton_kvm_pg_add" : [ui,action_kvm_pg_create],
        "pushButton_kvm_pg_delete" : [ui,action_kvm_pg_delete],
        "pushButton_kvm_pg_edit" : [ui,action_kvm_pg_edit],
        "pushButton_kvm_virt_clear" :  [ui,action_kvm_virt_clear],
        "pushButton_kvm_virt_disk_add" : [ui,lambda:kvm_virt_disk_table.new_row()],
        "pushButton_kvm_virt_disk_add_wiz" : [ui,action_dialog_kvm_virt_disk],
        "pushButton_kvm_virt_disk_del" : [ui,lambda:kvm_virt_disk_table.delete_row()],
        "pushButton_kvm_virt_disk_down" : [ui,lambda:kvm_virt_disk_table.down_row()],
        "pushButton_kvm_virt_disk_up" : [ui,lambda:kvm_virt_disk_table.up_row()],
        "pushButton_kvm_virt_export" :  [ui,action_kvm_virt_export],
        "pushButton_kvm_virt_gen_iso" : [ui,action_kvm_iso_gen],
        "pushButton_kvm_virt_import" :  [ui,action_kvm_virt_import],
        "pushButton_kvm_virt_misc_add" : [ui,lambda:kvm_virt_misc_table.new_row()],
        "pushButton_kvm_virt_misc_del" : [ui,lambda:kvm_virt_misc_table.delete_row()],
        "pushButton_kvm_virt_misc_down" : [ui,lambda:kvm_virt_misc_table.down_row()],
        "pushButton_kvm_virt_misc_up" : [ui,lambda:kvm_virt_misc_table.up_row()],
        "pushButton_kvm_virt_net_add" : [ui,lambda:kvm_virt_net_table.new_row()],
        "pushButton_kvm_virt_net_add_wiz" : [ui,action_dialog_kvm_virt_net],
        "pushButton_kvm_virt_net_del" : [ui,lambda:kvm_virt_net_table.delete_row()],
        "pushButton_kvm_virt_net_down" : [ui,lambda:kvm_virt_net_table.down_row()],
        "pushButton_kvm_virt_net_up" : [ui,lambda:kvm_virt_net_table.up_row()],
        "pushButton_kvm_virt_run" :  [ui,action_kvm_virt_run],
        "pushButton_mgmt_testssh" : [ui,action_testssh],
        "pushButton_mgmt_add" : [ui,action_mgmt_add],
        "pushButton_mgmt_del" : [ui,action_mgmt_del],
        "pushButton_mgmt_del_all" : [ui,action_mgmt_del_all],
        "pushButton_mgmt_edit" : [ui,action_mgmt_edit],
        "pushButton_mgmt_export" : [ui,action_mgmt_export],
        "pushButton_mgmt_findovs" : [mgmt_ui,lambda:action_findovs(mgmt_ui.lineEdit_mgmt_switch)],
        "pushButton_mgmt_import" : [ui,action_mgmt_interactive_import],
        "pushButton_mgmt_select_customscript" : [mgmt_ui,action_mgmt_select_customscript],
        "pushButton_mirror_add" : [ui,action_mirror_add],
        "pushButton_mirror_del" : [ui,action_mirror_del],
        "pushButton_mirror_list" : [ui,action_mirror_list],
        "pushButton_mirror_refresh" : [ui,action_mirror_refresh],
        "pushButton_mirror_select_dst" : [ui,lambda:action_mirror_select_port(ui.lineEdit_mirror_select_dst,single=False)],
        "pushButton_mirror_select_outputport" : [ui,lambda:action_mirror_select_port(ui.lineEdit_mirror_output_port,single=True)],
        "pushButton_mirror_select_src" : [ui,lambda:action_mirror_select_port(ui.lineEdit_mirror_select_src,single=False)],
        "pushButton_netflow_clear" : [ui,action_netflow_clear],
        "pushButton_netflow_create" : [ui,action_netflow_create],
        "pushButton_netflow_list" : [ui,lambda:action_netflow_list(output=True)],
        "pushButton_netflow_refresh" : [ui,lambda:action_netflow_list(output=False)],
        "pushButton_netflow_update" : [ui,action_netflow_update],
        "pushButton_of_add" : [of_ui,action_of_add],
        "pushButton_of_delete" : [ui,action_of_delete],
        "pushButton_of_delete_all" : [ui,action_of_delete_all],
        "pushButton_of_dialog_action_add" : [of_ui,action_of_dialog_action_add],
        "pushButton_of_dialog_action_del" : [of_ui,action_of_dialog_action_del],
        "pushButton_of_dialog_action_del_all": [of_ui,action_of_dialog_action_del_all],
        "pushButton_of_dialog_action_down" : [of_ui,action_of_dialog_action_down],
        "pushButton_of_dialog_action_up" : [of_ui,action_of_dialog_action_up],
        "pushButton_of_dialog_cond_add" : [of_ui,action_of_dialog_cond_add],
        "pushButton_of_dialog_cond_del" : [of_ui,action_of_dialog_cond_del],
        "pushButton_of_dialog_cond_del_all": [of_ui,action_of_dialog_cond_del_all],
        "pushButton_of_dialog_floweditor" : [ui,action_of_floweditor],
        "pushButton_of_edit" : [of_ui,action_of_edit],
        "pushButton_of_export" : [ui,action_of_export],
        "pushButton_of_import" : [ui,action_of_import],
        "pushButton_of_refresh" : [ui,action_of_refresh],
        "pushButton_dpctl_dumpflows" : [ui,action_of_dpctl_dumpflows],
        "pushButton_dumpflows" : [ui,action_of_dumpflows],
        "pushButton_of_trace_add" : [oftrace_ui,action_trace_add],
        "pushButton_of_trace_del" : [oftrace_ui,action_trace_del],
        "pushButton_of_trace_del_all" : [oftrace_ui,action_trace_del_all],
        "pushButton_of_trace_export" : [oftrace_ui,action_trace_export],
        "pushButton_of_trace_import" : [oftrace_ui,action_trace_import],
        "pushButton_of_trace_packet_load" : [oftrace_ui,action_trace_packet_load],
        "pushButton_of_trace_run" : [oftrace_ui,action_trace_run],
        "pushButton_ofgroup_add" : [ofgroup_ui,lambda:action_ofgroup_add(newgroup=True)],
        "pushButton_ofgroup_bucket_add"  : [ofgroup_ui,action_ofgroup_bucket_add],
        "pushButton_ofgroup_bucket_del"  : [ofgroup_ui,action_ofgroup_bucket_del],
        "pushButton_ofgroup_bucket_del_all"  : [ofgroup_ui,action_ofgroup_bucket_del_all],
        "pushButton_ofgroup_bucket_down"  : [ofgroup_ui,action_ofgroup_bucket_down],
        "pushButton_ofgroup_bucket_up"  : [ofgroup_ui,action_ofgroup_bucket_up],
        "pushButton_ofgroup_delete"  : [ui,action_ofgroup_delete],
        "pushButton_ofgroup_delete_all" : [ui,action_ofgroup_delete_all],
        "pushButton_ofgroup_edit" : [ofgroup_ui,lambda:action_ofgroup_add(newgroup=False)],
        "pushButton_ofgroup_editor"  : [ui,action_ofgroup_editor],
        "pushButton_ofgroup_export" : [ui,action_ofgroup_export],
        "pushButton_ofgroup_import" : [ui,action_ofgroup_import],
        "pushButton_ofgroup_param_add"  : [ofgroup_ui,action_ofgroup_param_add],
        "pushButton_ofgroup_param_del"  : [ofgroup_ui,action_ofgroup_param_del],
        "pushButton_ofgroup_param_del_all"  : [ofgroup_ui,action_ofgroup_param_del_all],
        "pushButton_ofgroup_param_down"  : [ofgroup_ui,action_ofgroup_param_down],
        "pushButton_ofgroup_param_up"  : [ofgroup_ui,action_ofgroup_param_up],
        "pushButton_ofgroup_refresh" : [ui,action_ofgroup_refresh],
        "pushButton_oftrace": [ui,action_trace_packet_show],
        "pushButton_open_vswitch_refresh" : [ui,action_open_vswitch_refresh],
        "pushButton_open_vswitch_show" : [ui,action_open_vswitch_show],
        "pushButton_open_vswitch_validate" : [ui,action_open_vswitch_validate],
        "pushButton_open_vswitch_validate_stats" : [ui,action_open_vswitch_stats_validate],
        "pushButton_output" : [ui,output_dialog_show],
        "pushButton_output_batch_exec" : [output_ui,output_batch_exec],
        "pushButton_output_command_exec" : [output_ui,output_command_exec],
        "pushButton_output_select_batch_file" : [output_ui,output_select_batch],
        "pushButton_outputclear" : [output_ui,action_output_clear],
        "pushButton_outputsave" : [output_ui,action_output_save],
        "pushButton_ovs_route_show" : [ui,action_ovs_route_show],
        "pushButton_packetin_off"  : [ui,lambda:action_mod_port('no-packet-in')],
        "pushButton_packetin_on"  : [ui,lambda:action_mod_port('packet-in')],
        "pushButton_plotnet_refresh" : [ui,action_plotnet_refresh],
        "pushButton_plotnet_export" : [ui,action_plotnet_export],
        "pushButton_plotnet_import" : [ui,action_plotnet_import],
        "pushButton_port_add" : [ui,action_port_add],
        "pushButton_port_del" : [ui,action_port_del],
        "pushButton_port_dock" :  [ui,action_port_dock],
        "pushButton_port_filter" : [ui,action_port_filter],
        "pushButton_port_list" : [ui,action_port_list],
        "pushButton_qos_add_qos" :  [ui,lambda:action_dialog_qos_qos(True)],
        "pushButton_qos_add_queue" :  [ui,action_dialog_qos_queue],
        "pushButton_qos_addflow" : [ui,action_qos_addflow],
        "pushButton_qos_edit_qos" : [ui,lambda:action_dialog_qos_qos(False)],
        "pushButton_qos_findport" : [ui,action_qos_find_ports],
        "pushButton_qos_link_queue" :  [ui,action_qos_link_queue],
        "pushButton_qos_port_set" : [ui,action_qos_port_set],
        "pushButton_qos_port_unset" : [ui,action_qos_port_unset],
        "pushButton_qos_qos_list" :  [ui,lambda:action_qos_porttree_refresh(True)],
        "pushButton_qos_qos_refresh" :  [ui,lambda:action_qos_porttree_refresh(False)],
        "pushButton_qos_queue_edit" :  [ui,action_dialog_qos_edit_queue],
        "pushButton_qos_queue_list" :  [ui,lambda:action_qos_queue_refresh(True)],
        "pushButton_qos_queue_refresh" :  [ui,lambda:action_qos_queue_refresh(False)],
        "pushButton_qos_remove_qos" :  [ui,action_qos_remove_qos],
        "pushButton_qos_remove_queue" :  [ui,action_qos_remove_queue],
        "pushButton_qos_unlink_queue" :  [ui,action_qos_unlink_queue],
        "pushButton_qos_qos_show_types" :  [ui,action_qos_qos_show_types],
        "pushButton_qos_qos_show" :  [ui,action_qos_qos_show],
        "pushButton_qos_qos_show_stats" :  [ui,action_qos_show_stats],
        "pushButton_receive_off"  : [ui,lambda:action_mod_port('noreceive')],
        "pushButton_receive_on"  : [ui,lambda:action_mod_port('receive')],
        "pushButton_receivestp_off"  : [ui,lambda:action_mod_port('no-receive-stp')],
        "pushButton_receivestp_on"  : [ui,lambda:action_mod_port('receive-stp')],
        "pushButton_selectssh" : [mgmt_ui,action_selectssh],
        "pushButton_sflow_clear" : [ui,action_sflow_clear],
        "pushButton_sflow_create" : [ui,action_sflow_create],
        "pushButton_sflow_list" : [ui,lambda:action_sflow_list(output=True)],
        "pushButton_sflow_refresh" : [ui,lambda:action_sflow_list(output=False)],
        "pushButton_sflow_update" : [ui,action_sflow_update],
        "pushButton_ssl_load_cacert" : [ui,lambda:load_filename_to_widget(ui.lineEdit_ssl_ca_cert,'Select private ca cert to load',keyDir)],
        "pushButton_ssl_load_cert" : [ui,lambda:load_filename_to_widget(ui.lineEdit_ssl_cert,'Select private cert to load',keyDir)],
        "pushButton_ssl_load_privatekey" : [ui,lambda:load_filename_to_widget(ui.lineEdit_ssl_private_key,'Select private key to load',keyDir)],
        "pushButton_ssl_refresh" : [ui,action_ssl_refresh],
        "pushButton_ssl_show" : [ui,action_ssl_show],
        "pushButton_ssl_update" : [ui,action_ssl_update],
        "pushButton_state_down"  : [ui,lambda:action_mod_port('down')],
        "pushButton_state_up"  : [ui,lambda:action_mod_port('up')],
        "pushButton_stats_dialog" : [ui,action_stats_dialog_show],
        "pushButton_stats_dialog_refresh" : [stats_ui,action_interface_statistics_refresh],
        "pushButton_stats_set_delta_origin" : [stats_ui,action_set_delta_origin],
        "pushButton_stp_off"  : [ui,lambda:action_mod_port('no-stp')],
        "pushButton_stp_on"  : [ui,lambda:action_mod_port('stp')],
        "pushButton_vlan_modify" : [ui,action_vlan_modify],
        "pushButton_vlan_refresh" : [ui,action_vlan_refresh],
        "pushButtonif_close" : [if_ui,if_close],
        "pushButtonif_refresh" : [if_ui,action_interface_list],
        "pushButtonpt_close" : [pt_ui,pt_close],
        "pushButtonpt_refresh" : [pt_ui,action_port_list],
        #"pushButton_kvm_virt_misc_add_wiz" : [ui,action_dialog_misc],
    }

    kvm_virt_mapping={
        '--name' : ui.lineEdit_kvm_virt_vmname,
        '--ram': ui.lineEdit_kvm_virt_ram,
        '--vcpu': ui.lineEdit_kvm_virt_vcpu,
    }

    lineedit_mapping={
        "lineEdit_port" : [ui,action_port_add],
        "lineEdit_port_filter" : [ui,action_port_filter],
        "lineEdit_ovs_name" : [ui,lambda:refresh_destination()],
        "lineEdit_bond_try_mac" : [ui,action_bond_hash],
        "lineEdit_plotnet_label_filter" : [ui,action_plotnet_refresh],
    }

    combobox_mapping={
        "comboBox_STP_enable" : [ui,action_STP_toggle],
        "comboBox_RSTP_enable" : [ui,action_RSTP_toggle],
        "comboBox_MCAST_enable" : [ui,action_MCAST_toggle],
        "comboBox_type" : [ui,action_interface_type_enable_fields],
        "comboBox_dockernet" : [dockernet_ui,action_dockernet_enable_fields],
        "comboBox_mgmt_comm" : [mgmt_ui,action_mgmt_access_enable_fields],
        "comboBox_mgmt_custom" : [mgmt_ui,action_mgmt_custom_enable_fields],
        "comboBox_dialog_qos_qos_type" : [qqos_ui,action_qos_dialog_enable_fields],
        "comboBox_if_ar" : [if_ui,action_interface_list_refresh],
        "comboBox_pt_ar" : [pt_ui,action_port_list_refresh],
        "comboBox_dialog_kvm_virt_device" :  [vn_ui,action_kvm_virt_net_fill],
    }

    menu_mapping={
        "actionQuit" : [ui,ovs_close],
        "actionSave_preferences" : [ui,save_preferences],
        "actionShow_moduleversion"  : [ui,about_versions],
        "actionAbout_Qt"  : [ui,lambda:action_about('Qt')],
        "actionAbout_icons"  : [ui,lambda:action_about('icons')],
        "actionAbout_OpenvSwitch"  : [ui,lambda:action_about('ovs')],
        "actionAbout_plotnetcfg"  : [ui,lambda:action_about('plotnetcfg')],
        "actionAbout_KVM"  : [ui,lambda:action_about('kvm')],
        "actionAbout_Docker"  : [ui,lambda:action_about('Docker')],
        "actionAbout_Python"  : [ui,lambda:action_about('Python')],
        "actionAbout_Orbitron_font"  : [ui,lambda:action_about('Orbitron')],
        "actionAbout"  : [ui,lambda:action_about('project')],
        "actionApache2_license"  : [ui,lambda:action_about('apache2')],
        "actionAbout_Graphviz"  : [ui,lambda:action_about('graphviz')],
        "actionStylesheet01" : [ui,lambda:define_stylesheet('01.qss')],
        "actionStylesheet02" : [ui,lambda:define_stylesheet('02.qss')],
        "actionStylesheetNone" : [ui,lambda:define_stylesheet('nostylesheet')],
        "actionStylesheetCustom" : [ui,lambda:define_stylesheet('custom')],
        "actionExport_current_stylesheet_to_file" : [ui,action_export_stylesheet],
        "actionFontSize12" : [ui,lambda:change_font_size(12)],
        "actionFontSize16" : [ui,lambda:change_font_size(16)],
        "actionFontSize20" : [ui,lambda:change_font_size(20)],
        "actionFontSize24" : [ui,lambda:change_font_size(24)],
        "actionFontSize28" : [ui,lambda:change_font_size(28)],
        "actionFontSize32" : [ui,lambda:change_font_size(32)],
        "actionFontSize36" : [ui,lambda:change_font_size(36)],
        "actionFontSize40" : [ui,lambda:change_font_size(40)],
        "actionFontSize44" : [ui,lambda:change_font_size(44)],
        "actionFontSize48" : [ui,lambda:change_font_size(48)],
        "actionFontSize52" : [ui,lambda:change_font_size(52)],
        "actionFontSize56" : [ui,lambda:change_font_size(56)],
        "actionFontSize60" : [ui,lambda:change_font_size(60)],
        "actionFontSize64" : [ui,lambda:change_font_size(64)],
        "actionIconSize12" : [ui,lambda:change_icon_size(12)],
        "actionIconSize16" : [ui,lambda:change_icon_size(16)],
        "actionIconSize20" : [ui,lambda:change_icon_size(20)],
        "actionIconSize24" : [ui,lambda:change_icon_size(24)],
        "actionIconSize28" : [ui,lambda:change_icon_size(28)],
        "actionIconSize32" : [ui,lambda:change_icon_size(32)],
        "actionIconSize36" : [ui,lambda:change_icon_size(36)],
        "actionIconSize40" : [ui,lambda:change_icon_size(40)],
        "actionIconSize44" : [ui,lambda:change_icon_size(44)],
        "actionIconSize48" : [ui,lambda:change_icon_size(48)],
        "actionIconSize52" : [ui,lambda:change_icon_size(52)],
        "actionIconSize56" : [ui,lambda:change_icon_size(56)],
        "actionIconSize60" : [ui,lambda:change_icon_size(60)],
        "actionIconSize64" : [ui,lambda:change_icon_size(64)],
    }

    list_mapping={
        "listWidget_kvm_net" : [ui,action_kvm_net_select],
    }

    name2label_mapping={
        "UUID" : ui.label_kvm_net_uuid,
        "Active" : ui.label_kvm_net_active,
        "Persistent" : ui.label_kvm_net_persistent,
        "Autostart" : ui.label_kvm_net_autostart,
        "Bridge" : ui.label_kvm_net_bridge,
    }

    
    style_property_mapping={
        if_ui.if_scrollAreaWidgetContents : "paintme01",
        if_ui.if_frame : "paintme01",
        pt_ui.pt_scrollAreaWidgetContents : "paintme01",
        pt_ui.pt_frame : "paintme01",
    }


    
    virt_man={
    }

    
    kvm_net_list=Mylist(ui.listWidget_kvm_net)

    ui.tabs_ports.currentChanged.connect(tabs_port_changed)
    ui.port_treeView.clicked.connect(list_port_select)
    ui.tabs_main.currentChanged.connect(main_tab_changed)

    for wid,prop in style_property_mapping.items():
        wid.setProperty(prop,True)


    pattern_name = re.compile(r'name\s+\:\s\"?([\w_\-]+)')
    pattern_word = re.compile(r'^([\w_\-]+)$')
    pattern_portname = re.compile(r'^([\w_\-\.\@\:]+)$')
    pattern_pgname = pattern_word
    pattern_XX = re.compile(r'(\d\d)$')
    pattern_XX_ipv4 = re.compile(r'\.\d+\/')
    pattern_XX_ipv6 = re.compile(r'\:[0-9a-fA-F]+\/')
    pattern_tag = re.compile(r'tag\s+\:\s(\d+)')
    pattern_trunk = re.compile(r'trunks\s+\:\s\[([\d\,\s]+)\]')
    pattern_space = re.compile(r'\s+')
    pattern_quote = re.compile(r'[\"\']+')
    pattern_comma = re.compile(r'\s*\,\s*')
    pattern_vlanmode = re.compile(r'vlan_mode\s+\:\s([\w\-]+)')
    pattern_type = re.compile(r'type\s+\:\s([\w\-\_\"]+)')
    pattern_options = re.compile(r'options\s+\:\s\{[\w\-]+\=(.*)\}')
    pattern_if_field = re.compile(r'^(\S+)\s*\:\s+(\S.*)')
    pattern_field = re.compile(r'^(\S+)\s*\:\s+(\S.*)')
    pattern_docker_image = re.compile(r'^(\S+)\s')
    pattern_bond = re.compile(r'^(\S+)\s')
    pattern_number = re.compile(r'^(\d+)$')
    pattern_number_list = re.compile(r'^(\d+)(?:\:(\d+))*$')
    pattern_vlan = re.compile(r'^(\d+)([tu]?)$')
    pattern_begin_by_letter = re.compile(r'^(\w.*)')
    pattern_net = pattern_begin_by_letter
    pattern_net_uuid = re.compile(r'\s*<uuid>')
    pattern_colon = re.compile(r':')
    pattern_colon2 = re.compile(r'^(.+):(.+)')
    pattern_brackets=re.compile(r'(?:^[\[\{])|(?:[\]\}]$)')
    pattern_surrounding_quotes=re.compile(r'(?:^[\"\'])|(?:[\"\']$)')
    pattern_other_config=re.compile(r'(?:\s*\=\s*)|(?:\s*\,\s+)')
    pattern_flow_table=re.compile(r'\s*table=(\d+)\,')
    pattern_flow_group=re.compile(r'\s*group_id=(\d+)\,type=(\w+),(bucket=.+)')
    pattern_flow_actions=re.compile(r'\s*actions\=(.+)')
    pattern_flow_cond=re.compile(r'\s*(.+?)(?=\sactions\=)')
    pattern_SWITCHNAME=re.compile(r'_SWITCHNAME_')
    pattern_action_code=re.compile(r'^(?:(\w+?[\(\:])(.*))|(\w+)$')
    pattern_equal=re.compile(r'=')
    pattern_slash=re.compile(r'\/')
    pattern_tracefile=re.compile(r'(?:\#:\#)|(?:\#,\#)')
    pattern_bucket=re.compile(r'bucket\=')
    pattern_bucket_params_actions=re.compile(r'(.*?)actions\=(.+)')
    pattern_enclosing_quote=re.compile(r'^\'(.*)\'$',flags=re.MULTILINE)
    pattern_dockerfile=re.compile(r'(\S*)\s(.+)')
    pattern_iplink=re.compile(r'^(\S*?)[\@\s]')
    pattern_comment=re.compile(r'(\#)(.*)')
    pattern_begin_space=re.compile(r'^\s')
    pattern_interface_desc=re.compile(r'^\s*\w+\(([\w_-]+)\):')
    pattern_interface_nodesc=re.compile(r'^\s*port\s+([\w_-]+):')
    pattern_space_comma=re.compile(r'[\s,]+')
    pattern_queue_map=re.compile(r'(\d+)\=')
    pattern_dot_label=re.compile(r'\[label\=\"(.+?)\"',flags=re.MULTILINE)
    pattern_dot_arrow=re.compile(r'^\"(.+?)\"\s->\s\"(.+?)\"')
    pattern_dot_subgraph_end=re.compile(r'^}')
    pattern_dot_subgraph_begin=re.compile(r'^subgraph\s')
    pattern_dot_subgraph_label=re.compile(r'^label=\"(.+?)\"')
    pattern_dot_node=re.compile(r'^(node\s\[.+?)(\])')
    pattern_qos_param=re.compile(r'^(.*?)=(.*)$')
    pattern_of_stats=re.compile(r'(?:\scookie=0x0,)|(?:\sduration=.+?,)|(?:\sn_packets=.+?,)|(?:\sn_bytes=.+?,)')
    pattern_ip_zeroprefix=re.compile(r'\.0(\d)')

    html_replace = {
        "<": "&lt;",
        '"': "&quot;",
        "&": "&amp;",
        ">": "&gt;",
        "'": "&apos;",
    }

    setEnableWidgetDic('INTERFACE','ALL',False)    
    setEnableWidgetList(ports_widget_list,False)
    setEnableWidgetList(vn_all_list,False)

    misc_dict={}


    comboBox_Write(mgmt_ui.comboBox_mgmt_openflow_protocol,'openflow14')
    
    bind_actions()

    timer_interfacelist=QTimer()
    timer_interfacelist.timeout.connect(action_interface_list)
    timer_portlist=QTimer()
    timer_portlist.timeout.connect(action_port_list)


    #1000x860

    ui.label_plotnet=QtWidgets.QLabel()
    ui.label_plotnet.setBackgroundRole(QPalette.Base)
    ui.label_plotnet.setSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Ignored)
    ui.label_plotnet.setScaledContents(True)

    ui.scrollArea_plotnet = QtWidgets.QScrollArea(ui.frame_for_scrollarea_plotnet)
    ui.scrollArea_plotnet.setBackgroundRole(QPalette.Dark)
    ui.scrollArea_plotnet.setWidget(ui.label_plotnet)
    ui.gridLayout_for_plotnet.addWidget(ui.scrollArea_plotnet, 1, 0, 1, 1)


    
    begin_pref()

    
    action_mgmt_auto_import()
    Mymgmt.create_system_mgmt()


    legal={
        'Qt':"""
This Project is using Qt.

Qt is a C++ toolkit for cross-platform application development.
Qt provides single-source portability across all major desktop operating systems.
It is also available for embedded Linux and other embedded and mobile operating systems.
Qt is available under three different licensing options designed to accommodate the needs of our various users.
Qt licensed under our commercial license agreement is appropriate for development of proprietary/commercial software where you do not want to share any source code with third parties or otherwise cannot comply with the terms of the GNU LGPL version 3.
Qt licensed under the GNU LGPL version 3 is appropriate for the development of Qt applications provided you can comply with the terms and conditions of the GNU LGPL version 3.
Please see qt.io/licensing for an overview of Qt licensing.
Copyright (C) 2017 The Qt Company Ltd and other contributors.
Qt and the Qt logo are trademarks of The Qt Company Ltd.
Qt is The Qt Company Ltd product developed as an open source project.

See qt.io for more information.

        """,
        
        'icons' : """
Icons used in this project come from Feather !

Feather is a collection of simply beautiful open source icons.
Each icon is designed on a 24x24 grid with an emphasis on simplicity, consistency and readability.

https://feathericons.com

        """,
        
        'ovs' : """
Open vSwitch is a production quality, multilayer virtual switch licensed under the open source Apache 2.0 license.
It is designed to enable massive network automation through programmatic extension, while still supporting standard management interfaces and protocols (e.g. NetFlow, sFlow, IPFIX, RSPAN, CLI, LACP, 802.1ag).

https://www.openvswitch.org/
        
        """,
        'Docker' : """
Docker is the world's leading software containerization platform.

https://www.docker.com/
        """,
        
        'plotnetcfg' : """
plotnetcfg is a tool that scans networking configuration on the machine and outputs a diagram of the configuration hierarchy.

https://github.com/jbenc/plotnetcfg
        """,
        'Orbitron' : """
Orbitron font was used for Ovs-ToolBox front page
        
https://fonts.google.com/specimen/Orbitron
        """,
        
        'kvm':"""
KVM (for Kernel-based Virtual Machine) is a full virtualization solution for Linux on x86 hardware containing virtualization extensions (Intel VT or AMD-V).

https://www.linux-kvm.org/page/Main_Page
        """,
        'Python' : """
This project is using Python.

Python is a programming language that lets you work quickly and integrate systems more effectively.

https://www.python.org/
        """,
        'graphviz' : """
This project is using Graphviz.

Graphviz is open source graph visualization software. Graph visualization is a way of representing structural information as diagrams of abstract graphs and networks. It has important applications in networking, bioinformatics,  software engineering, database and web design, machine learning, and in visual interfaces for other technical domains.
        
https://www.graphviz.org/ 
        """,
        
        'project':"""
OvS-ToolBox

release: {}
buildtime: {}
        
Copyright 2018 Nicolas Bonnand

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
        """.format(project_release,buildtime),

        'apache2':"""
                                 Apache License
                           Version 2.0, January 2004
                        http://www.apache.org/licenses/

   TERMS AND CONDITIONS FOR USE, REPRODUCTION, AND DISTRIBUTION

   1. Definitions.

      "License" shall mean the terms and conditions for use, reproduction,
      and distribution as defined by Sections 1 through 9 of this document.

      "Licensor" shall mean the copyright owner or entity authorized by
      the copyright owner that is granting the License.

      "Legal Entity" shall mean the union of the acting entity and all
      other entities that control, are controlled by, or are under common
      control with that entity. For the purposes of this definition,
      "control" means (i) the power, direct or indirect, to cause the
      direction or management of such entity, whether by contract or
      otherwise, or (ii) ownership of fifty percent (50%) or more of the
      outstanding shares, or (iii) beneficial ownership of such entity.

      "You" (or "Your") shall mean an individual or Legal Entity
      exercising permissions granted by this License.

      "Source" form shall mean the preferred form for making modifications,
      including but not limited to software source code, documentation
      source, and configuration files.

      "Object" form shall mean any form resulting from mechanical
      transformation or translation of a Source form, including but
      not limited to compiled object code, generated documentation,
      and conversions to other media types.

      "Work" shall mean the work of authorship, whether in Source or
      Object form, made available under the License, as indicated by a
      copyright notice that is included in or attached to the work
      (an example is provided in the Appendix below).

      "Derivative Works" shall mean any work, whether in Source or Object
      form, that is based on (or derived from) the Work and for which the
      editorial revisions, annotations, elaborations, or other modifications
      represent, as a whole, an original work of authorship. For the purposes
      of this License, Derivative Works shall not include works that remain
      separable from, or merely link (or bind by name) to the interfaces of,
      the Work and Derivative Works thereof.

      "Contribution" shall mean any work of authorship, including
      the original version of the Work and any modifications or additions
      to that Work or Derivative Works thereof, that is intentionally
      submitted to Licensor for inclusion in the Work by the copyright owner
      or by an individual or Legal Entity authorized to submit on behalf of
      the copyright owner. For the purposes of this definition, "submitted"
      means any form of electronic, verbal, or written communication sent
      to the Licensor or its representatives, including but not limited to
      communication on electronic mailing lists, source code control systems,
      and issue tracking systems that are managed by, or on behalf of, the
      Licensor for the purpose of discussing and improving the Work, but
      excluding communication that is conspicuously marked or otherwise
      designated in writing by the copyright owner as "Not a Contribution."

      "Contributor" shall mean Licensor and any individual or Legal Entity
      on behalf of whom a Contribution has been received by Licensor and
      subsequently incorporated within the Work.

   2. Grant of Copyright License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      copyright license to reproduce, prepare Derivative Works of,
      publicly display, publicly perform, sublicense, and distribute the
      Work and such Derivative Works in Source or Object form.

   3. Grant of Patent License. Subject to the terms and conditions of
      this License, each Contributor hereby grants to You a perpetual,
      worldwide, non-exclusive, no-charge, royalty-free, irrevocable
      (except as stated in this section) patent license to make, have made,
      use, offer to sell, sell, import, and otherwise transfer the Work,
      where such license applies only to those patent claims licensable
      by such Contributor that are necessarily infringed by their
      Contribution(s) alone or by combination of their Contribution(s)
      with the Work to which such Contribution(s) was submitted. If You
      institute patent litigation against any entity (including a
      cross-claim or counterclaim in a lawsuit) alleging that the Work
      or a Contribution incorporated within the Work constitutes direct
      or contributory patent infringement, then any patent licenses
      granted to You under this License for that Work shall terminate
      as of the date such litigation is filed.

   4. Redistribution. You may reproduce and distribute copies of the
      Work or Derivative Works thereof in any medium, with or without
      modifications, and in Source or Object form, provided that You
      meet the following conditions:

      (a) You must give any other recipients of the Work or
          Derivative Works a copy of this License; and

      (b) You must cause any modified files to carry prominent notices
          stating that You changed the files; and

      (c) You must retain, in the Source form of any Derivative Works
          that You distribute, all copyright, patent, trademark, and
          attribution notices from the Source form of the Work,
          excluding those notices that do not pertain to any part of
          the Derivative Works; and

      (d) If the Work includes a "NOTICE" text file as part of its
          distribution, then any Derivative Works that You distribute must
          include a readable copy of the attribution notices contained
          within such NOTICE file, excluding those notices that do not
          pertain to any part of the Derivative Works, in at least one
          of the following places: within a NOTICE text file distributed
          as part of the Derivative Works; within the Source form or
          documentation, if provided along with the Derivative Works; or,
          within a display generated by the Derivative Works, if and
          wherever such third-party notices normally appear. The contents
          of the NOTICE file are for informational purposes only and
          do not modify the License. You may add Your own attribution
          notices within Derivative Works that You distribute, alongside
          or as an addendum to the NOTICE text from the Work, provided
          that such additional attribution notices cannot be construed
          as modifying the License.

      You may add Your own copyright statement to Your modifications and
      may provide additional or different license terms and conditions
      for use, reproduction, or distribution of Your modifications, or
      for any such Derivative Works as a whole, provided Your use,
      reproduction, and distribution of the Work otherwise complies with
      the conditions stated in this License.

   5. Submission of Contributions. Unless You explicitly state otherwise,
      any Contribution intentionally submitted for inclusion in the Work
      by You to the Licensor shall be under the terms and conditions of
      this License, without any additional terms or conditions.
      Notwithstanding the above, nothing herein shall supersede or modify
      the terms of any separate license agreement you may have executed
      with Licensor regarding such Contributions.

   6. Trademarks. This License does not grant permission to use the trade
      names, trademarks, service marks, or product names of the Licensor,
      except as required for reasonable and customary use in describing the
      origin of the Work and reproducing the content of the NOTICE file.

   7. Disclaimer of Warranty. Unless required by applicable law or
      agreed to in writing, Licensor provides the Work (and each
      Contributor provides its Contributions) on an "AS IS" BASIS,
      WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
      implied, including, without limitation, any warranties or conditions
      of TITLE, NON-INFRINGEMENT, MERCHANTABILITY, or FITNESS FOR A
      PARTICULAR PURPOSE. You are solely responsible for determining the
      appropriateness of using or redistributing the Work and assume any
      risks associated with Your exercise of permissions under this License.

   8. Limitation of Liability. In no event and under no legal theory,
      whether in tort (including negligence), contract, or otherwise,
      unless required by applicable law (such as deliberate and grossly
      negligent acts) or agreed to in writing, shall any Contributor be
      liable to You for damages, including any direct, indirect, special,
      incidental, or consequential damages of any character arising as a
      result of this License or out of the use or inability to use the
      Work (including but not limited to damages for loss of goodwill,
      work stoppage, computer failure or malfunction, or any and all
      other commercial damages or losses), even if such Contributor
      has been advised of the possibility of such damages.

   9. Accepting Warranty or Additional Liability. While redistributing
      the Work or Derivative Works thereof, You may choose to offer,
      and charge a fee for, acceptance of support, warranty, indemnity,
      or other liability obligations and/or rights consistent with this
      License. However, in accepting such obligations, You may act only
      on Your own behalf and on Your sole responsibility, not on behalf
      of any other Contributor, and only if You agree to indemnify,
      defend, and hold each Contributor harmless for any liability
      incurred by, or claims asserted against, such Contributor by reason
      of your accepting any such warranty or additional liability.

   END OF TERMS AND CONDITIONS

   APPENDIX: How to apply the Apache License to your work.

      To apply the Apache License to your work, attach the following
      boilerplate notice, with the fields enclosed by brackets "[]"
      replaced with your own identifying information. (Don't include
      the brackets!)  The text should be enclosed in the appropriate
      comment syntax for the file format. We also recommend that a
      file or class name and description of purpose be included on the
      same "printed page" as the copyright notice for easier
      identification within third-party archives.

   Copyright 2018 Nicolas Bonnand

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

        """
    }

    random.seed()
    ui.tabs_main.setCurrentIndex(0)

    splash_ui.label_release.setText("buidtime: {}       release: {}".format(buildtime,project_release))
    splash_width=int(QDesktopWidget().availableGeometry().size().width()/2)
    splash_height=int(QDesktopWidget().availableGeometry().size().height()/2)

    new_pixmap=QPixmap(':/images/splashscreen.jpg').scaled(splash_width,splash_height, QtCore.Qt.KeepAspectRatio)
    splash_ui.label_splashscreen.setPixmap(new_pixmap);

    splash_ui.label_splashscreen.clicked.connect(lambda:splash_Dialog.close())

    MainWindow.show()
    splash_Dialog.show()
    sys.exit(app.exec_())
