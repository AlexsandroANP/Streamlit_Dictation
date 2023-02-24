#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from pydub import AudioSegment
import os # os系统文件处理库
import random # 随机化动作库
import time #计时库
import datetime
import re

# 设置网页标题
st.title('英语听力速记训练')
st.markdown("__*可以随机生成一段用于英语听力速记的音频*__")

for curDir, dirs, files in os.walk("/app/Streamlit_Dictation/", topdown=True):
  st.text("现在的目录：" + curDir)
  st.text("该目录下包含的子目录：" + str(dirs))
  st.text("该目录下包含的文件：" + str(files))

a1 = AudioSegment.from_wav('/app/Streamlit_Dictation/audio_chuncks/a.wav')
a2 = AudioSegment.from_wav('/app/Streamlit_Dictation/audio_chuncks/b.wav')

#print(type(a1))
#print(type(a2))

final_track = a1+a2
#print(type(final_track))
#print(type(final_track[0]))
#print(final_track[0])

buff = final_track.raw_data
#print(buff)
#print(type(buff))

st.audio(buff)

#samples = final_track.get_array_of_samples()

#final_track.export("/")
