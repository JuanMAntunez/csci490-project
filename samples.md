# Samples from the training split (3 per venue)

## AAAI

**RIS-GAN: Explore Residual and Illumination with Generative Adversarial Networks for Shadow Removal** (2020)

Residual images and illumination estimation have been proved very helpful in image enhancement. In this paper, we propose a general and novel framework RIS-GAN which explores residual and illumination with Generative Adversarial Networks for shadow removal. Combined with the coarse shadow-removal image, the estimated negative residual images and inverse illumination maps can be used to generate indirect shadow-removal images to refine the coarse shadow-removal result to the fine shadow-free image in a coarse-to-fine fashion. Three discriminators are designed to distinguish whether the predicte...

Label: aaai (index 0)

**Dist2Cycle: A Simplicial Neural Network for Homology Localization** (2022)

Simplicial complexes can be viewed as high dimensional generalizations of graphs that explicitly encode multi-way ordered relations between vertices at different resolutions, all at once. This concept is central towards detection of higher dimensional topological features of data, features to which graphs, encoding only pairwise relationships, remain oblivious. While attempts have been made to extend Graph Neural Networks (GNNs) to a simplicial complex setting, the methods do not inherently exploit, or reason about, the underlying topological structure of the network. We propose a graph convol...

Label: aaai (index 0)

**Towards Explainable Action Recognition by Salient Qualitative Spatial Object Relation Chains** (2022)

In order to be trusted by humans, Artificial Intelligence agents should be able to describe rationales behind their decisions. One such application is human action recognition in critical or sensitive scenarios, where trustworthy and explainable action recognizers are expected. For example, reliable pedestrian action recognition is essential for self-driving cars and explanations for real-time decision making are critical for investigations if an accident happens. In this regard, learning-based approaches, despite their popularity and accuracy, are disadvantageous due to their limited interpre...

Label: aaai (index 0)

## ACL

**What Question Answering can Learn from Trivia Nerds** (2020)

In addition to the traditional task of machines answering questions, question answering (QA) research creates interesting, challenging questions that help systems how to answer questions and reveal the best systems. We argue that creating a QA dataset—and the ubiquitous leaderboard that goes with it—closely resembles running a trivia tournament: you write questions, have agents (either humans or machines) answer the questions, and declare a winner. However, the research community has ignored the hard-learned lessons from decades of the trivia community creating vibrant, fair, and effective que...

Label: acl (index 1)

**On the Calibration of Pre-trained Language Models using Mixup Guided by Area Under the Margin and Saliency** (2022)

A well-calibrated neural model produces confidence (probability outputs) closely approximated by the expected accuracy. While prior studies have shown that mixup training as a data augmentation technique can improve model calibration on image classification tasks, little is known about using mixup for model calibration on natural language understanding (NLU) tasks. In this paper, we explore mixup for model calibration on several NLU tasks and propose a novel mixup strategy for pre-trained language models that improves model calibration further. Our proposed mixup is guided by both the Area Und...

Label: acl (index 1)

**KG-FiD: Infusing Knowledge Graph in Fusion-in-Decoder for Open-Domain Question Answering** (2022)

Current Open-Domain Question Answering (ODQA) models typically include a retrieving module and a reading module, where the retriever selects potentially relevant passages from open-source documents for a given question, and the reader produces an answer based on the retrieved passages. The recently proposed Fusion-in-Decoder (FiD) framework is a representative example, which is built on top of a dense passage retriever and a generative reader, achieving the state-of-the-art performance. In this paper we further improve the FiD approach by introducing a knowledge-enhanced version, namely KG-FiD...

Label: acl (index 1)

## CVPR

**Texture and Shape Biased Two-Stream Networks for Clothing Classification and Attribute Recognition** (2020)

Clothes category classification and attribute recognition have achieved distinguished success with the development of deep learning. People have found that landmark detection plays a positive role in these tasks. However, little research is committed to analyzing these tasks from the perspective of clothing attributes. In our work, we explore the usefulness of landmarks and find that landmarks can assist in extracting shape features; and using landmarks for joint learning can increase classification and recognition accuracy effectively. We also find that texture features have an impelling effe...

Label: cvpr (index 2)

**HL-Net: Heterophily Learning Network for Scene Graph Generation** (2022)

Scene graph generation (SGG) aims to detect objects and predict their pairwise relationships within an image. Current SGG methods typically utilize graph neural networks (GNNs) to acquire context information between objects/relationships. Despite their effectiveness, however, current SGG methods only assume scene graph homophily while ignoring heterophily. Accordingly, in this paper, we propose a novel Heterophily Learning Network (HL-Net) to comprehensively explore the homophily and heterophily between objects/relationships in scene graphs. More specifically, HL-Net comprises the following 1)...

Label: cvpr (index 2)

**Templates for 3D Object Pose Estimation Revisited: Generalization to New Objects and Robustness to Occlusions** (2022)

We present a method that can recognize new objects and estimate their 3D pose in RGB images even under partial occlusions. Our method requires neither a training phase on these objects nor real images depicting them, only their CAD models. It relies on a small set of training objects to learn local object representations, which allow us to locally match the input image to a set of "templates", rendered images of the CAD models for the new objects. In contrast with the state-of-the-art methods, the new objects on which our method is applied can be very different from the training objects. As a ...

