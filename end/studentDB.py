from tkinter import*
from operator import itemgetter
 
window=Tk()

#frame
dbio = Frame(window)
midb = Frame(window)
stus = Frame(window)

dbio.grid(row=0, column=0)
midb.grid(row=1, column=0)
stus.grid(row=2, column=0)


#label
label_name=[
    '점수: ', '번호: ', '파일이름: ', '파일이름: '
    ]

Label(dbio,text="이름: ")\
                         .grid(row=0, column=0)
c=0
for lname in label_name:
    Label(dbio,text=lname)\
                         .grid(row=c, column=2, sticky=E)
    c+=1


#row=0
entry=[]
entry.append(Entry(dbio, width=20, bg="light green"))
entry[0].grid(row=0, column=1)

entry.append(Entry(dbio, width=7, bg="light green"))
entry[1].grid(row=0, column=3,  sticky=W)
 
#row=1
entry.append(Entry(dbio, width=5, bg="light green"))
entry[2].grid(row=1, column=3, sticky=W)
 
#row=2
entry.append(Entry(dbio, width=20, bg="light blue"))
entry[3].grid(row=2, column=3, sticky=W)
 
#row=3
entry.append(Entry(dbio, width=20, bg="light blue"))
entry[4].grid(row=3, column=3, sticky=W)

for x in range(0,4):
    type(entry[x])


#func1
dbcnt=0
cnt=1
vtype=100
ins=[[0 for col in range(3)] for row in range(100)]

def Bfunc(cnt):
    if cnt==0 :
       insert()
       
    elif cnt==1 :
        delete()
        
    elif cnt==2 :
        save()

    elif cnt==3 :
        opener()


def insert():
    global dbcnt #update local variable dictionary
    global cnt

    sentry.delete("1.0",END)
    
    if(entry[0].get()==''):
        sentry.insert(END, "이름을 입력하세요!")
    else:
        for y in range(0,2):
            ins[dbcnt][y]=entry[y].get()
            entry[y].delete(0,END)
            ins[dbcnt][2]=cnt
        sentry.insert(END, "입력되었습니다.")
        dbcnt+=1
        cnt+=1
    updateview()


def delete():
    sentry.delete("1.0",END)
    global dbcnt #update local variable dictionary
    dnum=entry[2].get()
    for x in range(0,dbcnt):
        if ins[x][2]==int(dnum):
            del ins[x]
            sentry.insert(END, "삭제가 완료되었습니다.")
            dbcnt-=1
    entry[2].delete(0,END)
    updateview()

def save():
    global dbcnt #update local variable dictionary
    sentry.delete("1.0",END)
    ctd= str(dbcnt)
    filen=entry[3].get()+".txt"
    if(filen!=''):
        filed=open(filen, 'w')
        filed.write(ctd)
        filed.write("\n")
        for x in range(0,dbcnt):
            filed.write(ins[x][0])
            filed.write("\n")
            filed.write(ins[x][1])
            filed.write("\n")
            filed.write(str(ins[x][2]))
            filed.write("\n")
        sentry.insert(END, "저장이 완료됐습니다.")
        entry[3].delete(0,END)
        filed.close()
    else:
        sentry.insert(END, "파일이름을 입력해주세요")
    
def opener():
    global dbcnt #update local variable dictionary
    global cnt
    sentry.delete("1.0",END)
    filed=open(entry[4].get()+'.txt', 'r')
    temp=filed.readline()
    temp.rstrip()
    dbcnt=int(temp)
    for x in range(0,dbcnt):
        temp=filed.readline()
        ins[x][0]= temp[0:len(temp)-1]
        temp=filed.readline()
        ins[x][1]= temp[0:len(temp)-1]
        temp=filed.readline()
        temp=temp[0:len(temp)-1]
        ins[x][2]=int(temp)
    cnt=ins[dbcnt-1][2]+1
    sentry.insert(END, "열기 성공했습니다.")
    entry[4].delete(0,END)
    updateview()


def updateview():
    temp=[[0 for col in range(3)] for row in range(dbcnt)]
    for x in range(0,dbcnt):
        temp[x][0]=ins[x][0]
        temp[x][1]=float(ins[x][1])
        temp[x][2]=ins[x][2]
    if vtype==0 :
        temp.sort(key=itemgetter(2))
    elif vtype ==1:
        temp.sort(key=itemgetter(0))
    elif vtype ==2:
        temp.sort(key=itemgetter(1))
        temp.reverse()
    elif vtype==3:
        temp.sort(key=itemgetter(1))

    for x in range(0,dbcnt):
        ins[x][0]=temp[x][0]
        ins[x][1]=str(temp[x][1])
        ins[x][2]=temp[x][2]
    dentry.delete("1.0",END)
    for instance in range(0, dbcnt):
        dentry.insert(END, ins[instance][2])
        dentry.insert(END, "    ")
        dentry.insert(END, ins[instance][0])
        dentry.insert(END, "    ")
        dentry.insert(END, ins[instance][1])
        dentry.insert(END, "\n")    
        
    #print(dbcnt)

#func2
def Bfunc2(x2):
    global vtype
    if x2<4:
        vtype=x2
        updateview()
        sentry.delete("1.0",END)
  
#button
button_name=[
    "추가", "삭제", "저장", "열기"
    ]
c=0
for bname in button_name :
    def click(x=c):
        Bfunc(x)
    Button(dbio, text=bname, width="5", command=click)\
                 .grid(row=c, column=4, sticky=E)
    c+=1 

button_name2=[
    "번호순", "이름순", "점수내림차순", "점수오름차순"
    ]
c=0
for bname2 in button_name2 :
    def click2(x=c):
        Bfunc2(x)
    Button(midb, text=bname2 , width="10", command=click2)\
                 .grid(row=0, column=c, sticky=E)
    c+=1


#frame stus

dentry=Text(stus, width=60, height=10, bg="light yellow")
dentry.grid(row=0, column=0)
type(dentry)

sentry=Text(stus, width=60, height=1, bg="light pink")
sentry.grid(row=1, column=0)
type(sentry)

