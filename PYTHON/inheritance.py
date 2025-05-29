class Model:
    def train(self):
        print('Training the generic model.')

class LinearRegression(Model):
    def train(self):
        print('Training the linear regression model.')
        Model.train(self)
# Usage:
model = LinearRegression()
model.train()

# -------------------------------------------------------------

# Multiple
class Regression:
    def type(self):
        print("I am a regression model.")

class Classification:
    def category():
        print("I am a classification model.")

class HybridModel(Regression, Classification):
    def info(self):
        print("I can perform both Regression and Classification.")

# Usage:
hybrid = HybridModel()
hybrid.type()
hybrid.category()
hybrid.info()

# ----------------------------------------------------------------------------------

# Multilevel Inheritance
# A class inherits from another class, which itself inherits from a third class (creating a chain).
class MLModel:
    def info(self):
        print("General ML model.")

class NeuralNetwork(MLModel):
    def layers(self):
        print("Neural Network has layers.")

class CNN(NeuralNetwork):
    def convolutional_layer(self):
        print("CNN includes convolutional layers.")

# Usage:
cnn = CNN()
cnn.info()
cnn.layers()
cnn.convolutional_layer()

# #---------------------------------------------------------------------------------------

# # Hierarchical Inheritance
# # Multiple child classes inherit from one common parent class.
# class Dataset:
#     def load_data(self):
#         print("Dataset loaded.")

# class ImageDataset(Dataset):
#     def process_image(self):
#         print("Processing image data.")

# class TextDataset(Dataset):
#     def process_text(self):
#         print("Processing text data.")

# # Usage:
# img = ImageDataset()
# txt = TextDataset()

# img.load_data()
# img.process_image()

# txt.load_data()
# txt.process_text()

# # # ---------------------------------------------------------------------------------

# # # Hybrid Inheritance (Combination of types)
# # # Hybrid inheritance combines multiple types of inheritance.
# def new_func():
#     class Data:
#         def read_data(self):
#             print("Reading data")

#     class CSVData(Data):
#         def parse_csv(self):
#             print("Parsing CSV data")

#     class JSONData(Data):
#         def parse_json(self):
#             print("Parsing JSON data")

#     class MixedData(CSVData, JSONData):
#         def process_all(self):
#             print("Processing CSV and JSON data")

# # Usage:
#     mixed = MixedData()
#     mixed.read_data()
#     mixed.parse_csv()
#     mixed.parse_json()
#     mixed.process_all()

# new_func()





# Inheritance Type	Structure	Explanation
# Single	A → B	One parent, one child
# Multiple	A, B → C	Multiple parents, one child
# Multilevel	A → B → C	Chain of inheritance
# Hierarchical	A → B, A → C	One parent, multiple child classes
# Hybrid	Combination of above types	Complex structures combining above
# Inheritance Type	Structure	Explanation
# Single	A → B	One parent, one child