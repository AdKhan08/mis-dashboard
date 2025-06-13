import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# --- HEADER ---
st.markdown(
    '<div style="background: #ffe600; padding: 0.5rem 0; text-align: left; font-size: 2.5rem; font-weight: bold; color: #111; border-bottom: 2px solid #111;">'
    'MIS Dashboard</div>',
    unsafe_allow_html=True
)

# --- PAGE TITLE & BUTTONS ---
header_col, download_col, share_col = st.columns([6, 1, 1])
with header_col:
    st.markdown('<div style="text-align:right; font-size:1.5rem; font-weight:bold; color:#00338D; margin-bottom:1rem;">Main Page</div>', unsafe_allow_html=True)
with download_col:
    st.button("Download")
with share_col:
    st.button("Share")

# --- FILTERS ---
filter1, filter2, filter3, filter4, filter5 = st.columns(5)
with filter1:
    date_range = st.date_input("Date Range", value=(datetime.now() - timedelta(days=30), datetime.now()))
with filter2:
    department = st.selectbox("Department", ["All", "Property Tax", "Trade License", "Complaints", "MCollect", "Fire NOC", "Finance"])
with filter3:
    ulb = st.selectbox("ULB", ["All ULBs", "Kothaguru", "Machhliwara", "Boha"])
with filter4:
    ddr = st.selectbox("DDR", ["All DDRs", "DDR 1", "DDR 2"])
with filter5:
    denomination = st.selectbox("Denomination", ["Cr", "Lac", "Unit"])

st.markdown("---")

# --- KPI CARDS ---
st.markdown("""
<style>
.kpi-card {
    background: #e3f0fa;
    border-radius: 1rem;
    padding: 1.5rem 1rem;
    margin-bottom: 1rem;
    box-shadow: 0 2px 8px rgba(0,0,0,0.07);
    text-align: left;
}
.kpi-title { font-size: 1.1rem; color: #00338D; font-weight: bold; }
.kpi-value { font-size: 2.2rem; color: #222; font-weight: bold; }
.kpi-sub { font-size: 1rem; color: #666; }
</style>
""", unsafe_allow_html=True)

kpis = [
    {"title": "Total Collection", "value": "₹4,326.07 Lac", "sub": "Overview"},
    {"title": "Target Achievement", "value": "0.00 %", "sub": "0% than LY"},
    {"title": "Total Applications", "value": "1,37,808", "sub": "63.31% than LY"},
    {"title": "SLA Achievement", "value": "100.00 %", "sub": "0% than LY"},
]

kpi_cols = st.columns(4)
for i, kpi in enumerate(kpis):
    with kpi_cols[i]:
        st.markdown(f'<div class="kpi-card"><div class="kpi-title">{kpi["title"]}</div>'
                    f'<div class="kpi-value">{kpi["value"]}</div>'
                    f'<div class="kpi-sub">{kpi["sub"]}</div></div>', unsafe_allow_html=True)

st.markdown("---")

# --- SUB KPI CARDS ---
sub_kpis = [
    {"title": "Property Tax", "value": "₹4,208.68 Lac", "sub": "Total Properties Assessed: 1,20,020", "trend": "68.45% than LY", "color": "#a48be0"},
    {"title": "Trade License", "value": "₹117.40 Lac", "sub": "Total Applications: 9,444", "trend": "71.54% than LY", "color": "#f7b7a3"},
    {"title": "Complaints", "value": "8,344", "sub": "SLA Achievement: 100%", "trend": "78.55% than LY", "color": "#8fd19e"},
    {"title": "MCollect", "value": "₹6,045.30 Lac", "sub": "Total Receipts: 55,606", "trend": "68.52% than LY", "color": "#ffe066"},
    {"title": "Fire NOC", "value": "₹217.22 Lac", "sub": "Total NOCs: 1,634", "trend": "133.62% than LY", "color": "#a3d2f7"},
    {"title": "Finance", "value": "Bills: 1,67,340", "sub": "Payments: 94,717", "trend": "-", "color": "#d1b3e0"},
]

sub_kpi_cols = st.columns(3)
for i, sub_kpi in enumerate(sub_kpis):
    with sub_kpi_cols[i % 3]:
        st.markdown(f'<div class="kpi-card" style="background:{sub_kpi["color"]}"><div class="kpi-title">{sub_kpi["title"]}</div>'
                    f'<div class="kpi-value">{sub_kpi["value"]}</div>'
                    f'<div class="kpi-sub">{sub_kpi["sub"]}<br><span style="font-size:0.9rem;color:#444;">{sub_kpi["trend"]}</span></div></div>', unsafe_allow_html=True)
    if (i+1) % 3 == 0 and i+1 < len(sub_kpis):
        sub_kpi_cols = st.columns(3)

st.markdown("---")

# --- TOGGLE SWITCHES & INDICATORS ---
st.markdown("#### Service Toggles & Indicators")
toggle_col1, toggle_col2 = st.columns([1,3])
with toggle_col1:
    st.write("Enable Service 1")
    st.toggle("Service 1", value=True)
    st.write("Enable Service 2")
    st.toggle("Service 2", value=False)
    st.write("Enable Service 3")
    st.toggle("Service 3", value=True)
with toggle_col2:
    st.write("**Status Indicators**")
    st.markdown('<div style="display:flex;gap:1rem;">'
        '<div style="width:20px;height:20px;border-radius:50%;background:#1f77b4;display:inline-block;"></div> Service 1 '
        '<div style="width:20px;height:20px;border-radius:50%;background:#ff7f0e;display:inline-block;"></div> Service 2 '
        '<div style="width:20px;height:20px;border-radius:50%;background:#2ca02c;display:inline-block;"></div> Service 3 '
        '</div>', unsafe_allow_html=True)

st.markdown("---")

# --- HORIZONTAL PROGRESS BARS ---
st.markdown("#### Performance Bars")
bar_data = [
    ("Service A", 0.7),
    ("Service B", 0.45),
    ("Service C", 0.85),
]
for label, val in bar_data:
    st.write(f"{label} ({int(val*100)}%)")
    st.progress(val)

st.markdown("---")

# --- CIRCULAR PROGRESS INDICATORS ---
st.markdown("#### Circular Progress Indicators")
circ_col1, circ_col2, circ_col3, circ_col4 = st.columns(4)
with circ_col1:
    st.plotly_chart(go.Figure(go.Indicator(mode="gauge+number", value=75, gauge={'axis':{'range':[0,100]},'bar':{'color':'#1f77b4'}}, title={'text':'Scheme 1'})), use_container_width=True)
with circ_col2:
    st.plotly_chart(go.Figure(go.Indicator(mode="gauge+number", value=45, gauge={'axis':{'range':[0,100]},'bar':{'color':'#00338D'}}, title={'text':'Scheme 2'})), use_container_width=True)
with circ_col3:
    st.plotly_chart(go.Figure(go.Indicator(mode="gauge+number", value=75, gauge={'axis':{'range':[0,100]},'bar':{'color':'#ff7f0e'}}, title={'text':'Scheme 3'})), use_container_width=True)
with circ_col4:
    st.plotly_chart(go.Figure(go.Indicator(mode="gauge+number", value=85, gauge={'axis':{'range':[0,100]},'bar':{'color':'#d62728'}}, title={'text':'Scheme 4'})), use_container_width=True)

st.markdown("---")

# --- PLACEHOLDER FOR CHARTS ---
st.markdown("#### Revenue & Service Overview")
chart_col1, chart_col2, chart_col3 = st.columns([2,1,1])

with chart_col1:
    st.plotly_chart(px.line(x=["Apr-2024","May-2024","Jun-2024","Jul-2024","Aug-2024","Sep-2024","Oct-2024","Nov-2024","Dec-2024","Jan-2025","Feb-2025","Mar-2025"],
                            y=[1000,2000,2500,3000,3500,4000,4200,4300,4400,4600,4800,6000],
                            labels={"x":"Month","y":"Collections (Lac)"},
                            title="Total Cumulative Collection (In Lac)"), use_container_width=True)
with chart_col2:
    st.plotly_chart(go.Figure(go.Pie(labels=["Cash","Online","Card"], values=[40,35,25], hole=0.6)), use_container_width=True)
with chart_col3:
    st.plotly_chart(go.Figure(go.Pie(labels=["Residential","Commercial","Industrial"], values=[60,30,10], hole=0.6)), use_container_width=True)

# --- PROGRESS BAR / GAUGE ---
gauge = go.Figure(go.Indicator(
    mode = "gauge+number+delta",
    value = 75,
    delta = {'reference': 80},
    gauge = {'axis': {'range': [0, 100]},
             'bar': {'color': "#00338D"},
             'steps' : [
                 {'range': [0, 50], 'color': "#8fd19e"},
                 {'range': [50, 80], 'color': "#ffe066"},
                 {'range': [80, 100], 'color': "#f7b7a3"}
             ]},
    title = {'text': "Target Achievement (%)"}
))
st.plotly_chart(gauge, use_container_width=True)

# --- FOOTER ---
st.markdown('<div style="margin-top:2rem; text-align:center; color:#888;">KPMG India | Municipal Corporation MIS Dashboard</div>', unsafe_allow_html=True) 