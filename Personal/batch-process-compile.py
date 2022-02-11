import re
chapter = 1
start = 0
end = 1

compilefile = ""
filenames = [[] for i in range(end-start + 1)]
str = [[] for i in range(end-start + 1)]
for i in range(start, end+1):
    filenames[i-start] = "ch{}_{}.txt".format(chapter, i)

rmwordbreaks = re.compile('-\n')
rmdoublebreaks = re.compile('\n\n')
rmlinebreaks = re.compile('\n')
replacedoublebreaks = re.compile('42069') # insert temporary variable for \n\n

text = ""
for f in filenames:
    print(f, '...')
    with open(f) as fd:
        for line in fd:
            text += line

text = rmwordbreaks.sub('', text)
text = rmdoublebreaks.sub('42069', text) # replace \n\n
text = rmlinebreaks.sub(' ', text)
text = replacedoublebreaks.sub('\n\n', text)

with open('ch{}.txt'.format(chapter), 'w') as rf:
    rf.write(text)
