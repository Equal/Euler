{- 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
 -
 - What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? -}

isEvenlyDivisible :: Int -> Bool
isEvenlyDivisible x
    | x `mod` 19 /= 0 = False
    | x `mod` 18 /= 0 = False
    | x `mod` 17 /= 0 = False
    | x `mod` 16 /= 0 = False
    | x `mod` 15 /= 0 = False
    | x `mod` 14 /= 0 = False
    | x `mod` 13 /= 0 = False
    | x `mod` 12 /= 0 = False
    | x `mod` 11 /= 0 = False
    | otherwise = True

p5 :: Int
p5 = head $ [ x | x <- [20,40..], isEvenlyDivisible x ]

{-- MUCH SMARTER SOLUTION FROM FORUMS --}

p5smart :: Int
p5smart = foldl lcm 1 [1..20]
