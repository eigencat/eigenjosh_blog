---
title: "Stirling's Approximation"
date: 2022-05-15T15:02:13-07:00
tags: [discrete math, combinatorics]
categories: [math]
linktomarkdown: true
draft: true
---

In large systems where probability and statistics are the tools of choice to analyze system behavior, it's inevitable that we come across combinatorial calculations that require us to compute large factorials. With sufficiently large numbers, it becomes impractical for computers to perform those factorial operations in the way that you and I might do them. Instead, it becomes significantly more feasible to employ approximations such as **Stirling's approximation** in order to get results that a very accurate without being as compuationally intensive.

## Stirling's Approximation
Suppose we are tasked with computing $N!$ for some large $N$. Factorials of large numbers are impractical to compute using the traditional $N\cdot(N-1)\cdots 1$ definition, partially due to the memory required but also due to the fact that this brute force method is $O(N)$, and it would be nice to have a faster algorithm. Luckily we have approximations that help us approach these large factorials, such as **Stirling's approximation**:
\\[ N! \approx \left(\frac{N}{e}\right)^N\sqrt{2\pi N}. \\]
At first glance it may seem like this does not help us simplify the computation, given that $N^N$ is larger than $N!$ and requires the same number of operations to compute if we're going by the definition of the power operator. But exponentiation algorithms such as [exponentiation by squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) allow us to compute $N^N$ in around $O(\log N)$ operations. As such, this approximation is significantly easier to compute than brute forcing the factorial.

This approximation becomes even simpler if we're interested in the logarithm of $N!$. If we take the log of both sides of the expression above, we find
\\[ \ln N! \approx N\ln N - N + \frac{1}{2}\ln N + \frac{1}{2}\ln(2\pi). \\]
When $N$ is large, the last two terms become very small in relation to the final answer, so they're often omitted and the approximation becomes
\\[ \ln N! \approx N\ln N - N. \\]

Given that this is an approximation, it is essential to understand what the error bounds are. This is tricky to summarize before we've seen the derivation of the approximation (see below!), but for now I'll say that the error in the factorial approximation is asymptotically equal to a multiplicative factor of $1 + \frac{1}{12N}$. For this reason, you'll often see the error denoted as $O(1/N)$ and included in the statement of the approximation in order to turn it into an "equality:"
\\[ N! = \left(\frac{N}{e}\right)^N\sqrt{2\pi N} \left(1 + O\left(\frac{1}{N}\right)\right). \\]

Now let's return to our task of calculating $10^{23}!$. 

## Stirling's Approximation of the Gamma Function
The **Gamma function** $\Gamma(z)$ is a well-known extension of the factorial function which operates on complex and real numbers, not just the non-negative integers. For those unfamiliar with this function, it's defined as
\\[ \Gamma(z) = \int_0^{\infty}x^{z-1}e^{-x} \mathrm{d}x \\]
for $z\in\mathbb{C}$ where $\Re(z) > 0$. This simplifies nicely when the function's input is a positive integer. Given $n > 0 \in\mathbb{Z}$, we find
\\[ \Gamma(n) = (n-1)! \\]
Note: this result will become more clear in the section on derivation.

Given the success of Stirling's approximation for factorial, it's natural to ask whether the approximation also extends to the gamma function. And indeed it does! The approximation for the Gamma function looks nearly identical to that for factorial:
\\[ \Gamma(z) \approx \sqrt{\frac{2\pi}{z}}\left(\frac{z}{e}\right)^z \\]
again with an error term on the order of $1/z$, so the approximation is often written as
\\[ \Gamma(z) = \sqrt{\frac{2\pi}{z}}\left(\frac{z}{e}\right)^z \left(1 + O\left(\frac{1}{z}\right)\right). \\]
Simlarly to the approximation for factorial, we can use this to write an approximation for the log of the gamma function
\\[ \ln\Gamma(z) \approx \left(z - \frac{1}{2}\right)\ln z - z + \frac{1}{2}\ln(2\pi). \\]
Just like before, the $z$ and constant terms become negligable for large $z$, so the approximation that's often used is
\\[ \ln\Gamma(z) \approx \left(z-\frac{1}{2}\right)\ln z. \\]

## Derivation
How do we go about proving that Stirling's approximation is an approximation of factorial? The derivation of this approximation begins with the integral of $e^x$. Recall that
\\[ \int e^{-x} \mathrm{d}x = -e^{-x} + C. \\]
If we scale the exponent, this relationship becomes
\\[ \int e^{-ax} \mathrm{d}x = -\frac{1}{a}e^{-ax} + C. \\]
If we turn this into a definite integral from $0$ to $\infty$, we'll find that
\\[ \int_0^\infty e^{-ax} \mathrm{d}x = a^{-1}. \\]
Pretty simple so far. Now let's differentiate this expression $n$ times with respect to $a$ (yes, $a$ not $x$):
\\[ \int_0^\infty x^ne^{-ax}\mathrm{d}x = n!\cdot a^{-(n+1)} \\]
and we've managed to introduce a factorial into this expression! By setting $a=1$, we can write down the following integral identity for $n!$:
\\[ n! = \int_0^\infty x^ne^{-x}\mathrm{d}x. \\]
Does this look familiar? It should! This looks like the definition of the **gamma function**. And indeed, this is why the gamma function is considered an extension of factorial. It simply takes this identity for factorial and uses the integral definition (substituting $n-1$ for $n$ thanks to Legendre's tomfoolery) in order to extend the function outside the non-negative integers.

Now we can use this identity to derive Stirling's approximation. 

