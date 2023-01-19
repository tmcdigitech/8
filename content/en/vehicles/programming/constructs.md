---
title: Constructs
weight: 10
---
*from [Khan Academy](https://www.khanacademy.org/computing/ap-computer-science-principles/algorithms-101/building-algorithms/a/the-building-blocks-of-algorithms)*

An algorithm is a mindless, step by step process that describes how to solve a problem in a way that always gives a correct answer. When there are multiple algorithms for a particular problem (and there often are!), the best algorithm is typically the one that solves it the fastest.

As computer programmers, we are constantly using algorithms, whether it's an existing algorithm for a common problem, like sorting an array, or if it's a completely new algorithm unique to our program. By understanding algorithms, we can make better decisions about which existing algorithms to use and learn how to make new algorithms that are correct and efficient.

An algorithm is made up of three basic building blocks: sequencing, selection, and iteration.

## Sequencing
An algorithm is a step-by-step process, and the order of those steps are crucial to ensuring the correctness of an algorithm.

Here's an algorithm for translating a word into Pig Latin, like from "pig" to "ig-pay":

```
1. Append "-".
2. Append first letter
3. Append "ay"
4. Remove first letter
```
{{< alert color="info" >}}
Note: **append** means to add to the end of something.
{{< /alert >}}

🔍 Try following those steps in different orders and see what comes out. Not the same, is it?

## Selection
Algorithms can use selection to determine a different set of steps to execute based on a Boolean expression.

Here's an improved algorithm for Pig Latin that handles words that starts with vowels, so that "eggs" becomes "eggs-yay" instead of the unpronounceable "ggs-eay":

```
1. Append "-"
2. If first letter is vowel, then:
    a. Append "yay"
3. Otherwise:
    a. Append first letter
    b. Append "ay"
    c. Remove first letter
```

## Iteration
Algorithms often use repetition to execute steps a certain number of times or until a certain condition is met.

We can add iteration to the previous algorithm to translate a complete phrase, so that "peanut butter and jelly" becomes "eanut-pay utter-bay and-yay elly-jay":

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

By combining sequencing, selection, and iteration, we've successfully come up with an algorithm for Pig Latin translation.

🤔 Can you think of situations where it produces an incorrect output?