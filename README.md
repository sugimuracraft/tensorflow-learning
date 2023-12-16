# Run
```sh
source ~/venv/bin/activate
python main.py
```

# Result
## with Metal (MacBook Pro 2023 Late: M3 Max 16C CPU, 40C GPU, 128GB Mem, 8TB SSD)
```plain
Epoch 1/5
782/782 [==============================] - 57s 60ms/step - loss: 4.6716 - accuracy: 0.0705
Epoch 2/5
782/782 [==============================] - 47s 60ms/step - loss: 4.0654 - accuracy: 0.1376
Epoch 3/5
782/782 [==============================] - 46s 59ms/step - loss: 3.7118 - accuracy: 0.1769
Epoch 4/5
782/782 [==============================] - 46s 59ms/step - loss: 3.9363 - accuracy: 0.1529
Epoch 5/5
782/782 [==============================] - 46s 59ms/step - loss: 3.4397 - accuracy: 0.2178
```
## without Metal (MacBook Pro 2023 Late: M3 Max 16C CPU, 40C GPU, 128GB Mem, 8TB SSD)
```plain
Epoch 1/5
782/782 [==============================] - 493s 629ms/step - loss: 4.7655 - accuracy: 0.0669
Epoch 2/5
782/782 [==============================] - 486s 622ms/step - loss: 4.0756 - accuracy: 0.1457
Epoch 3/5
782/782 [==============================] - 481s 615ms/step - loss: 4.0541 - accuracy: 0.1309
Epoch 4/5
782/782 [==============================] - 479s 613ms/step - loss: 3.5985 - accuracy: 0.1885
Epoch 5/5
782/782 [==============================] - 480s 614ms/step - loss: 3.5101 - accuracy: 0.2165
```
## without Metal (MacBook Air 2020 Early: Intel i5 4C CPU, 8GB Mem, 512GB SSD)
```plain
Epoch 1/5
782/782 [==============================] - 1723s 2s/step - loss: 4.6148 - accuracy: 0.0845   
Epoch 2/5
782/782 [==============================] - 1671s 2s/step - loss: 4.3524 - accuracy: 0.1081
Epoch 3/5
782/782 [==============================] - 1677s 2s/step - loss: 4.1284 - accuracy: 0.0953
Epoch 4/5
782/782 [==============================] - 1647s 2s/step - loss: 3.7689 - accuracy: 0.1531
Epoch 5/5
782/782 [==============================] - 1612s 2s/step - loss: 3.6255 - accuracy: 0.1735
```

# Init
see: https://developer.apple.com/metal/tensorflow-plugin/

## Install Pip packages
```sh
python3.9 -m venv ~/venv
source ~/venv/bin/activate
```

## Upgrade pip
```sh
pip install -U pip
```

## Install Packages
```sh
pip install tensorflow
pip install tensorflow-metal
```
