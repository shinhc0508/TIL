#!/usr/bin/env python
# coding: utf-8

# In[55]:


import seaborn as sns
import pandas as pd
df=sns.load_dataset ('titanic')


# In[16]:


# df.isnull() Nan 값조회
df.isnull().sum() #nan값 합
# df.head()


# In[9]:


df['deck'].unique()


# In[19]:


nan_deck = df['deck'].value_counts(dropna=False)
print(nan_deck)


# In[28]:


df.notnull().sum(axis=1)
df['pclass'].value_counts()


# In[23]:


#결측치 확인 for반복문으로 각 열의ㅡ NaN 개수 계산
missing_df=df.isnull()
for col in missing_df.columns:
    missing_count= missing_df[col].value_counts()
    try:
        print(col, ':',missing_count[True]) #Nan값이 있으면 개수를 
    except:
        print(col,":",missing_count[0]) #Nan값이 없으면 0을 출력


# In[29]:


#Nan 값이 500개 이상인 열을 모두 삭제 - deck열(891개중 688개 Nan)삭제
df_tresh = df.dropna(axis=1,thresh=500)
print(len(df_tresh.columns))


# In[31]:


# age 열에 나이데이터 없는 모든 행을  삭제()
df_age=df.dropna(subset=['age'],how='any',axis=0)


# In[33]:


df_age.isnull().sum()


# In[42]:


#age 열의 Nan값을 다른 나이 데이터의 평균으로 변경
mean_age=df['age'].mean(axis=0) #age열의 평균을 계산(nan값을 제외)
df['age'].fillna(mean_age, inplace=True)
df.info()


# In[46]:


#embark_town 승선지는 최빈값(가장 많이 출연한 값)
most_freq=df['embark_town'].value_counts(dropna=True).idxmax()
# most_freq=df['embark_town'][100:500].value_counts(dropna=True).idxmax()
# 위처럼 인덱싱도 가능
print(most_freq)


# In[48]:


df['embark_town'].fillna(most_freq,inplace=True)


# In[51]:


df.info()


# In[54]:


#embark 열의 Nan값을 바로 앞에 있는 변경하기
df['embarked'].fillna(method='ffill',inplace=True)
df.info()


# In[60]:


#중복 데이터를 갖는 데이터 찾기
df2= pd.DataFrame({'c1':['a','a','b','a','b'],
                 'c2':[1,1,1,2,2],
                 'c3':[1,1,2,2,2]})
df2


# In[61]:


df_dup=df2.duplicated()
print(df_dup)


# In[63]:


#데이터 프레임의 특정열에서 데이터 중복 값을 찾기
col_dup=df2['c2'].duplicated()
print(col_dup)


# In[65]:


# 데이터프레임에서 중복 행 제거
df3 = df2.drop_duplicates()
print(df3)


# In[66]:


#특정열을 기준으로 중복행 제거
df4 = df2.drop_duplicates(subset=['c2','c3'])
print(df4)


# In[69]:


# 값 변환 conversion
df = pd.read_csv('./auto-mpg.csv',header=None)
df.head()


# In[71]:


df.columns=['mpg','cylinders','displacement','horsepower',
            'weight','acceleration','model year','origin','name']


# In[74]:


#mpg (mile per gallon) 를 kpl(kilometer per liter)을 생성 (mpg_to_kpl)
mpg_to_kpl=1.60934/3.78541
#mpg 열에 0.425를 곱해서 새로운 kpl 컬럼을 생성
df['kpl'] = df['mpg']*mpg_to_kpl
df.head(3)
#kpl열을 소수점 아래 둘째자리 반올림
df['kpl']= df['kpl'].round(2)
df.head(2)


# In[75]:


df.dtypes


# In[77]:


#hores 열의 고유값
print(df['horsepower'].unique())


# In[100]:


import numpy as np
df['horsepower'].replace('?',np.nan,inplace=True)
# print(df.innull().sum)
df.dropna(subset=['horsepower'], axis=0 ,inplace=True)
# print()
# df.info()로 확인 후 ['horsepower']데이터 타입을 float64로 변경
df['horsepower']=df['horsepower'].astype('float64')
df.info()


# In[80]:


#origin 열의 고유값을 확인
df['origin'].unique()


# In[86]:


df['origin'].replace({1:'US',2:'EU',3:"JAP"},inplace=True)
df['origin'].unique()


