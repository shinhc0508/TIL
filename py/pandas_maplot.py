#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl


# In[2]:


df=pd.read_csv('./auto-mpg.csv', header=None)


# In[3]:


df.columns=['map','cylinders','displacement','horsepower',
            'weight','acceleration','model year','origin','name']


# In[4]:


df.columns


# In[5]:


df.plot(x= 'weight' ,y='map',kind='scatter') #scatter 산전도


# In[6]:


#열을 선택해서 박스 플롯 그리기
df.describe()


# In[7]:


df[['map','cylinders']].plot(kind='box')


# In[8]:


df1=pd.read_excel('./시도별 전출입 인구수.xlsx',engine='openpyxl', header=0)


# In[9]:


#시도별 전출입 인구수 데이터 시각화
import matplotlib.pyplot as plt


# In[10]:


df1.head(4)


# In[11]:


df1.info()


# In[12]:


df1.describe()


# In[13]:


#누락값(NaN)을 앞 데이터로 채움
df2=df1.fillna(method='ffill') # ffill은 forward로 fill함
df2


# In[14]:


# 서울에서 다른 지역으로 이동한 데이터만 추출하여 정리
mask=(df1['전출지별']=='서울특별시')&(df1['전입지별']!='서울특별시') # 서울지역에서 전출한사람 & 서울지역이외엥 전입한사람
df_seoul = df1[mask]
df_seoul = df_seoul.drop(['전출지별'], axis=1)
df_seoul.rename({'전입지별':'전입지'}, axis=1, inplace=True)
df_seoul.set_index('전입지', inplace=True)
df_seoul


# In[15]:


sr_one=df_seoul.loc['경기도']


# In[ ]:


sr_one


# In[ ]:


#그래프 x축 y축지정
plt.plot(sr_one.index,sr_one.values, marker='o',markersize=20)


# In[ ]:


plt.figure(figsize=(12,6))#그림사이즈(가로인치,세로인치)
plt.plot(sr_one)

plt.title('서울 -> 경기 인구 이동') #타이틀 이름
plt.xlabel('년도',size=30) #x축의 이름
plt.xticks(size=20, rotation='vertical')
plt.ylabel('이동인구수') #y축의 이름
plt.ylim(50000, 800000)#y축의 범위지정(최소값,최대값)
plt.legend(fontsize=25, labels=['서울->경기'], loc='best') #범례
#주석표시
plt.annotate("인구이동증가(1970-1995)", #텍스트입력
            xy=(10,550000),             #텍스트위치 기준점
            rotation=25,                #텍스트회전 각도
            va='baseline',              #텍스트의 상하 정렬
            ha='center',                #텍스트의 좌우 정렬
            fontsize=20,)               #텍스트 폰트 사이즈
plt.annotate("인구이동증가(1995-2017)", 
            xy=(10,550000),             
            rotation=25,                
            va='baseline',              
            ha='center',                
            fontsize=20,)               
            
plt.show() # 변경 사항을 저장하고 출력


# In[42]:


from matplotlib import font_manager , rc
# font_path="./맑은 고딕/malgun.ttf"
# font_name=font_manager.FontProperties(fname=font_path).get_name()
# rc('font', family=font_name)
mpl.rcParams['axes.unicode_minus']=False
plt.rc('font',family='Malgun Gothic')


# In[ ]:


fig=plt.figure(figsize=(10,10))
ax1=fig.add_subplot(2,1,1)
ax2=fig.add_subplot(2,1,2)

ax1.plot(sr_one,marker='o',markersize=5)
ax2.plot(sr_one,marker='v',markerfacecolor='green',
             markersize=8 ,color='olive', linewidth=4,
            label='서울->경기')

ax2.legend(loc='best')
ax1.set_ylim(50000,800000)
ax2.set_ylim(50000,800000)

ax1.set_xticklabels(sr_one.index, rotation=75)
ax2.set_xticklabels(sr_one.index, rotation=75)
plt.show()


# In[ ]:


col_years = list(map(str,range(1970,2018)))
df3 = df_seoul.loc[['충청남도','경상북도','강원도'],col_years]


# In[ ]:


#스타일 서식 지정
plt.style.use('ggplot')
fig = plt.figure(figsize=(20,5))
ax = fig.add_subplot(1,1,1)

ax.plot(col_years, df3.loc['충청남도',:],marker='o',markerfacecolor='green',
       markersize=10, color='olive',linewidth=2, label='서울->충남')
ax.plot(col_years, df3.loc['경상북도',:],marker='o',markerfacecolor='blue',
       markersize=10, color='skyblue',linewidth=2, label='서울->경북')
ax.plot(col_years, df3.loc['강원도',:],marker='o',markerfacecolor='red',
       markersize=10, color='magenta',linewidth=2, label='서울->강원')

ax.legend(loc='best')
ax.set_title('서울 -> 충남.경북.강원',size=20)
ax.set_xlabel('년도',size=12)
ax.set_ylabel('인구수',size=12 ,rotation= 0)
ax.set_xticklabels(col_years,rotation= 90)
plt.show()


# In[ ]:


df4 = df_seoul.loc[['충청남도','경상북도','강원도','전라남도'],col_years]
fig = plt.figure(figsize=(40,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

ax1.plot(col_years, df4.loc['충청남도',:],marker='o',markerfacecolor='green',
       markersize=10, color='olive',linewidth=2, label='서울->충남')
ax2.plot(col_years, df4.loc['경상북도',:],marker='o',markerfacecolor='blue',
       markersize=10, color='skyblue',linewidth=2, label='서울->경북')
ax3.plot(col_years, df4.loc['강원도',:],marker='o',markerfacecolor='red',
       markersize=10, color='magenta',linewidth=2, label='서울->강원')
ax4.plot(col_years, df4.loc['전라남도',:],marker='o',markerfacecolor='orange',
       markersize=10, color='yellow',linewidth=2, label='서울->전남')

ax1.legend(loc='best')
ax1.set_title('서울 -> 충남',size=20)
ax1.set_xlabel('년도',size=12)
ax1.set_ylabel('인구수',size=12, rotation= 0)
ax1.set_xticklabels(col_years,rotation= 90)

ax2.legend(loc='best')
ax2.set_title('서울 -> 경북',size=20)
ax2.set_xlabel('년도',size=12)
ax2.set_ylabel('인구수',size=12, rotation= 0)
ax2.set_xticklabels(col_years,rotation= 90)

ax3.legend(loc='best')
ax3.set_title('서울 -> 강원',size=20)
ax3.set_xlabel('년도',size=12)
ax3.set_ylabel('인구수',size=12, rotation= 0)
ax3.set_xticklabels(col_years,rotation= 90)

ax4.legend(loc='best')
ax4.set_title('서울 -> 전남',size=20)
ax4.set_xlabel('년도',size=12)
ax4.set_ylabel('인구수',size=12, rotation= 0)
ax4.set_xticklabels(col_years,rotation= 90)

plt.show()


# In[ ]:


#색에 핵사코드가 있음
import matplotlib
colors={}
for name, hex in matplotlib.colors.cnames.items():
    colors[name]=hex
colors


# In[ ]:


df4 = df4.transpose()


# In[ ]:


df4.head()
df4.index = df4.index.map(int)


# In[ ]:


df4['합계']=df4.sum(axis=1)


# In[ ]:


df4.head()


# In[56]:


plt.style.use('ggplot')
df_total=df4[['합계']].sort_values(by='합계',ascending=True)
#면적 그래프 그리기
df_total.plot(kind='bar',figsize=(10,5),width=0.7,
        color='cornflowerblue')

plt.title('서울->타도시이동',size=25)
plt.ylabel('전입지',size=15,rotation= 0 )
plt.xlabel('인구수이동',size=15 )
plt.ylim(5000,30000)
plt.legend(loc='best',fontsize=15)
plt.show()


# In[26]:


df = pd.read_excel('./남북한발전전력량.xlsx',engine='openpyxl',convert_float=True)
df = df.loc[5:9]
df.drop("전력량 (억㎾h)",axis='columns', inplace=True)
df.set_index('발전 전력별', inplace=True) #인덱스를 '발전 전력별'로 변경
# df.head()


# In[27]:


df = df.T
df.tail()


# In[28]:


#증감율 (변동률) 계산
df = df.rename(columns={'합계':'총발전량'})
df.head(2)


# In[29]:


df['총발전량 - 1년']=df['총발전량'].shift(1)
df.head()


# In[30]:


df['증감율']=((df['총발전량']/df['총발전량 - 1년'])-1)*100
df.head()


# In[43]:


#2축 그래프 그리기
ax1 = df[['수력','화력']].plot(kind='bar',figsize=(20,10), width=0.5,stacked=True)
ax2 = ax1.twinx() #ax1을 ax2에 복사함

ax2.plot(df.index, df.증감율,ls='--',marker='o',markersize=20,
        color='green', label='전년대비 증감율(%)')
#ls는 라인 스타일
ax1.set_ylim(0,500)
ax2.set_ylim(-50,50)

ax1.set_xlabel('연도', size=20)
ax1.set_ylabel('발전량(억 Kwh)')
ax2.set_ylabel('전년대비 증감율')
plt.title('북한 전력 발전량(1990-2016)',size=25)
ax1.legend(loc='best')
plt.show()


# In[48]:


#히스토그램 - 단변수 데이터의 빈도수를 나타냄
df = pd.read_csv('./auto-mpg.csv',header=None)
df.columns=['mpg','cylinders','displacement','horsepower',
            'weight','acceleration','model year','origin','name']


# In[52]:


plt.style.use('classic')
#연비(mpg) 열에 대한 히스토그램 그리기
df['mpg'].plot(kind='hist',bins=10,color='coral',figsize=(10,5))
# bins=10은 mpg10~50 정의 값을 10구간으로 나눈다.

plt.title('histogram')
plt.xlabel('mpg')
plt.show()


# In[54]:


#산점도 scatter
# plt.style.available    || plt에있는 스타일 확인
plt.style.use('ggplot')
df.plot(x='weight',y='mpg',kind='scatter',c='coral',figsize=(10,5))
plt.title('scatter plot')
plt.show()


# In[71]:


#버블차트
plt.style.use('_mpl-gallery-nogrid')
#버블차트를 그리기 위해 cylinder 개수의 상대적 비율을 계산하여 시리즈 생성
cylinder_size = df.cylinders / df.cylinders.max()*300
#plt.style.availabe : 스타일 확인코드
df.plot(x='weight',y='mpg',kind='scatter',c='coral',
        s=cylinder_size,figsize=(10,5), alpha=0.3)
plt.title('scatter plot')
plt.show()


# In[58]:





# In[76]:


plt.style.use('default')
# 3개의 변수로 산점도 그리기
df.plot(x='weight',y='mpg',kind='scatter',c=cylinder_size,
        s=50,marker='+',figsize=(10,5), alpha=0.3, cmap='viridis') 
# cmap은 color map의 준말 'viridis','jet','gray','hot'
plt.title('scatter plot')
plt.show()


# In[77]:


# pie 차트
df['count'] = 1
df_origin = df.groupby('origin').sum()
print(df_origin)


# In[82]:


df_origin.index=['USA','EU',"JAP"]
df_origin['count'].plot(kind='pie',figsize=(7,5),autopct='%1.1f%%',
                       startangle=10, # 파이조각을 나누는 시작점(각도표시)
                       colors=['red','green','blue']# 3개의 색상리스트
                       )
plt.title('pie',size = 20)
plt.axis('equal') #파이 차트의 비율을 같게(월에 가깝게) 조정
plt.legend(labels=df_origin.index, loc='best')
plt.show()


# In[89]:


#box plot
plt.style.use('classic')
#그래프의 객체를 생성 (fig에 2개의 서브플롯생성)
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
#ax객체에 boxplot을 메서드로 그래프 출력
ax1.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],labels=['USA','EU',"JAP"])

ax2.boxplot(x=[df[df['origin']==1]['mpg'],
               df[df['origin']==2]['mpg'],
               df[df['origin']==3]['mpg']],labels=['USA','EU',"JAP"],
               vert=False) # 박스플롯을 옆으로 그리기

ax1.set_title('수직박스')
ax2.set_title('수평박스')
plt.show()

