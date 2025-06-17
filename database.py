import mysql.connector
from mysql.connector import Error
import pandas as pd
import streamlit as st

# Database configuration - should be moved to environment variables in production
DB_CONFIG = {
    'host': 'your_host',
    'database': 'municipal_corp_db',
    'user': 'your_username',
    'password': 'your_password'
}

@st.cache_resource
def get_database_connection():
    """Create a database connection that can be reused"""
    try:
        connection = mysql.connector.connect(**DB_CONFIG)
        if connection.is_connected():
            return connection
    except Error as e:
        st.error(f"Error connecting to MySQL database: {e}")
        return None

def fetch_administrative_data():
    """Fetch administrative overview data"""
    conn = get_database_connection()
    if conn is None:
        return None
    
    try:
        query = """
        SELECT 
            COUNT(DISTINCT zone_id) as total_zones,
            COUNT(DISTINCT ward_id) as total_wards,
            COUNT(DISTINCT staff_id) as total_staff
        FROM zones z
        LEFT JOIN wards w ON z.zone_id = w.zone_id
        LEFT JOIN staff s ON w.ward_id = s.ward_id
        """
        return pd.read_sql(query, conn)
    except Error as e:
        st.error(f"Error fetching administrative data: {e}")
        return None
    finally:
        if conn.is_connected():
            conn.close()

def fetch_service_trends(start_date, end_date):
    """Fetch citizen services and grievances data"""
    conn = get_database_connection()
    if conn is None:
        return None
    
    try:
        query = """
        SELECT 
            DATE_FORMAT(service_date, '%b') as month,
            COUNT(CASE WHEN service_type = 'general' THEN 1 END) as services_delivered,
            COUNT(CASE WHEN service_type = 'grievance' THEN 1 END) as grievances_resolved
        FROM citizen_services
        WHERE service_date BETWEEN %s AND %s
        GROUP BY DATE_FORMAT(service_date, '%b')
        ORDER BY service_date
        """
        return pd.read_sql(query, conn, params=[start_date, end_date])
    except Error as e:
        st.error(f"Error fetching service trends: {e}")
        return None
    finally:
        if conn.is_connected():
            conn.close()

def fetch_department_performance():
    """Fetch department-wise performance metrics"""
    conn = get_database_connection()
    if conn is None:
        return None
    
    try:
        query = """
        SELECT 
            d.dept_name,
            ROUND(AVG(p.performance_score), 2) as performance_score,
            d.status
        FROM departments d
        LEFT JOIN performance_metrics p ON d.dept_id = p.dept_id
        WHERE p.metric_date >= DATE_SUB(CURRENT_DATE, INTERVAL 30 DAY)
        GROUP BY d.dept_id, d.dept_name, d.status
        """
        return pd.read_sql(query, conn)
    except Error as e:
        st.error(f"Error fetching department performance: {e}")
        return None
    finally:
        if conn.is_connected():
            conn.close()

def fetch_priority_tasks():
    """Fetch current priority tasks"""
    conn = get_database_connection()
    if conn is None:
        return None
    
    try:
        query = """
        SELECT 
            task_description,
            priority_level,
            CASE 
                WHEN priority_level = 'High' THEN '#F44336'
                WHEN priority_level = 'Medium' THEN '#FFC107'
                ELSE '#4CAF50'
            END as color_code
        FROM tasks
        WHERE status = 'Active'
        ORDER BY 
            CASE priority_level
                WHEN 'High' THEN 1
                WHEN 'Medium' THEN 2
                ELSE 3
            END
        LIMIT 3
        """
        return pd.read_sql(query, conn)
    except Error as e:
        st.error(f"Error fetching priority tasks: {e}")
        return None
    finally:
        if conn.is_connected():
            conn.close()

def fetch_kpi_metrics():
    """Fetch current KPI metrics"""
    conn = get_database_connection()
    if conn is None:
        return None
    
    try:
        query = """
        SELECT 
            metric_name,
            current_value,
            target_value,
            ROUND(current_value / target_value * 100, 2) as achievement_percentage
        FROM kpi_metrics
        WHERE metric_date = (SELECT MAX(metric_date) FROM kpi_metrics)
        """
        return pd.read_sql(query, conn)
    except Error as e:
        st.error(f"Error fetching KPI metrics: {e}")
        return None
    finally:
        if conn.is_connected():
            conn.close() 