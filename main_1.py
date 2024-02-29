#!/usr/bin/python3
from models.base_model import BaseModel

# Create a BaseModel instance without any arguments
my_model1 = BaseModel()

# Create a BaseModel instance using the to_dict() method of the first instance
my_model1_dict = my_model1.to_dict()
my_model2 = BaseModel(**my_model1_dict)

# Output the attributes of the first BaseModel instance
print("BaseModel instance without arguments:")
print(f"ID: {my_model1.id}")
print(f"Created At: {my_model1.created_at}")
print(f"Updated At: {my_model1.updated_at}")

# Output the attributes of the second BaseModel instance
print("\nBaseModel instance created from to_dict():")
print(f"ID: {my_model2.id}")
print(f"Created At: {my_model2.created_at}")
print(f"Updated At: {my_model2.updated_at}")
