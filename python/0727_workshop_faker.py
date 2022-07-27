#############################
# It was used in Jupyter Notebook
#############################

# In[1]:


from faker import Faker

fake = Faker()
fake.name()


# In[3]:


fake_ko = Faker('ko_KR')
fake_ko.name()


# In[7]:


import random

random.random()
random.random()

random.seed(7777)
random.random()

random.seed(8888)
random.random()


# In[12]:


fake1 = Faker('ko_KR')
Faker.seed(87654321)

print(fake1.name()) # 1 이진호

fake2 = Faker('ko_KR')
print(fake2.name()) # 2 강은주


# In[13]:


fake1 = Faker('ko_KR')
fake1.seed_instance(87654321)

print(fake1.name()) # 1 이진호

fake2 = Faker('ko_KR')
print(fake2.name()) # 2 김은정

