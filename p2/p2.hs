{-Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:
 -
 - 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
 -
 - By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.-}

-- Wow, this solution is slow. Correct, but slow.

fibonacci :: Int -> [Int]
fibonacci 0 = [0]
fibonacci 1 = [1, 0]
fibonacci n = [(head (fibonacci (n - 1))) + (head (fibonacci (n - 2)))] ++ fibonacci (n - 1)

fibUpTo' :: Int -> Int -> [Int]
fibUpTo' x y
    | head (fibonacci y) > x = fibonacci (y - 1)
    | otherwise = fibUpTo' x (y + 1)

fibUpTo :: Int -> [Int]
fibUpTo x = fibUpTo' x 0

p2 :: Int
p2 = sum [ x | x <- fibUpTo 4000000, even x ]