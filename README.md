# 📊 Seaborn 예제 갤러리

공식 seaborn 문서의 모든 예제 그래프를 보여주는 아름다운 Streamlit 애플리케이션입니다. 깔끔하고 현대적인 인터페이스로 다양한 플롯 유형을 대화형으로 탐색해보세요.<br>
https://stylesheet-seaborn.onrender.com

## 기능

- **50개 이상의 Seaborn 예제**: seaborn 갤러리의 모든 주요 플롯 유형
- **대화형 사이드바 네비게이션**: 그래프 카테고리와 유형을 쉽게 선택
- **아름다운 스타일링**: 우아한 보기 경험을 위한 사용자 정의 CSS
- **실시간 렌더링**: Streamlit을 사용한 빠른 시각화
- **공식 데이터셋**: seaborn의 내장 예제 데이터셋 사용

## 카테고리

- **관계형 플롯 (Relational Plots)**: lmplot, scatterplot, lineplot, relplot
- **분포 플롯 (Distribution Plots)**: displot, histplot, kdeplot
- **범주형 플롯 (Categorical Plots)**: catplot, boxplot, violinplot, stripplot, swarmplot
- **행렬 플롯 (Matrix Plots)**: heatmap, clustermap
- **회귀 플롯 (Regression Plots)**: lmplot, residplot, jointplot
- **다중 플롯 그리드 (Multi-plot Grids)**: FacetGrid, PairGrid, JointGrid, pairplot

## 설치

### 사전 요구사항

- Python 3.8 이상
- pip 패키지 관리자

### 설정

1. 프로젝트 디렉토리로 이동:
```bash
cd e:\study\sk_playdata\personal\seaborn
```

2. 필요한 종속성 설치:
```bash
pip install -r requirements.txt
```

## 애플리케이션 실행

다음 명령으로 Streamlit 애플리케이션을 시작하세요:

```bash
streamlit run app.py
```

애플리케이션이 기본 웹 브라우저에서 `http://localhost:8501`로 자동 열립니다.

## 사용법

1. **카테고리 선택**: 사이드바를 사용하여 그래프 카테고리 탐색
2. **그래프 선택**: 드롭다운에서 특정 그래프 유형 선택
3. **플롯 보기**: 설명과 함께 그래프가 표시됩니다
4. **탐색**: seaborn의 기능을 이해하기 위해 다양한 그래프 시도

## 종속성

- `streamlit>=1.28.0` - 웹 애플리케이션 프레임워크
- `seaborn>=0.13.0` - 통계 데이터 시각화
- `matplotlib>=3.7.0` - 플로팅 라이브러리
- `pandas>=2.0.0` - 데이터 조작
- `numpy>=1.24.0` - 수치 계산

## 프로젝트 구조

```
seaborn/
├── app.py              # 메인 Streamlit 애플리케이션
├── requirements.txt    # Python 종속성
└── README.md          # 이 파일
```

## 포함된 예제

애플리케이션에는 다음이 포함되어 있습니다:
- 앤스컴의 쿼텟 (Anscombe's Quartet, lmplot)
- 다양한 스타일링 옵션이 있는 산점도
- 오차 밴드가 있는 선 그래프
- 패싯 플롯 (relplot, catplot, displot)
- 분포 플롯 (히스토그램, KDE, ECDF)
- 범주형 플롯 (bar, box, violin, strip, swarm)
- 히트맵 및 클러스터맵
- 신뢰 구간이 있는 회귀 플롯
- 다중 플롯 그리드 (FacetGrid, PairGrid, JointGrid)
- 쌍별 산점도 행렬

## 팁

- 사이드바를 사용하여 다른 그래프 유형 간에 빠르게 탐색
- 각 플롯에는 표시 내용을 설명하는 설명이 포함됩니다
- 앱은 seaborn의 내장 데이터셋(tips, penguins, iris 등)을 사용합니다
- 최적의 보기를 위해 브라우저 창 크기 조정

## 라이선스

이 프로젝트는 교육 목적을 위한 것입니다. Seaborn은 BSD 3-Clause 라이선스 하에 라이선스가 부여됩니다.

## 크레딧

- [Seaborn 문서](https://seaborn.pydata.org/examples/index.html)
- [Streamlit](https://streamlit.io/)

<img width="1057" height="1482" alt="image" src="https://github.com/user-attachments/assets/ae4a5a60-4a4f-4021-8c4d-3cd50fb9d6ac" />
<img width="1057" height="1292" alt="image" src="https://github.com/user-attachments/assets/3e7e572f-9ae9-485f-bbac-d324d76da4bd" />
<img width="1057" height="1769" alt="image" src="https://github.com/user-attachments/assets/035fba4a-b27e-42df-9920-6e1bafdb052f" />
<img width="1057" height="1769" alt="image" src="https://github.com/user-attachments/assets/455339fa-2549-4935-99e7-246f518b0432" />
<img width="1057" height="1769" alt="image" src="https://github.com/user-attachments/assets/0ee14fa2-5020-4905-85fb-9f3ef0c3ed62" />
<img width="1057" height="1125" alt="image" src="https://github.com/user-attachments/assets/53884247-a87d-47a2-b39c-11196783cd95" />
<img width="1057" height="1529" alt="image" src="https://github.com/user-attachments/assets/7292fac9-c20a-4180-b830-ecd66185c982" />
<img width="1057" height="1460" alt="image" src="https://github.com/user-attachments/assets/2fda51c3-48ac-4230-ba79-1c2f08b57b01" />
<img width="1057" height="1555" alt="image" src="https://github.com/user-attachments/assets/9a07bdac-d0a3-4c24-a250-812785b71000" />
<img width="1057" height="806" alt="image" src="https://github.com/user-attachments/assets/db9936c4-95d3-4d44-9ddb-2d327f48931b" />



