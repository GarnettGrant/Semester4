# %% [markdown]
# ## Pizza Class
# 
#  <blockquote style="padding-top:20px;">Name: Garnett Grant</blockquote>
#  <blockquote>Student Number: 301188923</blockquote>
#  <blockquote style="padding-bottom:20px;">Date: Jan 27th, 2023</blockquote>
#  

# %% [markdown]
# ## Class:
# 

# %%
class Pizza():

    ## Class Attributes:

    # 1. Class level collection to contain pizza sizes
    sizes = ["small","medium","large","x-large"]

    #2. Class level collection containing prices for each valid size
    pizza_prices = {"small":6.94,"medium":8.49,"large":10.49,"x-large":13.49}


    ## Constructor
    def __init__(self,size="medium",toppings= ["cheese"]) -> None:

        ## Instance Attributes: 

        # 1. / #9. Pizza size 
        self.__size = size
        
        ## 2. / #10. Pizza Toppings 
        self.__toppings = toppings



    ## Instance Properties:

    # 6.Pizza Price Property
    @property
    def pizza_price(self):
        return Pizza.pizza_prices[self.__size] + (len(self.__toppings) * 0.50)
    
    # Pizza Size Property   
    @property
    def size(self):
        return self.__size

    # Pizza Size Setter
    @size.setter
    def size(self,value):
        # Size is verified:
        if value in Pizza.sizes:
            self.__size = value
        else:
            raise ValueError(f"ERROR: {value} is not a valid size for a pizza")

    ## Instance Methods:

    # 4. Method to add toppings to pizza

    def add(self,toppings):
        self.__toppings.extend(toppings)

    # 5. __str__ method to return a formatted string of the pizza
    def __str__(self) -> str:
        return (f"{self.__size} pizza with {self.__toppings} for ${self.pizza_price}")

        
       



# %%
#Create a Test PyUnit
import unittest

class TestPizza(unittest.TestCase):
    
        def test_size(self):
            pizza = Pizza()
            self.assertEqual(pizza.size,"medium")
            pizza.size = "small"
            self.assertEqual(pizza.size,"small")
            with self.assertRaises(ValueError):
                pizza.size = "jumbo"
    
        def test_pizza_price(self):
            pizza = Pizza()
            self.assertEqual(pizza.pizza_price,8.99)
            pizza.add(["pepperoni","sausage"])
            self.assertEqual(pizza.pizza_price,9.99)
    
        def test_pizza_str(self):
            pizza = Pizza()
            self.assertEqual(str(pizza),"You ordered a medium pizza with cheese toppings. Total Price: $8.99")
            pizza.add(["pepperoni","sausage"])
            self.assertEqual(str(pizza),"You ordered a medium pizza with cheese pepperoni sausage toppings. Total Price: $9.99")

if __name__ == "__main__":
    unittest.main()
    

# %% [markdown]
# ## Test Harness:

# %%
print(f'Creating a default pizza')
p = Pizza()
print(p)

toppings = 'cheese olive'.split()
print(f'\nAdding topping: {toppings}')
p.add(toppings=toppings)
print(p)

print(f'\nCreating a new pizza')
p = Pizza('large', 'cheese pepper'.split())
print(p)

toppings = ['pineapple', 'mushroom']
print(f'\nAdding topping: {toppings}')
p.add(toppings)
print(p)

size = 'x-large'
p.size = size
print(f'\nChanging order size to {size}')
print(p)

size = 'gigantic'
print(f'\nChanging order size to {size}')
try:
  p.size = size
except ValueError as err:
  print(err) 



