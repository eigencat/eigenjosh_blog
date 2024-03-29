---
title: "A Brief Introduction to Fourier Series"
date: 2022-10-17T00:00:00-00:00
featuredImage: ""
featuredImagePreview: ""
description: ""
toc: true
tags: [fourier, pdes]
categories: [math]
linkToMarkdown: true
draft: false
---

In this post we'll take the first steps towards understanding the Fourier transform and its many applications. Note: if you're looking to really learn, go watch [3Blue1Brown's video](https://www.youtube.com/watch?v=spUNpyF58BY)! This post is really just an excuse for me to review the topic and make pretty graphs.

<!--more-->

## Motivation
If you come from a background in math or engineering, you have almost certainly heard of the Fourier transform and some of the ways in which it is useful. From partial differential equations to signal processing, the Fourier transform proves to be a weapon of choice for analyzing a wide variety of problems. But for any reader who is not familiar with these applications, I want to spend a little time trying to give some background on why this is something worth studying.

The example that I find most intuitive is the example of **sound**. You may recall that sound is comprised of waves, and each wave has characteristics such as amplitude and frequency. In the context of sound waves, _amplitude_ governs the volume of the sound while _frequency_ governs the pitch of the sound. I want to focus especially on frequency. To illustrate the role that frequency plays, have a listen to the two audio samples I've embedded below:
{{< wav 261>}}
{{< wav 523 >}}

Each of these samples is a sine wave. They're identical in every way except for their frequencies; the first is 261 Hz and the second is 523 Hz (these are approximately C$_4$ and C$_5$ on a [standard piano](https://en.wikipedia.org/wiki/Piano_key_frequencies)). Note how the second is notably higher pitch than the first! The difference helps us isolate the role of frequency in sound.

{{< admonition note "Aside" true >}}
If you'd like to verify that these two samples are indeed identical except for their frequencies, you can recreate them yourself by running the following lightweight python program:

```python
import numpy as np
import soundfile as sf

volume = 0.4    # range(0.0, 1.0)
fs = 44100      # sampling frequency in Hz
length = 3      # length in seconds

def generateSound(freq):
    data = (np.sin(2*np.pi*np.arange(fs*length)*freq/fs)).astype(np.float32)
    sf.write(str(freq)+'.wav',data,fs)

generateSound(261)
generateSound(523)
```
{{< /admonition >}}

Now suppose I didn't tell you what frequency these samples are. It would be relatively simple to find out: just run the sound through an oscilloscope, take a look at the space between peaks on the curve, and use that to calculate the sine's frequency. Here are some simplified plots of those curves just show show their shapes:
{{< figure src="sine.svg" title="$\sin(x)$" >}}
{{< figure src="sine2.svg" title="$\sin(2x)$" >}}

Given these simple curves alone, you can determine the frequency of each. But what if we have something more complicated?
{{< figure src="sine_add.svg" title="A mystery wave" >}}

This wave is still periodic like the sine waves we saw before, so we could certainly pick out a frequency. But what if I told you that this wave is actually a composite wave made by combining multiple sine waves? How would you go about finding out which sine building blocks were used to create this wave?

The tool that we'll use to decompose this wave into its components is the **Fourier Transform**. It will be able to take the composite wave from above and break it down to tell us exactly the frequencies and amplitudes of the individual sine waves that construct it!

{{< admonition warning "Spoiler" false >}}
This composite wave is just $\sin(x) + \sin(2x)$.
{{< /admonition >}}

## The Series
Before we can get to the Fourier transform, we must first discuss the **Fourier Series**. A Fourier series is a sum of sine and cosine functions that allows us to approximate any periodic function.

Given a periodic function $f(x)$ over a fixed range $x\in[-\ell,\ell]$, we aim to decompose $f$ into a linear combination of constants, sines, and cosines. We'll use $\hat{f}$ to denote the Fourier series representation of $f$:

\\[ \hat{f}(x) \equiv \frac{a_0}{2} + \sum_{n=1}^{\infty}a_n\cos\left(\frac{n\pi x}{\ell}\right) + b_n\sin\left(\frac{n\pi x}{\ell}\right) \\]

where the coefficients $a$ and $b$ are defined to be

\begin{align*}
    a_0 &= \frac{1}{\ell}\int_{-\ell}^\ell f(x) \mathrm{d}x \\\
    a_n &= \frac{1}{\ell}\int_{-\ell}^\ell f(x)\cos\left(\frac{n\pi x}{\ell}\right) \mathrm{d}x \\\
    b_n &= \frac{1}{\ell}\int_{-\ell}^\ell f(x)\sin\left(\frac{n\pi x}{\ell}\right) \mathrm{d}x
\end{align*}

{{< admonition note "Aside" >}}
Wait a minute, where does all this come from? Unfortunately it's not very straightforward to discuss a derivation of this series in this post. I might make a more detailed post later on, but for now I'll give you enough information that you could chase up the details on your own if you wanted.

There is a class of differential equations called **Sturm-Liouville Eigenvalue Problems**. These problems are a type of _boundary value problem_, meaning they're comprised of a differential equation and several _boundary conditions_ which represent known values of the solution to the equation. These problems take the form
\begin{align*}
    & f''(x) + \lambda f(x) = 0 \qquad 0 < x < \pi \\\
    & f(0) = 0, \qquad f(\pi) = 0
\end{align*}
By adjusting the format of this problem a little, we can define three types of **Fourier Eigenvalue Problems**. These problems all have a differential equation of the form
\\[ f'' = \lambda f \qquad a < x < b \\]
and then we define three different boundary conditions that correspond to the three types of problems:
\begin{align*}
    f(a) = 0, \quad f(b) = 0 \qquad & \text{Dirichlet BCs} \\\
    f'(a) = 0, \quad f'(b) = 0 \qquad & \text{Neumann BCs} \\\
    f''(a) = f''(b), \quad f'(a) = f'(b) \qquad & \text{Periodic BCs}
\end{align*}
The solutions to these problems take the form
\begin{align*}
    f_0(x) = \frac{1}{2} &\qquad \lambda_0 = 0 \\\
    f_n^{\cos}(x) = \cos\left(\frac{n\pi x}{\ell}\right) &\qquad \lambda_n = \frac{n^2\pi^2}{\ell^2} \text{ for } n\in\mathbb{Z}^+ \\\
    f_n^{\sin}(x) = \sin\left(\frac{n\pi x}{\ell}\right) &\qquad \lambda_n = \frac{n^2\pi^2}{\ell^2} \text{ for } n\in\mathbb{Z}^+
\end{align*}
and together they form an orthogonal set according to the $L^2$ inner product. The implication here is that they're all linearly independent, and furthermore they can serve as basis functions for a space of continuous functions on the interval $[-\ell,\ell]$. Hence why we are using them as the terms in our Fourier series representation of a periodic function on that interval.

That's all the detail I'll go into here, but hopefully this is enough to point you in the right direction to learn more!
{{< /admonition >}}

### Example

To illustrate the power of the Fourier series, let's work through an example.

**Example:** Find the Fourier series for
\\[ f(x) = x^2 \qquad -\pi \leq x \leq \pi. \\]

The first thing to notice is that $\ell = \pi$, so all of our $b$ coefficients will disappear:
\\[ b_n = \frac{1}{\pi} \int_{-\pi}^\pi x^2\sin(nx) \mathrm{d}x = 0. \\]
In contrast, our $a$ coefficients are
\\[ a_n = \frac{1}{\pi}\int_{-\pi}^\pi x^2\cos(nx) \mathrm{d}x. \\]
Carrying out this integral gives us
\\[ a_0 = \frac{2\pi^2}{3} \qquad \text{and} \qquad a_n = \frac{4(-1)^n}{n^2}, \quad n\in\mathbb{Z}^+. \\]
Putting this together, we can say the Fourier series representation of $f(x)=x^2$ is
\\[ \boxed{\hat{f}(x) = \frac{\pi^2}{3} + \sum_{n=1}^\infty \frac{4(-1)^n}{n^2}\cos nx.} \\]

In practice, we cannot make use of an infinite number of terms of this series. Instead we can keep a finite number of terms and verify the accuracy of the approximation. Let's examine (graphically) how accurate this series is for various numbers of terms. For each of these illustrations, $x^2$ is the dashed parabolic curve, while the solid curve is the series up to the number of terms indicated by the caption.

{{< figure src="1term.svg" title="First partial sum" >}}
{{< figure src="2term.svg" title="Second partial sum" >}}
{{< figure src="3term.svg" title="Third partial sum" >}}
{{< figure src="4term.svg" title="Fourth partial sum" >}}

Note how each successive approximation gets closer and closer to the actual curve, but also note how the approximation is only valid within the range $-\pi<x<\pi$ (the peaks of the approximation curves). Hopefully this gives you an idea of how the Fourier series can be a powerful tool for approximating functions!

## The Complex Fourier Series
Before we move onto the idea of the Fourier transform, we must go over an alternate way of representing this series. Recall Euler's Formula:
\\[ e^{i\theta} = \cos\theta + i\sin\theta \\]
This affords us a conversion between our previous sine and cosine basis into a complex basis that still spans the the space of continuous functions over the interval $[-\ell,\ell]$. In particular, we propose our new basis functions to be
\\[ f_n(x) = e^{i(n\pi x/\ell)} \quad \text{ for } n\in\mathbb{Z} \\]
Note how each of these basis functions is just a complex linear combination of our old basis functions! We'll return to that in a moment, but first let's write down the complex fourier series using this basis:
\\[ \hat{f}(x) = \sum_{n=-\infty}^{\infty} c_n e^{i(n\pi x/\ell)} \\]
where
\\[ c_n = \frac{1}{2\ell}\int_{-\ell}^\ell f(x)e^{-i(n\pi x/\ell)}\mathrm{d}x. \\]
Comparing this to our old definition, we can find the following relationships between our coefficients:
\begin{align*}
    c_0 &= \frac{a_0}{2} \\\
    c_n &= \frac{a_n-ib_n}{2} \\\
    c_{-n} &= \frac{a_n+ib_n}{2}
\end{align*}
or equivalently:
\begin{align*}
    a_0 &= 2c_0 \\\
    a_n &= c_n + c_{-n} \\\
    b_n &= i(c_n - c_{-n})
\end{align*}
This linear conversion helps establish the intuition that our new basis functions span the same space of continuous functions as our sine and cosine basis. These functions can also be shown to be orthogonal according to the $L^2$ inner product. As a result, we can confidently say that the real and complex Fourier series are equivalent.

## The Fourier Transform
Earlier we saw an example of how the partial sums of the Fourier series gave us closer and closer approximations for some function $f(x)$ that we attempted to represent with the series. This example worked for a bounded region $x\in[-\ell,\ell]$, but what if we didn't limit ourselves to that region? Can we extend the ideas we've seen so that they apply over an infinite interval?

Indeed we can! The idea is to take the limit of the complex Fourier series as $\ell \to \infty$. You can look this up in more detail elsewhere but we end up defining the Fourier transform $\mathcal{F}$ of some function $f(x)$ at a point $\xi$ to be
\\[ \boxed{\mathcal{F}\\{f\\} = \hat{f}(\xi) = \int_{-\infty}^\infty f(\xi)e^{-2\pi i\xi x} \mathrm{d}x} \\]
as long as $f$ is absolutely integrable.

## What's Next
We now have the basic tools in our toolbelt to take steps towards understanding applications such as sound wave decomposition. In my next post we'll go over properties of the Fourier transform, discuss the discrete vs continuous transform, and examine how these are used to solve other problems.

## Acknowledgements

Thanks to Professor [Andrew Bernoff](https://www.math.hmc.edu/~ajb/) for teaching me most of this material in an intro partial differential equations class. This post is primarily based on my notes from that class as well as Prof. Bernoff as-of-yet unpublished PDEs textbook.
