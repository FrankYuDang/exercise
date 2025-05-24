# Below is psudo code for training a RNN model using PyTorch
# 循环结构的伪代码

num_epochs = 50 
batch_size = 64 
training_data = [...] # 你的N个训练样本 
for epoch in range(num_epochs): 
	shuffle(training_data) # 打乱整个训练数据 

	for i in range(0, len(training_data), batch_size): 
		# 1. 获取当前的 mini-batch 
		current_mini_batch = training_data[i : i + batch_size] 

		# 2. 将 mini-batch 数据输入模型 (例如 (nx, m, Tx) 或 (m, features) 等) 
		# 进行前向传播 
		predictions = model.forward(current_mini_batch_inputs) 
		
		# 3. 计算损失 
		loss = calculate_loss(predictions, current_mini_batch_labels)
		
		# 4. 反向传播计算梯度 
		model.backward(loss) 
		
		# 5. 更新模型参数 
		optimizer.step() 
		
	print(f"Epoch {epoch+1}/{num_epochs} completed.")