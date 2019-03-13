
# coding: utf-8

# In[10]:


import random
class caishuzi:
    #alpha=[0,0,0,0]
    alpha=[]
    beta=[]#set()
    result=[]
    length=4
    def __init__(self,length=4):
        #for i in range(4):
            #self.alpha[i]=str(math.floor(10*random.random()))
        self.alpha=[]
        self.length=length
        while(len(self.alpha)<length):
            x=str(random.randint(0,9))
            if x not in self.alpha:
                self.alpha.append(x)
        self.beta=set(self.alpha) 
    def show(self):
        print("揭晓答案：",self.alpha)
        #return self.s
    def caiyicai(self):
        A=0
        while(A<self.length):
            A=0
            B=0
            num=input("请输入一个数字:")
            def check(num):
                try:
                    if len(num)>self.length or len(num)<0 or len(set(num))!=self.length:
                        raise Exception
                    else:
                        return(num)
                except Exception:
                    print("数字不符合规范，请重新输入")
                    num=input("请再输入一个数字:")
                    check(num)
                    return num
            num=check(num)
            #print('numnow',num,type(num))
            for i in range(self.length):
                if num[i]==self.alpha[i]:
                    A=A+1
                elif num[i] in self.beta:
                    B=B+1
            if A==4:
                print("you win")
            else:
                print(num+" %sA%sB" %(A,B))
                #self.result.append(num+" %sA%sB" %(A,B))
                #print(self.result)


# In[11]:


if __name__=='__main__':
    cai=caishuzi()
    cai.caiyicai()