# In[88]:


print(df['origin'].dtypes)


# In[89]:


#origin 열의 문자열 자료형을 범주형으로 변환
df['origin']=df['origin'].astype('category')
print(df['origin'].dtype)


# In[93]:


##origin 열의 문자열 카테고리를 자료형으로 변환
df['origin']=df['origin'].astype('str')
print(df['origin'].dtype)


# In[98]:


#model_year 정수를 범주형으로 변환
df['model year'].sample(3)


# In[102]:


df['model year']=df['model year'].astype('category')
df['model year'].sample(3)


# In[105]:


#horsepower를 3개 등급으로 나누기
#np.histogram 함수로 3개의 bin 으로 나누는 경계 값의 리스트 구하기
count, bin_dividers = np.histogram(df['horsepower'],bins=3)
print(bin_dividers)


# In[107]:


#3개의 bins에 이름지정
bin_name=['저출력','보통출력','고출력']


# In[113]:


#cut 함수로 각데이터를 3개의 bin에 할당
df['hp_bin']=pd.cut(x=df['horsepower'],
                   bins=bin_dividers, # 경계값 리스트
                   labels=bin_name,    # 해당구간 이름
                   include_lowest=True)#첫 경계값을 포함
print(df[['horsepower','hp_bin']].head(10))


# In[115]:


#hp_bin 열의 범주형 데이터를 더미변소 변환(원핫인코딩)
horsepower_dummies = pd.get_dummies(df['hp_bin'])
print(horsepower_dummies.head(10))


# In[116]:


#원핫 인코딩을 다른 패키지로 사용가능
#sklearn = 라이브러리 불러오기

from sklearn


# In[118]:


df = pd.read_csv('./stock-data.csv')
df.head(4)


# In[119]:


df.info()


# In[120]:


df['new_date']=pd.to_datetime(df['Date'])


# In[122]:


df.head(2)


# In[125]:


df.set_index('new_date',inplace=True)


# In[126]:


df.drop('Date',axis=1,inplace=True)


# In[127]:


df.head(3)


# In[129]:


dates=['2019-01-01','2020-03-01','2021-06-01']
ts_dates=pd.to_datetime(dates)
print(ts_dates)


# In[131]:


#Timestamp를 period로 변환
pr_day = ts_dates.to_period(freq='D')
print(pr_day)
pr_month = ts_dates.to_period(freq='M')
print(pr_month)
pr_year = ts_dates.to_period(freq='A')
print(pr_year)


# In[133]:


#timestamp의 배열 만들기 - 월간격,월의 시작일 기준
ts_ms=pd.date_range(start='2019-01-01', #날짜범위 시작
                   end=None, #날짜범위끝
                   periods=6,#생성할 timestamp의 개수
                   freq='MS',#시간간격 MS:월의 시작일
                   tz='Asia/Seoul'#시간대 지역
                   ) 
print(len(ts_ms))      
print(ts_ms)


# In[137]:


#월간격, 월의 마지막 날 기준
ts_me = pd.date_range(start='2023-01-01',
                      periods=6,
                     freq='M',
                     tz='Asia/Seoul')
print(len(ts_me))
print(ts_me)


# In[138]:


#분기(3개월), 간격 , 월의 마지막날 기준
ts_3m = pd.date_range(start='2019-01-01',
                      periods=6,
                     freq='3M',
                     tz='Asia/Seoul')
print(len(ts_3m))
print(ts_3m)


# In[144]:


import seaborn as sns
titanic=sns.load_dataset('titanic')
df=titanic.loc[:,['age','fare']]


# In[145]:


def add_10(n):
    return n+10 


# In[148]:


df_map=df.applymap(add_10)
df_map


# In[149]:


def missing_value(series):
    return series.isnull() # boolean 시리즈로 변환


# In[150]:


result = df.apply(missing_value, axis=0)
print(result.head(3))


# In[151]:


def min_max(x):
    return x.max()-x.min()


# In[153]:


result2=df.apply(min_max) #axis=0
print(result2)


# In[159]:


df['ten']=10


# In[160]:


def add_two_obj(a,b):
    return a+b


# In[163]:


#데이터프레임의 2개열을 선택해서 적용
df['add']=df.apply(lambda x : add_two_obj(x['age'],x['ten']),axis=1)
df.head(3)


# In[165]:


filename = './서울시CCTV설치운영현황(자치구)_년도별_211231기준.csv'


