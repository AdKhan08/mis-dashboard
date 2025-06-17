import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# Configure page with light theme
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    page_title="Municipal Corporation MIS Dashboard",
    menu_items={
        'About': 'Municipal Corporation Management Information System'
    }
)

# Custom CSS for light theme with darker text
st.markdown("""
<style>
    .block-container {
        padding: 1rem 2rem;
        background-color: #ffffff;
    }
    .element-container {
        margin: 0;
    }
    .stProgress > div > div > div {
        height: 10px;
    }
    div[data-testid="stHorizontalBlock"] > div {
        padding: 0 1rem;
        background-color: #ffffff;
    }
    .main {
        background-color: #ffffff;
    }
    .plot-container .gtitle, .plot-container .xtitle, .plot-container .ytitle {
        color: #000000 !important;
        font-weight: 600 !important;
    }
    .js-plotly-plot .plotly .modebar {
        color: #000000 !important;
    }
</style>
""", unsafe_allow_html=True)

# Title and date range
col1, col2 = st.columns([6,1])
with col1:
    st.markdown('<div style="text-align:right; font-size:1.2rem; font-weight:600; color:#000000;">Municipal Corporation MIS Dashboard</div>', unsafe_allow_html=True)
with col2:
    current_month = datetime.now().strftime("%b %Y")
    st.markdown(f'<div style="text-align:right; font-size:0.9rem; color:#000000;">{current_month}</div>', unsafe_allow_html=True)

# Main content
left_col, center_col, right_col = st.columns([1,2,1], gap="large")

# LEFT COLUMN
with left_col:
    # Administrative Overview
    st.markdown(
        '<div style="background:#ffffff; border-radius:8px; padding:1.2rem; text-align:center; border:1px solid #e0e0e0; box-shadow: 0 2px 4px rgba(0,0,0,0.05);">'
        '<div style="font-size:1.2rem; font-weight:600; color:#000000;">Administrative Overview</div>'
        '<div style="font-size:2.2rem; font-weight:bold; color:#000000;">15 Zones</div>'
        '<div style="font-size:0.9rem; color:#000000;">75 Wards | 450 Staff</div>'
        '</div>', 
        unsafe_allow_html=True
    )
    
    # Key Performance Areas
    st.markdown(
        '<div style="padding:1rem 0;">'
        '<div style="font-size:1.2rem; font-weight:600; color:#000000; margin-bottom:0.5rem;">Key Performance Areas</div>'
        '<div style="font-size:0.9rem; color:#000000; line-height:1.4;">'
        '• Citizen Grievances Resolved: 89%<br>'
        '• Project Completion Rate: 76%<br>'
        '• Staff Attendance Rate: 92%<br>'
        '• Budget Utilization: 68%'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    # Department Status
    st.markdown('<div style="font-size:1rem; font-weight:600; color:#000000; margin:0.5rem 0;">Department Status</div>', unsafe_allow_html=True)
    departments = [
        ('Administration', '#4CAF50', 'Optimal'),
        ('Engineering', '#FFC107', 'Review'),
        ('Health & Sanitation', '#2196F3', 'Active')
    ]
    for dept, color, status in departments:
        st.markdown(
            f'<div style="display:flex; align-items:center; margin:0.4rem 0; padding:0.4rem; background:#ffffff; border:1px solid #e0e0e0; border-radius:4px;">'
            f'<div style="width:8px; height:8px; border-radius:50%; background:{color}; margin-right:0.5rem;"></div>'
            f'<div style="font-size:0.9rem; color:#000000; flex-grow:1;">{dept}</div>'
            f'<div style="font-size:0.8rem; color:{color}; font-weight:600;">{status}</div>'
            '</div>', 
            unsafe_allow_html=True
        )

# CENTER COLUMN
with center_col:
    # Citizen Services Trend
    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
    grievances_resolved = [820, 945, 1060, 1185, 1210, 1130, 1245, 1360, 1280, 1390, 1310, 1430]
    services_delivered = [1200, 1325, 1440, 1560, 1680, 1500, 1615, 1730, 1645, 1760, 1680, 1790]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, 
        y=services_delivered,
        name="Services Delivered",
        line=dict(color='#1976D2', width=3),
        fill='tozeroy',
        fillcolor='rgba(25, 118, 210, 0.1)'
    ))
    fig.add_trace(go.Scatter(
        x=months, 
        y=grievances_resolved,
        name="Grievances Resolved",
        line=dict(color='#4CAF50', width=2)
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor='white',
        plot_bgcolor='white',
        title=dict(
            text="Citizen Services & Grievance Resolution (Monthly)",
            font=dict(size=14, color='#000000', weight=600)
        ),
        title_x=0,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            font=dict(color='#000000')
        ),
        xaxis=dict(
            showgrid=False,
            tickfont=dict(color='#000000'),
            title=dict(text="Month", font=dict(color='#000000'))
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            tickfont=dict(color='#000000'),
            title=dict(text="Count", font=dict(color='#000000'))
        )
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Key Metrics
    metric_cols = st.columns(4)
    metrics = [
        ("Grievance Resolution", "89%", "#1976D2"),
        ("Project Progress", "76%", "#4CAF50"),
        ("Staff Efficiency", "92%", "#FFC107"),
        ("Budget Usage", "68%", "#F44336")
    ]
    
    for i, (title, value, color) in enumerate(metrics):
        with metric_cols[i]:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=float(value.strip('%')),
                number={'font': {'size': 24, 'color': '#000000'}, 'suffix': '%'},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#000000"},
                    'bar': {'color': color},
                    'borderwidth': 2,
                    'bordercolor': "#000000"
                },
                title={'text': title, 'font': {'size': 12, 'color': '#000000', 'weight': 600}}
            ))
            fig.update_layout(height=150, margin=dict(l=5, r=5, t=25, b=5))
            st.plotly_chart(fig, use_container_width=True)
    
    # Department Performance
    categories = ["Administration", "Engineering", "Health", "Water Supply", "Solid Waste"]
    values = [92, 76, 88, 82, 85]
    
    bar_fig = go.Figure(go.Bar(
        x=categories,
        y=values,
        marker_color='#1976D2',
        text=[f"{v}%" for v in values],
        textposition='outside',
        textfont=dict(color='#000000')
    ))
    bar_fig.update_layout(
        height=180,
        margin=dict(l=0, r=0, t=30, b=0),
        title=dict(
            text="Department-wise Performance (%)",
            font=dict(size=14, color='#000000', weight=600)
        ),
        title_x=0,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(
            showgrid=False,
            tickfont=dict(color='#000000'),
            title=dict(text="Department", font=dict(color='#000000'))
        ),
        yaxis=dict(
            showgrid=True,
            gridcolor='rgba(0,0,0,0.1)',
            range=[0, 100],
            tickfont=dict(color='#000000'),
            title=dict(text="Performance (%)", font=dict(color='#000000'))
        )
    )
    st.plotly_chart(bar_fig, use_container_width=True)

