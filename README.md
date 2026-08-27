# Gitmore-v2
Gitmore v2.0 is an NN model built-on (Recurrent Neural Networks entirely).
<p align="center">
  <img src="https://github.com/Ordnmash/GitMore-v1/blob/3d7ba9b423f5c95147f3a3f15067081110a4ab66/gitmore_logo.png" width="800" height="400" alt="GiMore_logo">
</p>
<hr>
<b>The size of Gitmore v2.0 model is `4 layers` with `40k parameters`.</b> <br>
<i>This model really outperformed the GitMore v1 with `250k parameters`</i> <br>
<br>
<b>-----performance-----</b><br>
<i>The model achieved training loss of <b>1.394651</b> and validation loss of <b>1.508826</b></i><br>
<i>Yet this came with a problem of vanishing gradients, as the activation on the hidden layer got roughly 70% saturation, which was not good at all.</i> But this still keeps the performance of the model pretty good!<br>
<br>
Because the training and the validation loss are less different - that means we can extent the hyperParameters to increase the model's performance which would drive the loss down. However training and validation loss would start to decay. 
