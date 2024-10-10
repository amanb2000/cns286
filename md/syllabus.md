# CNS286 Syllabus Fall 2024 

Home: [Course Index](https://lancelot.languagegame.io/cns286/index.html)

_Aman Bhargava, Thomson Lab, Caltech_

 - **Meetings**: Thursdays 5:30-7pm.
 - **Units**: 6 hours per week.
 - **Grading**: Projects with code review and discussion. 

## Lectures + Slides

 1. **Mathematics of Prediction**: [Chapter 1 Slides](ch01.html)
 	 - Review: Probability distributions, conditional distributions and likelihood. 
	 - Statistical inference.
	 - Shannon N-gram models. 
	 - Parameter estimation (ML, MAP).
	 - Chain rule of probability for sequential prediction. 
	 - Log-likelihood loss function for sequences. 
	 - _Bonus: Markov models, hidden Markov models_
	 - **Project 1**: Build a dictionary-based N-gram++ character language model. 
 2. **Computational Predictive Models and Learning**:
 	 - Parameter estimation $\sim$ optimization $\sim$ learning $\sim$ function approximation. 
	 - Linear regression as a model learning system. 
	 - Loss functions, gradient descent. 
	 - Neural networks and the chain rule of calculus (backpropagation).
	 - The miracle of deep learning and the bitter lesson. 
	 - **Project 2**: Linear and MLP N-gram models in PyTorch. 
 3. **Sequence Prediction with Recurrent Neural Networks**: 
 	 - Markov processes as canonical sequential statistical processes. 
 	 - Challenge of sequential prediction with neural networks. 
	 - Latent states for sequence prediction. 
	 - Backpropagation through time. 
	 - Problems with backpropagation through time. 
	 - **Project 3**: Character-based RNN in PyTorch.
 4. **Attention is all you need**: 
 	 - Self-attention for sequence modelling. 
	 - Transformer blocks as multi-head self-attention + nonlinearities. 
	 - Masked language modelling with transformers (BERT).
	 - Causal auto-regressive language modelling with transformers (GPT). 
 5. **Build a Generative Pre-Trained Transformer from Scratch**: 
 	 - **Project 4**: Follow along with Andrej Karpathy's [GPT tutorial](https://youtu.be/kCc8FmEb1nY?si=k4UW-QmI4bM5r3ky). 
 6. **Train GPT-2 HuggingFace Template Model**: 
 	 - **Project 5**: Recapitulate your results from the transformer you build from scratch with your own [newly-trained GPT2LMHeadModel](https://github.com/huggingface/transformers/blob/v4.45.2/src/transformers/models/gpt2/modeling_gpt2.py#L1179). 
 7. **Use and Fine-Tune Pre-Trained Transformers**: 
 	 - **Project 6**: Prompt HuggingFace pre-trained autoregressive transformer LLMs for various tasks, apply low-rank fine-tuning (LoRA) to efficiently modify behavior. 
 8. **Learn to use LLM APIs Properly**: HTTP requests, asynchronous scripting for high-throughput tasks, best practices for organizing scripts.
 	 - **Project 7**: Build an auto-grader for short-answer text responses to high school science questions. 
 9. **Hack and Control Transformers**: Explore LLM-based prompt optimization, greedy coordinate gradient adversarial prompt optimization, and soft prompting as LLM control methods ([example code](https://github.com/amanb2000/Magic_Words))
 10. **Analyze LLM Representations**: Visualize activations, apply linear probes to analyze informational content of representations, analyze geometry and structure in representations ([starter code](#)). 

