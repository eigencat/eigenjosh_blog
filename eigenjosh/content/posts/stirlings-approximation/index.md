---
title: "Stirling's Approximation"
date: 2022-05-15T15:02:13-07:00
featuredImage: "./gaussian.svg"
featuredImagePreview: "preview.png"
description: "Exploring an approximation for large factorials"
tags: [discrete math, combinatorics]
categories: [math]
linkToMarkdown: true
draft: false
---

In large systems where probability and statistics are the tools of choice to analyze system behavior, it's inevitable that we come across combinatorial calculations that require us to compute large factorials. With sufficiently large numbers, it becomes impractical for computers to perform those factorial operations in the way that you and I might do them. Instead, it becomes significantly more feasible to employ approximations such as **Stirling's approximation** in order to get results that a very accurate without being as computationally intensive.

## Stirling's Approximation
Suppose we are tasked with computing $N!$ for some large $N$. Factorials of large numbers are impractical to compute using the traditional $N\cdot(N-1)\cdots 1$ definition, partially due to the memory required but also due to the fact that this brute force method is $O(N)$, and it would be nice to have a faster algorithm. Luckily we have approximations that help us approach these large factorials, such as **Stirling's approximation**:
\\[ N! \approx \left(\frac{N}{e}\right)^N\sqrt{2\pi N}. \\]
At first glance it may seem like this does not help us simplify the computation, given that $N^N$ is larger than $N!$ and requires the same number of operations to compute if we're going by the definition of the power operator. But exponentiation algorithms such as [exponentiation by squaring](https://en.wikipedia.org/wiki/Exponentiation_by_squaring) allow us to compute $N^N$ in around $O(\log N)$ operations. As such, this approximation is significantly easier to compute than brute forcing the factorial.

This approximation becomes even simpler if we're interested in the logarithm of $N!$. If we take the log of both sides of the expression above, we find
\\[ \ln N! \approx N\ln N - N + \frac{1}{2}\ln N + \frac{1}{2}\ln(2\pi). \\]
When $N$ is large, the last two terms become very small in relation to the final answer, so they're often omitted and the approximation becomes
\\[ \ln N! \approx N\ln N - N. \\]

Given that this is an approximation, it is essential to understand how accurate it is or is not. This is tricky to summarize before we've seen the derivation of the approximation (see below!), but for now I'll say that the error in the factorial approximation is asymptotically equal to a multiplicative factor of $1 + \frac{1}{12N}$. For this reason, you'll often see the error denoted as $O(1/N)$ and included in the statement of the approximation in order to turn it into an "equality:"
\\[ N! = \left(\frac{N}{e}\right)^N\sqrt{2\pi N} \left(1 + O\left(\frac{1}{N}\right)\right). \\]

## Stirling's Approximation of the Gamma Function
The **Gamma function** $\Gamma(z)$ is a well-known extension of the factorial function. As an extension, it operates on complex and real numbers rather than being limited to the natural numbers as factorial is. For those unfamiliar with this function, it's defined as
\\[ \Gamma(z) = \int_0^{\infty}x^{z-1}e^{-x} \mathrm{d}x \\]
for $z\in\mathbb{C}$ where $\Re(z) \gt 0$. This simplifies nicely when the function's input is a positive integer. Given $n \in\mathbb{N}$, we find
\\[ \Gamma(n) = (n-1)! \\]
Note: this result will become more clear in the section on derivation.

Given the success of Stirling's approximation for factorial, it's natural to ask whether the approximation also extends to the gamma function. And indeed it does! The approximation for the Gamma function looks nearly identical to that for factorial:
\\[ \Gamma(z) \approx \sqrt{\frac{2\pi}{z}}\left(\frac{z}{e}\right)^z \\]
again with an error term on the order of $1/z$, so the approximation is often written as
\\[ \Gamma(z) = \sqrt{\frac{2\pi}{z}}\left(\frac{z}{e}\right)^z \left(1 + O\left(\frac{1}{z}\right)\right). \\]
Similarly to the approximation for factorial, we can use this to write an approximation for the log of the gamma function
\\[ \ln\Gamma(z) \approx \left(z - \frac{1}{2}\right)\ln z - z + \frac{1}{2}\ln(2\pi). \\]
Just like before, the $z$ and constant terms become negligible for large $z$, so the approximation that's often used is
\\[ \ln\Gamma(z) \approx \left(z-\frac{1}{2}\right)\ln z. \\]

