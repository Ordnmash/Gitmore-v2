# Gitmore-v2
Gitmore v2.0 is an NN model built on (Recurrent Neural Networks entirely).
The Gitmore v2.0 is almost 10x smaller than the v1 built on MLP with context window. 

within the Jupyter-Notebook file we show plot of the tanh layer of RNN, the plot indicates the saturation of tanh layer which leads
to vanishing gradient problem which slows our model down.

to make the Network more deeper we need Layer Normalization instead of BatchNorm - BatchNorm fails at different timesteps

this would be the foundation of GitMore v3 which would be built on LSTMs

then after LSTMs we would deeper the model through WaveNets character LM