# RIGHT COLUMN
with right_col:
    # Overall Efficiency Score
    st.markdown('<div style="font-size:1rem; font-weight:600; color:#000000; margin-bottom:0.5rem;">Overall Efficiency Score</div>', unsafe_allow_html=True)
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=85,
        number={'font': {'size': 28, 'color': '#000000'}, 'suffix': '%'},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#000000"},
            'bar': {'color': "#1976D2"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#000000",
            'steps': [
                {'range': [0, 60], 'color': '#FFCDD2'},
                {'range': [60, 80], 'color': '#FFECB3'},
                {'range': [80, 100], 'color': '#C8E6C9'}
            ],
            'threshold': {
                'line': {'color': "green", 'width': 4},
                'thickness': 0.75,
                'value': 90
            }
        }
    ))
    gauge.update_layout(height=200, margin=dict(l=10, r=10, t=20, b=10))
    st.plotly_chart(gauge, use_container_width=True)
    
    # Performance Metrics
    st.markdown('<div style="font-size:1rem; font-weight:600; color:#000000; margin:0.5rem 0;">Key Indicators</div>', unsafe_allow_html=True)
    kpis = [
        ("Citizen Service Efficiency", 0.89),
        ("Infrastructure Projects", 0.76),
        ("Administrative Efficiency", 0.92)
    ]
    
    for label, val in kpis:
        st.markdown(f'<div style="font-size:0.85rem; color:#000000; margin:0.2rem 0;">{label}</div>', unsafe_allow_html=True)
        st.progress(val)
    
    # Priority Tasks
    st.markdown('<div style="font-size:1rem; font-weight:600; color:#000000; margin:1rem 0 0.5rem;">Priority Tasks</div>', unsafe_allow_html=True)
    tasks = [
        ("Infrastructure Project Review - Zone 3", "#F44336", "High"),
        ("Staff Training Program", "#FFC107", "Medium"),
        ("Budget Review Meeting", "#4CAF50", "Scheduled")
    ]
    
    for task, color, priority in tasks:
        st.markdown(
            f'<div style="display:flex; align-items:center; margin:0.4rem 0; padding:0.4rem; background:#ffffff; border:1px solid #e0e0e0; border-radius:4px;">'
            f'<div style="width:8px; height:8px; border-radius:50%; background:{color}; margin-right:0.5rem;"></div>'
            f'<div style="font-size:0.85rem; color:#000000; flex-grow:1;">{task}</div>'
            f'<div style="font-size:0.75rem; color:{color}; font-weight:600;">{priority}</div>'
            '</div>',
            unsafe_allow_html=True
        )

# Footer
st.markdown(
    '<div style="text-align:center; color:#000000; font-size:0.8rem; padding:1rem 0; border-top:1px solid #eee; margin-top:2rem;">'
    'Municipal Corporation Management Information System | Last Updated: ' + datetime.now().strftime("%d %b %Y, %H:%M") +
    '</div>', 
    unsafe_allow_html=True)