SELECT * FROM Recipe as r, NumRatings as nr WHERE r.recipeId = nr.recipeId ORDER BY nr DESC limit 3