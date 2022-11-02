# ----------------------------------------------------------
# --------            HW 8: Food Cupboard          ---------
# ----------------------------------------------------------

# ----------------------------------------------------------
# Please answer these questions after you have completed this
# program
# ----------------------------------------------------------
# Name:
# Time spent on this problem:
#
# Collaborators and sources:
#   (List any collaborators or sources here.)
#
# ----------------------------------------------------------

banner = """                        WELCOME TO THE HAMILTON
  ______              _    _____            _                         _ 
 |  ____|            | |  / ____|          | |                       | |
 | |__ ___   ___   __| | | |    _   _ _ __ | |__   ___   __ _ _ __ __| |
 |  __/ _ \ / _ \ / _` | | |   | | | | '_ \| '_ \ / _ \ / _` | '__/ _` |
 | | | (_) | (_) | (_| | | |___| |_| | |_) | |_) | (_) | (_| | | | (_| |
 |_|  \___/ \___/ \__,_|  \_____\__,_| .__/|_.__/ \___/ \__,_|_|  \__,_|
                                     | |                                
                                     |_|                                
"""

categories = ["Fruit", "Vegetable", "Fruit", "Vegetable", "Grain", "Grain", "Dairy", "Dairy"]
foods = ["Bananas", "Cauliflower", "Mangoes", "Cabbage", "Wheat bread", "Rice", "Yogurt", "Milk"]

def main():
    print(banner)

if __name__ == '__main__':
    import doctest
    doctest.testmod()

    main()