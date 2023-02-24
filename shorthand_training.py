#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from pydub import AudioSegment
import os # os系统文件处理库
import random # 随机化动作库
import time #计时库
import datetime
import re

a1 = AudioSegment.from_wav('')
a2 = AudioSegment.from_wav('')

#print(type(a1))
#print(type(a2))

final_track = a1+a2
#print(type(final_track))
#print(type(final_track[0]))
#print(final_track[0])

buff = final_track.raw_data
#print(buff)
#print(type(buff))
# 设置网页标题
st.title('英语听力速记训练')
st.markdown("__*可以随机生成一段用于英语听力速记的音频*__")
st.audio(buff)

#samples = final_track.get_array_of_samples()

#final_track.export("/")
