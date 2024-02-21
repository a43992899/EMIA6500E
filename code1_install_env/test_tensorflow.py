# Import Packages
import tensorflow as tf
import numpy as np
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Generate Noisy Training Data
np.random.seed(42) # For reproducibility
x = np.linspace(-10, 10, 100000).reshape(-1, 1)
a, b, c = 2, 3, -1 # True parameters
y = a * x ** 2 + b * x + c + np.random.normal(0, 1, len(x)).reshape(-1, 1)

# Prepare Dataset
def prepare_dataset(x, y, batch_size=128, shuffle=False):
    dataset = tf.data.Dataset.from_tensor_slices((x, y))
    if shuffle:
        dataset = dataset.shuffle(buffer_size=1024)
    dataset = dataset.batch(batch_size)
    return dataset

# Split train, val, test
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
x_train, x_val, y_train, y_val = train_test_split(x_train, y_train, test_size=0.25, random_state=42)  # 0.25 x 0.8 = 0.2

train_dataset = prepare_dataset(x_train, y_train, shuffle=True)
val_dataset = prepare_dataset(x_val, y_val)
test_dataset = prepare_dataset(x_test, y_test)

# Define Model
class NetQuadratic(tf.keras.Model):
    def __init__(self):
        super(NetQuadratic, self).__init__()
        self.a = tf.Variable(tf.random.normal([1]), name='a')
        self.b = tf.Variable(tf.random.normal([1]), name='b')
        self.c = tf.Variable(tf.random.normal([1]), name='c')

    def call(self, inputs):
        return self.a * inputs ** 2 + self.b * inputs + self.c

# Initialize Model, Loss, and Optimizer
model = NetQuadratic()
loss_object = tf.keras.losses.MeanSquaredError()
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-3)

# Training Function
@tf.function
def train_step(model, inputs, targets, loss_object, optimizer):
    with tf.GradientTape() as tape:
        predictions = model(inputs)
        loss = loss_object(targets, predictions)
    gradients = tape.gradient(loss, model.trainable_variables)
    optimizer.apply_gradients(zip(gradients, model.trainable_variables))
    return loss

# Fit the Neural Network
TOTAL_EPOCHS = 100
for epoch in range(TOTAL_EPOCHS):
    # Train
    for x_batch, y_batch in train_dataset:
        loss = train_step(model, x_batch, y_batch, loss_object, optimizer)

    # Validate
    if epoch % 10 == 0:
        val_loss = np.mean([loss_object(y_val_batch, model(x_val_batch)).numpy()
                            for x_val_batch, y_val_batch in val_dataset])
        print(f'Epoch {epoch}/{TOTAL_EPOCHS}, Train Loss: {loss.numpy()}, Val Loss: {val_loss}')


# Visualization
plt.title('Training set')
plt.scatter(x_train.flatten(), y_train.flatten(), s=1)
x_line = np.linspace(-10, 10, 100000).reshape(-1, 1)
y_pred = model.predict(x_line)
plt.plot(x_line.flatten(), y_pred.flatten(), color='red')
plt.show()
