import streamlit as st
import plotly.graph_objects as go

st.set_page_config(page_title="HR Intelligence", layout="wide")

st.markdown("""
<style>
    .main { background-color: #f5f5f5; }
    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #ffffff 0%, #f8f9fa 100%);
    }
    h1 { font-weight: 600; font-size: 32px; color: #1a1a1a; }
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        border-radius: 8px;
        padding: 12px 24px;
        font-weight: 600;
    }
    .stButton>button:hover {
        transform: translateY(-2px);
        box-shadow: 0 4px 12px rgba(102, 126, 234, 0.4);
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### 🏢 HR Intelligence")
    page = st.radio("Navigation", ["🏠 Home", "📊 Analytics", "🔮 Predictions", "⚙️ Settings"])

st.title("Dashboard Overview")

col1, col2, col3, col4 = st.columns(4)
with col1:
    st.metric("Total Employees", "847", "+23")
with col2:
    st.metric("Avg Performance", "4.2", "+0.3")
with col3:
    st.metric("Turnover Rate", "8.5%", "-2.1%")
with col4:
    st.metric("High Risk", "12", "⚠️")

st.subheader("Performance Distribution")
st.progress(0.85)
st.caption("85% of employees meet or exceed expectations")

st.subheader("Monthly Trends")
fig = go.Figure()
fig.add_trace(go.Scatter(
    x=["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
    y=[4.1, 4.2, 4.3, 4.2, 4.3, 4.4],
    mode="lines+markers",
    line=dict(color="#667eea", width=3),
    marker=dict(size=10)
))
fig.update_layout(
    height=300,
    margin=dict(l=20, r=20, t=20, b=20),
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(0,0,0,0)',
)
st.plotly_chart(fig, use_container_width=True)
```

**2.4 - Commit (save) the file**
- Scroll down to the green **"Commit changes"** button
- Click it (you can leave the default message)

### Step 3: Create requirements.txt

**3.1 - Create another file**
- Click **"Add file"** again
- Select **"Create new file"**

**3.2 - Name it**
- Type: `requirements.txt`

**3.3 - Paste this:**
```
streamlit
plotly
