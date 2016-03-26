{-The prime factors of 13195 are 5, 7, 13 and 29.
 -
 - What is the largest prime factor of the number 600851475143 ?-}

listOfPrimes :: Int -> [Int]
listOfPrimes x = eraSieve sieve
    where sieve = [2..x]

eraSieve :: [Int] -> [Int]
eraSieve [] = []
eraSieve (x:xs) = x:remainingPrimes
    where clearedSieve = [ y | y <- xs, y `mod` x /= 0 ]
          remainingPrimes = eraSieve clearedSieve

largestPrimeFactor :: Int -> Int
largestPrimeFactor x = last primeFactors
    where maxPrime = floor $ sqrt $ fromIntegral x
          primes = listOfPrimes maxPrime
          primeFactors = [y | y <- primes, x `mod` y == 0]

p3 :: Int
p3 = largestPrimeFactor 600851475143
