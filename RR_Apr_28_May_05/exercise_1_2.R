# Exercise 1
convert <- function(f, target = 'c'){
  if (target == 'c'){
    return ((f-32)/1.8)
  } else if  (target == 'k'){
    return ((f-32)/1.8) + 273.15
  } else{
    stop('wrong target')
  }
}

# Exercise 2
testthat::test_that('50 conversion', {
  testthat::expect_equal(convert(50), 10, tolerance=1e-5)
})

testthat::test_that('70 conversion', {
  testthat::expect_equal(convert(70), 21.11111, tolerance=1e-5)
})

testthat::test_that('90 conversion', {
  testthat::expect_equal(convert(90), 32.22222, tolerance=1e-5)
})