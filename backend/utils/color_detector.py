import cv2
import numpy as np
from sklearn.cluster import KMeans

COLOR_NAMES = {
    "Black": np.array([0, 0, 0]),
    "White": np.array([255, 255, 255]),
    "Red": np.array([255, 0, 0]),
    "Green": np.array([0, 255, 0]),
    "Blue": np.array([0, 0, 255]),
    "Yellow": np.array([255, 255, 0]),
    "Orange": np.array([255, 165, 0]),
    "Purple": np.array([128, 0, 128]),
    "Gray": np.array([128, 128, 128]),
    "Brown": np.array([165, 42, 42]),
    "Pink": np.array([255, 192, 203])
}


def closest_color(rgb):
    min_distance = float("inf")
    color_name = "Unknown"

    for name, value in COLOR_NAMES.items():
        distance = np.linalg.norm(rgb - value)

        if distance < min_distance:
            min_distance = distance
            color_name = name

    return color_name


def detect_color(image_path):
    image = cv2.imread(image_path)

    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

    pixels = image.reshape((-1, 3))

    kmeans = KMeans(
        n_clusters=3,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(pixels)

    centers = kmeans.cluster_centers_

    counts = np.bincount(labels)

    total = np.sum(counts)

    detected_colors = []

    for center, count in zip(centers, counts):

        percentage = (count / total) * 100

        # Ignore colors occupying less than 10% of image
        if percentage < 10:
            continue

        name = closest_color(center)

        if name not in detected_colors:
            detected_colors.append(name)

    if not detected_colors:
        return "Unknown"

    return ", ".join(detected_colors)