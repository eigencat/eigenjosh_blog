---
title: "Doing My Abstract Algebra Homework with Prolog"
date: 2022-06-19T15:00:00-00:00
featuredImage: ""
featuredImagePreview: ""
description: "Update Me"
toc: false
tags: [algebra, abstract algebra, logical programing, prolog]
categories: [computer science, math]
linkToMarkdown: true
draft: true
---

Prolog is a logic programming language, meaning that its programs are comprised of collections of facts that can be queried to determine the truth of related statements. For example, we could define two facts

```prolog
fallible(X) :- human(X).    % if X is human, then X is fallible
human(socrates).
```

Then we can ask Prolog whether Socrates is fallible:

```console
?- fallible(socrates).
true

?- human(X).
X = socrates.
```

This is pretty cool right? So where can we take this? Since math is built up on axioms and definitions like this, can we do some math homework in Prolog? Let's try!

<!--more-->

## Programming Rules
I've picked abstract algebra because it's constructed from some relatively straightforward facts, and my old homeworks primarily consisted of proving theorems that follow from those facts. So let's begin by going over some of the basics and and write them in Prolog!

A **group** is defined to be a set $G$ together with an operator $*$ that adheres to the following axioms:
* For all $a,b\in G$, the object $a\*b\in G$.
* There exists an element $e\in G$ such that for every element $a\in G$, $a\*e = a = e\*a$.
* For each $a\in G$, there exists an element $a^{-1}\in G$ such that $a\*a^{-1} = e = a^{-1}\*a$.
* For all $a,b,c\in G$, then $(a\*b)*c = a\*(b\*c)$.

Encoding these axioms in Prolog:
```prolog
inGroup(X) :- inGroup(a), inGroup(b), X is a*b

```

## Proving Stuff
