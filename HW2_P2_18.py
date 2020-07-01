#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 13:56:06 2020

@author: anhnguyen
"""
#Define class myException_1
class myException_1(Exception):
    pass

#Define function validate_input()
def validate_input():
    while True:
        try:
            mass = float(input("Enter a positive mass (in kilograms): "))
            velocity = float(input("Enter a positive velocity (in meters per second): "))
            if mass < 0 or velocity < 0: #check if inputs are negative
                raise myException_1("something happened")
            return mass, velocity
            break
        except ValueError: #check if inputs are not numbers
            print("Please enter only numbers. Try again!")
        except myException_1:
                print("Inputs should be positive, no negative. Try again!")
mass, velocity = validate_input()
#print(mass, velocity)

#Define function kinetic_energy:
def kinetic_energy(mass, velocity):
    kinetic = (1/2)*mass*(velocity**2) #formula calculate kinetic energy
    #Display the output
    print("The object's kinetic energy is: ", format(kinetic, '.2f'))
kinetic_energy(mass, velocity)