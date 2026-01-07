import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import os

# --- KONFIGURASI HALAMAN ---
st.set_page_config(
    page_title="Ecommerce Churn Intelligence Hub",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --- CUSTOM CSS (MODERN UI/UX) ---
st.markdown("""
    <style>
    /* Mengatur background utama */
    .main { background-color: #f4f7f6; }
    
    /* Style untuk Metric Cards */
    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.05);
        border: 1px solid #eef2f6;
    }
    
    /* Menghilangkan padding berlebih pada chart */
    .block-container { padding-top: 2rem; }
    
    /* Sidebar styling */
    .css-1d391kg { background-color: #ffffff; }
    </style>
    """, unsafe_allow_html=True)

# --- DATA HANDLING (PATH DINAMIS & CACHING) ---
@st.cache_data
def load_data():
    """Fungsi untuk memuat data dengan proteksi error dan perbaikan tipe data."""
    # Pastikan path file benar
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    file_path = os.path.join(base_dir, 'data', 'processed', 'final_predictions.csv')
    
    try:
        if not os.path.exists(file_path):
            st.error(f"⚠️ File tidak ditemukan di: {file_path}")
            st.stop()
            
        # Membaca data
        df = pd.read_csv(file_path, sep=';')
        
        # --- PERBAIKAN KRUSIAL: Konversi ke Numerik ---
        # Kolom yang harus dipastikan bertipe numerik agar bisa dikalkulasi
        numeric_cols = [
            'Churn_Probability', 'Churn_Prediction', 'Tenure', 
            'SatisfactionScore', 'WarehouseToHome', 'CashbackAmount'
        ]
        
        for col in numeric_cols:
            if col in df.columns:
                # Mengubah ke numerik dan paksa error menjadi NaN, lalu isi dengan 0
                df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0)
        
        # --- PERBAIKAN ERROR: Simulasi TotalSpend ---
        if 'TotalSpend' not in df.columns:
            # Pastikan CashbackAmount sudah float sebelum dikalikan
            # Ini mencegah error "multiply sequence by non-int"
            df['TotalSpend'] = df['CashbackAmount'].astype(float) * 12.5 
        else:
            df['TotalSpend'] = pd.to_numeric(df['TotalSpend'], errors='coerce').fillna(0)
            
        return df
    except Exception as e:
        st.error(f"❌ Terjadi kesalahan saat memuat data: {e}")
        st.stop()

# Load Data
df = load_data()

# --- SIDEBAR NAVIGATION ---
st.sidebar.image("https://cdn-icons-png.flaticon.com/512/2040/2040504.png", width=80)
st.sidebar.title("Churn Intelligence")
st.sidebar.markdown("---")
page = st.sidebar.radio(
    "Navigasi Dashboard", 
    ["Executive Overview", "Behavior Insights", "Risk Prediction Monitoring"]
)
st.sidebar.markdown("---")
st.sidebar.caption("v1.0.0 | © 2026 E-Commerce Project")

# --- PAGE 1: EXECUTIVE OVERVIEW ---
if page == "Executive Overview":
    st.title("📈 Executive Overview")
    st.markdown("Ringkasan metrik utama untuk pemantauan kesehatan retensi pelanggan.")
    
    # METRICS ROW
    total_cust = len(df)
    churn_count = int(df['Churn_Prediction'].sum())
    churn_rate = (churn_count / total_cust)
    lost_revenue = df[df['Churn_Prediction'] == 1]['TotalSpend'].sum()
    avg_tenure = df['Tenure'].mean()
    
    m1, m2, m3, m4 = st.columns(4)
    m1.metric("Total Customers", f"{total_cust:,}")
    m2.metric("Churn Rate", f"{churn_rate:.2%}")
    m3.metric("Est. Lost Revenue", f"${lost_revenue:,.0f}")
    m4.metric("Avg. Tenure", f"{avg_tenure:.1f} Mo")
    
    st.markdown("---")
    
    # CHARTS ROW
    c1, c2 = st.columns([4, 6])
    
    with c1:
        st.subheader("Customer Composition")
        fig_donut = px.pie(
            df, names='Churn_Prediction', hole=0.6,
            color='Churn_Prediction',
            color_discrete_map={0: '#2ecc71', 1: '#e74c3c'},
            labels={'0': 'Loyal', '1': 'Churn'}
        )
        fig_donut.update_traces(textinfo='percent+label', pull=[0.05, 0])
        st.plotly_chart(fig_donut, use_container_width=True)
        
    with c2:
        st.subheader("Churn Rate Status")
        fig_gauge = go.Figure(go.Indicator(
            mode = "gauge+number",
            value = churn_rate * 100,
            domain = {'x': [0, 1], 'y': [0, 1]},
            title = {'text': "Percentage Churn (%)", 'font': {'size': 18}},
            gauge = {
                'axis': {'range': [None, 100], 'tickwidth': 1},
                'bar': {'color': "#e74c3c"},
                'bgcolor': "white",
                'borderwidth': 2,
                'bordercolor': "#d1d8e0",
                'steps': [
                    {'range': [0, 10], 'color': '#d4efdf'},
                    {'range': [10, 20], 'color': '#fcf3cf'}],
                'threshold': {
                    'line': {'color': "black", 'width': 4},
                    'thickness': 0.75,
                    'value': 15}
            }
        ))
        fig_gauge.update_layout(height=350, margin=dict(l=20, r=20, t=50, b=20))
        st.plotly_chart(fig_gauge, use_container_width=True)