Label: cvpr (index 2)

## ICLR

**Computation Reallocation for Object Detection** (2020)

The allocation of computation resources in the backbone is a crucial issue in object detection. However, classification allocation pattern is usually adopted directly to object detector, which is proved to be sub-optimal. In order to reallocate the engaged computation resources in a more efficient way, we present CR-NAS (Computation Reallocation Neural Architecture Search) that can learn computation reallocation strategies across different feature resolution and spatial position diectly on the target detection dataset. A two-level reallocation space is proposed for both stage and spatial reall...

Label: iclr (index 3)

**GeoDiff: A Geometric Diffusion Model for Molecular Conformation Generation** (2022)

Predicting molecular conformations from molecular graphs is a fundamental problem in cheminformatics and drug discovery. Recently, significant progress has been achieved with machine learning approaches, especially with deep generative models. Inspired by the diffusion process in classical non-equilibrium thermodynamics where heated particles will diffuse from original states to a noise distribution, in this paper, we propose a novel generative model named GeoDiff for molecular conformation prediction. GeoDiff treats each atom as a particle and learns to directly reverse the diffusion process ...

Label: iclr (index 3)

**CoST: Contrastive Learning of Disentangled Seasonal-Trend Representations for Time Series Forecasting** (2022)

Deep learning has been actively studied for time series forecasting, and the mainstream paradigm is based on the end-to-end training of neural network architectures, ranging from classical LSTM/RNNs to more recent TCNs and Transformers. Motivated by the recent success of representation learning in computer vision and natural language processing, we argue that a more promising paradigm for time series forecasting, is to first learn disentangled feature representations, followed by a simple regression fine-tuning step -- we justify such a paradigm from a causal perspective. Following this princi...

Label: iclr (index 3)

## ICML

**Fiedler Regularization: Learning Neural Networks with Graph Sparsity** (2020)

We introduce a novel regularization approach for deep learning that incorporates and respects the underlying graphical structure of the neural network. Existing regularization methods often focus on penalizing weights in a global/uniform manner that ignores the connectivity structure of the neural network. We propose to use the Fiedler value of the neural network’s underlying graph as a tool for regularization. We provide theoretical support for this approach via spectral graph theory. We show several useful properties of the Fiedler value that make it suitable for regularization. We provide a...

Label: icml (index 4)

**Improving Language Models by Retrieving from Trillions of Tokens** (2022)

We enhance auto-regressive language models by conditioning on document chunks retrieved from a large corpus, based on local similarity with preceding tokens. With a 2 trillion token database, our Retrieval-Enhanced Transformer (RETRO) obtains comparable performance to GPT-3 and Jurassic-1 on the Pile, despite using 25{\texttimes} fewer parameters. After fine-tuning, RETRO performance translates to downstream knowledge-intensive tasks such as question answering. RETRO combines a frozen Bert retriever, a differentiable encoder and a chunked cross-attention mechanism to predict tokens based on an...

Label: icml (index 4)

**Learning fair representation with a parametric integral probability metric** (2022)

As they have a vital effect on social decision-making, AI algorithms should be not only accurate but also fair. Among various algorithms for fairness AI, learning fair representation (LFR), whose goal is to find a fair representation with respect to sensitive variables such as gender and race, has received much attention. For LFR, the adversarial training scheme is popularly employed as is done in the generative adversarial network type algorithms. The choice of a discriminator, however, is done heuristically without justification. In this paper, we propose a new adversarial training scheme fo...

Label: icml (index 4)

## NEURIPS

**Constant-Expansion Suffices for Compressed Sensing with Generative Priors** (2020)

Generative neural networks have been empirically found very promising in providing effective structural priors for compressed sensing, since they can be trained to span low-dimensional data manifolds in high-dimensional signal spaces. Despite the non-convexity of the resulting optimization problem, it has also been shown theoretically that, for neural networks with random Gaussian weights, a signal in the range of the network can be efficiently, approximately recovered from a few noisy measurements. However, a major bottleneck of these theoretical guarantees is a network \emph{expansivity} con...

Label: neurips (index 5)

**REVIVE: Regional Visual Representation Matters in Knowledge-Based Visual Question Answering** (2022)

This paper revisits visual representation in knowledge-based visual question answering (VQA) and demonstrates that using regional information in a better way can significantly improve the performance. While visual representation is extensively studied in traditional VQA, it is under-explored in knowledge-based VQA even though these two tasks share the common spirit, i.e., rely on visual input to answer the question. Specifically, we observe in most state-of-the-art knowledge-based VQA methods: 1) visual features are extracted either from the whole image or in a sliding window manner for retrie...

Label: neurips (index 5)

**Seeing the forest and the tree: Building representations of both individual and collective dynamics with transformers** (2022)

Complex time-varying systems are often studied by abstracting away from the dynamics of individual components to build a model of the population-level dynamics from the start. However, when building a population-level description, it can be easy to lose sight of each individual and how they contribute to the larger picture. In this paper, we present a novel transformer architecture for learning from time-varying data that builds descriptions of both the individual as well as the collective population dynamics. Rather than combining all of our data into our model at the onset, we develop a sepa...

Label: neurips (index 5)

