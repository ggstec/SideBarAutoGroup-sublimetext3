# coding=utf8

import sublime, sublime_plugin
import configparser

st_version = 2
if sublime.version() == '' or int(sublime.version()) > 3000:
    st_version = 3



def Window(window=None):
    return sublime.active_window()

def group_get(filepath):
    variables=Window().extract_variables()
    folder=variables['folder']

    filepaths=filepath.split("/")
    del filepaths[0]
    folders=folder.split("/")
    arr=[]
    for i in range(len(folders),len(filepaths)):
        str1=""
        for k in range(0,i):
            str1=str1+"/"+filepaths[k]
        arr.append(str1)

    arr.reverse()

    group=setting_get(filepath)

    for item in arr:
        if group=="":
            group=setting_get(item)
        else:
            return group

    return group

def setting_get(path):
    variables=Window().extract_variables()
    folder=variables['folder']
    config = configparser.ConfigParser()
    config.read(folder+'/.autogroup',encoding="utf-8")
    
    path=path.replace(folder,'')
    path=path.lower()

    lists=config.sections()
    if len(lists)==0:
        config.add_section("setting")
        with open(folder+'/.autogroup', 'w',encoding="utf-8") as fw:
            config.write(fw)
        return ""
    else:
        options=config.options("setting")
        if(path in options):
            text=config.get("setting",path)
            return text
        else:
            return ""

def setting_save(path,value):
    variables=Window().extract_variables()
    folder=variables['folder']
    config = configparser.ConfigParser()
    config.read(folder+'/.autogroup',encoding="utf-8")

    lists=config.sections()
    if len(lists)==0:
        config.add_section("setting")

    path=path.replace(folder,'')

    config.set("setting",path,value)
    with open(folder+'/.autogroup', 'w',encoding="utf-8") as fw:
        config.write(fw)
    return True

class SideBarAutoGroupEventListener(sublime_plugin.EventListener):
    def on_load(self,v):        
        filepath=v.file_name()

        group=group_get(filepath)

        if group=="":
            group='1'

        group=int(group)-1
        
        Window().run_command("move_to_group", {"group": group})


class SideBarSetInGroup1Command(sublime_plugin.WindowCommand):
    def run(self, paths=[]):
        index=paths[0]
        setting_save(index,"1")

    def is_enabled(self, paths=[]):
        group=group_get(paths[0])
        if group=="1":
            return False
        else:
            return True
        

class SideBarSetInGroup2Command(sublime_plugin.WindowCommand):
    def run(self, paths=[]):
        index=paths[0]
        setting_save(index,"2")

    def is_enabled(self, paths=[]):
        group=group_get(paths[0])
        if group=="2":
            return False
        else:
            return True

class SideBarSetInGroup3Command(sublime_plugin.WindowCommand):
    def run(self, paths=[]):
        index=paths[0]
        setting_save(index,"3")

    def is_enabled(self, paths=[]):
        group=group_get(paths[0])
        if group=="3":
            return False
        else:
            return True

class SideBarSetInGroup4Command(sublime_plugin.WindowCommand):
    def run(self, paths=[]):
        index=paths[0]
        setting_save(index,"4")

    def is_enabled(self, paths=[]):
        group=group_get(paths[0])
        if group=="4":
            return False
        else:
            return True