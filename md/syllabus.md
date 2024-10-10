# CNS286 Syllabus Fall 2024 

Home: [Course Index](https://lancelot.languagegame.io/cns286/index.html)

_[Aman Bhargava](https://aman-bhargava.com/), Thomson Lab, Caltech_

 - **Meetings**: Thursdays 5:30-7pm.
 - **Units**: 6 hours per week.
 - **Grading**: Projects with code review and discussion. 

## Lectures, Slides, and Notes

The topics in this course can be roughly broken down into two halves: conceptual and practical. 


### Conceptual Topics

 1. **Mathematics of Prediction**: [Chapter 1 Notes](ch01.html)
 	 - Review: Probability distributions, conditional distributions and likelihood. 
	 - Statistical inference.
	 - Shannon N-gram models. 
	 - Chain rule of probability for sequential prediction. 
		 - Log-likelihood loss function for sequence prediction. 
	 - Estimation (ML, MAP).
	 - _Bonus: Markov models, hidden Markov models_
	 - **Project 1**: Build a dictionary-based N-gram++ character language model. 
 2. **Learning Predictive Models**: [Chapter 2 Notes](ch02.html)
 	 - Parameter estimation $\sim$ optimization $\sim$ learning $\sim$ function approximation. 
	 - Linear regression as a model learning system. 
	 - Loss functions, gradient descent. 
	 - Neural networks and the chain rule of calculus (backpropagation).
	 - The miracle of deep learning and the bitter lesson. 
	 - **Project 2**: Linear regression and MLP in Pyorch, apply models to N-gram text prediction. 
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
 	 - **Project 4**: Follow along with Andrej Karpathy's [GPT tutorial](https://youtu.be/kCc8FmEb1nY?si=k4UW-QmI4bM5r3ky). 


### Practical Topics

 5. **Train GPT-2 HuggingFace Template Model**: Recapitulate your results from the transformer you built from scratch (Project 4) with your own [newly-trained GPT2LMHeadModel](https://github.com/huggingface/transformers/blob/v4.45.2/src/transformers/models/gpt2/modeling_gpt2.py#L1179). 
 6. **Use and Fine-Tune Pre-Trained Transformers**: Prompt HuggingFace pre-trained autoregressive transformer LLMs for various tasks, apply low-rank fine-tuning (LoRA) to efficiently modify behavior. 
 7. **Learn to use LLM APIs Properly**: HTTP requests, asynchronous scripting for high-throughput tasks, best practices for organizing scripts.
 	 - Build an auto-grader for short-answer text responses to high school science questions. 
 8. **Hack and Control Transformers**: Explore token-based and activation based control methods. 
 	 - Human and LLM-based prompt engineering. 
	 - 1st-order discrete prompt optimization ([greedy coordinate gradient](https://github.com/amanb2000/Magic_Words)).
	 - Soft prompting (1st-order continuous prompt optimization).
	 - Try perturbing attention values or token representations by modifying the [past key and value representations](https://github.com/huggingface/transformers/blob/69b5ccb8878b58372ea326d17d9490d67ccf23a7/src/transformers/models/gpt2/modeling_gpt2.py#L725). 
 9. **Analyze LLM Representations**: 
 	 - Visualize full- and dimensionality-reduced transformer activations ([starter code](https://colab.research.google.com/drive/1NQseiwja2wTP4dpN4i8g1LxRo4_af3i4?usp=sharing)).
	 - Apply linear probes to analyze informational content of representations ([example code](https://github.com/amanb2000/Emo_LLM/blob/main/notebooks/GPT2_Adjective_Representation_PCA.ipynb)). 
	 - Use linear probes to perturb ("nudge") activations of LLM ([starter code](https://github.com/amanb2000/Emo_LLM/blob/main/notebooks/Nudge_Intrinsic_Geometry.ipynb)).
	 - [Sparse autoencoders for interpretability](https://colab.research.google.com/drive/1DeagoR31QM9qFsMkVMgEuJPst9OwsGv4) with Anthropic.

