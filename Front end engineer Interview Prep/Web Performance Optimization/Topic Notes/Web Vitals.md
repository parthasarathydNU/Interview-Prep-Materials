https://web.dev/articles/vitals?hl=en

## Overview

Web Vitals is an initiative by Google to provide unified guidance for quality signals that are essential to delivering a great user experience on the web.

Google has provided a number of tools over the years to measure and report on performance. Some developers are experts at using these tools, while others have found the abundance of both tools and metrics challenging to keep up with.

Site owners should not have to be performance experts to understand the quality of experience they are delivering to their users. The Web Vitals initiative aims to simplify the landscape, and help sites focus on the metrics that matter most, the **Core Web Vitals**.

## Core Web Vitals

Core Web Vitals are the subset of Web Vitals that apply to all web pages, should be measured by all site owners, and will be surfaced across all Google tools. Each of the Core Web Vitals represents a distinct facet of the user experience, is measurable [in the field](https://web.dev/articles/user-centric-performance-metrics#how_metrics_are_measured), and reflects the real-world experience of a critical [user-centric](https://web.dev/articles/user-centric-performance-metrics#how_metrics_are_measured) outcome.

The metrics that make up Core Web Vitals will [evolve](https://web.dev/articles/vitals?hl=en#evolving_web_vitals) over time. The current set for 2020 focuses on three aspects of the user experience—_loading_, _interactivity_, and _visual stability_—and includes the following metrics (and their respective thresholds):

![[Pasted image 20231014232010.png]]

- **[Largest Contentful Paint (LCP)](https://web.dev/articles/lcp)**: measures _loading_ performance. To provide a good user experience, LCP should occur within **2.5 seconds** of when the page first starts loading.
- **[First Input Delay (FID)](https://web.dev/articles/fid)**: measures _interactivity_. To provide a good user experience, pages should have a FID of **100 milliseconds** or less.
- **[Cumulative Layout Shift (CLS)](https://web.dev/articles/cls)**: measures _visual stability_. To provide a good user experience, pages should maintain a CLS of **0.1.** or less.