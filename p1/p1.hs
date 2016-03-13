{-If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.-}

{-Find the sum of all the multiples of 3 or 5 below 1000.-}

isMultipleOf x y =
    if x `mod` y == 0
        then True
        else False

p1 = sum [ x | x <- [1..999], (x `isMultipleOf` 3) || (x `isMultipleOf` 5)]
