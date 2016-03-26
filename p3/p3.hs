{-The prime factors of 13195 are 5, 7, 13 and 29.
 -
 - What is the largest prime factor of the number 600851475143 ?-}

isPrime :: Int -> Bool
isPrime 1 = True
isPrime 2 = True
isPrime 3 = True
isPrime x
    | even x = False
    | any (isFactor x) [y | y <- [3,5..x-1]] = False
    | otherwise = True

isFactor :: Int -> Int -> Bool
isFactor x y = x `mod` y == 0

largestPrimeFactor :: Int -> Int
largestPrimeFactor x = last primeFactors
    where maxPrime = floor $ sqrt $ fromIntegral x
          factors = [y | y <- [1..maxPrime], x `mod` y == 0]
          primeFactors = [y | y <- factors, isPrime y]

p3 :: Int
p3 = largestPrimeFactor 600851475143
