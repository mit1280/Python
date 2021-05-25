import pandas

f1 = open('author.csv',"w")
f2= open('authored.csv',"w")
f3 = open('magazine.csv',"w")
f4= open('articles.csv',"w")
header1 = '_id , fname, lname, email' + "\n"
header2 = 'ArticleId, AuthorId' + "\n"
header3 = '_id , journal' + "\n"
header4 = 'ArticleId, title, pageno, volumeNo, MagazineId, year' + "\n"

f1.write(header1)
f2.write(header2)
f3.write(header3)
f4.write(header4)

#Enter the appropriate 'Cluster', 'Collection' & ' DB'
#author
l=[]
#magazine
q=[]
mycol=pandas.read_json('articles.json')

for j in range(0,len(mycol)):
    if(isinstance(mycol['author'][j], list)):
        for k in range(len(mycol['author'][j])):
            if(l.count(k)==0):
                l.append(mycol['author'][j][k])
                data = mycol['author'][j][k].split()
                firstname=data[0]
                lastname=data[len(data)-1]
                f1.write(str(l.index(mycol['author'][j][k]))+","+firstname+","+lastname+","+"\n")
                f2.write(str(j)+","+str(l.index(mycol['author'][j][k]))+"\n")
        if(q.count(mycol['journal'][j])==0):
            q.append(mycol['journal'][j])
            f3.write(str(q.index(mycol['journal'][j]))+", "+mycol['journal'][j]+"\n") 
        f4.write(str(j)+","+str(mycol['title'][j])+","+str(mycol['pages'][j])+","+str(mycol['volume'][j])+","+str(q.index(mycol['journal'][j]))+","+str(mycol['year'][j])+"\n")
    else:
        if(l.count(mycol['author'][j])==0 ):
            l.append(mycol['author'][j])
            data = mycol['author'][j].split()
            firstname=data[0]
            lastname=data[len(data)-1]
            f1.write(str(l.index(mycol['author'][j]))+","+firstname+","+lastname+","+"\n")
            f2.write(str(j)+","+str(l.index(mycol['author'][j]))+"\n")
        if(q.count(mycol['journal'][j])==0):
            q.append(mycol['journal'][j])
            f3.write(str(q.index(mycol['journal'][j]))+", "+mycol['journal'][j]+"\n")    
        f4.write(str(j)+","+str(mycol['title'][j])+","+str(mycol['pages'][j])+","+str(mycol['volume'][j])+","+str(q.index(mycol['journal'][j]))+","+str(mycol['year'][j])+"\n")
    
f1.close()
f2.close()

