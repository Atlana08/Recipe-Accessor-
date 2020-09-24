class Category:
    def __init__(self, category):
        self.__category = category

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category


class Area:
    def __init__(self, area):
        self.__area = area

    def get_area(self):
        return self.__area

    def set_category(self, area):
        self.__area = area


class Meal:
    def __init__(self, meal_id, meal, meal_thumb):
        self.__meal_id = meal_id
        self.__meal = meal
        self.__meal_thumb = meal_thumb

    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_meal(self):
        return self.__meal

    def set_meal(self, meal):
        self.__meal = meal

    def get_meal_thumbI(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb


class Recipe:
    def __init__(self, meal_id, meal, category, instructions, meal_thumb,
                 strIngredient1, strIngredient2,strIngredient3, strIngredient4,
                 strIngredient5, strIngredient6,strIngredient7, strIngredient8,
                 strIngredient9, strIngredient10,strIngredient11, strIngredient12,
                 strIngredient13, strIngredient14,strIngredient15, strIngredient16,
                 strIngredient17, strIngredient18,strIngredient19, strIngredient20,
                 strMeasure1, strMeasure2, strMeasure3, strMeasure4,
                 strMeasure5, strMeasure6, strMeasure7, strMeasure8,
                 strMeasure9, strMeasure10, strMeasure11, strMeasure12,
                 strMeasure13, strMeasure14, strMeasure15, strMeasure16,
                 strMeasure17, strMeasure18, strMeasure19, strMeasure20):
        self.__meal_id = meal_id
        self.__meal = meal
        self.__category = category
        self.__instructions = instructions
        self.__meal_thumb = meal_thumb
        self.__strIngredient1 = strIngredient1
        self.__strIngredient2 = strIngredient2
        self.__strIngredient3 = strIngredient3
        self.__strIngredient4 = strIngredient4
        self.__strIngredient5 = strIngredient5
        self.__strIngredient6 = strIngredient6
        self.__strIngredient7 = strIngredient7
        self.__strIngredient8 = strIngredient8
        self.__strIngredient9 = strIngredient9
        self.__strIngredient10 = strIngredient10
        self.__strIngredient11 = strIngredient11
        self.__strIngredient12 = strIngredient12
        self.__strIngredient13 = strIngredient13
        self.__strIngredient14 = strIngredient14
        self.__strIngredient15 = strIngredient15
        self.__strIngredient16 = strIngredient16
        self.__strIngredient17 = strIngredient17
        self.__strIngredient18 = strIngredient18
        self.__strIngredient19 = strIngredient19
        self.__strIngredient20 = strIngredient20
        self.__strMeasure1 = strMeasure1
        self.__strMeasure2 = strMeasure2
        self.__strMeasure3 = strMeasure3
        self.__strMeasure4 = strMeasure4
        self.__strMeasure5 = strMeasure5
        self.__strMeasure6 = strMeasure6
        self.__strMeasure7 = strMeasure7
        self.__strMeasure8 = strMeasure8
        self.__strMeasure9 = strMeasure9
        self.__strMeasure10 = strMeasure10
        self.__strMeasure11 = strMeasure11
        self.__strMeasure12 = strMeasure12
        self.__strMeasure13 = strMeasure13
        self.__strMeasure14 = strMeasure14
        self.__strMeasure15 = strMeasure15
        self.__strMeasure16 = strMeasure16
        self.__strMeasure17 = strMeasure17
        self.__strMeasure18 = strMeasure18
        self.__strMeasure19 = strMeasure19
        self.__strMeasure20 = strMeasure20


    def get_meal_id(self):
        return self.__meal_id

    def set_meal_id(self, meal_id):
        self.__meal_id = meal_id

    def get_meal(self):
        return self.__meal

    def set_meal(self, meal):
        self.__meal = meal

    def get_category(self):
        return self.__category

    def set_category(self, category):
        self.__category = category

    def get_instructions(self):
        return self.__instructions

    def set_instructions(self, instructions):
        self.__instructions = instructions

    def get_meal_thumb(self):
        return self.__meal_thumb

    def set_meal_thumb(self, meal_thumb):
        self.__meal_thumb = meal_thumb

    def get_strIngredient1(self):
        return self.__strIngredient1

    def set_strIngredient1(self, strIngredient1):
        self.__strIngredient1 = strIngredient1

    def get_strIngredient2(self):
        return self.__strIngredient2

    def set_strIngredient2(self, strIngredient2):
        self.__strIngredient2 = strIngredient2

    def get_strIngredient3(self):
        return self.__strIngredient3

    def set_strIngredient3(self, strIngredient3):
        self.__strIngredient3 = strIngredient3

    def get_strIngredient4(self):
        return self.__strIngredient4

    def set_strIngredient4(self, strIngredient4):
        self.__strIngredient4 = strIngredient4

    def get_strIngredient5(self):
        return self.__strIngredient5

    def set_strIngredient5(self, strIngredient5):
        self.__strIngredient5 = strIngredient5

    def get_strIngredient6(self):
        return self.__strIngredient6

    def set_strIngredient6(self, strIngredient6):
        self.__strIngredient6 = strIngredient6

    def get_strIngredient7(self):
        return self.__strIngredient7

    def set_strIngredient7(self, strIngredient7):
        self.__strIngredient7 = strIngredient7

    def get_strIngredient8(self):
        return self.__strIngredient8

    def set_strIngredient8(self, strIngredient8):
        self.__strIngredient8 = strIngredient8

    def get_strIngredient9(self):
        return self.__strIngredient9

    def set_strIngredient9(self, strIngredient9):
        self.__strIngredient9 = strIngredient9

    def get_strIngredient10(self):
        return self.__strIngredient10

    def set_strIngredient10(self, strIngredient10):
        self.__strIngredient10 = strIngredient10

    def get_strIngredient11(self):
        return self.__strIngredient11

    def set_strIngredient11(self, strIngredient11):
        self.__strIngredient10 = strIngredient11

    def get_strIngredient12(self):
        return self.__strIngredient12

    def set_strIngredient12(self, strIngredient12):
        self.__strIngredient12 = strIngredient12

    def get_strIngredient13(self):
        return self.__strIngredient13

    def set_strIngredient13(self, strIngredient13):
        self.__strIngredient13 = strIngredient13

    def get_strIngredient14(self):
        return self.__strIngredient14

    def set_strIngredient14(self, strIngredient14):
        self.__strIngredient14 = strIngredient14

    def get_strIngredient15(self):
        return self.__strIngredient15

    def set_strIngredient15(self, strIngredient15):
        self.__strIngredient15 = strIngredient15

    def get_strIngredient16(self):
        return self.__strIngredient16

    def set_strIngredient16(self, strIngredient16):
        self.__strIngredient16 = strIngredient16

    def get_strIngredient17(self):
        return self.__strIngredient17

    def set_strIngredient17(self, strIngredient17):
        self.__strIngredient17 = strIngredient17

    def get_strIngredient18(self):
        return self.__strIngredient18

    def set_strIngredient18(self, strIngredient18):
        self.__strIngredient18 = strIngredient18

    def get_strIngredient19(self):
        return self.__strIngredient19

    def set_strIngredient19(self, strIngredient19):
        self.__strIngredient19 = strIngredient19

    def get_strIngredient20(self):
        return self.__strIngredient20

    def set_strIngredient20(self, strIngredient20):
        self.__strIngredient20 = strIngredient20

    def get_strMeasure1(self):
        return self.__strMeasure1

    def set_strMeasure1(self, strMeasure1):
        self.__strMeasure1 = strMeasure1

    def get_strMeasure2(self):
        return self.__strMeasure2

    def set_strMeasure2(self, strMeasure2):
        self.__strMeasure2 = strMeasure2

    def get_strMeasure3(self):
        return self.__strMeasure3

    def set_strMeasure3(self, strMeasure3):
        self.__strMeasure3 = strMeasure3

    def get_strMeasure4(self):
        return self.__strMeasure4

    def set_strMeasure4(self, strMeasure4):
        self.__strMeasure4 = strMeasure4

    def get_strMeasure5(self):
        return self.__strMeasure5

    def set_strMeasure5(self, strMeasure5):
        self.__strMeasure5 = strMeasure5

    def get_strMeasure6(self):
        return self.__strMeasure6

    def set_strMeasure6(self, strMeasure6):
        self.__strMeasure6 = strMeasure6

    def get_strMeasure7(self):
        return self.__strMeasure7

    def set_strMeasure7(self, strMeasure7):
        self.__strMeasure7 = strMeasure7

    def get_strMeasure8(self):
        return self.__strMeasure8

    def set_strMeasure8(self, strMeasure8):
        self.__strMeasure8 = strMeasure8

    def get_strMeasure9(self):
        return self.__strMeasure9

    def set_strMeasure9(self, strMeasure9):
        self.__strMeasure9 = strMeasure9

    def get_strMeasure10(self):
        return self.__strMeasure10

    def set_strMeasure10(self, strMeasure10):
        self.__strMeasure10 = strMeasure10

    def get_strMeasure11(self):
        return self.__strMeasure11

    def set_strMeasure11(self, strMeasure11):
        self.__strMeasure11 = strMeasure11

    def get_strMeasure12(self):
        return self.__strMeasure12

    def set_strMeasure12(self, strMeasure12):
        self.__strMeasure12 = strMeasure12

    def get_strMeasure13(self):
        return self.__strMeasure13

    def set_strMeasure13(self, strMeasure13):
        self.__strMeasure13 = strMeasure13

    def get_strMeasure14(self):
        return self.__strMeasure14

    def set_strMeasure14(self, strMeasure14):
        self.__strMeasure14 = strMeasure14

    def get_strMeasure15(self):
        return self.__strMeasure15

    def set_strMeasure15(self, strMeasure15):
        self.__strMeasure15 = strMeasure15

    def get_strMeasure16(self):
        return self.__strMeasure16

    def set_strMeasure16(self, strMeasure16):
        self.__strMeasure16 = strMeasure16

    def get_strMeasure17(self):
        return self.__strMeasure17

    def set_strMeasure17(self, strMeasure17):
        self.__strMeasure17 = strMeasure17

    def get_strMeasure18(self):
        return self.__strMeasure18

    def set_strMeasure18(self, strMeasure18):
        self.__strMeasure18 = strMeasure18

    def get_strMeasure19(self):
        return self.__strMeasure19

    def set_strMeasure19(self, strMeasure19):
        self.__strMeasure19 = strMeasure19

    def get_strMeasure20(self):
        return self.__strMeasure20

    def set_strMeasure20(self, strMeasure20):
        self.__strMeasure20 = strMeasure20














