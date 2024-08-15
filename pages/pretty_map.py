import streamlit as st
import logging 
import prettymaps
import sys

st.set_page_config(layout='wide')

logger = logging.getLogger(__name__)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
logger.info('Succsessful imports')

presets = prettymaps.presets()['preset'].values

if 'location' not in st.session_state:
    st.session_state['location'] = 'Vake, Tbilisi, Georgia'

if  'preset' not in st.session_state:
    st.session_state['preset'] = 'heerhugowaard'

if 'radius' not in st.session_state:
    st.session_state['radius'] = True

logger.info('Session states loaded...')

def draw_plot(title=None):
    logger.info('Start drawing..')
    fig = prettymaps.plot(
        query=st.session_state['location'],
        preset=st.session_state['preset'],
        circle=st.session_state['circle'],
        radius=st.session_state['radius']
    )
    if title:
        fig.fig.patch.set_facecolor('#F2F4CB')
        _ = fig.ax.set_title(
            title,
            font = 'serif',
            size = 50
        )
    st.pyplot(fig.fig)
    logger.info('Figure created')

param_col, plot_col = st.columns([.2, .8])

with param_col:
    with st.form('Set params'):
        location = st.text_input(
            'Input city or coords', 
            value=st.session_state['location']
            )
        # lcol, rcol = st.columns(2)
        preset = st.selectbox('Select color theme', presets, index=5)
        circle = st.checkbox('Circle', True)
        radius = st.slider(
            'Radius', 
            min_value=.1,
            max_value=1000.,
            step=5.,
            value=500.)
        title = st.text_input('Input title')
        st.session_state['location'] = location
        st.session_state['preset'] = preset
        st.session_state['radius'] = radius
        st.session_state['circle'] = circle
        draw_btn = st.form_submit_button('Draw')

    st.markdown(f'Inspired by [Almaty_pretty_map](https://github.com/Nurasssyl/Almaty_pretty_map) and [prettymaps](https://github.com/marceloprates/prettymaps)')



with plot_col:
    if draw_btn and location:
        logger.info('Button ok! ')
        with st.spinner('Getting OSM data...'):
            draw_plot(title)