## Derivation
How do we go about proving that Stirling's approximation is an approximation of factorial? There are a few approaches, but I'd like to walk through a derivation that begins with the integral of $e^x$. Recall that
\\[ \int e^{-x} \mathrm{d}x = -e^{-x} + C, \\]
and that when we scale the exponent by another variable $a$ this relationship becomes
\\[ \int e^{-ax} \mathrm{d}x = -\frac{1}{a}e^{-ax} + C. \\]
If we turn this into a definite integral from $0$ to $\infty$, we'll find that
\\[ \int_0^\infty e^{-ax} \mathrm{d}x = a^{-1}. \\]
Pretty simple so far. Now let's differentiate this expression $n$ times with respect to $a$ (yes, $a$ not $x$):
\\[ \int_0^\infty x^ne^{-ax}\mathrm{d}x = n!\cdot a^{-(n+1)} \\]
and we've managed to introduce a factorial into this expression! By setting $a=1$, we can write down the following integral identity for $n!$:
\\[ n! = \int_0^\infty x^ne^{-x}\mathrm{d}x. \\]
Does this look familiar? It should! This looks like the definition of the **gamma function**. And indeed, this is why the gamma function is considered an extension of factorial. It simply takes this identity for factorial and uses the integral definition (substituting $n-1$ for $n$ thanks to Legendre's tomfoolery) in order to extend the function outside the non-negative integers.

---

Let's take a moment to examine the integrand from the identity above. Geometrically the function $x^ne^{-x}$ is somewhat reminiscent of a Gaussian function. Indeed, we can find a Gaussian that's a pretty good approximation of it. Below is a graph comparing it to a Gaussian that we'll derive in a moment. Note how the two curves share the following properties:
1. Both curves peak at $x=n$
2. The height of that peak in both is $n^ne^{-n}$

Note also how closely the two mirror each other when changing values of $n$ (use the slider!).

{{< desmos kz4yhhvqya 600 >}}

So how did I find the Gaussian plotted above? Recall that Gaussians take the form $e^{-x^2}$, so let's attempt to put our integrand in that form. First note how we can consolidate the integrand into a single exponential:
\\[ x^ne^{-x} = e^{n\ln x - x}. \\]
From here, we'll use the Taylor expansion for $\ln x$.
{{< admonition tip "Recall" true >}}
Recall that the first few terms of the Taylor expansion for $\ln x$ are
\\[ \ln x = (x-1) - \frac{(x-1)^2}{2} + \frac{(x-1)^3}{3} - \cdots. \\]
{{< /admonition >}}

We'll use the first two terms of this expansion together with a convenient variable substitution of $y = x - n$ in order to expand our integrand's exponent as follows
\begin{align*}
    n\ln x - x &= n\ln(n+y)-n-y \\\\
    &= n\ln\left(n\left(1+\frac{y}{n}\right)\right)-n-y \\\\
    &= n\ln n - n - y + n\underbrace{\ln\left(1+\frac{y}{n}\right)}_{\text{expand by Taylor}} \\\\
    &\approx n\ln n - n - y + n\left(\frac{y}{n}-\frac{1}{2}\left(\frac{y}{n}\right)^2\right) \\\\
    &= n\ln n - n -\frac{y^2}{2n}
\end{align*}
Now we can reintroduce this as our exponent and find that
\begin{align*}
    x^ne^{-x} &\approx e^{n\ln n - n - y^2/(2n)} \\\\
    &= n^ne^{-n}e^{-y^2/(2n)}
\end{align*}
Finally, with this $e^{-y^2/(2n)}$ term, we have reached the form of a Gaussian! As a final step, let's plug this approximation back into our integral identity for $n!$. When we do this, note that $dy = d(x-n) = dx$, so our change of variables does not introduce any new terms through the differential. However we do have a slight change in our limits of integration:

\begin{align*}
    n! &\approx n^ne^{-n} \int_{-n}^\infty e^{-y^2/(2n)}\mathrm{d}y \\\\
    &\approx n^ne^{-n} \int_{-\infty}^{\infty} e^{-y^2/(2n)}\mathrm{d}y
\end{align*}
And finally, we can use the result from [my post about Gaussian integrals]({{< ref "/posts/my-favorite-integral/index.md" >}} "My Favorite Integral") to evaluate this final step
\\[ n! \approx n^ne^{-n}\sqrt{2\pi n} \\]
And there we have it! Sterling's approximation derived using the integral definition of factorial, the Taylor expansion for a logarithm, and a Gaussian integral.

{{< admonition note "Aside" true >}}
Above I make a change to the limits of the integral when I extend the lower limit from $-n$ down to $-\infty$. How did I do this?

Remember we are interested in large values of $n$. Geometrically, let's examine what we can say about the area under the Gaussian for $y \lt -n$ when $n$ is large. Note that we can rephrase this problem as trying to justify extending the lower limit down from $0$ for our integral in $x$. I think it's more intuitive to think about the region $x\lt 0$ rather than $y \lt -n$.

See the following plot where our Gaussian and the original function are both normalized to always have an amplitude of 1. By normalizing the functions in this way, we can more easily see them evolve over a wider range of $n$, and we can also gain some perspective about where the majority of the area under the curve lies.
{{< desmos sh1hfq5fz1 600 >}}
Even for relatively small $n$ such as 50, we see that the area under the Gaussian when $x\lt 0$ is negligible. The vast majority of the area under the curve comes from the local region around the peak of the function, so we can freely expand the limits of the integral without losing much accuracy in our result. Hence why we can extend that lower limit in $x$ from $0$ to $-\infty$, and thus the lower limit in our $y$ integral from $-n$ to $-\infty$ without compromising the approximation.

If this feels a bit hand-wavey to you, then you're right. I'm not going by any rigorous definition of "negligible" and "vast majority", and I'm relying on the visual cues of a geometric representation in order to make my argument. To be fair, my main reference for this post is a physics textbook, not a math one!

So let's try to put some concrete numbers on it. The standard deviation $\sigma$ of a Gaussian function can be found in the definition of a Gaussian:
\\[ f(x) = a\cdot e^{-\frac{(x-b)^2}{2\sigma^2}}. \\]
Our particular Gaussian when written in this form is
\\[ f(x) = 1\cdot e^{-\frac{(x-0)^2}{2(\sqrt{n})^2}}, \\]
so we deduce that $\sigma = \sqrt{n}$. So even with the relatively small $n=50$, the left tail where $x \lt 0$ is over 7 standard deviations away from the mean (which is $n$ by the way). If you told a statistician that you have verified a result to a significance level of $7\sigma$, they would either worship you or call you a liar. In other words, the area under that extended tail is so small it's inconsequential.

And as you increase $n$, so too do you increase the number of standard deviations separating this region and the mean. Specifically, the number of standard deviations away for any given $n$ is $\sqrt{n}$. When $n$ goes to $100$, the number of standard deviations goes to $10$. This should convince you that the extension of the integral limits becomes more and more insignificant as $n$ increases.
{{< /admonition >}}

## Error Estimation and Stirling's Series
Given the derivation in the previous section, we now have the tools we need in order to estimate the error in Stirling's Approximation.

Recall that we derived the approximation using only the first two terms of the Taylor expansion for $\ln x$. One might conjecture that we can improve the accuracy of the approximation by keeping more terms from that expansion. Furthermore, the _difference_ between the approximation based on 2 terms and the approximation based on more terms is an estimate for our error!

Most literature does not walk through the process of including more terms of the Taylor expansion, and for good reason - it gets very messy! I too will follow this precedent because I do not think the exercise contributes much to the intuition that I hope to establish in this post. Also I am lazy. Allow me to instead state the result of following that expansion:

\\[ n! \approx \left(\frac{n}{e}\right)^n\sqrt{2\pi n}\left(1 + \frac{1}{12n} + \frac{1}{288n^2} - \frac{139}{51840n^3} - \cdots\right) \\]

The series on the right has come to be known as [Stirling's Series](https://mathworld.wolfram.com/StirlingsSeries.html). The standard form of Stirling's approximation comes from truncating all but the first term of this series, while the commonly-referenced $O(1/n)$ correction term is a result of truncating all terms past the $1/12n$ term.

{{< admonition info "Bonus" true >}}
The coefficients for Stirling's Series are detailed in the following OEIS entries:
* Numerators: [OEIS A001163](https://oeis.org/A001163)
* Denominators: [OEIS A001164](https://oeis.org/A001164)
{{< /admonition >}}

## Acknowledgments
My primary source for this post is _Thermal Physics_ by Daniel V. Schroeder. This book covers Stirling's approximation in the context of statistical mechanics - a branch of physics that uses probability and statistics to describe the behavior of large systems of particles. It's a very accessible read and I would highly recommend it to anyone interested in the topic.
