Title: Beam Search
Date: 2024-11-13 10:20
Category: Neural Networks

Hi folks! In this post I'm doing a summary of Beam Search so I can understand it better and hopefully help someone :) 
Beam search is a heuristic search algorithm used in sequence problems such as translation, text generation, or voice recognition. It is an improvement
over breadth-first search.

## How it works?
At each step of the process, *beam search* keeps a limited set of sequences that seem promising given a score or probability. 
This set is called the *beam* and its size is controlled by a parameter called *beam width*, usually represented by the character `K`.

### Steps to create a sequence

1. We start with the initial state, which could be <start\> or the tag that you are using.
2. **Expansion:** Generate all possible words or tokens given the current sequences. At the starting point, it is *<start\>* + all the tokens in the vocabulary.
3. **Selection:** Get a score for each extended sequence and pick the **K** best.
4. **Repeat:** Repeat the process until you reach <stop\> or a "stop" token you define.

## Whiteboard explanation

![Beam Search Diagram](draws/beam_search.png)

## In other words 👨🏻‍💼:

Let's say we have the following set at a given time **t**, and let's call that set **C** for candidates.

$$
C_t = \{ (x_1^1, \dots, x_t^1), \dots, (x_1^K, \dots, x_t^K) \}
$$
At time **t+1** we have $\tilde{C} _{t+1}$ which expands $C_t$:

$$
\tilde{C_{t+1}} =  \{ (x_1^k, \dots, x_t^k, v_1), \dots, (x_1^k, \dots, x_t^k, v_{|V|}) \}
$$

This gives us a set of size: K\*|V|, where |V| is the size of the vocabulary; here we need to pick again the best **K** candidates. 
In seq2seq architectures the size is usually K\*K, but it depends on the implementation. 

## Benefits
- Balance between exploration and efficiency: Does not explore all options, but is better than greedy search.
- Precision: Usually gets better sequences than other simpler strategies.

## Cons
- Does not guarantee a global optimum.
- Computationally Expensive: Requires more calculations than simpler strategies.
