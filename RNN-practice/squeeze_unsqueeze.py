# 2025/05/24
# squeeze and unsequeeze

import torch 

# 利用squeeze, unsqueeze来处理batch_size为1的情况
single_batch_output = torch.randn(1, 10) # shape (1, 10)
squeezed_output = single_batch_output.squeeze(0) # shape (10,)
print("Single batch output shape:", single_batch_output.shape)

import tensorflow as tf 
single_batch_output_tf = tf.random.normal([1,10])
squeezed_output_tf = tf.squeeze(single_batch_output_tf, axis=0) # shape (10,)
print("Single batch output shape (TensorFlow):", single_batch_output_tf.shape)

