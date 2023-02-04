#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 13

@author: Professor Hammett

Welcome to Week 7. This is your template to work with today as we learn about writing our own classes.
Classes are objects. They have attributes and functions.
Our dog dataset contains rows that correspond to one dog each. This is a perfect candidate for a class.
The dataset gives us the attributes we need for our dog. But we will create a function ourselves.

"""
my_favorite_dog_breed = "Boxer"

import datetime
import pandas as pd

class Dog:

    
    def __init__(self, name, gender, birth_year, breed):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.breed = breed

    def is_favorite(self):
        if(my_favorite_dog_breed.lower() in self.breed.lower()):
            return(True)
        else:
            return(False)

    def __repr__(self):
        return("Hello I am a dog named " + self.name + ". I'm an " + self.breed + " and I'm " + str(self.age()) + " years old")

    def age(self):
        now = datetime.datetime.now()
        current_year = now.year
        return( current_year )

    
dog_data = pd.read_csv(r"C:\Users\jpatel17\Downloads\pydatasets\DogDataset.csv") #ENTER YOUR STRING FILE NAME OF THE DOG DATA 

dog_list = []
for row in range(len(dog_data)):
    dog = Dog(dog_data['AnimalName'][row], dog_data['AnimalGender'][row], dog_data['AnimalBirthYear'][row], dog_data['BreedName'][row])
    dog_list.append(dog)
  
print(dog_list[0].is_favorite())
print(dog.age())
print(dog.is_favorite())
print(dog.breed)
favorite_count =0
for dog in dog_list:
            if (dog.is_favorite()):
                favorite_count += 1
print("Number of my favorite breed: " + str(favorite_count))