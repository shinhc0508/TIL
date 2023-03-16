#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd # 딕셔너리와 비슷함
#panel datas의 약자


# In[13]:


dict_data={'a':1,'b':2,'c':3}
sr=pd.Series(dict_data)


# In[14]:


print(type(dict_data))
print(type(sr))


# In[15]:


print(sr)


# In[18]:


list_data=['2018-01-01',3.14,'abc',100,True]
sr_list=pd.Series(list_data)


# In[21]:


print(type(sr_list))
print(sr_list)


# In[30]:


idx = sr_list.index
val = sr_list.values


# In[29]:


print(type(idx))
print(idx)


# In[28]:


print(type(val))
print(val)


# In[35]:


tup_data = ('영인','2010-05-01','여',True)
sr_tup=pd.Series(tup_data, index=['이름','생년월일','성별','학생여부'])


# In[36]:


print(sr_tup)


# In[39]:


#원소를 1개 선택하는 2가지 방식

#sr의 1번째 원소를 선택(정수형 위치 인덱스를 이용)
print(sr_tup[0]) 

#'이름'라벨을 가진 원소를 선택(인덱스이름 활용)
print(sr_tup['이름'])


# In[40]:


#여러개의 원소를 선택하는 2가지 방식
print(sr_tup[[1,2]])
print(sr_tup[['생년월일','성별']])


# In[41]:


#시리즈 생성 실습


# In[55]:


s=(9904312,3448737,2890451,2466052)
sr=pd.Series(s, index=['서울','부산','인천','대구'])
#s=pd.Series([9904312,3448737,2890451,2466052],
#            index=['서울','부산','인천','대구'])
print(sr[1], sr['부산'])
print(sr[[1,3]], sr[['부산','대구']])


# In[46]:


for key,value in sr.items():
    print(f'key={key}이고 value={value}다.')


# In[48]:


sr/100000


# In[51]:


dict_sr = {'서울':2222222,'부산':1111111} 
#딕셔너리는 아래와 같은 연산이 안댐

dict_sr/1000 # 시리즈로 바꾸면 이런연산도 가능


# In[69]:


sr2=pd.Series({'서울':9631482 ,'부산':3393191,'인천':2632035,'대전':1490158 })
sr=pd.Series([9904312,3448737,2890451,2466052],
           index=['서울','부산','인천','대구'])
ds = sr-sr2 
# 인덱스 값이 다른 데이터는 연산이 되지만 잘안됨
# 연산이 안되는것의 결과는 NaN(Not a Number=결측치)
# np.nan 데이터 타입은 실수 float


# In[60]:


sr.index , sr.values


# In[62]:


#엘러먼트의 개수를 세는 메소드
sr.count()


# In[64]:


sr2.count()


# In[71]:


ds.count() #nan은 갯수로 치지 않음


# In[74]:


#카테고리의 값을 세는 메소드
sr.value_counts()


# In[76]:


#값을 세는 메서드 예시
get_ipython().system('pip install seaborn')


# In[81]:


import seaborn as sns
iris=sns.load_dataset('iris')
print(iris)


# In[86]:


#unique 카테고리형 자료의 종류의 갯수를 파악
iris['species'].unique()


# In[84]:


iris['sepal_length'].value_counts()


# In[88]:


#인구데이터
sr.sum(), sr.mean()


# In[92]:


#정렬메소드 시리즈는 어센딩을 쓰고 True는 정순 False는 역순
sr.sort_values(ascending=False)


# In[ ]:




