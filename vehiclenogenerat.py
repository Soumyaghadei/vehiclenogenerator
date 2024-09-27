import numpy as np
states=["OD","AP","TS","TN","KA","MH","RJ","HR","WB","CH","UP","MP"]
state=np.array(list(states))
rtacodes=[10,11,12,13,14,15,16,17,18,19,20]
rtacode=np.array(list(rtacodes))
nos=[0,1,2,3,4,5,6,7,8,9]
alpha=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
print("-"*50)
for i in range(20):
    s=np.random.choice(state)
    r=np.random.choice(rtacode)
    n=np.random.choice(nos,4)
    n1="".join(map(str,n))
    
    a=np.random.choice(alpha,2)
    a1="".join(a)
    print(f"{s}{r}{a1}{n1}")