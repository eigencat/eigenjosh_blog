---
title: "My Favorite Integral"
date: 2022-05-22T20:04:22-07:00
featuredImage: ""
featuredImagePreview: ""
description: "Integrating the Gaussian"
toc: false
tags: [gaussians, probability, calculus]
categories: [math]
linkToMarkdown: true
draft: false
---

In this post I'll go over an integral that _blew my mind_ when I first saw it.

<!--more-->

Suppose your probability professor tasks you with normalizing the [standard normal distribution](https://en.wikipedia.org/wiki/Normal_distribution#Standard_normal_distribution). You're given the following un-normalized probability density function
\\[ f(x) = e^{-x^2/2} \\]
to start with. In order to normalize this and turn it into a valid probability distribution, we need to integrate this function to find the area underneath it. Then we can divide $f(x)$ by that area in order to normalize it. We'll do that soon, but first let's tackle a very similar integral, and the star of this post:
\\[ \int_{-\infty}^\infty e^{-x^2}\mathrm{d}x. \\]
Note how we've stripped away the scalar from the exponent. Don't worry, we'll reintroduce it soon!

If you try to integrate this function using your standard integration techniques, you won't have much luck at all. So I'd like to resort to a bit of trickery to evaluate this integral. Let's define
\\[ I = \int_{-\infty}^\infty e^{-x^2}\mathrm{d}x. \\]
Then we can _square_ both sides of this equation to obtain
\\[ I^2 = \left(\int_{-\infty}^\infty e^{-x^2}\mathrm{d}x\right) \left(\int_{-\infty}^\infty e^{-y^2}\mathrm{d}y\right) \\]
Note how I have changed the right integral to be an integral in $y$ rather than $x$. This can be done because the value of the integral is the same regardless of the name of the variable. From here, a key observation is that each integral is a constant, so either one can be absorbed into the other. Furthermore, each integrand is independent of the other, so this can be further condensed into a double integral over the $x$-$y$ plane:

\begin{align*}
    I^2 &= \int_{-\infty}^\infty e^{-x^2} \left(\int_{-\infty}^\infty e^{-y^2}\mathrm{d} y\right) \mathrm{d}x \\\\
    &= \int_{-\infty}^\infty \int_{-\infty}^\infty e^{-x^2}e^{-y^2}\mathrm{d}y\mathrm{d}x.
\end{align*}

So now we have an integral over all of 2-dimensional space. If you're questioning whether that's true, let me remind you that $y$ is independent from $x$. Given two vectors that are linearly independent, those vectors span a 2-dimensional plane. So we really can say that this is an integral over all of 2d space, and we can even think of $x$ and $y$ as the traditional Cartesian axes.

Thinking of $x$ and $y$ in this way gives us access to the ability to transform from Cartesian coordinates into polar coordinates! Believe it or not, this will simplify our integral significantly.

{{< admonition tip "Recall" true >}}
To transform between Cartesian coordinates and polar coordinates, recall the following relations:

\begin{align*}
    x &= r\cos\theta \\\\
    y &= r\sin\theta \\\\
    r &= \sqrt{x^2+y^2} \\\\
    \mathrm{d}y\mathrm{d}x &= r \ \mathrm{d}\theta\mathrm{d}r
\end{align*}
{{< /admonition >}}

Going through with this coordinate transformation, we find that
\\[ I^2 = \int_0^\infty \int_0^{2\pi} e^{-r^2}r \ \mathrm{d}\theta\mathrm{d}r. \\]
The inner integral is easy to evaluate. We don't have any $\theta$ terms in our integrand, so it evaluates to a constant $2\pi$. We're left with
\\[ I^2 = 2\pi\int_0^\infty e^{-r^2}r \ \mathrm{d}r  = 2\pi\left[-\frac{1}{2}e^{-r^2}\right]_0^\infty = \pi. \\]
Then we take the square root, leaving us with
\\[ \boxed{I = \sqrt{\pi}.} \\]
Note how we do not keep the negative square root. This is because $I$ is intrinsically a positive value; it represents the area beneath a positive function. The negative square root would simply have been an irrelevant artifact. For example, suppose I defined $x=1$. Then I squared both sides to find $x^2 = 1$, then took the square root again to get $x = \pm 1$. It would be ridiculous to maintain that $x=-1$ is a valid statement since $x$ is intrinsically positive by definition.

Ok so we've solved my favorite integral! Now we can relate this back to the normal distribution. Suppose we were to introduce a scaling term $a>0$ into the exponent of our integrand. Doing this and then following the same steps would reveal that
\\[ \int_{-\infty}^\infty e^{-ax^2} = \sqrt{\frac{\pi}{a}}. \\]
In the un-normalized normal distribution, we take $a=1/2$, so we find that the normalizing term for the distribution is
\\[ \sqrt{2\pi}, \\]
which leads us to the reason why the standard normal distribution is given to be
\\[ f(x) = \frac{1}{\sqrt{2\pi}}e^{-x^2/2} . \\]
