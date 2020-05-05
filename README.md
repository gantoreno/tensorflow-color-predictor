# Tensorflow Color Predictor

A Tensorflow neural network that receives RGB values and predicts an optimal foreground color for optimized legibility and contrast ratio.

## Usage

You'll need to have `tensorflow`, `numpy`, and `pyfiglet` to get the project up and running.

First, clone the repo:

```sh
$ git clone https://github.com/hollandsgabe/tensorflow-color-predictor
```

Move into the project directory, and run the `main.py` file with Python 3.x:

```sh
$ cd tensorflow-color-predictor
$ python3 main.py
```

After that, a model will be created in the `models` directory once, every future execution will load the saved model.

To generate a new training dataset, run the following command:

```sh
$ node utils/randomColor.js > data/train.json
```