# In[169]:


cctv=pd.read_csv(filename, skiprows=1 ,encoding='EUC-KR')
cctv.head()


# In[171]:


cctv['총계']=cctv['총계'].apply(lambda x : int(x.replace(',','')))


# In[172]:


cctv.head()


# In[175]:


#결측치를 0으로 대체, 정수로 변환
cctv.isna().sum() #isna() == isnull()


# In[176]:


cctv['2012년'].fillna('0',inplace=True)
cctv['2013년'].fillna('0',inplace=True)


# In[179]:


for col in cctv.columns[2:]:
    cctv[col]=cctv[col].apply(lambda x : int(x.replace(',','')))
    


# In[180]:


cctv.head(3)


# In[181]:


cctv.info()


# In[184]:


titanic.head()


# In[185]:


import seaborn as sns
titanic=sns.load_dataset('titanic')


# In[192]:


# age를 평균으로 대체
mean_age=titanic['age'].mean(axis=0)
titanic['age'].fillna(mean_age, inplace=True)


# In[197]:


# embarked 을 최빈값으로 대체
count=titanic['embarked'].value_counts(dropna=True).idxmax()
titanic['embarked'].fillna(count,inplace=True)


# In[202]:


# embark_town 결측값이 있는 행 삭제
titanic.dropna(subset=['embark_town'],how='any',axis=0)


# In[218]:


# deck 삭제
titanic.drop(columns=['deck'],inplace=True)
titanic.shape


# In[221]:


# titanic['adult/child'] 컬럼을 만들고 20살이상이면 adult  이하면 child
# apply와 lambda활용
titanic['adult/child']=titanic.age.apply(lambda x: 'adult'
                                        if x>20 else 'child')
titanic


# In[225]:


# age 기준으로'age_cut'칼럼을 생성후 두 칼럼을 출력하기
# age, age_cut
bins=[1,20,30,50,70,100]
labels=['미성년자','청년','중년','장년','노년']
titanic['age_cut']=pd.cut(titanic.age , bins ,labels=labels)
titanic


# In[228]:


# pd.concat(데이터프레임 리스트,axia=축)
df1=pd.DataFrame([['a',1],['b',2]],columns=['letter','number'])
df2=pd.DataFrame([['c',3],['d',4]],columns=['letter','number'])
df3=pd.DataFrame([['e',5,'!'],['f',6,'?']],columns=['letter','number','etc'])


# In[230]:


print(df1)
print(df2)
print(df3)


# In[237]:


df_rcc = pd.concat([df1,df2,df3],axis=0)
df_rcc


# In[240]:


#공통된 컬럼만 남기기
df_rcc2=pd.concat([df1,df2,df3],join='inner')
df_rcc2


# In[242]:


#인덱스 재지정
df_rcc3=pd.concat([df1,df2,df3],join='inner',
                 ignore_index=True)
df_rcc3


# In[245]:


#열로 연결하기
df4 = pd.DataFrame({'age':[20,21,22]},
                   index=['amy','james','david'])
df5 = pd.DataFrame({'phone':['010-1234-4567',
                            '010-1234-4568',
                            '010-1234-4569']},
                   index=['amy','james','david'])
df6 = pd.DataFrame({'job':['student','programer','ceo','pro']},
                   index=['amy','james','david','kim'])
print(df4)
print(df5)
print(df6)


# In[252]:


df_cc = pd.concat([df4,df5,df6], axis=1)
df_cc


# In[253]:


df_cc2 = pd.concat([df4,df5,df6], axis=1, join='inner')
df_cc2


# In[320]:


# pd.merge(left,right,on=기준컬럼,how=연결방법)
df = pd.read_csv('./scores.csv', encoding='utf-8')


# In[321]:


df7=df.loc[[1,2,3]][['name','eng']]
df8=df.loc[[1,2,4]][['name','math']]
print(df7)
print(df8)


# In[276]:


#공통데이터로만 연결
c=pd.merge(df7,df8,on='name',how='outer') #defalut는 how='inner'
a=pd.merge(df7,df8,on='name',how='left') # 왼쪽
b=pd.merge(df7,df8,on='name',how='right') #오른쪽

print(c,a,b)


# In[279]:


# melt
df.melt() # == pd.melt(df)


# In[281]:


#고정할 컬러를 지정하여 melt =>id_vars=[열이름리스트]
#name을 고정
df.melt(id_vars=['name','kor'])


# In[282]:


# 행으로 위치를 변경할 열 지정
# value_vars=[열이름리스트]
df.melt(id_vars='name',value_vars='kor')


# In[284]:


df.melt(id_vars='name',value_vars=['kor','eng'])


# In[285]:


df.melt(id_vars='name',value_vars=['kor','eng'], # 행이
       var_name='subject', value_name='score')


# In[302]:


# 열을 행으로 보내기(pivot)
df = df.melt(id_vars='name',var_name='subject' ,value_name='scores')
df


# In[303]:


def get_grade(x):
    if x > 90 :
        grade = 'A'
    elif x >= 80 :
        grade = 'B'
    elif x >= 70 :
        grade = 'C'
    elif x >= 60 :
        grade = 'D'
    else :
        grade = 'F'
    return grade


# In[305]:


df['grade'] = df['scores'].apply(get_grade)
df=df.sort_values('name')
df


# In[308]:


#데이터프레임.pivot (index=인덱스로 사용할 컬럼,
#columns = 컬럼으로 사용할 컬럼, values=값으로 사용할 컬럼)
#name, subject, scores
df.pivot(index='name',columns='subject', values='scores')


# In[309]:


df.pivot(index='name',columns='subject', values='grade')


# In[312]:


df.pivot(index='name',columns='subject', values=['scores','grade'])


# In[319]:


df.transpose()


# In[322]:


df = pd.DataFrame({"item": ["shirts", "shirts", "shirts", "shirts", "shirts",
                          "pants", "pants", "pants", "pants"],
                    "color": ["white", "white", "white", "black", "black",
                          "white", "white", "black", "black"],
                   "size": ["small", "large", "large", "small",
                          "small", "large", "small", "small",
                         "large"],
                   "sale": [1, 2, 2, 3, 3, 4, 5, 6, 7],
                   "inventory": [2, 4, 5, 5, 6, 6, 8, 9, 9]})


# In[325]:


df


# In[334]:


# 집계분석 item, size별 재고 합계를 pivot_table메소드로 분석
# 재고, pants와 shirt large small
df.pivot_table(index=['item','color'],columns='size', values=['inventory','sale'], 
               aggfunc='sum',fill_value=0)



# In[370]:


df_tt = sns.load_dataset('titanic')
df_tt = df_tt[['survived','pclass','sex',
             'age','embarked']]
df_tt.dropna(inplace=True)
df_tt.head(4)


# In[372]:


#성별, 객실등급별 승선자수
# aggfunc = 총명수 count 생존자수 sum 생존율 mean
# mean은 디폴트 값이다.
df_tt.pivot_table(index='sex',columns='pclass', values='survived',
                 aggfunc='count',fill_value=0, margins=True)


# In[373]:


df_tt[['pclass','sex']].value_counts()


# In[374]:


tips=sns.load_dataset('tips')


# In[390]:


tips.head()


# In[379]:


tips['tip_pct']=((tips.tip/tips.total_bill)*100).round(2)


# In[382]:


tips.pivot_table('tip_pct','sex')


# In[404]:


tips.pivot_table('tip_pct','sex','smoker'
                aggfunc='count',margins=True,margins_name='계')


# In[408]:


tips.pivot_table('tip_pct',['sex','smoker'])


# In[407]:


tips.pivot_table('tip_pct','smoker',aggfunc=['mean','min','max'])


# In[409]:


# df.groupby(그룹기준컬럼),통계적용컬럼,통계함수
# .count(): 누락값을 제외한 데이터 수
# .size() : 누락값을 포함한 데이터 수
# .mean() .sum() .std() .min() .max()


# In[445]:


#객실별 승선자수
df_titanic1=df_tt.groupby('pclass').survived.count().to_frame()
df_titanic1


# In[446]:


#객실등급 별 생존자 수
df_titanic2=df_tt.groupby('pclass').survived.sum().to_frame()
df_titanic2


# In[447]:


#생존비율
df_titanic3=df_tt.groupby('pclass').survived.mean().to_frame()
df_titanic3


# In[448]:


df_titanic4 = pd.concat([df_titanic1, df_titanic2, df_titanic3], 
                      axis=1)
df_titanic4.columns = ['승선자수', '생존자수', '생존비율']
df_titanic4


# In[ ]:


#성별 생존

