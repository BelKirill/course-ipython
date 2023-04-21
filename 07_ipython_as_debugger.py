def division_product(a: int, b: int) -> float:
  breakpoint()
  return a / b

def faulty_division(x: int) -> float:
  return division_product(x, 0)

print(faulty_division(5))
