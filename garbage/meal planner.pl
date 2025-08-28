% Define customer and preferences
customer(john).
goal(john, weight_loss).
allergy(john, nuts).
preference(john, vegetarian).

% Define ingredients and meals
ingredient(apple, vegetarian, 52, 0.3, 0.2).
ingredient(chicken, non_vegetarian, 165, 31, 3.6).
ingredient(rice, vegetarian, 130, 2.7, 0.3).
ingredient(broccoli, vegetarian, 55, 3.7, 0.6).
ingredient(almonds, vegetarian, 579, 21, 49).

meal(veggie_salad, [apple, broccoli]).
meal(chicken_rice, [chicken, rice]).
meal(vegan_burger, [rice, broccoli]).

% Rule to find suitable meals based on dietary preferences and allergies
suitable_meal(Customer, Meal) :-
    customer(Customer),
    meal(Meal, Ingredients),
    \+ (member(Ingredient, Ingredients), allergy(Customer, Ingredient)),
    \+ (member(Ingredient, Ingredients), ingredient(Ingredient, non_vegetarian, _, _, _), preference(Customer, vegetarian)),
    goal_based_meal(Customer, Meal).

% Rule for weight loss (low-calorie meals)
goal_based_meal(Customer, Meal) :-
    goal(Customer, weight_loss),
    meal(Meal, Ingredients),
    check_calories(Ingredients, MaxCalories),
    total_calories(Ingredients, TotalCalories),
    TotalCalories =< MaxCalories.

% Calculate total calories in a meal
total_calories([], 0).
total_calories([Ingredient | Rest], TotalCalories) :-
    ingredient(Ingredient, _, Calories, _, _),
    total_calories(Rest, RestCalories),
    TotalCalories is Calories + RestCalories.

% Check if total calories are within the desired limit
check_calories(Ingredients, MaxCalories) :-
    length(Ingredients, Length),
    MaxCalories is 500 / Length.  % Example: max 500 calories per meal

% Rule to suggest vegetarian meals
meal_suggestion(Customer, Meal) :-
    suitable_meal(Customer, Meal),
    format('I recommend the meal: ~w\n', [Meal]).
