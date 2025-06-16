import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
from datetime import datetime, timedelta

# Configure page
st.set_page_config(
    layout="wide",
    initial_sidebar_state="collapsed",
    page_title="Performance Management Dashboard"
)

# Custom CSS
st.markdown("""
<style>
    .block-container {
        padding: 1rem 2rem;
    }
    .element-container {
        margin: 0;
    }
    .stProgress > div > div > div {
        height: 10px;
    }
    div[data-testid="stHorizontalBlock"] > div {
        padding: 0 1rem;
    }
</style>
""", unsafe_allow_html=True)

# Title and date range
col1, col2 = st.columns([6,1])
with col1:
    st.markdown('<div style="text-align:right; font-size:1.2rem; font-weight:500; color:#333;">Main Dashboard</div>', unsafe_allow_html=True)
with col2:
    current_month = datetime.now().strftime("%b %Y")
    st.markdown(f'<div style="text-align:right; font-size:0.9rem; color:#666;">{current_month}</div>', unsafe_allow_html=True)

# Main content
left_col, center_col, right_col = st.columns([1,2,1], gap="large")

# LEFT COLUMN
with left_col:
    # Revenue KPI
    st.markdown(
        '<div style="background:#f8f9fa; border-radius:8px; padding:1.2rem; text-align:center; border:1px solid #eee;">'
        '<div style="font-size:2.5rem; font-weight:bold; color:#2196F3;">₹243.5Cr</div>'
        '<div style="font-size:0.9rem; color:#666;">Total Revenue (YTD)</div>'
        '<div style="font-size:0.8rem; color:#4CAF50; margin-top:0.5rem;">↑ 12.4% vs Last Year</div>'
        '</div>', 
        unsafe_allow_html=True
    )
    
    # Performance Summary
    st.markdown(
        '<div style="padding:1rem 0;">'
        '<div style="font-size:1.2rem; font-weight:bold; margin-bottom:0.5rem;">Performance Highlights</div>'
        '<div style="font-size:0.9rem; color:#666; line-height:1.4;">'
        '• Revenue target achievement: 94%<br>'
        '• Customer satisfaction score: 4.2/5<br>'
        '• Operational efficiency: 87%<br>'
        '• Cost optimization: 8.3% savings'
        '</div>'
        '</div>',
        unsafe_allow_html=True
    )
    
    # Department Status
    st.markdown('<div style="font-size:1rem; font-weight:500; margin:0.5rem 0;">Department Status</div>', unsafe_allow_html=True)
    departments = [
        ('Sales & Marketing', '#4CAF50', 'On Track'),
        ('Operations', '#2196F3', 'Needs Attention'),
        ('Finance', '#FFC107', 'Under Review')
    ]
    for dept, color, status in departments:
        st.markdown(
            f'<div style="display:flex; align-items:center; margin:0.4rem 0; padding:0.4rem; background:#f8f9fa; border-radius:4px;">'
            f'<div style="width:8px; height:8px; border-radius:50%; background:{color}; margin-right:0.5rem;"></div>'
            f'<div style="font-size:0.9rem; color:#444; flex-grow:1;">{dept}</div>'
            f'<div style="font-size:0.8rem; color:{color};">{status}</div>'
            '</div>', 
            unsafe_allow_html=True
        )

# CENTER COLUMN
with center_col:
    # Revenue Trend
    months = ["Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec", "Jan", "Feb", "Mar"]
    current_year = [180, 210, 220, 250, 270, 300, 320, 340, 360, 380, 400, 450]
    last_year = [160, 180, 190, 210, 230, 260, 280, 290, 310, 320, 340, 380]
    
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=months, 
        y=current_year,
        name="FY 2023-24",
        line=dict(color='#2196F3', width=3),
        fill='tozeroy',
        fillcolor='rgba(33, 150, 243, 0.1)'
    ))
    fig.add_trace(go.Scatter(
        x=months, 
        y=last_year,
        name="FY 2022-23",
        line=dict(color='#90CAF9', width=2, dash='dot')
    ))
    
    fig.update_layout(
        height=300,
        margin=dict(l=0, r=0, t=30, b=0),
        paper_bgcolor='white',
        plot_bgcolor='white',
        title="Monthly Revenue Trend (₹ Crores)",
        title_x=0,
        showlegend=True,
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1
        ),
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)')
    )
    st.plotly_chart(fig, use_container_width=True)
    
    # Key Metrics
    metric_cols = st.columns(4)
    metrics = [
        ("Revenue Growth", "12.4%", "#2196F3"),
        ("Market Share", "23.5%", "#4CAF50"),
        ("Customer Base", "84.2K", "#FFC107"),
        ("Profitability", "18.7%", "#F44336")
    ]
    
    for i, (title, value, color) in enumerate(metrics):
        with metric_cols[i]:
            fig = go.Figure(go.Indicator(
                mode="gauge+number",
                value=float(value.strip('%').strip('K')),
                number={'font': {'size': 24, 'color': '#444'}, 'suffix': value[-1] if value[-1] in ['%', 'K'] else ''},
                gauge={
                    'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#444"},
                    'bar': {'color': color},
                    'borderwidth': 2,
                    'bordercolor': "#444"
                },
                title={'text': title, 'font': {'size': 12}}
            ))
            fig.update_layout(height=150, margin=dict(l=5, r=5, t=25, b=5))
            st.plotly_chart(fig, use_container_width=True)
    
    # Performance by Category
    categories = ["Product A", "Product B", "Product C", "Product D", "Product E"]
    values = [450, 380, 320, 280, 220]
    
    bar_fig = go.Figure(go.Bar(
        x=categories,
        y=values,
        marker_color='#2196F3',
        text=values,
        textposition='outside'
    ))
    bar_fig.update_layout(
        height=180,
        margin=dict(l=0, r=0, t=30, b=0),
        title="Revenue by Product Category (₹ Lakhs)",
        title_x=0,
        showlegend=False,
        plot_bgcolor='white',
        paper_bgcolor='white',
        xaxis=dict(showgrid=False),
        yaxis=dict(showgrid=True, gridcolor='rgba(0,0,0,0.1)')
    )
    st.plotly_chart(bar_fig, use_container_width=True)

# RIGHT COLUMN
with right_col:
    # Overall Performance Gauge
    st.markdown('<div style="font-size:1rem; font-weight:500; margin-bottom:0.5rem;">Overall Performance</div>', unsafe_allow_html=True)
    gauge = go.Figure(go.Indicator(
        mode="gauge+number",
        value=87,
        number={'font': {'size': 28, 'color': '#444'}, 'suffix': '%'},
        gauge={
            'axis': {'range': [0, 100], 'tickwidth': 1, 'tickcolor': "#444"},
            'bar': {'color': "#2196F3"},
            'bgcolor': "white",
            'borderwidth': 2,
            'bordercolor': "#444",
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
    
    # KPI Achievement
    st.markdown('<div style="font-size:1rem; font-weight:500; margin:0.5rem 0;">KPI Achievement</div>', unsafe_allow_html=True)
    kpis = [
        ("Revenue Target", 0.94),
        ("Cost Optimization", 0.83),
        ("Customer Satisfaction", 0.88)
    ]
    
    for label, val in kpis:
        st.markdown(f'<div style="font-size:0.85rem; color:#666; margin:0.2rem 0;">{label}</div>', unsafe_allow_html=True)
        st.progress(val)
    
    # Critical Alerts
    st.markdown('<div style="font-size:1rem; font-weight:500; margin:1rem 0 0.5rem;">Critical Alerts</div>', unsafe_allow_html=True)
    alerts = [
        ("Revenue gap in Region North", "#F44336", "High"),
        ("Customer churn rate increased", "#FFC107", "Medium"),
        ("Inventory optimization needed", "#4CAF50", "Low")
    ]
    
    for alert, color, priority in alerts:
        st.markdown(
            f'<div style="display:flex; align-items:center; margin:0.4rem 0; padding:0.4rem; background:#f8f9fa; border-radius:4px;">'
            f'<div style="width:8px; height:8px; border-radius:50%; background:{color}; margin-right:0.5rem;"></div>'
            f'<div style="font-size:0.85rem; color:#444; flex-grow:1;">{alert}</div>'
            f'<div style="font-size:0.75rem; color:{color}; font-weight:500;">{priority}</div>'
            '</div>',
            unsafe_allow_html=True
        )

# Footer
st.markdown(
    '<div style="text-align:center; color:#666; font-size:0.8rem; padding:1rem 0; border-top:1px solid #eee; margin-top:2rem;">'
    'Performance Management Dashboard | Last Updated: ' + datetime.now().strftime("%d %b %Y, %H:%M") +
    '</div>', 
    unsafe_allow_html=True
) 