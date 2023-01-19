---
title: Flowcharts
weight: 20
reveal: true
---
Flowcharts are a visual representation of an algorithm.
A flowchart normally uses a combination of blocks and arrows
to represent actions and sequences.
Blocks typically represent actions.
The order in which actions occur is shown
using arrows that point from statement to statement.
Sometimes a block will have multiple arrows coming out of it, 
representing a step where a decision must be made
about which path to follow. 

{{< revealx makingFlowcharts >}}

## Sequencing
```
1. Append "-".
2. Append first letter
3. Append "ay"
4. Remove first letter
```

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2023-01-19T03:06:11.218Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15\&quot; version=\&quot;20.8.5\&quot; etag=\&quot;468pmvhNVO4-uIaTliIi\&quot;&gt;&lt;diagram id=\&quot;p1AgiMrpuAm8F1ZPscJE\&quot; name=\&quot;Page-1\&quot;&gt;7ZhLc5swEMc/Dcd4eNs5+tkc2ks59HGTYQ1qBKJCGNNPXwmEMUOckrQpzgwXm/1rxUra1Q+NNGsdnz4wlEafaABEM/XgpFkbzTSN+dwSf1IplWIYTq2EDAdKawUP/wIl6krNcQBZx5FTSjhOu6JPkwR83tEQY7Touh0o6UZNUQg9wfMR6atfcMCjWl2Y81Z/ABxGTWTDva9bYtQ4q5lkEQpocSFZW81aM0p5/RSf1kDk6jXrUvfbXWk9D4xBwod0WIXzfZCCvf2+fkzQcbPz9sWdSk/Gy2bCEIj5K5MyHtGQJohsW3XFaJ4EIN+qC6v1+UhpKkRDiD+A81IlE+WcCiniMVGtYsCs/Cr7z5zG/KZeVxmbU8cqlXWgCd+hGBMpLPkjTjKaiNE/lCkwAiHeV+OTbh7NmS+jR5yLSjEdayl+xNrIH+mQzUJKQwIoxdnMp3HV4GeV6+5QBxGPF2Ecc/VUoHqShivsei3lAl5NkZKyZnjX8tKUOmIh8Gf8zHMhiS0INAaxXqIfA4I4PnbHgdRWCM9+bbWIB1UwLyge9d4jIrmK5IkB835JESK2q1yxIsIcvBRVcy8EMrqF0VaW8W7SfQTG4fR8wvsJUh0Wig1l1yxa0hiu0qILytj6G2V0PuHgJnFgDsSBPSYOzB4OlmkKSaDJD5P7M5cfutVd+9irte72/wMr3kf2/yUdzigYDQ+LCQ83iQd7IB6cMfFgX8fDAbNMHBt0IgoB2MSFl3HhvN9H48L9xIWb5IIzkAvumFxwhhwbUDmdG17LB8scmw+G0cvZBIhbAIQ7EBCG/nTB/R9CuD1CfIaYiqjTyeHvyGDro5NB7+V2K9E/3SC9MqNveIUkzPa2umq7uPS3tr8B&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>

## Selection
```
1. Append "-"
2. If first letter is vowel, then:
    a. Append "yay"
3. Otherwise:
    a. Append first letter
    b. Append "ay"
    c. Remove first letter
```

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2023-01-19T03:25:07.939Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15\&quot; version=\&quot;20.8.5\&quot; etag=\&quot;Q8mRePD-Fc-F5gGkALNG\&quot;&gt;&lt;diagram id=\&quot;p1AgiMrpuAm8F1ZPscJE\&quot; name=\&quot;Page-1\&quot;&gt;7VrJkpswEP0aHz2F2Ow5jrdMqpKqVHzIcpONDGQETYQwJl8fyQhjSvaE2QJTxcVWP1prP56kLkbWPDp8YDgJPoNH6Mg0vMPIWoxME00mlviTSKEQhJwS8VnoKawG1uEfokBDoVnokbThyAEoD5MmuIU4JlvewDBjkDfddkCbvSbYJxqw3mKqo99CjwclOjUnNX5PQj+oekbubfkkwpWzmkkaYA/yM8hajqw5A+BlKTrMCZWrV61LWW915elpYIzEvE2FmT/ZeAmxlz/nDzHeL1brTT5W4Ul5UU2YeGL+ygTGA/AhxnRZozMGWewR2aohrNrnE0AiQCTAX4TzQgUTZxwEFPCIqqdiwKz4LuvfOJX5QzV3NBaHhlUoawcxX+EopBK44w9hnEIsRn9fJIRR4oeb4/ik2xoytpW9B5wLppiOdSd+xNrIH+mQ3vgAPiU4CdObLUTHB9v06LralZ2I4lk3jjm71FE5SeQKu1xLuYBXQ6SgtBretbhUVMfMJ/wRP/NEJPEKEoiIWC9RjxGKebhvjgOrV8E/+dVsEQVFmCeQR7W7xzRTPa3FgLlOKUrF6ypXLA9CTtYJPs49F5LRJEbNLPRuwr0njJPD4wHXA6QqTJU2FE0zr5UGuQoLzlTGNt4qooMe9FMPzJZ6gDoVBFMThLskIbE3kluT+zuTW91sXBc1sjUF4B9q8T7C/5r6cBKDzgRiOuhDL/XBbqkPTpfyYF+Xh13IUnFwMKggAmGDLjxNF6zOdeF20IVe6oLTUhfcLnXBaXNswMVwbniuPth21/qAkBazQSD6IBBu24uFcZlw/0chXE0hvpIIRK/DyeFlyuCYnSuDocV2KaV/yCE9L6Ku0XlE9XN+DIP891L+UdvEkv0oB8dyhRuZCkWu1tuDavoLhDE/c4HdLiVco+RpBC9gqb6nFCTtgqYD3S44XklU1Hy7bfBt/A4Ip2dHP6YXDjAulVecjSz5x4uPrAM5EZ2t9ONNANEmS4ejjb4Rmm0vPdM32wiHbGlPZahtWgRNurz1oFaJkWLIjDxBJPqXOkWT4QL0qiF9y2yXMOsvdsqTQf3hk7X8Cw==&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>

