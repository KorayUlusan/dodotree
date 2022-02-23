# dodotree

*Special thanks to dodoturkoz*

Starting from $1$, you can get to any number in $\mathbb{Q}$ only with these two functions:

<!-- this is not python lol -->
```python
f(x) = x + 1
g(x) = -1 / x
```

It has (of course) a mathematical proof BUT **what if** you want to visualise it?

## SAY NO MORE

you can do it now!

Spoiler alert: this wasn't my brightest idea.

```sh
# run
python3 dodotree.py
```

### a sample tree

```markdown
  _1___________________                              
 /                     \                             
-1     ________________2______________               
  \   /                               \              
  0 -1/2___                ___________3_______       
           \              /                   \      
          1/2_____      -1/3_____         ____4____  
         /        \              \       /         \ 
        -2      _3/2_          _2/3_   -1/4_      _5 
               /     \        /     \       \    /  \
             -2/3   5/2     -3/2   5/3     3/4 -1/5 6
```

looks nice
