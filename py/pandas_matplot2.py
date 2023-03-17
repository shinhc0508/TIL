#!/usr/bin/env python
# coding: utf-8

# In[6]:


import seaborn as sns
import matplotlib.pyplot as plt
titanic = sns.load_dataset('titanic')
titanic.head(2)


# In[4]:


titanic.info()


# In[12]:


sns.set_style('dark') # 시몬 스타일 기본 테마 : darkgird.whitegird,dark,white,ticks
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)

#그래프 그리기 - 선형회귀선 표시
sns.regplot(x='age',y='fare', data=titanic, ax=ax1) #회귀선(분석)-regression
#그래프 그리기 - 선형회귀선 미표시
sns.regplot(x='age',y='fare', data=titanic, ax=ax2, fit_reg=False) #회귀선(분석)-regression
plt.show()


# In[14]:


#heatmap
flights = sns.load_dataset('flights')
flights_passenger= flights.pivot('month','year','passengers')
flights.head()


# In[15]:


flights.tail() #1949~1960 년까지 월별 여객기 이용승객수


# In[22]:


plt.figure(figsize=(10,8))
plt.title('연도,월별 승격수에 대한 hea')
sns.heatmap(flights_passenger, annot=True,fmt='d',linewidths=1)
plt.show()


# In[26]:


#seaborn의 scatter
sns.set_style('whitegrid')

fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,2,1)
ax2 = fig.add_subplot(1,2,2)
#이산형 변수의 분포 - 데이터의 분산 미고려
sns.stripplot(x='class', y='age',data=titanic,ax=ax1)
#이산형 변수의 분포 - 데이터의 분산 고려 (중복x)
sns.swarmplot(x='class', y='age',data=titanic,ax=ax2)
#차트의 제목
ax1.set_title('stripplot')
ax2.set_title('swarmplot')
plt.show()


# In[31]:


#bar plot
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)
#x축과 y축에 변수를 할당
sns.barplot(x='sex',y='survived',data=titanic,ax=ax1)
ax1.set_title('titanic survived -sex')
#x축과 y축에 변수를 할당 hue 옵션 class
sns.barplot(x='sex',y='survived',hue='class',data=titanic,ax=ax2)
ax2.set_title('titanic survived -sex/class')
#x축과 y축에 변수를 할당 hue 옵션 class 누적으로 표시
sns.barplot(x='sex',y='survived',hue='class',data=titanic,ax=ax3, dodge=False)
ax3.set_title('titanic survived -sex/class')
plt.show()


# In[44]:


#count plot
fig = plt.figure(figsize=(15,5))
ax1 = fig.add_subplot(1,3,1)
ax2 = fig.add_subplot(1,3,2)
ax3 = fig.add_subplot(1,3,3)

#기본값
sns.countplot(x='class',palette='Set1',data=titanic,ax=ax1)
sns.countplot(x='class',hue='who',data=titanic,ax=ax2 , palette='Set2')
sns.countplot(x='class', hue='who', data=titanic, ax=ax3, palette='Set3', dodge=False)
ax1.set_title('titanic class')
ax2.set_title('titanic class -who')
ax3.set_title('titanic class -who(stacked)')
plt.show()


# In[56]:


sns.set_style('whitegrid')
fig = plt.figure(figsize=(15,10))
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)

#ax1 boxplot 기본값
sns.boxplot(x='alive',y='age',data=titanic,ax=ax1)
#ax2 boxplot hue
sns.boxplot(x='alive',y='age',hue='sex',data=titanic,ax=ax2)
#ax3 바이올린그래프 기본값
sns.violinplot(x='alive',y='age',data=titanic,ax=ax3)
#ax4 바이올린그래프 hue = sex
sns.violinplot(x='alive',y='age',hue='sex', data=titanic,ax=ax4)
plt.show()


# In[61]:


# join plot : 산점도 + 히스토그램
sns.set_style('whitegrid')
fig = plt.figure(figsize=(15,10))

# 조인트그래프 - 기본값
j1=sns.jointplot(x='fare',y='age', data=titanic )
# 조인트그래프 -회귀선
j2=sns.jointplot(x='fare',y='age',kind='reg',data=titanic )
# 조인트그래프 - 육각그래프
j3=sns.jointplot(x='fare',y='age',kind='hex',data=titanic )
# 조인트그래프 - 커널 밀집그래프
j4=sns.jointplot(x='fare',y='age',kind='kde',data=titanic )

# 차트제목
j1.fig.suptitle('title fare- scatter',size=15)
j2.fig.suptitle('title fare- reg',size=15)
j3.fig.suptitle('title fare- hex',size=15)
j4.fig.suptitle('title fare- kde',size=15)


# In[55]:


iris = sns.load_dataset('iris')
sns.pairplot(iris, hue='species')
plt.title('iris의 pair plot')
plt.show()


# In[ ]:




