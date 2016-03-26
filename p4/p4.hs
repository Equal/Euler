import Data.Digits
import Data.List
{- A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
 -
 - Find the largest palindrome made from the product of two 3-digit numbers. -}

listOfMultiples :: [Int]
listOfMultiples = reverse $ sort [ x * y | x <- [999,998..100], y <- [999,998..100] ]

isPalindrome :: Int -> Bool
isPalindrome x = (reverse digs) == digs
    where digs = digits 10 x

p4 :: Int
p4 = head [ x | x <- listOfMultiples, isPalindrome x ]
