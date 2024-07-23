# Task 1

x = input("Enter text: ").lower()
print(x.count('b'))


# Task 2

name = input('Enter your name: ')

res = 'Valid' if name.istitle() and name.replace(' ', '').isalpha() else print('Invalid name')
print(res)

# Task 3

x = input("Enter text")
sum_cod = 0
for i in x:
    sum_cod += ord(i)
print(sum_cod)


# Task 4
import math

for i in range(2, 12):
    print(f"{math.pi:.{i}f}")



# Task 5

import string

x = input(" Enter text: ").lower()
for i in string.punctuation:
    x = x.replace(i, ' ')
x = x.split()

max_word = x[0]
for i in x:
    if len(i) > len(max_word):
        max_word = i
print(max_word)


# Task 5_2

import string

x = input(" Enter text: ").lower()
for i in string.punctuation:
    x = x.replace(i, ' ')
x = x.split()

print(max(x, key=len))



# Task 6

text = input('Enter your text: ')
lenght = len(text)

short_word = text

for i in range(1, lenght):
    word = text[:i]
    if text == word * (lenght // i):
        short_word = word

print(short_word)



# Task 7 FALSE


cod = input("Past yor code: ")
clear = 0
clear_text = ''

for i in cod:
    if i == '<':
        clear = 1
    elif i == '>':
        clear = 0
    elif clear == 0:
        clear_text += i
print(clear_text)


# Task 7 TRUE

html = """
<ul class="menu" role="tree">
    <li class="python-meta current_item selectedcurrent_branch selected">
        <a href="/" title="The Python Programming Language" class="current_item selectedcurrent_branch selected">Python</a>
    </li>
    <li class="psf-meta ">
        <a href="https://www.python.org/psf/" title="The Python Software Foundation" >PSF</a>
    </li>
    <li class="docs-meta ">
        <a href="https://docs.python.org" title="Python Documentation" >Docs</a>
    </li>
    <li class="pypi-meta ">
        <a href="https://pypi.org/" title="Python Package Index" >PyPI</a>
    </li>
    <li class="jobs-meta ">
        <a href="/jobs/" title="Python Job Board" >Jobs</a>
    </li>
    <li class="shop-meta ">
        <a href="/community-landing/"  >Community</a>
    </li>
</ul>
"""

while '<' in html:
    start = html.find('<')
    end = html.find('>')
    tag = html[start:end + 1]
    html = html.replace(tag, '')

print(html)


# Klass work

text = input("Enter text")

while "  " in text:
    text = text.replace("  ", " ")
print({text})

# Klass work v2

x = input("Enter text")
res = x.split()
print(res)

# Klass work v3

text = input("Enter text")
res = " ".join(text.split())
print(res)


# Klass work v4
import string
text = input("Enter text")
for item in string.punctuation:
    text=text.replace(item, " ")
res = " ".join(text.split())
print(res)


# Klass work 2

import string

text = input("Enter text: ")
for item in string.punctuation:
    text = text.replace(item, " ")
res = text.split()
print(len(res))