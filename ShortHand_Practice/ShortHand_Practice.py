#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import streamlit as st
from pydub import AudioSegment
import random 
import re
import io
import glob 
import os

def audio_generater(playlist,pause):
    track = AudioSegment.silent(3000)
    pause = AudioSegment.silent(pause*1000)
    for i in playlist:
        track = track + AudioSegment.from_ogg(i) + pause
    buf = io.BytesIO()
    track.export(buf, format="wav")
    buf.getvalue()
    return buf

def vocaburaries_displayer(playlist):
    st.header('Vocaburaries list')
    st.caption('☟ 单词表')
    for i in playlist:
        name = re.compile(r'audio_chuncks/(.*?).ogg').findall(i)
        if '_' in name[0]:
            display = name[0].split('_')
            st.text('{:0>2d} {:^3} {:^15} {:>3} {:^10}'.format(playlist.index(i)+1,'｜',display[0],'｜',display[1]))
        else:
            st.text('{:0>2d} {:^20}'.format(playlist.index(i)+1,name[0]))
            

with st.spinner('Fetching Chuncks ...'):
    chuncks_list = glob.glob('/app/streamlit_apps/shorthand_practice/audio_chuncks/*.ogg')
    chuncks_numbers = len(chuncks_list)
    
    f_view = os.listdir()
    for i in f_view:
        st.text(f_view)
    
st.title('ShortHand Practice for Dictation')
st.caption('英文关键词速记练习')
st.markdown("__*Generating a Slice of Audio in ramdom words to Practise Shorthand Skill by Dictation*__")
st.caption("__*可以随机生成一段用于英语听力速记的音频*__")
'==================='
st.header("Preferences Settings")
st.markdown("**生成设定**")
''
input_numbers = st.number_input('How Many words to Be dictated?',
                                1, chuncks_numbers, 20,1)
st.caption('☝︎ 单词出现数量')
''
pause = st.number_input('How long the pause would take?',
                                1, chuncks_numbers, 3,1)
st.caption('☝︎  停顿间隔长短')
''
st.text('☟  生成')
if st.button('🎲Ready to Go!'):
    with st.spinner('Generating Playlist ...'):
        playlist = random.sample(chuncks_list,input_numbers)
    st.header('The Audio')
    st.caption('☟ 音频')
    with st.spinner('Generating Audio, Take a Deep Breath ...'):
        st.audio(audio_generater(playlist,pause),format='audio/wav')
        vocaburaries_displayer(playlist)

        
        
