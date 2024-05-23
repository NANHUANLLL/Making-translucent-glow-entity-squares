# -*- coding: utf-8 -*-

from mod.common.mod import Mod


@Mod.Binding(name="Script_NeteaseModk04rni4j", version="0.0.1")
class Script_NeteaseModk04rni4j(object):

    def __init__(self):
        pass

    @Mod.InitServer()
    def Script_NeteaseModk04rni4jServerInit(self):
        pass

    @Mod.DestroyServer()
    def Script_NeteaseModk04rni4jServerDestroy(self):
        pass

    @Mod.InitClient()
    def Script_NeteaseModk04rni4jClientInit(self):
        pass

    @Mod.DestroyClient()
    def Script_NeteaseModk04rni4jClientDestroy(self):
        pass
