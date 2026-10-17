# Keras (TensorFlow) Intro: build, train, evaluate and save a neural network

from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
from tensorflow import keras
from tensorflow.keras import layers

FOLDER = Path(__file__).parent
HISTORY_PLOT_PATH = FOLDER / "keras_training_history.png"
MODEL_PATH = FOLDER / "keras_student_model.keras"


# 1. Sample dataset — predict pass/fail from study hours and attendance
print("1. Sample dataset")
rng = np.random.default_rng(42)

study_hours = rng.uniform(0, 10, 400)      # hours studied per week
attendance = rng.uniform(50, 100, 400)     # attendance percentage
noise = rng.normal(0, 0.12, 400)

# Pass if study hours and attendance together are high, plus a little noise
study_score = study_hours / 10                        # normalised to 0 - 1
attendance_score = (attendance - 50) / 50             # normalised to 0 - 1
score = 0.5 * study_score + 0.5 * attendance_score + noise
# Half of the students pass at the 0.5 mark
passed = (score >= 0.5).astype("float32")
print(f"Pass rate: {passed.mean():.0%}")

# Scale inputs to 0-1 — networks train much more reliably on small, comparable ranges
features = np.column_stack([study_score, attendance_score]).astype("float32")

# Split into 80% training and 20% testing data
split = int(len(features) * 0.8)
x_train, x_test = features[:split], features[split:]
y_train, y_test = passed[:split], passed[split:]

print(f"Training samples: {len(x_train)}, Testing samples: {len(x_test)}")
print(f"First input: {x_train[0]} -> passed: {int(y_train[0])}")


# 2. Build the model
print("\n2. Build the model")
model = keras.Sequential([
    keras.Input(shape=(2,)),
    layers.Dense(8, activation="relu"),
    layers.Dense(8, activation="relu"),
    layers.Dense(1, activation="sigmoid"),   # outputs a probability between 0 and 1
])
model.summary()


# 3. Compile the model — choose optimizer, loss and metrics
print("\n3. Compile the model")
model.compile(
    optimizer="adam",
    loss="binary_crossentropy",
    metrics=["accuracy"],
)


# 4. Train the model
print("\n4. Train the model (50 epochs)")
history = model.fit(
    x_train,
    y_train,
    epochs=50,
    batch_size=16,
    validation_split=0.2,   # 20% of training data held back for validation
    verbose=0,
)
print(f"Final training accuracy:     {history.history['accuracy'][-1]:.3f}")
print(f"Final validation accuracy:   {history.history['val_accuracy'][-1]:.3f}")


# 5. Evaluate on unseen test data
print("\n5. Evaluate on the test set")
test_loss, test_accuracy = model.evaluate(x_test, y_test, verbose=0)
print(f"Test loss: {test_loss:.3f}")
print(f"Test accuracy: {test_accuracy:.3f}")


# 6. Make predictions
print("\n6. Predictions for the first 5 test samples")
predictions = model.predict(x_test[:5], verbose=0).ravel()
for prediction, actual in zip(predictions, y_test[:5]):
    print(
        f"  predicted {prediction:.2f} -> {'Pass' if prediction >= 0.5 else 'Fail'}"
        f"  (actual: {'Pass' if actual else 'Fail'})"
    )


# 7. Chart: training history — loss and accuracy over epochs
print("\n7. Plot training history")
epochs = range(1, len(history.history["loss"]) + 1)

figure, axes = plt.subplots(1, 2, figsize=(12, 5))

axes[0].plot(epochs, history.history["loss"], label="Training loss")
axes[0].plot(epochs, history.history["val_loss"], label="Validation loss")
axes[0].set_title("Model Loss over Epochs")
axes[0].set_xlabel("Epoch")
axes[0].set_ylabel("Loss")
axes[0].legend()

axes[1].plot(epochs, history.history["accuracy"], label="Training accuracy")
axes[1].plot(epochs, history.history["val_accuracy"], label="Validation accuracy")
axes[1].set_title("Model Accuracy over Epochs")
axes[1].set_xlabel("Epoch")
axes[1].set_ylabel("Accuracy")
axes[1].set_ylim(0, 1)
axes[1].legend()

figure.tight_layout()
figure.savefig(HISTORY_PLOT_PATH, dpi=150)
plt.show()


# 8. Save the trained model
print("\n8. Save the model")
model.save(MODEL_PATH)
print(f"Model saved to: {MODEL_PATH.name}")

print("\nKeras intro completed.")