import pickle

class Serialization:
    @staticmethod
    def save_object(obj, filename):
        with open(filename, 'wb') as file:
            pickle.dump(obj, file)

    @staticmethod
    def load_object(filename):
        with open(filename, 'rb') as file:
            return pickle.load(file)

# # Example Usage:
# if __name__ == "__main__":
#     # Sample class to serialize
#     class MyClass:
#         def __init__(self, name, value):
#             self.name = name
#             self.value = value

#     # Create an instance of MyClass
#     my_instance = MyClass(name="Example", value=42)

#     # Save the instance to a file
#     Serialization.save_object(my_instance, 'serialized_object.pkl')

#     # Load the instance from the file
#     loaded_instance = Serialization.load_object('serialized_object.pkl')

#     # Print loaded instance attributes
#     print(f"Name: {loaded_instance.name}, Value: {loaded_instance.value}")
