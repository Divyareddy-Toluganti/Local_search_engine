from flask import Flask,render_template,request
from nltk.stem import PorterStemmer
class divya:
    def fun1(self,filename,huy):
        # reading every file 
        file=open(filename)
        filecon=file.read()
        #Tokenzation 
        spe_char = ['!','"','#','$','%','&','(',')','*','+','/',':',';','<','=','>','@','[','\\',']','^','`','{','|','}','~','\t','.',',','\n','-','?']
        #here removing special characters from the file information and created into tokens
        for i in spe_char:
            filecon=filecon.replace(i," ")
        g=filecon.split(' ')
        #print(g)
        #print("****************************************************************")
        f=open(huy,'w')
        #converted all tokens in to lower case using casefold method and  storing all tokens in file
        for k in g:
            f.write(str(k.casefold()))
            f.write('\n')
        f.close()
        #took all tokens in list for storing in dictionary  
        l=[]
        for k in g:
            l.append(k.casefold())
        dic={}
        #created a dictionary to count the frequency of each token 
        for k in l:
            dic[k]=dic.get(k,0)+1
        #print(dic)
        #print("****************************************************************")
        #sorted the dictionary based on the token occurance frequency in descending order
        p=dict(sorted(dic.items(), key = lambda x: x[1], reverse = True))
        return p,l
    def fun2(self,l,K):
        c=0
        w=[]
        stop=['the','and','it','not','as','to','a','is','I','that','had','has','were','was','or','type','by','but','stop','an']
        # which top words occured in dictionary first they are removed until 3 words removed 
        for g in l:
            if(g in stop):
                w.append(g)
                c=c+1
                if(c==3):
                    break
        #here we removed 
        for i in w:
            for k in l:
                if(i==k):
                    l.remove(k)

            
        #print(pig) 
        # as imported the library pf porter Stemmer which helps to remove prefix and suffix of word which is common
        ps = PorterStemmer()
        div=l
        documentdic={}
        #after doing porterstemmer then we sent words into dictionary with their frequency 
        #the words are sent in to dictionary as {word:{document number, frequency}}
        for g in div:
            mur=ps.stem(g)
            documentdic[mur]=K
            p=documentdic.get(mur,0)
        print(documentdic)
        print("******************************************************************************************")
        return documentdic,lis

def check(do,final_dic):
    for i in do:
        p=final_dic.get(i,0)
        if(p==0):
            final_dic[i]=[do[i]]
        else:
            x=final_dic[i]
            x.append(do[i])
            final_dic[i]=x
    return final_dic
def intersection(p1,p2):
    if p1 is not None and p2 is not None:
        intersection = list(set(p1) & set(p2)) 
        return intersection
    else:
        return []


def union(p1,p2):
    if(p1==None):
        p1=[]
    if(p2==None):
        p2=[]
    return list(set().union(p1,p2))


def get_posting_list(word) :
    given_value = word
    for key, val in final_dic.items() :
        if key == given_value :
            p1 = val      
            return p1

def query_handler(query,inverted_index):
    query = query.split(" ")
    term = query[0]
    posting = get_posting_list(term)
    documents = posting
    an=[term]
    for index in range(1,len(query)):
        if(query[index] == "and"):
            op = '&'
        elif(query[index]== "or"):
            op = '||'
        elif(query[index]== "not"):
            op = '!'
        else:
            term = query[index]
            an.append(term)
            if(op == '&'):
                term = query[index]
                term = get_posting_list(term)
                documents = intersection(documents,term)
    
            elif(op == '||'):
                term = query[index]
                term = get_posting_list(term)
                documents = union(documents,term)

                
         
            elif(op == '!'):
                term = query[index]
                term = get_posting_list(term)
                if(documents==None):
                    documents=[]
                if(term==None):
                    term=[]
                documents = list(set(documents) - set(term))
    return documents,an







app = Flask(__name__)
@app.route("/")
def hello():
    return render_template('myform.html')
#@app.route('/submit',methods=['POST','GET'])
    
@app.route('/submit',methods=['POST','GET'])
def submit():
    if request.method=='POST':
        word=(request.form['word'])
        word=word.lower()
        p=final_dic.get(word,0)
        '''
        if(p==0):

            return "MG"
        else:
            s=""
            love=list(final_dic[word])
            hate=list(final_pos_dic[word])
            for i in love:
                s=s+"document"+str(i)+"\n"
            s=s+"POSITIONAL_INDEX"
    
            s=s+"\n"
            for j in hate:
                s=s+str(j)+"\n"
                '''

        potti,an=query_handler(word,final_dic)
        #return "This is boolean"+potti+"-->>----->>>>"+word+" ==>"+s
        q=""
        for i in potti:
            q=q+str(i)+" "

        print("#############################################################2@W@@@@@@@@@@@@@@@@@@@@@@@@@",an)
        
        for i in an:
            k=1
            for j in potti:
                if(j==1):
                    di=dic
                elif(j==2):
                    di=dic1
                elif(j==3):
                    di=dic2
                else:
                    di=dic3
                d=di.get(i,0)
                if(d!=0):
                    if(k==1):
                #print(i+"->",end=" ")
                        q=q+"Positional Index :  "+str(i)+"->"+" "
                        k=0
            #print(gau,end="  
                    q=q+str(d)+" "
        return "Non -positional Index  :  "+q +" "
        






def positional(lis,n):
    dicpb={}
    for i in range(len(lis)):
        if(dicpb.get(lis[i],0)==0):
            dicpb[lis[i]]={n:[i]}
        else:
            x=dicpb.get(lis[i])
            x[n].append(i)
            dicpb[lis[i]]={n:x[n]}
    return dicpb

def check1(do,final_pos_dic):
    for i in do:
        p=final_pos_dic.get(i,0)
        if(p==0):
            final_pos_dic[i]=[do[i]]
        else:
            x=final_pos_dic[i]
            x.append(do[i])
            final_pos_dic[i]=x
    return final_pos_dic





    
if __name__ == "__main__":
    div= divya()
    pig,lis=div.fun1("Boolean.txt","Div1.txt")
    document1dic,lis1=div.fun2(lis,1)

    pig,lis=div.fun1("Inverted.txt","Div2.txt")#SENDING FILE TO STORE TOKENS
    document2dic,lis2=div.fun2(lis,2)

    pig,lis=div.fun1("precisionandrecall.txt","Div3.txt")
    document3dic,lis3=div.fun2(lis,3)

    pig,lis=div.fun1("PositionalPosting.txt","Div4.txt")
    document4dic,lis4=div.fun2(lis,4)

    final_dic={}
    for i in document1dic:
        final_dic[i]=[document1dic[i]]
    final_dic=check(document2dic,final_dic) 
    final_dic=check(document3dic,final_dic)
    final_dic=check(document4dic,final_dic)

    final_dic1=sorted(final_dic.items(),key=lambda x:x[0])
    print(final_dic)
    print("********************************************************************************************************************")
    print(final_dic1)
    print("********************************************************************************************************************")
    print("POSITIONAL INDEX")
    dic=positional(lis1,1)
    dic1=positional(lis2,2)
    dic2=positional(lis3,3)
    dic3=positional(lis4,4)
    final_pos_dic={}
    for i in dic:
        final_pos_dic[i]=[dic[i]]
    
    final_pos_dic=check1(dic1,final_pos_dic)
    final_pos_dic=check1(dic2,final_pos_dic)
    final_pos_dic=check1(dic3,final_pos_dic)
     
    #potti=query_handler(y,final_dic)








    app.run(debug=True)