# --- PAGE 2: BEHAVIOR INSIGHTS ---
elif page == "Behavior Insights":
    st.title("🔍 Behavior Insights")
    st.markdown("Analisis mendalam mengenai faktor pendorong perilaku berhenti pelanggan.")
    
    row1_c1, row1_c2 = st.columns(2)
    
    with row1_c1:
        st.subheader("Churn by Order Category")
        fig_bar = px.histogram(
            df, x="PreferedOrderCat", color="Churn_Prediction",
            barmode="group",
            color_discrete_map={0: '#2ecc71', 1: '#e74c3c'},
            text_auto=True
        )
        st.plotly_chart(fig_bar, use_container_width=True)
        
    with row1_c2:
        st.subheader("Satisfaction Score vs Churn")
        fig_box = px.box(
            df, x="Churn_Prediction", y="SatisfactionScore",
            color="Churn_Prediction",
            color_discrete_map={0: '#2ecc71', 1: '#e74c3c'},
            points="all"
        )
        st.plotly_chart(fig_box, use_container_width=True)
        
    st.markdown("---")
    st.subheader("Logistics Impact: Warehouse to Home Distance")
    fig_dist = px.histogram(
        df, x="WarehouseToHome", color="Churn_Prediction",
        marginal="rug", nbins=50,
        color_discrete_map={0: '#2ecc71', 1: '#e74c3c'},
        opacity=0.7
    )
    st.plotly_chart(fig_dist, use_container_width=True)

# --- PAGE 3: RISK PREDICTION MONITORING ---
elif page == "Risk Prediction Monitoring":
    st.title("🔮 Risk Prediction Monitoring")
    st.markdown("Identifikasi profil risiko pelanggan untuk strategi intervensi yang presisi.")
    
    # SCATTER PLOT ANALYSIS
    st.subheader("High-Value High-Risk Mapping")
    fig_scatter = px.scatter(
        df, x="Churn_Probability", y="TotalSpend",
        color="Churn_Probability",
        size="TotalSpend",
        color_continuous_scale="RdYlGn_r",
        hover_data=['Tenure', 'Complain', 'PreferedOrderCat'],
        title="Probabilitas Churn vs Nilai Ekonomi Pelanggan"
    )
    # Menambahkan garis threshold risiko
    fig_scatter.add_vline(x=0.8, line_dash="dash", line_color="red", 
                          annotation_text="Critical Risk Zone", annotation_position="top right")
    
    st.plotly_chart(fig_scatter, use_container_width=True)
    
    st.markdown("---")
    
    # PRIORITY LIST TABLE
    st.subheader("🚨 Priority Intervention List (Risk > 80%)")
    priority_df = df[df['Churn_Probability'] >= 0.8].sort_values(by='Churn_Probability', ascending=False)
    
    # Formatting tabel agar profesional
    st.dataframe(
        priority_df[['Churn_Probability', 'TotalSpend', 'Tenure', 'Complain', 'PreferedOrderCat']].style.format({
            'Churn_Probability': '{:.2%}',
            'TotalSpend': '${:,.2f}'
        }).background_gradient(subset=['Churn_Probability'], cmap='Reds'),
        use_container_width=True
    )
    
    st.info("💡 **Rekomendasi:** Berikan penawaran khusus atau survei kepuasan mendalam kepada pelanggan dalam daftar di atas untuk mencegah Churn.")

# --- FOOTER ---
st.markdown("---")
st.caption("Developed with ❤️ for Data Excellence.")