## Iteration
```
1. Store list of words
2. For each word in words:
    a. Append hyphen
    b. If first letter is vowel, then:
        i.   Append "yay"
    c. Otherwise:
        i.   Append first letter
        ii.  Append "ay"
        iii. Remove first letter
```

<div class="mxgraph" style="max-width:100%;border:1px solid transparent;" data-mxgraph="{&quot;highlight&quot;:&quot;#0000ff&quot;,&quot;nav&quot;:true,&quot;resize&quot;:true,&quot;toolbar&quot;:&quot;zoom layers tags lightbox&quot;,&quot;edit&quot;:&quot;_blank&quot;,&quot;xml&quot;:&quot;&lt;mxfile host=\&quot;app.diagrams.net\&quot; modified=\&quot;2023-01-19T03:29:30.993Z\&quot; agent=\&quot;5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.1 Safari/605.1.15\&quot; version=\&quot;20.8.5\&quot; etag=\&quot;vJ7LxtydbY2v5cujE5Lb\&quot;&gt;&lt;diagram id=\&quot;p1AgiMrpuAm8F1ZPscJE\&quot; name=\&quot;Page-1\&quot;&gt;7Ztdk5owFIZ/jZfuyKd6qa7udqad6dSLftxFiUA3EBqiSH99Ewgim8XFVQvO5EbJITEh5+XJyQF7xizYPxEQeV+wA1FPHzj7nvHY03VtODTYF7ekwqJpVm5xie8IW2lY+n+hMA6Edes7MK5UpBgj6kdV4xqHIVzTig0QgpNqtQ1G1V4j4ELJsFwDJFu/+w71cutIH5b2Z+i7XtGzZo/zMwEoKosriT3g4OTIZMx7xoxgTPOjYD+DiM9eMS95u0XN2cPACAxpkwZTd7hyImjOf81eQrB7XCxXSV8X/olpWlwxdNgEiCIm1MMuDgGal9YpwdvQgfxnB6xU1vmMccSMGjP+hpSmwptgSzEzeTRA4iwbMUl/8PYPVlH8KX4uKzzuK6VUlDY4pAsQ+IgbJvTFD2McstE/pxEkCLr+Khsfr7bEW7LmvXuUMqnoljFhH2xy+AevED+4GLsIgsiPH9Y4yE6s46zqYpN3wg6PurH06Vsd5Rep2ayczyWfwFofCVNcDK/OMYXWAXEhPeXAUkrsJoQ4gGzCWEMCEaD+rjoQIG4G91Cv1As7EJI5Qz7id3cAbUVPSzZiKmsKIXbD8ilLPJ/CZQSyi08YNKrKKKWl3Y2/d5BQuD/tcdlBosFI0CGtFpOSNZotbN4RZ8zBrTyqgNBNIOgNgaDpbQJBl4AwiSIYOj3OKfvPli920355KImtCoB3aHEf7r8mH0yzbUCMFB86yQezIR+sNvFg1uNh45OYBQ4DxIQAieLCeVywW+fCWHGhk1ywGnLBbpMLVpOwAaQqbvgoH4Z623zQNMln/wEQ9+Hpq9zol97AoulX7Ie01NFBJEJIY/2VQHKwiFavNHIYxsdlY0tk+AYDzC5HRQyXZhpaJ4IcDYZYRRGdhIvWNP1gntRgn8/wsQqLNP9HKVVUwZtNDG8CIE0mUApjtZZ1Q25azXa21Nu4orf+HQhOzqF9it9Y7mzEA+EVP3Kz8Ji3wQlknS3kxdDDwWobq4VQXgitpqHx6GYLYSs5tfvw9HVwcmnSq1lsrDeMjSeE8L3soVrEK8T1/Rg1Mfiipr55UfVXz5HZQT7e60Ku0Y4/VVv+M7jWvZygbqpwvpNALED1/usF7T5NHEiUWFJM+OYf+VkwhDdc35g4ckSu8HAy7DmQoD06qEeJHaVD45ePWoWD/PLRE9+RDUK4p4IKCgrnQcFoHwpyYKiSgl3lRNMszTsivMOsYPH+r8oKdlJvNc/C7jgrWFz78YY5C4ST/FFY6Mcel5FK/Z2x3OlNd8g3S/3p8tOFeSiHLer96aZJj1tGMKxY/l0jv7HLf70Y838=&lt;/diagram&gt;&lt;/mxfile&gt;&quot;}"></div>
<script type="text/javascript" src="https://viewer.diagrams.net/js/viewer-static.min.js"></script>