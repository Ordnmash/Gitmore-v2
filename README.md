# Gitmore-v2
Gitmore v2.0 is an NN model built on (Recurrent Neural Networks entirely).
The Gitmore v2.0 is twice smaller than the v1 built on MLP with context window. 

-GitMore v2 is a very small model it removes all the deep layers which found to be contributing almost nothing to the model.

-After we inspected GitMore v2 which was deeper NN, we found that the BatchNorm layer was holding the model's performance.
