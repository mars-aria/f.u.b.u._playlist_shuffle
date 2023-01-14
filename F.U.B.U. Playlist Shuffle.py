#!/usr/bin/env python
# coding: utf-8

#  # F.U.B.U. (*For Us By Us) Playlist Shuffle ✊🏿✊🏾✊🏽

# For my final project, I decided to do a lyrical analysis of the songs "Almeda" and "Don't Touch My Hair" by the artist Solange (a.k.a. Beyonce's sister). Through this lens of cultural and computing exploration, I was able to discover some meaningful things about the importance of rhetorical and poetical word order in black creativity/self expression. Therefore, without further a do: Welcome to the Black Parade (https://www.youtube.com/watch?v=MiUqA3jJ7Cw)! 🎵🎺

# # 'Almeda' 🤎🥃 by Solange

# To conduct my linguistic analysis on "Almeda", I created a solange() function which I used to segment into pieces an excerpt of catalogic text described by the colors "brown" and "black" in the song. I was delighted to see that the mixing of terms produced by the shuffling still captures the quintessential essence behind Solange's lyrics, which convey a celebration of blackness in the midst of its accompanying sorrows ("They takin' me in, what I done?" likely references police brutality against Black folks and/or the prejudicial injustice of being arrested simply for being Black). For example, I found the shuffled output of "Brown days" and "brown baes" to be just as relevantly Afrocentric as the original phrases "black days" and "Black baes". No love was lost, which I considered to be a huge flex. 👏🏾

# Watch: https://www.youtube.com/watch?v=6giKIu5jUvA | Song Lyrics: https://genius.com/Solange-almeda-lyrics

# In[15]:


black_owned_things = ['liquor', 'liquor', 'skin', 'face', 'leather', 'sugar', 'leaves', 'keys', 'creepers', 'face', 'skin', 'braids', 'waves', 'days', 'baes', 'things']


# In[16]:


def solange(almeda):
    from re import sub
    verse = """Brown _, brown _
    Brown _, brown _
    Brown _, brown _
    Brown _, brown _
    Brown _, brown _
    Black _, black _
    Black _, black _
    Black _, black _
    These are black-owned things
    Black faith still can't be washed away"""
    for word in almeda:
        verse = sub('_', word, verse, 1)
    return verse


# In[17]:


print(solange(black_owned_things))


# In[18]:


from random import shuffle


# In[19]:


shuffle(black_owned_things)


# In[20]:


print(solange(black_owned_things))


# In[21]:


shuffle(black_owned_things)


# In[22]:


print(solange(black_owned_things))


# # 'Don't Touch My Hair' 👩🏾‍🦱🚫🙅🏾‍♀ by Solange

# Using the same solange() function, I discovered that shuffling the lyrics of "Don't Touch My Hair" resulted in different outputs that were the complete opposite of "Almeda". Most, if not all, of the meaning behind the song lyrics becomes disappointingly lost in translation because of the scrambled sentence structures and misplaced words. Linguistically, the lyrics cease to make sense and feel disjointed from the soulful intention behind Solange's art. For example, the shuffled outputs "Don't touch my there" and "Don't touch my know" are nowhere near as powerful/impactful as the original phrases "Don't touch my soul" and "Don't touch my crown". Solange speaks from the heart, conveying in sweet yet funky tones the thoughts - and the countering rebuttal infused with White privilege ("What you say to me?") - that every black person (but especially black women) have undoubtedly experienced at least once in their lives when someone has disrespectfully touched their 'do without permission. Ultimately, the magic of her passionate plea as a woman of color for R-E-S-P-E-C-T and understanding here is left diminished in comparison to its former glory.

# Watch: https://www.youtube.com/watch?v=YTtrnDbOQAU | Song Lyrics: https://genius.com/Solange-dont-touch-my-hair-lyrics

# In[8]:


black_pride = ['hair', 'feelings', 'wear', 'soul', 'rhythm', 'know', 'crown', 'vision', 'found', 'there', 'feelings', 'wear']


# In[9]:


def solange(dont_touch):
    from re import sub
    verse = """Don't touch my _
    When it's the _ I _
    Don't touch my _
    When it's the _ I _
    Don't touch my _
    They say the _ I've _
    Don't touch what's _
    When it's the _ I _"""
    for word in dont_touch:
        verse = sub('_', word, verse, 1)
    return verse


# In[10]:


print(solange(black_pride))


# In[11]:


from random import shuffle


# In[13]:


shuffle(black_pride)


# In[14]:


print(solange(black_pride))


# In[15]:


shuffle(black_pride)


# In[16]:


print(solange(black_pride))

