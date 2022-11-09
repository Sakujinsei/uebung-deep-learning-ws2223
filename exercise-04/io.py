# TASK:
# Write a new python script called io.py. The script reads in the file wiki.txt, which contains 10000 randomly selected sentences from the German Wikipedia. The script then filters the sentences, and produces three output files:

# The file short.txt contains all sentences that contain less than 30 characters. You can use the function len() to determine the length of a string.
# The file articles.txt contains all sentences that start with an article (for simplicity, let's just use "Der", "Die", and "Das"). You can use the function startswith(...) on a string, to find out if it has a certain prefix.
# The file april.txt contains all sentences that contain the string "April". To check wether a string contains another string, you can use the in-expression, e.g., if "April" in sentence:.
# In all cases, try to use list comprehension.

#v1
# # src = open ("exercise-04\wiki.txt").readlines()
# open("short.txt",'w').writelines(line for line in src if len(line) < 30)
# open("articles.txt",'w').writelines(line for line in src if line.startswith("Der") or line.startswith("Die") or line.startswith("Das"))
# open("april.txt",'w').writelines(line for line in src if "April" in line)

#v2
# with open('exercise-04\wiki.txt') as src:
#     txt = src.readlines()
#     f = [f.replace('\n', '') for f in txt]

# with open('exercise-04\short.txt', 'w') as src:
#     [src.write(f + '\n') for f in f if len(f) < 30]

# with open('exercise-04\articles.txt', 'w') as src:
#     [src.write(f + '\n') for f in f if f.startswith('Der') or f.startswith('Die') or f.startswith('Das')]

# with open('exercise-04\april.txt', 'w') as src:
#     [src.write(f + '\n') for f in f if 'April' in f]


# heck I hope UE will clarify hence the directory is correct, yet produces the error here


wiki = open("exercise-04/wiki.txt", encoding='utf-8').readlines()

open("exercise-04/short.txt", mode='w', encoding='utf-8').writelines(line for line in wiki if len(line) < 30)
open("exercise-04/articles.txt", mode='w', encoding='utf-8').writelines\
    (line for line in wiki if line[0:4] in ["Der ", "Die ", "Das"])
open("exercise-04/april.txt", mode='w', encoding='utf-8').writelines(line for line in wiki if 'April' in line)

# oh, I forgot encoding. now thats working. lol