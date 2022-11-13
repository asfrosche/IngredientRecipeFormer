# THESE ARE THE QUERY FORMAT STRINGS WE USE
food_to_recipe_id = "SELECT recipeId FROM Ingredients as I, (SELECT foodId FROM Food WHERE name LIKE '%{}%') as F WHERE F.foodId = I.foodId"
recipe_to_recipe_id = "SELECT * from Recipe WHERE name LIKE '%{}%'"
recipe_from_id = "SELECT * from Recipe as r, {} as query WHERE r.recipeId = query.recipeId"
get_top_n_recipes = "SELECT * FROM Recipe as r, NumRatings as nr WHERE r.recipeId = nr.recipeId ORDER BY nr DESC limit {}"
get_unrated_recipes = "SELECT * FROM Recipe as r WHERE r.recipeId NOT IN(SELECT recipeId FROM Rating) ORDER BY r.name LIMIT {}"
user_add_rating ="INSERT INTO Rating (userId, recipeId, value) VALUES ({}, {}, {}) ON DUPLICATE KEY UPDATE value = {};"
recipe_id_to_rating ="SELECT nr FROM NumRatings WHERE recipeId = {};"