
import streamlit as st
import pandas as pd
import os
import plotly.express as px

# ------------------ Login ------------------ #
if 'logged_in' not in st.session_state:
    st.session_state['logged_in'] = False

if not st.session_state['logged_in']:
    with st.sidebar:
        st.subheader("Login Pegawai")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        if st.button("Login"):
            if username == "admin" and password == "pln123":
                st.session_state['logged_in'] = True
                st.success("Login berhasil!")
                st.rerun()
            else:
                st.error("Username/password salah")
    st.stop()

# ------------------ Tombol Logout ------------------ #
st.markdown("""
    <style>
    .logout-button {
        position: absolute;
        top: 10px;
        right: 16px;
        background-color: #f44336;
        color: white;
        border: none;
        padding: 6px 12px;
        border-radius: 6px;
        cursor: pointer;
    }
    </style>
    <form action="#" method="post">
        <button class="logout-button" onclick="window.location.reload();">Logout</button>
    </form>
""", unsafe_allow_html=True)

# ------------------ Setup ------------------ #
st.set_page_config(page_title="Dashboard TO AMR", layout="wide")
st.title("📊 Dashboard Target Operasi AMR - P2TL")
st.markdown("---")

# ------------------ Ambil parameter threshold dan alias ------------------ #
param = {k: v for k, v in st.session_state.items() if isinstance(v, (int, float))}
param['i_over'] = param.get('over_i_tm', 5.0)
param['i_max'] = param.get('max_i_tm', 100.0)
param['cos_phi_max'] = param.get('cos_phi_tm', 0.85)
param['v_over_tm'] = param.get('vmax_tm', 240.0)
param['v_over_tr'] = param.get('vmax_tr', 241.0)
param['v_drop_min'] = param.get('low_v_diff_tm', 10.0)
param['unbalance_tol'] = param.get('unbal_tol_tm', 0.15)

# (kode lain tetap mengikuti...)

