#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File  : Endalarm.py
# @Author: Jeff Liu
# @Date  : 2019/6/17
# @Desc  :

def alarm(song):
    from pygame import mixer
    import time
    mixer.init()
    mixer.music.load(song)
    mixer.music.play()
    time.sleep(20)
    mixer.music.stop()



