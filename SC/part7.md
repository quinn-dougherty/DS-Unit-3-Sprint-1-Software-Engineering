# _Why is code review important_

Code review is a great way to keep a team responsible for each other. 

A team has 3 kinds of people: 
1. _present you_
2. _future you_
3. _not you_

The goals of style enforcement and code review practices are to keep _all three of these parties satisfied_, **minimizing** stress for everyone. 

### What I like to see 
When I'm reviewing code, I really like to see **input and output types** very clearly in docstrings. A method's docstring should make input and output extremely easy to read. The second thing that should pop out in a docstring is **side effects**. If *state is mutated* in the function (like `x+= foo` where `x` is some global variable, instance attribute, etc.) then a priority of a docstring is to alert me to this. After that, description of the computation in plain english is nice, but if i could only pick two, i'd pick type info and side effect info.

### Attributes I appreciate in a reviewer 
I think the most important piece of information a reviewer can give me is if my variable names are intuitive, legible, and useful. 

If you find my variables are too tearse and unhelpful, I want to know about it. If you think they're longer than necessary, then let's make them shorter. 

The first impression of someone who didn't write the code can be helpful to guage it's general level of **human readability**. After _correctness_, human readability is my top priority (I'd only worry about refactoring for performance on an as-needed basis) 

# Containers
We might be able to containerize part of our service to reduce interdependence of mutable global states. 

So, for example, suppose we have to spin up thousands of instances of an app each of which read from and write to our central database of `Product`s thousands of times per hour. We would have a large risk of errors due to race conditions, two apps/instances trying to write conflicting things to the same point in the database, etc. Here, containers could be a smart way of concentrating operations on _localized_ states and only accessing global state once or twice per hour (rather than several thousand times per hour).




