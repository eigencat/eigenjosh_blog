---
title: "A Brief Introduction to Fourier Series"
date: 2022-06-04T15:00:00-00:00
featuredImage: ""
featuredImagePreview: ""
description: ""
toc: true
tags: [fourier, pdes]
categories: [math]
linkToMarkdown: true
draft: true
---

In this post, we'll take the first step towards understanding the Fourier transform and its many applications.

<!--more-->

## Motivation
If you come from a background in math or engineering, you have almost certainly heard of the Fourier transform and some of the ways in which it is useful. From partial differential equations to signal processing, the Fourier transform proves to be a weapon of choice for analyzing a wide variety of problems. But for any reader who is not familiar with these applications, I want to spend a little time trying to give some background on why this is something worth studying.

The example that I find most intuitive is the example of _sound_. You may recall that sound is comprised of waves, and each wave has characteristics such as speed, frequency, and wavelength. For simplicity let's assume the speed of sound is fixed, so we are left with frequency and wavelength to describe a given wave. But with a fixed speed, we can use either one of these descriptors to uniquely identify a wave. Let's pick frequency!

So how does frequency play a role in sound? 

## The Series

