import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(
    page_title="Seaborn Examples Gallery",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better styling
st.markdown("""
<style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .plot-container {
        background: white;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        margin: 20px 0;
    }
    .description {
        font-size: 1.1rem;
        color: #555;
        margin: 10px 0;
    }
    .code-block {
        padding: 15px;
        border-radius: 5px;
        border-left: 4px solid #1f77b4;
        margin: 10px 0;
        font-family: monospace;
        font-size: 0.9rem;
        overflow-x: auto;
    }
    .category-title {
        font-size: 1.8rem;
        font-weight: bold;
        color: #2c3e50;
        margin: 2rem 0 1rem 0;
        padding-bottom: 0.5rem;
        border-bottom: 3px solid #1f77b4;
    }
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-header">📊 Seaborn 예제 갤러리</div>', unsafe_allow_html=True)

# Helper function to display plot with code
def display_plot(fig, title, description, code):
    st.markdown(f"#### {title}")
    st.markdown(f'<p class="description">{description}</p>', unsafe_allow_html=True)
    if hasattr(fig, 'fig'):
        st.pyplot(fig.fig)
    else:
        st.pyplot(fig)
    st.markdown(f'<div class="code-block"><pre>{code}</pre></div>', unsafe_allow_html=True)
    st.markdown("---")

# 관계형 플롯 (Relational Plots)
st.markdown('<div class="category-title">관계형 플롯 (Relational Plots)</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time", size="size", ax=ax)
    plt.close()
    display_plot(fig, "scatterplot - 다양한 변수", 
                 "총 청구액과 팁의 관계를 보여주는 산점도. 시간을 색상과 스타일로, 인원을 점 크기로 표현합니다.",
                 """tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip", hue="time", style="time", size="size)""")
    
    fmri = sns.load_dataset("fmri")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", errorbar="sd", ax=ax)
    plt.close()
    display_plot(fig, "lineplot - 오차 밴드",
                 "시간점에 따른 신호를 보여주는 선 그래프. 오차 밴드와 함께 다른 이벤트별로 표시합니다.",
                 """fmri = sns.load_dataset("fmri")
sns.lineplot(data=fmri, x="timepoint", y="signal", hue="event", errorbar="sd)""")
    
    geyser = sns.load_dataset("geyser")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=geyser, x="duration", y="waiting", hue="kind", ax=ax)
    plt.close()
    display_plot(fig, "scatterplot - 간헐천 분석",
                 "간헐천 분출 지속 시간과 대기 시간의 관계를 분출 종류별로 색상 구분하여 표시합니다.",
                 """geyser = sns.load_dataset("geyser")
sns.scatterplot(data=geyser, x="duration", y="waiting", hue="kind)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.scatterplot(data=tips, x="total_bill", y="tip", ax=ax)
    sns.scatterplot(data=tips[tips["smoker"] == "Yes"], x="total_bill", y="tip", color="red", ax=ax)
    plt.close()
    display_plot(fig, "scatterplot - 레이어드",
                 "모든 팁을 파란색으로 표시하고 흡연자의 팁을 빨간색으로 겹쳐서 표시하는 레이어드 산점도입니다.",
                 """tips = sns.load_dataset("tips")
sns.scatterplot(data=tips, x="total_bill", y="tip")
sns.scatterplot(data=tips[tips["smoker"] == "Yes"], x="total_bill", y="tip", color="red)""")

with col2:
    healthexp = sns.load_dataset("healthexp")
    fig, ax = plt.subplots(figsize=(12, 6))
    sns.lineplot(data=healthexp, x="Year", y="Spending_USD", hue="Country", ax=ax)
    plt.close()
    display_plot(fig, "lineplot - 와이드 데이터",
                 "연도별 다른 국가의 의료 지출을 보여주는 선 그래프입니다.",
                 """healthexp = sns.load_dataset("healthexp")
sns.lineplot(data=healthexp, x="Year", y="Spending_USD", hue="Country)""")

# 분포 플롯 (Distribution Plots)
st.markdown('<div class="category-title">분포 플롯 (Distribution Plots)</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data=tips, x="total_bill", hue="day", multiple="stack", ax=ax)
    plt.close()
    display_plot(fig, "histplot - 스택 히스토그램",
                 "요일별 총 청구액 분포를 스택된 히스토그램으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.histplot(data=tips, x="total_bill", hue="day", multiple="stack)""")
    
    iris = sns.load_dataset("iris")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(data=iris, x="sepal_length", y="sepal_width", hue="species", ax=ax)
    plt.close()
    display_plot(fig, "kdeplot - 다변량 KDE",
                 "종별 꽃받침 길이와 너비의 관계를 다변량 KDE로 표시합니다.",
                 """iris = sns.load_dataset("iris")
sns.kdeplot(data=iris, x="sepal_length", y="sepal_width", hue="species)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.kdeplot(data=tips, x="total_bill", hue="day", fill=True, palette="deep", ax=ax)
    plt.close()
    display_plot(fig, "kdeplot - 팔레트",
                 "사용자 정의 팔레트를 사용하여 요일별 총 청구액 분포를 KDE로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.kdeplot(data=tips, x="total_bill", hue="day", fill=True, palette="deep)""")

with col2:
    tips = sns.load_dataset("tips")
    g = sns.FacetGrid(tips, row="day", hue="day", aspect=5, height=1.5)
    g.map(sns.kdeplot, "total_bill", fill=True, alpha=0.6)
    plt.close(g.fig)
    display_plot(g.fig, "kdeplot - 리지 플롯",
                 "요일별 총 청구액 분포를 리지 플롯(조이플롯)으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, row="day", hue="day", aspect=5, height=1.5)
g.map(sns.kdeplot, "total_bill", fill=True, alpha=0.6)""")

# 범주형 플롯 (Categorical Plots)
st.markdown('<div class="category-title">범주형 플롯 (Categorical Plots)</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=tips, x="day", y="total_bill", hue="sex", ax=ax)
    plt.close()
    display_plot(fig, "boxplot - 그룹화된 박스플롯",
                 "요일과 성별별 총 청구액 분포를 그룹화된 박스플롯으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.boxplot(data=tips, x="day", y="total_bill", hue="sex)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(data=tips, x="day", y="total_bill", hue="sex", ax=ax)
    plt.close()
    display_plot(fig, "violinplot - 그룹화된 바이올린플롯",
                 "요일과 성별별 총 청구액 분포를 그룹화된 바이올린플롯으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.violinplot(data=tips, x="day", y="total_bill", hue="sex)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxplot(data=tips, y="day", x="total_bill", hue="sex", ax=ax)
    plt.close()
    display_plot(fig, "boxplot - 수평 박스플롯",
                 "요일과 성별별 총 청구액 분포를 수평 박스플롯으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.boxplot(data=tips, y="day", x="total_bill", hue="sex)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.stripplot(data=tips, x="day", y="total_bill", hue="sex", jitter=True, ax=ax)
    plt.close()
    display_plot(fig, "stripplot - 지터 스트립플롯",
                 "요일과 성별별 개별 총 청구액 값을 지터와 함께 스트립플롯으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.stripplot(data=tips, x="day", y="total_bill", hue="sex", jitter=True)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=tips, x="day", y="total_bill", hue="sex", palette="muted", ax=ax)
    plt.close()
    display_plot(fig, "barplot - 팔레트",
                 "사용자 정의 팔레트를 사용하여 요일과 성별별 평균 총 청구액을 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.barplot(data=tips, x="day", y="total_bill", hue="sex", palette="muted)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.barplot(data=tips, x="day", y="total_bill", estimator=sum, errorbar=None, ax=ax)
    plt.close()
    display_plot(fig, "barplot - 전체-부분",
                 "요일별 총 팁을 전체-부분 바 플롯으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.barplot(data=tips, x="day", y="total_bill", estimator=sum, errorbar=None)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.swarmplot(data=tips, x="day", y="total_bill", hue="sex", ax=ax)
    plt.close()
    display_plot(fig, "swarmplot - 스웜플롯",
                 "요일과 성별별 개별 총 청구액 값을 중첩 없이 스웜플롯으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.swarmplot(data=tips, x="day", y="total_bill", hue="sex)""")
    
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(data=tips, x="day", y="total_bill", ax=ax)
    plt.close()
    display_plot(fig, "violinplot - 간단한 바이올린플롯",
                 "요일별 총 청구액 분포를 간단한 바이올린플롯으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.violinplot(data=tips, x="day", y="total_bill)""")

with col2:
    diamonds = sns.load_dataset("diamonds")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.boxenplot(data=diamonds, x="cut", y="price", ax=ax)
    plt.close()
    display_plot(fig, "boxenplot - 대규모 데이터",
                 "대규모 데이터셋에서 컷 품질별 가격 분포를 박엔플롯으로 표시합니다.",
                 """diamonds = sns.load_dataset("diamonds")
sns.boxenplot(data=diamonds, x="cut", y="price)""")
    
    penguins = sns.load_dataset("penguins")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.violinplot(data=penguins, x="species", y="bill_length_mm", ax=ax)
    plt.close()
    display_plot(fig, "violinplot - 와이드 폼",
                 "종별 부리 길이 분포를 바이올린플롯으로 표시합니다.",
                 """penguins = sns.load_dataset("penguins")
sns.violinplot(data=penguins, x="species", y="bill_length_mm)""")

# 행렬 플롯 (Matrix Plots)
st.markdown('<div class="category-title">행렬 플롯 (Matrix Plots)</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    penguins = sns.load_dataset("penguins")
    numeric_cols = penguins.select_dtypes(include=[np.number]).columns
    corr = penguins[numeric_cols].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
    plt.close()
    display_plot(fig, "heatmap - 상관관계",
                 "수치형 변수 간의 쌍별 상관관계를 히트맵으로 표시합니다.",
                 """penguins = sns.load_dataset("penguins")
numeric_cols = penguins.select_dtypes(include=[np.number]).columns
corr = penguins[numeric_cols].corr()
sns.heatmap(corr, annot=True, cmap="coolwarm)""")

with col2:
    flights = sns.load_dataset("flights")
    flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
    fig, ax = plt.subplots(figsize=(12, 8))
    sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlOrRd", ax=ax)
    plt.close()
    display_plot(fig, "heatmap - 스프레드시트",
                 "월 및 연도별 승객 수를 스프레드시트 스타일 히트맵으로 표시합니다.",
                 """flights = sns.load_dataset("flights")
flights_pivot = flights.pivot(index="month", columns="year", values="passengers")
sns.heatmap(flights_pivot, annot=True, fmt="d", cmap="YlOrRd)""")

# 회귀 플롯 (Regression Plots)
st.markdown('<div class="category-title">회귀 플롯 (Regression Plots)</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    tips = sns.load_dataset("tips")
    g = sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", height=6, aspect=1.67)
    plt.close(g.fig)
    display_plot(g.fig, "lmplot - 선형 회귀",
                 "총 청구액과 팁의 관계를 신뢰 구간과 함께 선형 회귀로 표시합니다. 흡연자 상태별로 색상 구분합니다.",
                 """tips = sns.load_dataset("tips")
sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker, height=6, aspect=1.67)""")
    
    tips = sns.load_dataset("tips")
    tips["big_tip"] = (tips["tip"] / tips["total_bill"]) > 0.2
    g = sns.lmplot(data=tips, x="total_bill", y="big_tip", logistic=True, y_jitter=0.03, height=6, aspect=1.67)
    plt.close(g.fig)
    display_plot(g.fig, "lmplot - 로지스틱 회귀",
                 "총 청구액에서 큰 팁 확률을 예측하는 로지스틱 회귀 플롯입니다.",
                 """tips = sns.load_dataset("tips")
tips["big_tip"] = (tips["tip"] / tips["total_bill"]) > 0.2
sns.lmplot(data=tips, x="total_bill", y="big_tip", logistic=True, y_jitter=0.03)""")
    
    tips = sns.load_dataset("tips")
    g = sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", col="time", row="sex", height=4, aspect=1.2)
    plt.close(g.fig)
    display_plot(g.fig, "lmplot - 다중 회귀",
                 "시간과 성별별로 패싯된 다중 회귀 플롯입니다.",
                 """tips = sns.load_dataset("tips")
sns.lmplot(data=tips, x="total_bill", y="tip", hue="smoker", col="time", row="sex)""")

with col2:
    tips = sns.load_dataset("tips")
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.residplot(data=tips, x="total_bill", y="tip", ax=ax)
    plt.close()
    display_plot(fig, "residplot - 잔차 플롯",
                 "총 청구액에 대한 팁의 선형 회귀 잔차를 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.residplot(data=tips, x="total_bill", y="tip)""")
    
    tips = sns.load_dataset("tips")
    g = sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg", height=6)
    plt.close(g.fig)
    display_plot(g.fig, "jointplot - 회귀",
                 "총 청구액과 팁의 관계를 회귀선과 함께 조인트 플롯으로 표시합니다.",
                 """tips = sns.load_dataset("tips")
sns.jointplot(data=tips, x="total_bill", y="tip", kind="reg)""")

# 다중 플롯 그리드 (Multi-plot Grids)
st.markdown('<div class="category-title">다중 플롯 그리드 (Multi-plot Grids)</div>', unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    tips = sns.load_dataset("tips")
    g = sns.FacetGrid(tips, col="time", row="sex", hue="smoker", height=3.5, aspect=1.2)
    g.map(sns.scatterplot, "total_bill", "tip")
    g.add_legend()
    plt.close(g.fig)
    display_plot(g.fig, "FacetGrid - 다중 패싯",
                 "시간, 성별, 흡연자 상태별로 패싯된 산점도를 표시합니다.",
                 """tips = sns.load_dataset("tips")
g = sns.FacetGrid(tips, col="time", row="sex", hue="smoker")
g.map(sns.scatterplot, "total_bill", "tip")
g.add_legend()""")
    
    iris = sns.load_dataset("iris")
    g = sns.PairGrid(iris, hue="species", height=2.5)
    g.map_upper(sns.scatterplot)
    g.map_lower(sns.kdeplot)
    g.map_diag(sns.histplot)
    g.add_legend()
    plt.close(g.fig)
    display_plot(g.fig, "PairGrid - KDE와 산점도",
                 "상단 삼각형에 산점도, 하단 삼각형에 KDE를 표시하는 PairGrid입니다.",
                 """iris = sns.load_dataset("iris")
g = sns.PairGrid(iris, hue="species")
g.map_upper(sns.scatterplot)
g.map_lower(sns.kdeplot)
g.map_diag(sns.histplot)
g.add_legend()""")
    
    penguins = sns.load_dataset("penguins")
    g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm", height=6)
    g.plot(sns.scatterplot, sns.histplot)
    plt.close(g.fig)
    display_plot(g.fig, "JointGrid - 히스토그램",
                 "산점도와 주변 히스토그램이 있는 JointGrid입니다.",
                 """penguins = sns.load_dataset("penguins")
g = sns.JointGrid(data=penguins, x="bill_length_mm", y="bill_depth_mm)
g.plot(sns.scatterplot, sns.histplot)""")
    
    penguins = sns.load_dataset("penguins")
    g = sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", kind="hex", height=6)
    plt.close(g.fig)
    display_plot(g.fig, "jointplot - 헥스빈",
                 "밀도를 헥스빈 집계로 표시하는 조인트 플롯입니다.",
                 """penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", kind="hex)""")
    
    penguins = sns.load_dataset("penguins")
    g = sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", kind="kde", height=6)
    plt.close(g.fig)
    display_plot(g.fig, "jointplot - KDE",
                 "밀도 분포를 KDE로 표시하는 조인트 플롯입니다.",
                 """penguins = sns.load_dataset("penguins")
sns.jointplot(data=penguins, x="bill_length_mm", y="bill_depth_mm", kind="kde)""")

with col2:
    iris = sns.load_dataset("iris")
    g = sns.pairplot(iris, hue="species", height=2.5)
    plt.close(g.fig)
    display_plot(g.fig, "pairplot - 산점도 행렬",
                 "종별 쌍별 관계를 산점도 행렬로 표시합니다.",
                 """iris = sns.load_dataset("iris")
sns.pairplot(iris, hue="species)""")

# Footer
st.markdown("---")

