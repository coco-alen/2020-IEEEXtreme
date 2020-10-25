
def clear_words(sentence):
    sentence = sentence.replace(',','')
    sentence = sentence.replace('.','')
    sentence = sentence.replace('?','')
    sentence = sentence.replace('!','')
    sentence = sentence.replace(' ','')
    return sentence
count = 0
eachline = []
while(1):
    word = input()
    eachline.append(word.lower())
    if word == '</response>' or word == '</other>':
        break

all = '\n'.join(eachline)


begin=all.find('<title>')
end=all.rfind('</title>')
titles = all[begin:end+1].lower()
begin=all.find('<abstract>')
end=all.rfind('</abstract>')
abstracts = all[begin:end+1].lower()
begin=all.find('<body>')
end=all.rfind('</body>')
bodys = all[begin:end+1].lower()


eachline = all.split('\n')
stops = eachline[0].split(";")
index = eachline[1].split(";")
score = dict()
for each in index:
    score[each] = 0
sum = 0

titles = titles.split('\n')
for title in titles:
    begin = title.find('>')
    end = title.rfind('<')
    if begin < end:
        title = title[begin+1:end]
    else:
        continue
    title = title.split(' ')
    for each in title:
        each = clear_words(each)
        if len(each) >=4 and each not in stops:
            sum +=1
        if each in index:
            score[each] +=5 


abstracts = abstracts.split('\n')
for abstract in abstracts:
    begin = abstract.find('>')
    end = abstract.rfind('<')
    if begin < end:
        abstract = abstract[begin+1:end]
    else:
        continue
    abstract = abstract.split(' ')
    for each in abstract:
        each = clear_words(each)
        if len(each) >=4 and each not in stops:
            sum +=1
        if each in index:
            score[each] +=3

bodys = bodys.split('\n')
for body in bodys:
    begin = body.find('>')
    end = body.rfind('<')
    if begin < end:
        body = body[begin+1:end]
    else:
        continue
    body = body.split(' ')
    for each in body:
        each = clear_words(each)
        if len(each) >=4 and each not in stops:
            sum +=1
        if each in index:
            score[each] +=1

items = sorted(score.values())
item = sorted(zip(score.values(),score.keys()))
'''
for i in range(len(items)):
    if items(i)(0)>=item[-3]:
        print("{a}: {b}".format(items(i)(1), b =items(i)(0)/sum*100))  
'''
print("{a}: {b}".format(a = item[-1][1], b = item[-1][0]/sum*100))
print("{a}: {b}".format(a = item[-2][1], b = item[-2][0]/sum*100))
print("{a}: {b}".format(a = item[-3][1], b = item[-3][0]/sum*100))

